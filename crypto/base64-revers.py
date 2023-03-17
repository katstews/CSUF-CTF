#had to implement my own custom base64 decoder using
#the given 64-bit long string
import base64

r_alphabet = "/+9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
cipher = "mZOemISdy5yUiMuNm4ygiM+Igv"

place = []
bin_string = []
final_bin = []
flag = []

#1. find where each letter in cipher belongs in r_alphabet, return its index
for x in cipher:
    place.append(r_alphabet.index(x)) 

#2. take that index # and convert into its respective 8 bit value
for x in place:
    bin_string.append(bin(x)[2:].zfill(8))
    # print(bin(x)[2:].zfill(8))

#3. remove the first two zeros in every byte in the list
for x in bin_string:
    final_bin.append((x[2:]))

#4. combine all of the 6 bits together into one long binary string. 
final_bin = "".join(final_bin)

#5. take the 6 bits and combine them again to form 1 byte
chunks = [final_bin[i:i+8] for i in range(0, len(final_bin), 8)]

#5. convert each byte into its respective base 2, char value!!!
for x in chunks:
    flag.append(int(x,2))
print(bytes(flag)) #woooooooo