#each value was xor'd with the next value, so nothing encrypted 27
cipher = [102, 10, 13, 6, 28, 74, 69, 43, 108, 93, 
 13, 17, 11, 9, 4, 7, 44, 110, 69, 7, 64,
 95, 10, 27]

flag = []
previous = 102

for x in range(1,len(cipher)):
    y = cipher[x] ^ previous
    previous = y
    flag.append(y)
    
    
print(bytes(flag))
print(102^10)
# print(ord("l"))
print(chr(108^13))
