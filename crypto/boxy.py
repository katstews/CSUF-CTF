encflag = "4670472452252025711303017137232076457155711523032423554456"
flag = []
matrix = [
['B', 'u', 'D', '0', 'X', 's', 'z', 'S'],
['S', 'k', 'h', 'y', 'E', 'p', 'x', 'o'], 
['1', 'Q', 'F', 'r', 'g', 'd', 'b', 'V'],
['M', 'j', '8', 'K', 'W', 'v', 'i', 'w'],
['I', 'Z', 'C', '3', 'm', 'e', 'f', 'a'],
['5', 'L', '{', '6', 'O', '4', '}', 'R'],
['c', 'q', 'n', 'H', 'G', 'N', 'U', 'Y'],
['l', '_', 'G', '7', 'T', 'P', 't', 'A'],
]

txt = list(encflag)

result = [txt[x:x+2] for x in range(0,len(txt),2)]
 
for x in result: 
    y = matrix[int(x[0])][int(x[1])]
    flag.append(y)
print("".join(flag))    
