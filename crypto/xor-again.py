cipher = [121, 115, 126, 120, 100, 46, 107, 64, 108, 107, 43, 109, 107, 108, 64, 104, 46, 107, 119, 64, 121, 115, 43, 120, 98]
flag = []

#I just brute-forced this until i found the flag... 
for z in range(1,50):
    for x in cipher: 
        y = x ^ z 
        flag.append(y)
    if b'flag{' in bytes(flag): #if whatever contains "flag{"
        print(bytes(flag))
    flag.clear() #make sure to clear list after each iter. or it will be HUGE
    