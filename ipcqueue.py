import numpy as np
import torch
import pickle

# a wrapper for MessageQueue for push()/pop()
class InterProcessQueue():
    def __init__(self, name, shape, qid:int = 0):
        self._name = name
        #logger.debug(f"shape:{shape}")
        assert isinstance(shape, tuple) and len(shape) > 0 and all([s > 0 and isinstance(s, int) for s in shape])
        self._shape = shape
        self._qid = qid # qid to see if which one blocks or fucked up
        self._dtype_str = np.dtype(np.float32).str
    
    def init_queue(self, queue):
        #print(f"{self._name} init")
        self._queue = queue
        ## q init with wrong message size
        #print(f"q init msg-size:{self._queue.max_message_size}")
        #print(f"q init max_messages:{self._queue.max_messages}")

    def __del__(self):
         #print(f"{self._name} del")
         self._queue.close()
         #self._queue.unlink()

    def destory(self):
         self._queue.unlink()

    def push_object(self, item: object):
        pickled = pickle.dumps(item)
        #logger.debug(f"pickled object length:{len(pickled)}")
        self._queue.send(pickled)

    def pop_object(self):
        # if self._queue_type == "state":
        #     item = self.state_pop_object()
        #     return item
        raw, _ = self._queue.receive()
        return pickle.loads(raw)
        
    def push_bytes(self, item: bytes, item_shape: tuple):    
        self._queue.send(item.tobytes())
        if(item.shape != item_shape or self._shape != item_shape):
            raise RuntimeError(f"POSIXMsgQueue {self._name} of {self._shape} \
                shape can't push with wrong arguement item_shape {item_shape} or wrong item.shape {item.shape}")
    
    def push_as_tensor(self, item: torch.tensor, item_shape: tuple, timeout=None, blocking=True):
        item_numpy = item.numpy()
        item_bytes = item_numpy.tobytes()
        #self._queue.send(item_bytes)
        if blocking == False and self._queue.current_messages == self._queue.max_messages:
            return
        self._queue.send(item_bytes, timeout=timeout)
    
    def push(self, item: np.ndarray, item_shape: tuple):
        self._dtype_str = '<f4'
        #self._typelist[self._qid] = item.dtype.str
        #logger.debug(f"item dtype.str {item.dtype.str}, typelist[qid] {self._typelist[self._qid]}")
        #item_float64 = item.astype(np.float64)
        item_bytes = item.tobytes()
        #print(f"msg-size:{self._queue.max_message_size}")
        self._queue.send(item_bytes)

        #print(f"current_messages:{self._queue.current_messages}")

        if(item.shape != item_shape or self._shape != item_shape):
            raise RuntimeError(f"POSIXMsgQueue {self._name} of {self._shape} \
                shape can't push with wrong arguement item_shape {item_shape} or wrong item.shape {item.shape}")

    def pop_as_tensor(self, timeout=None):
        raw, _ = self._queue.receive(timeout=timeout)
        raw = bytearray(raw)
        self._dtype_str = torch.float32
        item = torch.frombuffer(raw, dtype=torch.float32, count=-1)  
        recv_array = item.reshape(self._shape)
        #print(f"recv_array.shape {recv_array.shape} with dtype {self._dtype_str,}")
        return recv_array
    
    def pop(self):
        raw, _ = self._queue.receive()
        #print(f"raw recv len {len(raw)} with type {type(raw)} on queue {self.name}")
        self._dtype_str = '<f4' #self._typelist[self._qid]        
        #logger.debug(f"recv data type: {self._dtype_str}")
        item = np.frombuffer(raw, dtype=self._dtype_str, count=-1)  
        recv_array = item.reshape(self._shape)
        #logger.debug(f"recv_array.shape {recv_array.shape} with dtype {self._dtype_str,}")
        return recv_array
    
    @property
    def qid(self):
        return self._qid
    
    @property
    def qsize(self):
        return self._queue.current_messages

    @property
    def shape(self):
        return self._shape

    @property
    def name(self) -> str:
        return self._name

    @property
    def queue_type(self):
        return self._queue_type