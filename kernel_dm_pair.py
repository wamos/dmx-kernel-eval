import numpy as np
import torch
import posix_ipc
import os, time, sys
import multiprocessing as mp
from ipcqueue import InterProcessQueue

iterations = 100

class concat_cast_flatten(torch.nn.Module):
        def __init__(self):
            super(concat_cast_flatten, self).__init__() 

        def forward(self, x):       
            xc = torch.cat((x, x), 1)
            xt = xc.type(torch.IntTensor)
            xt = torch.div(xc,2)	
            xt = torch.transpose(xt,1,2)		
            xf = torch.flatten(xt,1)
            return xf

class reshape_casting(torch.nn.Module):
    def __init__(self):
        super(reshape_casting, self).__init__()

    def forward(self, x):
        y = torch.pow(x,2)
        y = torch.mul(x,0.5) # normalization constant                                
        #yt = torch.transpose(y,1,2)
        y = torch.reshape(y, (1024, 4096))
        y = y.type(torch.CharTensor)        
        return y

class image_resize(torch.nn.Module):
    def __init__(self):
        super(image_resize, self).__init__()            
        self.max_pool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        
    def forward(self, xt):
        #y  = nn.Identity(x)
        xt = torch.transpose(xt,1,2)
        #xt = torch.transpose(xt,2,3)
        z = self.max_pool(xt)
        return z

class mel_scale(torch.nn.Module):
    def __init__(self):
        super(mel_scale, self).__init__()
        
    def forward(self, x):
        #x = torch.transpose(x,1,2)
        x = torch.flatten(x,1)
        y = torch.pow(x,2)
        y = torch.mul(y,0.001)
        y = torch.add(y,1)
        y = torch.tanh(y) # replace log with tanh
        y = torch.mul(y,2595) 
        y = y.type(torch.CharTensor)
        return y

def kernel_emulation(state_name, state_shape, qid):
    q_name = f"{state_name}{qid}"
    proc_start = time.time()
    print(f"kernel, pid {os.getpid()}")    
    state_q = InterProcessQueue('/'+q_name, state_shape, qid)
    mq = posix_ipc.MessageQueue('/'+q_name, 0)
    state_q.init_queue(mq)
    time_list = np.zeros(iterations)
    # print(f"name:{state_q.name}")
    # print(f"qsize:{state_q.qsize}")

    if state_name == "mel_scale":
        delayed_secs = 1.5*6.498*0.001
    elif state_name == "reshape_casting":
        delayed_secs = 1.5*8.457*0.001
    elif state_name== "image_resize":
        delayed_secs = 1.5*3.385*0.001        
    elif state_name== "concat_cast_flatten_aes":
        delayed_secs = 1.5*43.734*0.001
    elif state_name== "concat_cast_flatten_gzip":
        delayed_secs = 1.5*22.254*0.001
    else:
        delayed_secs = 0.010
    print(f"{state_name}: emulated execution delay {delayed_secs}")

    torch.set_num_threads(2)
    #print(state_shape[0], state_shape[1], state_shape[2])
    input = torch.rand(state_shape[0], state_shape[1], state_shape[2], dtype=torch.float32) #benchmark-2, benchmark-1
    #input = torch.rand(4, 1024, 1024, dtype=torch.float32) #benchmark-3

    loop_start = time.time()    
    for i in range(iterations):    
        start  = time.time()    
        time.sleep(delayed_secs) # sleep 10 ms as the default setup
        #output = output.real
        end  = time.time()  
        #print(f"shape:{output.shape}, type:{output.dtype}")
        #state_q.push_as_tensor(input, (4,1024,768)) #benchmark-2, benchmark-1   
        state_q.push_as_tensor(input, state_shape) #benchmark-3
        time_list[i] = end - start
        #print(f"kernel, q {state_q._name} push")
    loop_end = time.time()    

    print(f"emu-kernel-{qid}, exec:{loop_end-loop_start}, overhead:{loop_start-proc_start}")
    #print(f"kernel:{np.median(time_list)}")

def kernel_fn(state_name, state_shape, qid):
    q_name = f"{state_name}{qid}"
    proc_start = time.time()
    print(f"kernel, pid {os.getpid()}")    
    state_q = InterProcessQueue('/'+q_name, state_shape, qid)
    mq = posix_ipc.MessageQueue('/'+q_name, 0)
    state_q.init_queue(mq)
    time_list = np.zeros(iterations)
    # print(f"name:{state_q.name}")
    # print(f"qsize:{state_q.qsize}")

    torch.set_num_threads(2)
    input = torch.rand(state_shape[0], state_shape[1], state_shape[2], dtype=torch.float32)

    loop_start = time.time()  
    for i in range(iterations):    
        start  = time.time()    
        output = torch.fft.fft(input)
        output = output.real
        end  = time.time()  
        #print(f"shape:{output.shape}, type:{output.dtype}")
        state_q.push_as_tensor(input, state_shape)        
        time_list[i] = end - start
        #print(f"kernel, q {state_q._name} push")
    loop_end = time.time()  

    #print(f"kernel:{np.median(time_list)}")
    print(f"kernel-{qid}, exec:{loop_end-loop_start}, overhead:{loop_start-proc_start}")

def datamotion_fn(state_name, state_shape, qid):
    proc_start = time.time()
    q_name = f"{state_name}{qid}"
    print(f"data-motion, pid {os.getpid()}")    
    state_q = InterProcessQueue('/'+q_name, state_shape, qid)
    mq = posix_ipc.MessageQueue('/'+q_name, 0)
    state_q.init_queue(mq)
    # print(f"name:{state_q.name}")
    # print(f"qsize:{state_q.qsize}")
    time_list = np.zeros(iterations)

    torch.set_num_threads(1)
    device = torch.device("cpu")
    if state_name == "mel_scale":
        model = mel_scale().to(device)
    elif state_name == "reshape_casting":
        model = reshape_casting().to(device)
    elif state_name== "image_resize":
        model = image_resize().to(device)     
    elif state_name== "concat_cast_flatten_aes":
        model = concat_cast_flatten().to(device)
    elif state_name== "concat_cast_flatten_gzip":
        model = concat_cast_flatten().to(device)
    else:
        model = mel_scale().to(device)
    print(f"using {state_name} data motion")

    model.eval()
    
    loop_start = time.time()  
    for i in range(iterations):
        input_tensor = state_q.pop_as_tensor()
        start  = time.time()      
        output = model(input_tensor)
        end  = time.time()      
        time_list[i] = end - start
        #print(f"data-motion, q {state_q._name} pop")    
    #print(input.shape)
    #print(f"data motion:{np.median(time_list)}")
    loop_end = time.time()  
    print(f"dm-{qid}, exec:{loop_end-loop_start}, overhead:{loop_start-proc_start}")


# setup for message queue
max_msg_count = 48
#max_msg_size = 12582912 #16777216 # 4096 * 768 * 4, 4 bytes for float32
max_msg_size = 16777216

num_kernels = 2
kernel_emulated = False
benchmark_name = sys.argv[1]
num_kernels = int(sys.argv[2])
kernel_emulated = bool(sys.argv[3])
#iterations = bool(sys.argv[3]) # 100 for 16 kernels, 2000 for 2 kernels

if kernel_emulated == True:
    print("kernel is emulated in this run")

shape = (1,1,1)
if benchmark_name == "mel_scale":
    shape = (4,1024,768)
    max_msg_size = 12582912
elif benchmark_name == "reshape_casting":
    shape = (4,1024,1024)
    max_msg_size = 16777216
elif benchmark_name== "image_resize":
    shape = (4,1024,768)
    max_msg_size = 12582912
elif benchmark_name== "concat_cast_flatten_aes":
    shape = (128,768,8)
    max_msg_size = 12582912
elif benchmark_name== "concat_cast_flatten_gzip":
    shape = (4, 1024, 512)
    max_msg_size = 12582912

print(f"{benchmark_name}: {shape} with max_msg_size {max_msg_size}")
#exit()

qlist = []
#shape = (4,1024,768)
#shape = (4,1024,1024)
#shape = (8,512,512)
for qid in range(num_kernels):
    q_name = f"{benchmark_name}{qid}"
    state_q = InterProcessQueue('/'+q_name, shape, qid)
    #state_q = InterProcessQueue('/'+state_name, (4,1024,768), qid)
    #state_q = InterProcessQueue('/'+state_name, (8,512,512), qid)
    mq = posix_ipc.MessageQueue('/'+q_name, posix_ipc.O_CREAT, max_messages=max_msg_count, max_message_size=max_msg_size)
    state_q.init_queue(mq)
    qlist.append(state_q)

#exit()
# for q in qlist:
#     print(q)
#     print(q.name)

dm_handle_list = []
kernel_handle_list = []
for qid in range(num_kernels):
    state_name = f"{benchmark_name}"

    if kernel_emulated == True:
        kernel_handle = mp.Process(target=kernel_emulation, args=(state_name, shape, qid))
    else:
        kernel_handle = mp.Process(target=kernel_fn, args=(state_name, shape, qid))

    dm_handle = mp.Process(target=datamotion_fn, args=(state_name, shape, qid))
    kernel_handle_list.append(kernel_handle)
    dm_handle_list.append(dm_handle)

start = time.time() 
for qid in range(num_kernels):
    dm_handle_list[qid].start()
    kernel_handle_list[qid].start()
 
for qid in range(num_kernels):
    dm_handle_list[qid].join()
    kernel_handle_list[qid].join()
end = time.time() 

print(f"total_req_latency:{end-start}")

per_req_latency = (end-start)/iterations
print(f"per_req_latency:{per_req_latency}")
per_req_latency = per_req_latency*1000
print_string ="{:.3f}".format(per_req_latency)
print(print_string)

for q in qlist:
    q.destory()
    #print(f"{q.name} unlinked")

#print(f"{os.getpid()}-> {time.time()} time")