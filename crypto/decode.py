import base64

f = open("cipher", "r")

s = f.read()

for x in range(25): 
    s = base64.b64decode(s)
print(s)