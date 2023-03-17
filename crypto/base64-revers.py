import base64

r_alphabet = "/+9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
cipher = "mZOemISdy5yUiMuNm4ygiM+Igv"

place = []
bin_string = []
final_bin = []
flag = []

for x in cipher:
    place.append(r_alphabet.index(x))

for x in place:
    bin_string.append(bin(x)[2:].zfill(8))
    # print(bin(x)[2:].zfill(8))
for x in bin_string:
    final_bin.append((x[2:]))

final_bin = "".join(final_bin)
chunks = [final_bin[i:i+8] for i in range(0, len(final_bin), 8)]

for x in chunks:
    flag.append(int(x,2))
print(bytes(flag))