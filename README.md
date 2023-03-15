# dmx-kernel-eval

## Prerequisites
```shell
    python3 -m pip install torch posix_ipc 
```
`posix_ipc` is a Python module (written in C) that permits creation and manipulation of POSIX inter-process semaphores, shared memory and message queues.

See [posix_ipc](https://github.com/osvenskan/posix_ipc/) for more details.

PyTorch is needed for both FFT and DMX operations.

## Message Queue Setup
We'll need to modify the resource limits of the OS so we can pass large block of data between processes.

1. Open the limits config file with `vim /etc/security/limits.conf` and append this line `* hard msgqueue 12884901888` at the end of the file. 

2. Reboot the machine to make this effective.

3. Set up `msgsize_max` and `msg_max` for every reboot. It can better but I haven't figure this out.
```shell
sudo su
echo 16777216 > /proc/sys/fs/mqueue/msgsize_max
echo 64 > /proc/sys/fs/mqueue/msg_max
```

4. Run the command to check out the current resource limit for message queues on the shell. 
The default value should be 819200 when you first start a shell.
```shell
ulimit -q
``` 

5. Set the limit to 12884901888, the value we used in the first step.
```shell
ulimit -q 12884901888
```

6. You should be good to go to run `kernel_dm_pair.py` with `rdtset`.
This runs two kernels with real FFT kernel, not emulated 
```shell
sudo rdtset -t 'l3=0x1f;cpu=0,2' -c 0,2  python3 kernel_dm_pair.py 2 0
```





