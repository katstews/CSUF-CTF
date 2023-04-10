#reverse this function encrypt. so decrypt. 
import string

alph = string.printable #prints all letters+alpha+specialchar
#0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 

#encrypted_flag = "flah{T3y3V58_t0 fCn1"
#the original flag was encrypted using the below function!

flag = []

def encrypt(s):
    encoded = []
    for i, c in enumerate(s):
        index = alph.index(c) #letter position in alph
        shifted_index = (index + (i % 2) * (i // 2)) % len(alph)
        #len of alph will never change
        encoded.append(alph[shifted_index])
    return ''.join(encoded)

# print(m)
# print(alph.index("j"))

#first letter will be 0,1,2,..mod by 2 * div by 2
def decrypt(s):
    #reverse encrypt
    for i,c in enumerate(s):
        cipher_index = alph.index(c)
        val = cipher_index - (((i%2) * (i//2)) % len(alph))
        flag.append(alph[val])
    print("".join(flag))

print(decrypt("flah{T3y3V58_t0 fCn1"))