# Scaling # of kernels with fixed cores

## Benchmark 2: FFT -> Data motion

### (4 physical cores, 2 way of LLC, 20% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py mel_scale 1 4 1 1`   

Output:  
```
cpu-emulated: 64.448
acc:64.869
```  

Command: 5 emulated kernels, using iterations = 1000  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py mel_scale 5 4 1 1`

Output:  
```
cpu-emulated:109.906
acc:108.695
```

Command: 10 emulated kernels, using iterations = 500
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py mel_scale 10 4 1 1`

Output:  
```
cpu-emulated:224.654
acc:217.210
```

Command: 15 emulated kernels, using iterations = 200
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py mel_scale 15 4 1 1`

Output:  
```
cpu-emulated:343.100
acc:331.811
```

### (8 physical cores, 4 way of LLC, 40% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16 python3 kernel_dm_pair.py mel_scale 1 8 1 1`  

Output:  
```
cpu-emulated:28.070
acc:28.110
```

Command: 5 emulated kernels, using iterations = 1000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16 python3 kernel_dm_pair.py mel_scale 5 8 1 1`

Output:  
```
cpu-emulated:51.743
acc:51.153
```

Command: 10 emulated kernels, using iterations = 500  
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16 python3 kernel_dm_pair.py mel_scale 10 8 1 1`

Output:  
```
cpu-emulated:102.899
acc:102.879
```

Command: 15 emulated kernels, using iterations = 200
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16 python3 kernel_dm_pair.py mel_scale 15 8 1 1`

Output:  
```
cpu-emulated:155.003
acc:154.617
```


### (16 physical cores, 8 way of LLC, 80% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 5000    
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py mel_scale 1 16 1 1`  

Output:  
```
cpu-emulated:22.706
acc:22.334
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py mel_scale 5 16 1 1`

Output:  
```
cpu-emulated:51.117
acc:50.579
```

Command: 10 emulated kernels, using iterations = 1000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py mel_scale 10 16 1 1`

Output:  
```
cpu-emulated:101.510
acc:100.806
```

Command: 15 emulated kernels, using iterations = 750
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py mel_scale 15 16 1 1`

Output:  
```
cpu-emulated:154.074
acc:153.319
```

## Benchmark 3: FFT -> Data motion
### (4 physical cores, 2 way of LLC, 20% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 2000  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py reshape_casting 1 4 1`  

Output:  
```
cpu-emulated:56.560
acc:57.164
```

Command: 5 emulated kernels, using iterations = 200 (2000 takes way too long)  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py reshape_casting 5 4 1 1`

Output:  
```
cpu-emulated:106.481
acc:107.751
```

Command: 10 emulated kernels, using iterations = 200 (2000 takes way too long)  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py reshape_casting 10 4 1`

Output:  
```
cpu-emulated:213.897
acc:213.897
```

Command: 15 emulated kernels, using iterations = 200 (2000 takes way too long)  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py reshape_casting 15 4 1`

Output:  
```
cpu-emulated:324.556
acc:328.855
```

### (8 physical cores, 4 way of LLC, 40% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py reshape_casting 1 8 1 1`  

Output:  
```
cpu-emulated:30.178
acc:25.693
```

Command: 5 emulated kernels, using iterations = 2000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py reshape_casting 5 8 1 1`  

Output:  
```
cpu-emulated:47.955
acc:47.783
```

Command: 10 emulated kernels, using iterations = 1000
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py reshape_casting 10 8 1 1`

Output:  
```
cpu-emulated:94.817
acc:95.118
```

Command: 15 emulated kernels, using iterations = 500 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py reshape_casting 15 8 1 1`

Output:  
```
cpu:emulated:145.658
acc:145.566
```

### (16 physical cores, 8 way of LLC, 80% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000    
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py reshape_casting 1 16 1 1`  

Output:  
```
cpu-emulated:29.111
acc:20.778
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py reshape_casting 5 16 1 1`

Output:  
```
cpu-emulated:47.446
acc:47.276
```

Command: 10 emulated kernels, using iterations = 1000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py reshape_casting 10 16 1 1`

Output:  
```
cpu-emulated:93.278
acc:93.770
```

Command: 15 emulated kernels, using iterations = 750
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py reshape_casting 15 16 1 1`

Output:  
```
cpu-emulated:141.426
acc:142.145
```

## Benchmark 1: Video Codec -> Data motion

### (4 physical cores, 2 way of LLC, 20% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 2000  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py image_resize 1 4 1 1`  

Output:  
```
cpu-emulated:65.778
acc:65.756
```

Command: 5 emulated kernels, using iterations = 1000 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py image_resize 5 4 1 1`

Output:  
```
cpu-emulated:114.323
acc:116.895
```

Command: 10 emulated kernels, using iterations = 1000 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py image_resize 10 4 1 1`

Output:  
```
cpu-emulated:231.393
acc:230.675
```

Command: 15 emulated kernels, using iterations = 500 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py image_resize 15 4 1 1`

Output:  
```
cpu-emulated:355.835
acc:354.092
```

### (8 physical cores, 4 way of LLC, 40% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py image_resize 1 8 1 1`  

Output:  
```
cpu-emulated:50.039
acc:50.006
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py image_resize 5 8 1 1`

Output:  
```
cpu-emulated:63.499
acc:65.734
```

Command: 10 emulated kernels, using iterations = 1000
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py image_resize 10 8 1 1`

Output:  
```
cpu-emulated:105.247
acc:103.713
```

Command: 15 emulated kernels, using iterations = 500
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py image_resize 15 8 1 1`

Output:  
```
cpu-emulated:158.783
acc:157.667
```

### (16 physical cores, 8 way of LLC, 80% of memory bandwidth)
Command: 1 emulated kernel, using iterations = 4000    
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py image_resize 1 16 1 1`  

Output:  
```
cpu-emulated:48.078
acc:47.851
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py image_resize 5 16 1 1`

Output:  
```
cpu-emulated:63.743
acc:66.933
```

Command: 10 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30  python3 kernel_dm_pair.py image_resize 10 16 1 1`

Output:  
```
cpu-emulated:91.783
acc:92.831
```

Command: 15 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py image_resize 15 16 1 1`

Output:  
```
cpu-emulated:125.691
acc:126.483
```

## Benchmark 4: AES -> regexp

### (4 physical cores, 2 way of LLC, 20% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_aes 1 4 1`  

Output:  
```
kernel:0.06579351425170898
emu-kernel-0, exec:227.853746175766, overhead:0.43759989738464355
dm-0, data motion:0.027834653854370117
dm-0, exec:228.06284141540527, overhead:0.26987433433532715
total_req_latency:228.35331988334656
per_req_latency:0.07611777329444885
76.118
```

Command: 5 emulated kernels, using iterations = 2000 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_aes 5 4 1`

Output:  
```
kernel:0.06574440002441406
emu-kernel-1, exec:152.3667562007904, overhead:1.3173577785491943
dm-1, data motion:0.02791726589202881
dm-1, exec:152.5160481929779, overhead:1.2088429927825928
kernel:0.06574344635009766
emu-kernel-2, exec:152.36154675483704, overhead:1.3225712776184082
dm-2, data motion:0.02790999412536621
dm-2, exec:153.35903453826904, overhead:0.45274829864501953
kernel:0.06574416160583496
emu-kernel-0, exec:152.49143862724304, overhead:1.3304431438446045
kernel:0.06574440002441406
emu-kernel-4, exec:152.4181866645813, overhead:1.177032232284546
dm-0, data motion:0.02789783477783203
dm-0, exec:153.14525747299194, overhead:0.7214875221252441
kernel:0.06574463844299316
emu-kernel-3, exec:152.44788575172424, overhead:1.2009894847869873
dm-4, data motion:0.02791452407836914
dm-4, exec:152.51126265525818, overhead:1.1269211769104004
dm-3, data motion:0.02789890766143799
dm-3, exec:152.77189087867737, overhead:1.0277516841888428
total_req_latency:153.96232390403748
per_req_latency:0.07698116195201873
76.981
```

Command: 10 emulated kernels, using iterations = 1000 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_aes 10 4 1`

Output:  
```
kernel:0.0657036304473877
emu-kernel-7, exec:93.94192457199097, overhead:1.3700923919677734
kernel:0.06570243835449219
emu-kernel-8, exec:94.54060816764832, overhead:0.9253580570220947
dm-7, data motion:0.07491731643676758
dm-7, exec:99.49142694473267, overhead:0.9828109741210938
dm-8, data motion:0.07442402839660645
dm-8, exec:99.72551941871643, overhead:0.8909711837768555
kernel:0.06570267677307129
emu-kernel-0, exec:105.94533205032349, overhead:1.5564625263214111
kernel:0.0657036304473877
emu-kernel-2, exec:105.83949398994446, overhead:1.757416009902954
dm-0, data motion:0.08413207530975342
dm-0, exec:111.73468399047852, overhead:0.6721806526184082
dm-2, data motion:0.08129000663757324
dm-2, exec:111.84784436225891, overhead:0.6396400928497314
kernel:0.0657033920288086
emu-kernel-4, exec:119.91793513298035, overhead:1.893984079360962
kernel:0.0657041072845459
emu-kernel-1, exec:121.56798887252808, overhead:1.5558998584747314
kernel:0.0657048225402832
emu-kernel-9, exec:121.68445920944214, overhead:0.876821756362915
dm-1, data motion:0.1047811508178711
dm-1, exec:123.59585070610046, overhead:0.7994258403778076
dm-9, data motion:0.09180760383605957
dm-9, exec:123.05385971069336, overhead:0.7764043807983398
dm-4, data motion:0.1039896011352539
dm-4, exec:124.73458194732666, overhead:1.2150053977966309
kernel:0.0657038688659668
emu-kernel-5, exec:125.80015754699707, overhead:1.6422722339630127
dm-5, data motion:0.10886180400848389
dm-5, exec:126.8727810382843, overhead:1.0267484188079834
kernel:0.0657041072845459
emu-kernel-3, exec:127.02431964874268, overhead:1.7331821918487549
dm-3, data motion:0.11501002311706543
dm-3, exec:128.19502925872803, overhead:0.9270343780517578
kernel:0.0657045841217041
emu-kernel-6, exec:126.5551061630249, overhead:1.670363426208496
dm-6, data motion:0.11183750629425049
dm-6, exec:127.43761873245239, overhead:1.0069985389709473
total_req_latency:129.35326743125916
per_req_latency:0.12935326743125916
129.35
```

Command: 15 emulated kernels, using iterations = 500
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_aes 15 4 1`

Output:  
```
kernel:0.0657038688659668
emu-kernel-7, exec:41.88586902618408, overhead:1.1926512718200684
kernel:0.06570315361022949
emu-kernel-2, exec:42.788540840148926, overhead:2.1499624252319336
dm-7, data motion:0.06997168064117432
dm-7, exec:47.3127875328064, overhead:0.718764066696167
dm-2, data motion:0.06611049175262451
dm-2, exec:48.76863622665405, overhead:1.0415196418762207
kernel:0.06570243835449219
emu-kernel-11, exec:71.69115281105042, overhead:1.3535382747650146
kernel:0.06570291519165039
emu-kernel-5, exec:72.85502862930298, overhead:1.75032639503479
kernel:0.06570351123809814
emu-kernel-14, exec:71.80100893974304, overhead:0.5570030212402344
kernel:0.06570315361022949
emu-kernel-4, exec:77.42955708503723, overhead:1.5770750045776367
kernel:0.06570267677307129
emu-kernel-0, exec:77.85663747787476, overhead:1.6115310192108154
dm-11, data motion:0.12215209007263184
dm-11, exec:79.94010949134827, overhead:0.6227405071258545
dm-5, data motion:0.12314343452453613
dm-5, exec:80.94459414482117, overhead:1.0229485034942627
dm-14, data motion:0.12598001956939697
dm-14, exec:79.10128021240234, overhead:0.6944866180419922
dm-4, data motion:0.09005653858184814
dm-4, exec:83.21845126152039, overhead:1.0634214878082275
dm-0, data motion:0.090096116065979
dm-0, exec:84.05402326583862, overhead:0.6419134140014648
kernel:0.0657033920288086
emu-kernel-13, exec:82.52045154571533, overhead:1.048604965209961
kernel:0.065704345703125
emu-kernel-6, exec:83.96281623840332, overhead:1.6170358657836914
kernel:0.0657045841217041
emu-kernel-1, exec:86.53218030929565, overhead:1.6430590152740479
dm-13, data motion:0.11747682094573975
dm-13, exec:87.8323302268982, overhead:0.6466131210327148
dm-6, data motion:0.11591660976409912
dm-6, exec:89.7760899066925, overhead:0.6148326396942139
dm-1, data motion:0.10783064365386963
dm-1, exec:93.2596378326416, overhead:1.217383623123169
kernel:0.0657045841217041
emu-kernel-8, exec:92.51426291465759, overhead:1.4490981101989746
kernel:0.06570553779602051
emu-kernel-12, exec:91.99429845809937, overhead:1.01283597946167
kernel:0.0657036304473877
emu-kernel-10, exec:92.72474598884583, overhead:1.5507049560546875
kernel:0.06570315361022949
emu-kernel-3, exec:94.45693826675415, overhead:1.8733632564544678
kernel:0.06570422649383545
emu-kernel-9, exec:93.03137683868408, overhead:1.3790102005004883
dm-8, data motion:0.1559123992919922
dm-8, exec:95.73294615745544, overhead:0.7424225807189941
dm-9, data motion:0.15574121475219727
dm-9, exec:95.45047903060913, overhead:1.006293535232544
dm-10, data motion:0.1598120927810669
dm-10, exec:95.51686096191406, overhead:0.7270081043243408
dm-12, data motion:0.15031301975250244
dm-12, exec:94.99890327453613, overhead:0.8035500049591064
dm-3, data motion:0.147896409034729
dm-3, exec:97.49137663841248, overhead:1.0952281951904297
total_req_latency:98.73428893089294
per_req_latency:0.1974685778617859
197.469
```

### (8 physical cores, 4 way of LLC, 40% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_aes 1 8 1`  

Output:  
```
kernel:0.06578874588012695
emu-kernel-0, exec:213.1657304763794, overhead:0.19409394264221191
dm-0, data motion:0.01402425765991211
dm-0, exec:213.2026810646057, overhead:0.17865562438964844
total_req_latency:213.4038712978363
per_req_latency:0.07113462376594544
71.135
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_aes 5 8 1`

Output:  
```
kernel:0.06578755378723145
emu-kernel-2, exec:142.6125190258026, overhead:0.6663787364959717
kernel:0.06574201583862305
emu-kernel-0, exec:142.61601543426514, overhead:0.6851544380187988
dm-2, data motion:0.014963388442993164
dm-2, exec:142.69558835029602, overhead:0.605719804763794
kernel:0.06573605537414551
emu-kernel-1, exec:142.62518787384033, overhead:0.6821715831756592
dm-0, data motion:0.015080571174621582
dm-0, exec:142.8028507232666, overhead:0.5216879844665527
dm-1, data motion:0.014777421951293945
dm-1, exec:142.83986902236938, overhead:0.48944735527038574
kernel:0.06575489044189453
emu-kernel-3, exec:142.61225628852844, overhead:0.7343401908874512
dm-3, data motion:0.01491701602935791
dm-3, exec:142.71706247329712, overhead:0.6503331661224365
kernel:0.06574201583862305
emu-kernel-4, exec:142.6132106781006, overhead:0.2474977970123291
dm-4, data motion:0.015119075775146484
dm-4, exec:142.98078608512878, overhead:0.4029068946838379
total_req_latency:143.41717052459717
per_req_latency:0.07170858526229859
71.709
```

Command: 10 emulated kernels, using iterations = 1000  
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_aes 10 8 1`

Output:  
```
kernel:0.06574106216430664
emu-kernel-0, exec:71.67755079269409, overhead:1.1537094116210938
dm-0, data motion:0.016497015953063965
dm-0, exec:72.39390015602112, overhead:0.4621152877807617
kernel:0.06574559211730957
emu-kernel-1, exec:71.85934662818909, overhead:1.1261019706726074
dm-1, data motion:0.01603400707244873
dm-1, exec:72.46621966362, overhead:0.5419211387634277
kernel:0.06574296951293945
emu-kernel-2, exec:71.92071604728699, overhead:1.0900523662567139
dm-2, data motion:0.017696738243103027
dm-2, exec:72.49808382987976, overhead:0.5391428470611572
kernel:0.06574249267578125
emu-kernel-3, exec:71.90083456039429, overhead:1.1348044872283936
kernel:0.0657418966293335
emu-kernel-5, exec:71.8002564907074, overhead:1.0167388916015625
dm-3, data motion:0.016533851623535156
dm-3, exec:72.2663562297821, overhead:0.7906758785247803
dm-5, data motion:0.01676476001739502
dm-5, exec:72.2051682472229, overhead:0.8353147506713867
kernel:0.06574654579162598
emu-kernel-7, exec:71.6604015827179, overhead:0.7086963653564453
kernel:0.06574201583862305
emu-kernel-4, exec:71.66975903511047, overhead:1.3368000984191895
kernel:0.06574583053588867
emu-kernel-6, exec:71.66670489311218, overhead:0.9328765869140625
dm-7, data motion:0.01726078987121582
dm-7, exec:72.06959843635559, overhead:0.5349748134613037
dm-4, data motion:0.01725935935974121
dm-4, exec:72.44018149375916, overhead:0.6634154319763184
dm-6, data motion:0.016443490982055664
dm-6, exec:72.21340441703796, overhead:0.6670570373535156
kernel:0.06573963165283203
emu-kernel-8, exec:71.64316654205322, overhead:0.5769295692443848
dm-8, data motion:0.017629027366638184
dm-8, exec:71.96396565437317, overhead:0.419055700302124
kernel:0.06574106216430664
emu-kernel-9, exec:71.69300699234009, overhead:0.46361804008483887
dm-9, data motion:0.016808748245239258
dm-9, exec:71.76075196266174, overhead:0.4910612106323242
total_req_latency:73.25048661231995
per_req_latency:0.07325048661231995
73.250
```

Command: 15 emulated kernels, using iterations = 500  
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_aes 15 8 1`

Output:  
```
kernel:0.06571459770202637
emu-kernel-0, exec:38.66532301902771, overhead:1.2470059394836426
kernel:0.06571507453918457
emu-kernel-11, exec:37.99569535255432, overhead:0.9566209316253662
kernel:0.06571459770202637
emu-kernel-12, exec:38.147313833236694, overhead:0.739243745803833
kernel:0.06571483612060547
emu-kernel-5, exec:39.94200396537781, overhead:1.0570952892303467
kernel:0.06571674346923828
emu-kernel-9, exec:39.499181509017944, overhead:0.7331762313842773
kernel:0.06571555137634277
emu-kernel-6, exec:40.220299243927, overhead:1.3288958072662354
kernel:0.06571447849273682
emu-kernel-13, exec:39.59831476211548, overhead:0.5910336971282959
dm-12, data motion:0.06437373161315918
dm-12, exec:40.14558172225952, overhead:0.6750779151916504
kernel:0.06571483612060547
emu-kernel-1, exec:41.37850260734558, overhead:1.1076257228851318
kernel:0.06571531295776367
emu-kernel-10, exec:40.523319244384766, overhead:1.0279860496520996
kernel:0.06571531295776367
emu-kernel-2, exec:41.49038600921631, overhead:1.4051878452301025
kernel:0.06571507453918457
emu-kernel-4, exec:42.03220796585083, overhead:1.0410089492797852
kernel:0.06571316719055176
emu-kernel-14, exec:40.969693183898926, overhead:0.5332686901092529
kernel:0.06571507453918457
emu-kernel-8, exec:42.28032326698303, overhead:1.1327919960021973
dm-0, data motion:0.062421441078186035
dm-0, exec:43.71422362327576, overhead:0.5193808078765869
kernel:0.06571555137634277
emu-kernel-3, exec:43.379029989242554, overhead:0.9361488819122314
dm-9, data motion:0.07031536102294922
dm-9, exec:42.98141670227051, overhead:0.4945981502532959
dm-11, data motion:0.06279373168945312
dm-11, exec:43.08871030807495, overhead:0.5950868129730225
dm-6, data motion:0.07018899917602539
dm-6, exec:44.541293144226074, overhead:0.9157543182373047
dm-5, data motion:0.06949448585510254
dm-5, exec:44.713789224624634, overhead:0.9397952556610107
dm-1, data motion:0.07021284103393555
dm-1, exec:45.16053485870361, overhead:0.6190412044525146
kernel:0.06571483612060547
emu-kernel-7, exec:44.81843328475952, overhead:0.924452543258667
dm-13, data motion:0.07003045082092285
dm-13, exec:44.324573040008545, overhead:0.40412259101867676
dm-4, data motion:0.07421410083770752
dm-4, exec:45.89364790916443, overhead:0.5479342937469482
dm-14, data motion:0.07328689098358154
dm-14, exec:44.40027475357056, overhead:0.43913912773132324
dm-2, data motion:0.0727992057800293
dm-2, exec:45.94885587692261, overhead:0.6592502593994141
dm-10, data motion:0.07129383087158203
dm-10, exec:44.94177746772766, overhead:0.6589710712432861
dm-3, data motion:0.07517015933990479
dm-3, exec:45.94612216949463, overhead:0.719907283782959
dm-8, data motion:0.07461428642272949
dm-8, exec:45.343958616256714, overhead:0.8990147113800049
dm-7, data motion:0.07506263256072998
dm-7, exec:45.92887568473816, overhead:0.7546851634979248
total_req_latency:47.10034513473511
per_req_latency:0.09420069026947021
94.201
```

### (16 physical cores, 8 way of LLC, 80% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 5000    
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_aes 1 16 1`  

Output:  
```
kernel:0.06578826904296875
emu-kernel-0, exec:352.01356959342957, overhead:0.1049501895904541
dm-0, data motion:0.011271357536315918
dm-0, exec:352.04679703712463, overhead:0.08953166007995605
total_req_latency:352.15565967559814
per_req_latency:0.07043113193511963
70.431
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_aes 5 16 1`

Output:  
```
kernel:0.06578755378723145
emu-kernel-4, exec:140.89512276649475, overhead:0.34041357040405273
kernel:0.0657346248626709
emu-kernel-3, exec:140.89155793190002, overhead:0.3480095863342285
kernel:0.06574058532714844
emu-kernel-0, exec:140.90391564369202, overhead:0.3625068664550781
dm-4, data motion:0.012549638748168945
dm-4, exec:140.99842977523804, overhead:0.2564399242401123
dm-3, data motion:0.012557744979858398
dm-3, exec:140.94726586341858, overhead:0.31201720237731934
kernel:0.06573629379272461
emu-kernel-2, exec:140.9064164161682, overhead:0.3551754951477051
kernel:0.0657355785369873
emu-kernel-1, exec:140.90489530563354, overhead:0.37375879287719727
dm-0, data motion:0.012547492980957031
dm-0, exec:141.04748034477234, overhead:0.23931193351745605
dm-2, data motion:0.012441039085388184
dm-2, exec:140.9774956703186, overhead:0.3034934997558594
dm-1, data motion:0.011229515075683594
dm-1, exec:140.993305683136, overhead:0.3030362129211426
total_req_latency:141.3196485042572
per_req_latency:0.0706598242521286
70.660
```

Command: 10 emulated kernels, using iterations = 1500
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_aes 10 16 1`

Output:  
```
kernel:0.06574249267578125
emu-kernel-3, exec:107.19406390190125, overhead:0.6559164524078369
dm-3, data motion:0.015975356101989746
dm-3, exec:107.5213737487793, overhead:0.3511333465576172
kernel:0.06574225425720215
emu-kernel-4, exec:107.21530723571777, overhead:0.6592788696289062
kernel:0.06574344635009766
emu-kernel-0, exec:107.38281989097595, overhead:0.5063834190368652
kernel:0.06574773788452148
emu-kernel-2, exec:107.19668555259705, overhead:0.7063801288604736
kernel:0.06574296951293945
emu-kernel-5, exec:107.23081302642822, overhead:0.6637523174285889
dm-4, data motion:0.017511963844299316
dm-4, exec:107.46506142616272, overhead:0.43534183502197266
dm-0, data motion:0.017567753791809082
dm-0, exec:107.41366600990295, overhead:0.502199649810791
dm-2, data motion:0.015987038612365723
dm-2, exec:107.57568955421448, overhead:0.3503572940826416
dm-5, data motion:0.01614832878112793
dm-5, exec:107.46162843704224, overhead:0.45569705963134766
kernel:0.06574618816375732
emu-kernel-1, exec:107.20818257331848, overhead:0.7220618724822998
kernel:0.06574344635009766
emu-kernel-6, exec:107.2024974822998, overhead:0.667374849319458
dm-1, data motion:0.016097187995910645
dm-1, exec:107.62005686759949, overhead:0.3297262191772461
dm-6, data motion:0.016291499137878418
dm-6, exec:107.23655819892883, overhead:0.4071462154388428
kernel:0.06574535369873047
emu-kernel-8, exec:107.21217584609985, overhead:0.5287048816680908
kernel:0.06574177742004395
emu-kernel-9, exec:107.20886993408203, overhead:0.39191460609436035
dm-9, data motion:0.01764678955078125
dm-9, exec:107.3193633556366, overhead:0.35925960540771484
dm-8, data motion:0.017601609230041504
dm-8, exec:107.30757689476013, overhead:0.5071241855621338
kernel:0.06574344635009766
emu-kernel-7, exec:107.23871088027954, overhead:0.5959463119506836
dm-7, data motion:0.016260385513305664
dm-7, exec:107.39541935920715, overhead:0.5189464092254639
total_req_latency:108.02081251144409
per_req_latency:0.07201387500762939
72.014
```

Command: 15 emulated kernels, using iterations = 750
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_aes 15 16 1`

Output:  
```
kernel:0.06578433513641357
emu-kernel-5, exec:67.82382988929749, overhead:0.7244999408721924
dm-5, data motion:0.0602726936340332
dm-5, exec:68.17378950119019, overhead:0.45249009132385254
kernel:0.06577539443969727
emu-kernel-2, exec:68.05192232131958, overhead:0.6912319660186768
kernel:0.06577920913696289
emu-kernel-8, exec:67.92721939086914, overhead:0.6646490097045898
dm-2, data motion:0.06033766269683838
dm-2, exec:68.46828317642212, overhead:0.37525343894958496
kernel:0.06577825546264648
emu-kernel-6, exec:67.95598983764648, overhead:0.8407166004180908
dm-6, data motion:0.06047868728637695
dm-6, exec:68.21096110343933, overhead:0.44363951683044434
dm-8, data motion:0.06024587154388428
dm-8, exec:68.32109117507935, overhead:0.4030725955963135
kernel:0.06577575206756592
emu-kernel-0, exec:68.23979878425598, overhead:0.7944033145904541
dm-0, data motion:0.060632944107055664
dm-0, exec:68.63602471351624, overhead:0.43507862091064453
kernel:0.06577706336975098
emu-kernel-9, exec:68.24958181381226, overhead:0.5331151485443115
dm-9, data motion:0.060428619384765625
dm-9, exec:68.45207047462463, overhead:0.34694647789001465
kernel:0.06577980518341064
emu-kernel-13, exec:68.08885598182678, overhead:0.3609287738800049
dm-13, data motion:0.060172080993652344
dm-13, exec:68.18839716911316, overhead:0.2797572612762451
kernel:0.06579005718231201
emu-kernel-3, exec:68.68801665306091, overhead:0.6879427433013916
kernel:0.06578254699707031
emu-kernel-1, exec:68.55784940719604, overhead:0.830944299697876
dm-3, data motion:0.06039106845855713
dm-3, exec:68.98594355583191, overhead:0.4152851104736328
dm-1, data motion:0.060268521308898926
dm-1, exec:69.07914757728577, overhead:0.3347005844116211
kernel:0.06578028202056885
emu-kernel-4, exec:68.59990525245667, overhead:0.8160827159881592
dm-4, data motion:0.06057465076446533
dm-4, exec:69.05779123306274, overhead:0.3797178268432617
kernel:0.06577932834625244
emu-kernel-14, exec:68.41723346710205, overhead:0.28537797927856445
dm-14, data motion:0.060450196266174316
dm-14, exec:68.52469730377197, overhead:0.22334527969360352
kernel:0.06577467918395996
emu-kernel-7, exec:68.62085461616516, overhead:0.8718633651733398
dm-7, data motion:0.060389041900634766
dm-7, exec:68.91785311698914, overhead:0.5946946144104004
kernel:0.06578779220581055
emu-kernel-12, exec:68.62147998809814, overhead:0.3449363708496094
dm-12, data motion:0.0605090856552124
dm-12, exec:68.7403564453125, overhead:0.2590768337249756
kernel:0.06577980518341064
emu-kernel-10, exec:68.66349077224731, overhead:0.5007612705230713
dm-10, data motion:0.060441017150878906
dm-10, exec:68.94459748268127, overhead:0.23918366432189941
kernel:0.06577587127685547
emu-kernel-11, exec:68.78582453727722, overhead:0.4501035213470459
dm-11, data motion:0.06038689613342285
dm-11, exec:68.97212147712708, overhead:0.20335888862609863
total_req_latency:69.82661485671997
per_req_latency:0.0931021531422933
93.102
```

## Benchmark 5: Gzip -> hash-join

### (4 physical cores, 2 way of LLC, 20% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000  
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_gzip 1 4 1`  

Output:  
```
kernel:0.0335085391998291
emu-kernel-0, exec:402.089492559433, overhead:0.4296259880065918
dm-0, data motion:0.12103450298309326
dm-0, exec:410.4752461910248, overhead:0.33942437171936035
total_req_latency:410.83719062805176
per_req_latency:0.13694573020935058
136.946
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_gzip 5 4 1`

Output:  
```
kernel:0.03346753120422363
emu-kernel-1, exec:378.6711926460266, overhead:1.1233670711517334
kernel:0.03346753120422363
emu-kernel-4, exec:380.18134927749634, overhead:0.8435769081115723
kernel:0.03346753120422363
emu-kernel-2, exec:382.18989086151123, overhead:1.1011106967926025
kernel:0.033468008041381836
emu-kernel-0, exec:388.98288202285767, overhead:1.1043975353240967
dm-1, data motion:0.15212512016296387
dm-1, exec:390.1847219467163, overhead:0.7239582538604736
dm-4, data motion:0.15240919589996338
dm-4, exec:390.64951515197754, overhead:0.926950216293335
dm-2, data motion:0.15543127059936523
dm-2, exec:392.40956377983093, overhead:0.8190100193023682
kernel:0.03346753120422363
emu-kernel-3, exec:392.8218412399292, overhead:1.1863386631011963
dm-0, data motion:0.1560649871826172
dm-0, exec:398.3476643562317, overhead:0.7004079818725586
dm-3, data motion:0.15480589866638184
dm-3, exec:401.65257835388184, overhead:0.7949156761169434
total_req_latency:402.5497360229492
per_req_latency:0.20127486801147462
201.275
```

Command: 10 emulated kernels, using iterations = 1000 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_gzip 10 4 1`

Output:  
```
kernel:0.033461570739746094
emu-kernel-3, exec:299.92877674102783, overhead:2.155719041824341
kernel:0.033461570739746094
emu-kernel-8, exec:301.1992995738983, overhead:1.0640883445739746
kernel:0.033461809158325195
emu-kernel-2, exec:301.95407581329346, overhead:2.3835580348968506
kernel:0.033461570739746094
emu-kernel-4, exec:302.75696563720703, overhead:1.7034521102905273
dm-3, data motion:0.2899719476699829
dm-3, exec:319.06114530563354, overhead:1.2270214557647705
dm-8, data motion:0.2875860929489136
dm-8, exec:319.12269163131714, overhead:1.2269387245178223
dm-2, data motion:0.29149091243743896
dm-2, exec:321.5401780605316, overhead:0.5722620487213135
dm-4, data motion:0.28836214542388916
dm-4, exec:321.05437541007996, overhead:0.9313340187072754
kernel:0.0334627628326416
emu-kernel-6, exec:383.6467912197113, overhead:1.5326528549194336
kernel:0.03346109390258789
emu-kernel-1, exec:385.16068053245544, overhead:1.5908632278442383
kernel:0.033463120460510254
emu-kernel-9, exec:387.2590274810791, overhead:1.0352420806884766
kernel:0.0334627628326416
emu-kernel-0, exec:388.79423451423645, overhead:1.579216480255127
kernel:0.0334622859954834
emu-kernel-7, exec:387.6657168865204, overhead:1.2197515964508057
kernel:0.0334627628326416
emu-kernel-5, exec:389.4880599975586, overhead:1.7597289085388184
dm-1, data motion:0.40394842624664307
dm-1, exec:397.40023493766785, overhead:1.0720429420471191
dm-9, data motion:0.40322649478912354
dm-9, exec:398.6017391681671, overhead:0.958749532699585
dm-6, data motion:0.40568745136260986
dm-6, exec:399.4261248111725, overhead:0.8147051334381104
dm-0, data motion:0.4076046943664551
dm-0, exec:401.2554895877838, overhead:0.5494191646575928
dm-5, data motion:0.4055330753326416
dm-5, exec:401.93681836128235, overhead:1.0009875297546387
dm-7, data motion:0.40567922592163086
dm-7, exec:402.4640054702759, overhead:0.566411018371582
total_req_latency:404.31476855278015
per_req_latency:0.40431476855278015
404.315
```

Command: 15 emulated kernels, using iterations = 500 
`sudo rdtset -t 'mba=20;l3=0x03;cpu=0,2,4,8' -c 0,2,4,8  python3 kernel_dm_pair.py concat_cast_flatten_gzip 15 4 1`

Output:  
```
kernel:0.03345966339111328
emu-kernel-11, exec:212.29880809783936, overhead:1.8314499855041504
kernel:0.03346049785614014
emu-kernel-7, exec:212.88062858581543, overhead:2.078726053237915
kernel:0.03346085548400879
emu-kernel-12, exec:213.12160301208496, overhead:1.4194166660308838
kernel:0.03346061706542969
emu-kernel-13, exec:214.32841753959656, overhead:1.0117926597595215
kernel:0.03345942497253418
emu-kernel-2, exec:215.35675024986267, overhead:2.836636781692505
kernel:0.03346097469329834
emu-kernel-14, exec:214.2785816192627, overhead:0.7811934947967529
dm-11, data motion:0.41477930545806885
dm-11, exec:240.17651295661926, overhead:0.8851134777069092
dm-7, data motion:0.4113858938217163
dm-7, exec:241.03523325920105, overhead:0.8101117610931396
dm-12, data motion:0.4162205457687378
dm-12, exec:240.75814390182495, overhead:0.9425790309906006
dm-2, data motion:0.41833531856536865
dm-2, exec:243.4436798095703, overhead:1.158508539199829
dm-13, data motion:0.41655588150024414
dm-13, exec:241.664648771286, overhead:0.7864401340484619
dm-14, data motion:0.41618597507476807
dm-14, exec:241.48902773857117, overhead:0.618959903717041
kernel:0.0334622859954834
emu-kernel-5, exec:265.4192519187927, overhead:2.4356887340545654
kernel:0.033461809158325195
emu-kernel-4, exec:265.61076164245605, overhead:2.4913625717163086
kernel:0.033460140228271484
emu-kernel-9, exec:265.12204098701477, overhead:1.9412384033203125
kernel:0.0334620475769043
emu-kernel-3, exec:266.5113682746887, overhead:2.711397647857666
dm-4, data motion:0.555525541305542
dm-4, exec:284.4843039512634, overhead:1.4354171752929688
dm-5, data motion:0.5546814203262329
dm-5, exec:284.6185145378113, overhead:1.1509194374084473
dm-9, data motion:0.5613667964935303
dm-9, exec:284.0054130554199, overhead:0.7304494380950928
dm-3, data motion:0.5598176717758179
dm-3, exec:285.34430956840515, overhead:1.3390369415283203
kernel:0.03346145153045654
emu-kernel-1, exec:287.58351826667786, overhead:1.7852516174316406
kernel:0.03346121311187744
emu-kernel-10, exec:286.881564617157, overhead:1.4518764019012451
kernel:0.033461809158325195
emu-kernel-8, exec:293.5681948661804, overhead:1.6316635608673096
kernel:0.03346216678619385
emu-kernel-6, exec:294.1114947795868, overhead:2.523205041885376
kernel:0.03346109390258789
emu-kernel-0, exec:296.20686626434326, overhead:1.8240869045257568
dm-1, data motion:0.6834831237792969
dm-1, exec:300.34956979751587, overhead:0.753993034362793
dm-10, data motion:0.6938661336898804
dm-10, exec:298.5035331249237, overhead:1.3870699405670166
dm-6, data motion:0.695191502571106
dm-6, exec:304.7052867412567, overhead:1.2196216583251953
dm-8, data motion:0.6968979835510254
dm-8, exec:304.3197720050812, overhead:0.9702045917510986
dm-0, data motion:0.6888341903686523
dm-0, exec:306.53642988204956, overhead:0.5502676963806152
total_req_latency:307.1081907749176
per_req_latency:0.6142163815498352
614.216
```

### (8 physical cores, 4 way of LLC, 40% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 3000 
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_gzip 1 8 1`  

Output:  
```
kernel:0.03350186347961426
emu-kernel-0, exec:222.01082563400269, overhead:0.16498875617980957
dm-0, data motion:0.06859898567199707
dm-0, exec:226.64980506896973, overhead:0.14361095428466797
total_req_latency:226.81321215629578
per_req_latency:0.07560440405209859
75.604
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_gzip 5 8 1`

Output:  
```
kernel:0.03350973129272461
emu-kernel-1, exec:195.48945593833923, overhead:0.6321582794189453
kernel:0.03350996971130371
emu-kernel-3, exec:199.49940967559814, overhead:0.6412210464477539
kernel:0.03350996971130371
emu-kernel-2, exec:199.93666768074036, overhead:0.6284739971160889
dm-1, data motion:0.09044921398162842
dm-1, exec:201.7106716632843, overhead:0.5496904850006104
dm-3, data motion:0.09155130386352539
dm-3, exec:205.7643918991089, overhead:0.35877394676208496
dm-2, data motion:0.09221255779266357
dm-2, exec:205.78756022453308, overhead:0.49849843978881836
kernel:0.03350996971130371
emu-kernel-0, exec:212.19138503074646, overhead:0.6014246940612793
dm-0, data motion:0.10021364688873291
dm-0, exec:217.37119030952454, overhead:0.47811174392700195
kernel:0.033509254455566406
emu-kernel-4, exec:224.00889945030212, overhead:0.6235556602478027
dm-4, data motion:0.10632181167602539
dm-4, exec:228.66272711753845, overhead:0.16689205169677734
total_req_latency:229.28760075569153
per_req_latency:0.11464380037784576
114.644
```

Command: 10 emulated kernels, using iterations = 1000
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_gzip 10 8 1`

Output:  
```
kernel:0.03346681594848633
emu-kernel-8, exec:152.78852605819702, overhead:0.7356255054473877
kernel:0.03346729278564453
emu-kernel-4, exec:152.97954726219177, overhead:1.2268481254577637
kernel:0.03346681594848633
emu-kernel-6, exec:162.000390291214, overhead:0.8432557582855225
dm-8, data motion:0.13032305240631104
dm-8, exec:162.11015701293945, overhead:0.6030652523040771
dm-4, data motion:0.1299344301223755
dm-4, exec:163.35226583480835, overhead:0.7230770587921143
kernel:0.03346657752990723
emu-kernel-0, exec:163.43136072158813, overhead:1.2919328212738037
kernel:0.03346729278564453
emu-kernel-1, exec:164.61292815208435, overhead:1.2885055541992188
kernel:0.03346729278564453
emu-kernel-9, exec:166.38847088813782, overhead:0.5033142566680908
kernel:0.03346681594848633
emu-kernel-3, exec:167.5996596813202, overhead:1.2523393630981445
kernel:0.03346705436706543
emu-kernel-2, exec:168.63284635543823, overhead:1.3202102184295654
dm-6, data motion:0.13445377349853516
dm-6, exec:170.2347867488861, overhead:0.6872448921203613
dm-0, data motion:0.14028751850128174
dm-0, exec:172.35233068466187, overhead:0.5980410575866699
dm-1, data motion:0.14286136627197266
dm-1, exec:173.2012197971344, overhead:0.46993017196655273
kernel:0.03346705436706543
emu-kernel-7, exec:172.85500526428223, overhead:0.7147114276885986
dm-9, data motion:0.14133179187774658
dm-9, exec:173.9077229499817, overhead:0.5390884876251221
dm-3, data motion:0.14080369472503662
dm-3, exec:175.36431789398193, overhead:0.5831718444824219
dm-2, data motion:0.14238429069519043
dm-2, exec:176.1236436367035, overhead:0.7383832931518555
kernel:0.03346729278564453
emu-kernel-5, exec:177.61342334747314, overhead:1.09531831741333
dm-7, data motion:0.14664244651794434
dm-7, exec:178.74080228805542, overhead:0.7472355365753174
dm-5, data motion:0.1536259651184082
dm-5, exec:182.90462183952332, overhead:0.7232036590576172
total_req_latency:183.72901010513306
per_req_latency:0.18372901010513307
183.729
```

Command: 15 emulated kernels, using iterations = 500
`sudo rdtset -t 'mba=40;l3=0x0f;cpu=0,2,4,8,10,12,14,16' -c 0,2,4,8,10,12,14,16  python3 kernel_dm_pair.py concat_cast_flatten_gzip 15 8 1`

Output:  
```
kernel:0.03346669673919678
emu-kernel-4, exec:110.60974717140198, overhead:1.3274896144866943
kernel:0.03346681594848633
emu-kernel-11, exec:111.6845350265503, overhead:0.8150684833526611
kernel:0.03346526622772217
emu-kernel-9, exec:111.85096263885498, overhead:0.9154062271118164
kernel:0.033466339111328125
emu-kernel-6, exec:113.0318067073822, overhead:1.003469705581665
kernel:0.033466339111328125
emu-kernel-3, exec:114.52278757095337, overhead:1.2918102741241455
kernel:0.033466339111328125
emu-kernel-8, exec:114.95442342758179, overhead:0.9402194023132324
kernel:0.03346681594848633
emu-kernel-1, exec:116.10953640937805, overhead:1.3189332485198975
kernel:0.03346753120422363
emu-kernel-12, exec:116.62695956230164, overhead:0.628375768661499
kernel:0.03346681594848633
emu-kernel-2, exec:117.33999133110046, overhead:1.2967290878295898
kernel:0.03346729278564453
emu-kernel-10, exec:117.58217406272888, overhead:0.9707009792327881
kernel:0.03346657752990723
emu-kernel-13, exec:118.35269141197205, overhead:0.5790703296661377
kernel:0.03346681594848633
emu-kernel-0, exec:119.9901750087738, overhead:0.9146139621734619
kernel:0.03346717357635498
emu-kernel-7, exec:121.25996398925781, overhead:1.3829984664916992
kernel:0.03346681594848633
emu-kernel-14, exec:121.94398093223572, overhead:0.5310184955596924
dm-4, data motion:0.2338477373123169
dm-4, exec:126.23906922340393, overhead:0.5954396724700928
kernel:0.033466339111328125
emu-kernel-5, exec:125.96687889099121, overhead:1.1398494243621826
dm-11, data motion:0.2357553243637085
dm-11, exec:126.46179413795471, overhead:0.3946199417114258
dm-9, data motion:0.23183465003967285
dm-9, exec:127.22597670555115, overhead:0.5354170799255371
dm-6, data motion:0.24162554740905762
dm-6, exec:128.1077115535736, overhead:0.6516869068145752
dm-3, data motion:0.23943400382995605
dm-3, exec:129.15094995498657, overhead:0.36190223693847656
dm-8, data motion:0.24111151695251465
dm-8, exec:129.00073909759521, overhead:0.5586445331573486
dm-1, data motion:0.24975788593292236
dm-1, exec:130.78378796577454, overhead:0.556718111038208
dm-2, data motion:0.24202477931976318
dm-2, exec:131.24707794189453, overhead:0.5216615200042725
dm-10, data motion:0.25027358531951904
dm-10, exec:130.55055356025696, overhead:0.5231091976165771
dm-12, data motion:0.25595641136169434
dm-12, exec:130.51228094100952, overhead:0.506657600402832
dm-0, data motion:0.2579993009567261
dm-0, exec:132.1898810863495, overhead:0.5301175117492676
dm-13, data motion:0.2476050853729248
dm-13, exec:130.93492364883423, overhead:0.4231278896331787
dm-7, data motion:0.2622702121734619
dm-7, exec:131.8928804397583, overhead:0.6584289073944092
dm-14, data motion:0.26232242584228516
dm-14, exec:132.20972418785095, overhead:0.3311495780944824
dm-5, data motion:0.265483021736145
dm-5, exec:134.30337047576904, overhead:0.6591699123382568
total_req_latency:135.21852350234985
per_req_latency:0.2704370470046997
270.437
```

### (16 physical cores, 8 way of LLC, 80% of memory bandwidth)
Command: 1 emulated kernels, using iterations = 5000    
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_gzip 1 16 1`  

Output:  
```
kernel:0.03350257873535156
emu-kernel-0, exec:307.91324949264526, overhead:0.13947391510009766
dm-0, data motion:0.0567474365234375
dm-0, exec:311.7539083957672, overhead:0.11807012557983398
total_req_latency:311.89225673675537
per_req_latency:0.06237845134735107
62.378
```

Command: 5 emulated kernels, using iterations = 2000
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_gzip 5 16 1`

Output:  
```
kernel:0.03350400924682617
emu-kernel-3, exec:186.32424354553223, overhead:0.36170363426208496
dm-3, data motion:0.08719301223754883
dm-3, exec:192.19181442260742, overhead:0.3028981685638428
kernel:0.033509016036987305
emu-kernel-0, exec:196.51338601112366, overhead:0.3718411922454834
kernel:0.03351020812988281
emu-kernel-1, exec:200.797917842865, overhead:0.3682723045349121
dm-0, data motion:0.09163546562194824
dm-0, exec:201.78517627716064, overhead:0.3500339984893799
dm-1, data motion:0.09197807312011719
dm-1, exec:206.27321028709412, overhead:0.3099346160888672
kernel:0.033509254455566406
emu-kernel-4, exec:213.46497058868408, overhead:0.36574769020080566
kernel:0.03350949287414551
emu-kernel-2, exec:217.57483386993408, overhead:0.3804326057434082
dm-4, data motion:0.10107624530792236
dm-4, exec:218.3789849281311, overhead:0.2875497341156006
dm-2, data motion:0.10269737243652344
dm-2, exec:221.67392826080322, overhead:0.2903616428375244
total_req_latency:221.99450039863586
per_req_latency:0.11099725019931793
110.997
```

Command: 5 emulated kernels, using iterations = 1500
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_gzip 10 16 1`

Output:  
```
kernel:0.033533334732055664
emu-kernel-8, exec:199.09311842918396, overhead:0.522817850112915
kernel:0.033533573150634766
emu-kernel-6, exec:201.1758086681366, overhead:0.674518346786499
dm-8, data motion:0.12083268165588379
dm-8, exec:207.66067671775818, overhead:0.48711180686950684
dm-6, data motion:0.12169337272644043
dm-6, exec:209.48199033737183, overhead:0.36317920684814453
kernel:0.03353404998779297
emu-kernel-7, exec:210.0710163116455, overhead:0.6796698570251465
kernel:0.033532142639160156
emu-kernel-5, exec:214.64180946350098, overhead:0.6984241008758545
dm-7, data motion:0.1273949146270752
dm-7, exec:217.92448616027832, overhead:0.5628209114074707
kernel:0.03353238105773926
emu-kernel-3, exec:218.4434688091278, overhead:0.7055056095123291
dm-5, data motion:0.13053417205810547
dm-5, exec:221.87642335891724, overhead:0.41234731674194336
kernel:0.033533334732055664
emu-kernel-2, exec:224.511577129364, overhead:0.7292678356170654
dm-3, data motion:0.1334371566772461
dm-3, exec:225.1818027496338, overhead:0.38341331481933594
dm-2, data motion:0.13719141483306885
dm-2, exec:230.9594395160675, overhead:0.41129302978515625
kernel:0.033531904220581055
emu-kernel-4, exec:231.160551071167, overhead:0.7181851863861084
kernel:0.03353118896484375
emu-kernel-1, exec:234.92238855361938, overhead:0.7329850196838379
dm-4, data motion:0.1453632116317749
dm-4, exec:236.9533565044403, overhead:0.38390445709228516
dm-1, data motion:0.1500941514968872
dm-1, exec:240.48408699035645, overhead:0.32259273529052734
kernel:0.03352856636047363
emu-kernel-0, exec:247.12036728858948, overhead:0.7444784641265869
kernel:0.033528804779052734
emu-kernel-9, exec:248.42764043807983, overhead:0.3748955726623535
dm-0, data motion:0.16748476028442383
dm-0, exec:251.94268679618835, overhead:0.5308384895324707
dm-9, data motion:0.16605150699615479
dm-9, exec:253.01890635490417, overhead:0.34705638885498047
total_req_latency:253.7654709815979
per_req_latency:0.1691769806543986
169.177
```

Command: 5 emulated kernels, using iterations = 750
`sudo rdtset -t 'mba=80;l3=0xff;cpu=0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30' -c 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30 python3 kernel_dm_pair.py concat_cast_flatten_gzip 15 16 1`

Output:  
```
kernel:0.0335468053817749
emu-kernel-11, exec:133.46885347366333, overhead:0.46349287033081055
kernel:0.03355062007904053
emu-kernel-1, exec:135.07729029655457, overhead:0.850576639175415
kernel:0.033537864685058594
emu-kernel-8, exec:140.3992886543274, overhead:0.6591081619262695
dm-11, data motion:0.16390001773834229
dm-11, exec:145.11713457107544, overhead:0.29525279998779297
kernel:0.03355228900909424
emu-kernel-13, exec:145.2647340297699, overhead:0.3237144947052002
kernel:0.03353548049926758
emu-kernel-4, exec:146.31012177467346, overhead:0.692469596862793
dm-1, data motion:0.17041397094726562
dm-1, exec:147.18283772468567, overhead:0.3401167392730713
kernel:0.0335538387298584
emu-kernel-6, exec:147.6654510498047, overhead:0.6426224708557129
kernel:0.03354346752166748
emu-kernel-10, exec:150.8385226726532, overhead:0.5345227718353271
dm-8, data motion:0.17480194568634033
dm-8, exec:151.74892354011536, overhead:0.5063705444335938
kernel:0.03354763984680176
emu-kernel-9, exec:151.38499975204468, overhead:0.6749744415283203
dm-13, data motion:0.1774827241897583
dm-13, exec:155.93386960029602, overhead:0.24322295188903809
dm-4, data motion:0.17998671531677246
dm-4, exec:156.8400480747223, overhead:0.41756463050842285
kernel:0.03354191780090332
emu-kernel-7, exec:157.21656465530396, overhead:0.8182103633880615
dm-6, data motion:0.18442118167877197
dm-6, exec:158.44238352775574, overhead:0.4590122699737549
dm-10, data motion:0.18802738189697266
dm-10, exec:160.9464590549469, overhead:0.3867051601409912
dm-9, data motion:0.18913233280181885
dm-9, exec:161.41163420677185, overhead:0.4904520511627197
kernel:0.03354477882385254
emu-kernel-2, exec:162.20858073234558, overhead:0.8309586048126221
kernel:0.03353893756866455
emu-kernel-5, exec:164.78234243392944, overhead:0.48533082008361816
dm-7, data motion:0.19668316841125488
dm-7, exec:165.45696783065796, overhead:0.6546816825866699
kernel:0.033539652824401855
emu-kernel-12, exec:165.48580980300903, overhead:0.3469655513763428
kernel:0.03353321552276611
emu-kernel-14, exec:166.451256275177, overhead:0.2889425754547119
kernel:0.03353762626647949
emu-kernel-3, exec:167.41913628578186, overhead:0.8354172706604004
kernel:0.03353381156921387
emu-kernel-0, exec:167.6567883491516, overhead:0.7577617168426514
dm-2, data motion:0.20827198028564453
dm-2, exec:169.83642506599426, overhead:0.44463491439819336
dm-5, data motion:0.213905930519104
dm-5, exec:171.63446354866028, overhead:0.542304515838623
dm-12, data motion:0.21832025051116943
dm-12, exec:172.414972782135, overhead:0.3110983371734619
dm-14, data motion:0.21926867961883545
dm-14, exec:173.12694025039673, overhead:0.1949160099029541
dm-0, data motion:0.2201709747314453
dm-0, exec:174.18760704994202, overhead:0.49256277084350586
dm-3, data motion:0.2212517261505127
dm-3, exec:174.22928094863892, overhead:0.4493722915649414
total_req_latency:174.71228504180908
per_req_latency:0.23294971338907877
232.950
```