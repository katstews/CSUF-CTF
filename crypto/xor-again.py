cipher = [120, 114, 127, 121, 101, 47, 106, 65, 109, 106, 42, 108, 106, 109, 65, 105, 47, 106, 118, 65, 120, 114, 42, 121, 99]

flag = []

for z in range(1,50):
    for x in cipher: 
        y = x ^ z 
        flag.append(y)
    if b'flag{' in bytes(flag):
        print(bytes(flag))
    flag.clear()
    