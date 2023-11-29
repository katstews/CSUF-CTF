mainly just for me to keep track of how I even was able to solve these challenges. 

## pwn - how2flag (bufferover flow challenge)
### ~~4/10/23~~
### 11/29/23 
I just learned out how to do a buffer overflow using python. Very interesting. First off in the pwn challenge, I was given a binary file and a C file containing how the program worked. The binary file was a executable ELF file. I used objdump to disassemble the elf file, meaning I "reverse engineered" the executable to try to find the closest match to its original C code. To do an bufferoverflow exploit, you would need to know the size of the buffer you want to exploit **plus** the address of the function you want to exploit. How it works is once you exploit the buffer you want to the tell the program what address you want to access. 

In this case objdump would work, but a friend recommended I try ghidra. Had to open it up with Kali, as it was too difficult (too much workkkk) to install on M1. Anyways, with the guidance of a friend, I found that the actual size of the buffer was not 64 but actually "0x48" which is 73 in decimal.

<img width="902" alt="Screenshot 2023-04-10 at 4 11 19 PM" src="https://user-images.githubusercontent.com/112781868/231016331-c9831d2d-5f00-484c-bd51-7e4bc35b819c.png">

As shown in the image, the actual size of the buffer was 73 🤔. So the input I needed to be shy of the size 73. Using Ghidra (or objdump), I was also able to find the address of the flag() function, which was at address, "0x04011d6"

<img width="1062" alt="Screenshot 2023-04-10 at 4 14 14 PM" src="https://user-images.githubusercontent.com/112781868/231016637-ac1edaae-a041-4c19-a80f-e0737fff03ad.png">

Now its time for the hecking 😎. 

I now know the max size of the buffer and the location of the flag() function, the two things I need to exploit this program. The biggest thing I forgot to mention, the **gets()** function is very unsafe in C, as it does **_not_** do __boundary checking__. This is only the thing making this whole buffer overflow thing from happening. 

Next thing I learned from the friend, when performing a buffer overflow, you have to input the address in little endian form. Not too sure why, but my understanding it has to do with how the computer relays information. Little endian stores the (LSB) Least Signifcant Byte first! Essentially, little endian stores the string backwards ISH. Luckily pwn has that kind of function, so I just ran p64(address), to convert the flag address to little endian format (I should have paid attention in intro to c++...).

I finally did the research, so little endian means to store the least significant bit first. So the least significant bit is the start of the string. So in essence, you do have to techincally "reverse" the string. Right so if the address was 0xDEAD (little endian) -> 0xADDE or (in shellcode) '/xAD/xDE'

Alright, so I created my 72 bit length string and added my little endian address and fed it to the remote program. The string is:
              b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xdb\x11@\x00\x00\x00\x00\x00'

First try, the address "0x0401146", did not work. Friend told me to brute force every address, and eventually 2 addresses down I got the flag, at address "0x04011db". And it took me awhile as I didn't put the other recvline to print the flag. But once I did, BOOM flag found! 

### OK quick add on
I finally understand now the whole point of a BFO challenge is to overwrite the return address to your desired address or you can put the address to point to the shell code you injected. Now this is a very high level explaniation on my part, and by no MEANS am I an expert. But this topic is supaaaa interesting. 

**flag{W4X_0N_W4X_0FF_MR_M1Y4G1}** 
wooooo! 
