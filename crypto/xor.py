val = [51, 57, 52, 50, 46, 45, 101, 39, 10, 55, 101, 33, 61, 10, 34, 97, 44, 38, 40]
flag = []

for x in val: 
    y = x ^ 85 
    flag.append(y)
print(bytes(flag))