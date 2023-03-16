import numpy as np
import torch
import posix_ipc
import os, time, sys
import multiprocessing as mp
from ipcqueue import InterProcessQueue

iterations = 4000

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

def kernel_emulation(q_name, state_shape, qid):
    proc_start = time.time()
    print(f"kernel, pid {os.getpid()}")    
    state_q = InterProcessQueue('/'+q_name, state_shape, qid)
    mq = posix_ipc.MessageQueue('/'+q_name, 0)
    state_q.init_queue(mq)
    time_list = np.zeros(iterations)
    # print(f"name:{state_q.name}")
    # print(f"qsize:{state_q.qsize}")

    torch.set_num_threads(2)
    input = torch.rand(4, 1024, 768, dtype=torch.float32)

    loop_start = time.time()    
    for i in range(iterations):    
        start  = time.time()    
        time.sleep(0.010) # sleep 10 ms
        #output = output.real
        end  = time.time()  
        #print(f"shape:{output.shape}, type:{output.dtype}")
        state_q.push_as_tensor(input, (4,1024,768))        
        time_list[i] = end - start
        #print(f"kernel, q {state_q._name} push")
    loop_end = time.time()    

    print(f"emu-kernel-{qid}, exec:{loop_end-loop_start}, overhead:{loop_start-proc_start}")
    #print(f"kernel:{np.median(time_list)}")

def kernel_fn(q_name, state_shape, qid):
    proc_start = time.time()
    print(f"kernel, pid {os.getpid()}")    
    state_q = InterProcessQueue('/'+q_name, state_shape, qid)
    mq = posix_ipc.MessageQueue('/'+q_name, 0)
    state_q.init_queue(mq)
    time_list = np.zeros(iterations)
    # print(f"name:{state_q.name}")
    # print(f"qsize:{state_q.qsize}")

    torch.set_num_threads(2)
    input = torch.rand(4, 1024, 768, dtype=torch.float32)

    loop_start = time.time()  
    for i in range(iterations):    
        start  = time.time()    
        output = torch.fft.fft(input)
        output = output.real
        end  = time.time()  
        #print(f"shape:{output.shape}, type:{output.dtype}")
        state_q.push_as_tensor(input, (4,1024,768))        
        time_list[i] = end - start
        #print(f"kernel, q {state_q._name} push")
    loop_end = time.time()  

    #print(f"kernel:{np.median(time_list)}")
    print(f"kernel-{qid}, exec:{loop_end-loop_start}, overhead:{loop_start-proc_start}")

def datamotion_fn(q_name, state_shape, qid):
    proc_start = time.time()
    print(f"data-motion, pid {os.getpid()}")    
    state_q = InterProcessQueue('/'+q_name, state_shape, qid)
    mq = posix_ipc.MessageQueue('/'+q_name, 0)
    state_q.init_queue(mq)
    # print(f"name:{state_q.name}")
    # print(f"qsize:{state_q.qsize}")
    time_list = np.zeros(iterations)

    torch.set_num_threads(1)
    device = torch.device("cpu")
    #model = concat_cast_flatten().to(device)
    #model = image_resize().to(device)
    model = mel_scale().to(device)
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
max_msg_size = 12582912 #16777216 # 4096 * 768 * 4, 4 bytes for float32

num_kernels = 2
kernel_emulated = False
num_kernels = int(sys.argv[1])
kernel_emulated = bool(sys.argv[2])
#iterations = bool(sys.argv[3]) # 100 for 16 kernels, 2000 for 2 kernels

if kernel_emulated == True:
    print("kernel is emulated in this run")

qlist = []
for qid in range(num_kernels):
    state_name = f"test_queue{qid}"
    #state_q = InterProcessQueue('/'+state_name, (4096,768), qid)
    state_q = InterProcessQueue('/'+state_name, (4,1024,768), qid)
    #state_q = InterProcessQueue('/'+state_name, (8,512,512), qid)
    mq = posix_ipc.MessageQueue('/'+state_name, posix_ipc.O_CREAT, max_messages=max_msg_count, max_message_size=max_msg_size)
    state_q.init_queue(mq)
    qlist.append(state_q)

# for q in qlist:
#     print(q)
#     print(q.name)

dm_handle_list = []
kernel_handle_list = []
for qid in range(num_kernels):
    state_name = f"test_queue{qid}"

    if kernel_emulated == True:
        kernel_handle = mp.Process(target=kernel_emulation, args=(state_name, (4,1024,768), qid))
    else:
        kernel_handle = mp.Process(target=kernel_fn, args=(state_name, (4,1024,768), qid))

    dm_handle = mp.Process(target=datamotion_fn, args=(state_name, (4,1024,768), qid))
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

per_req_latency= (end-start)/iterations
print(f"per_req_latency:{per_req_latency}")

for q in qlist:
    q.destory()
    #print(f"{q.name} unlinked")

#print(f"{os.getpid()}-> {time.time()} time")