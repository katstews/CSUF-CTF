mainly just for me to keep track of how I even was able to solve these challenges. 

## pwn - how2flag (bufferover flow challenge)
### 4/10/23
Just figured out how to do a buffer overflow using python. Very interesting. first off in the pwn challenge, I was given a binary file and a C file containing how the program worked. the binary file was a executable elf file. I used objdump to disassemble the elf file. To do an bufferoverflow exploit, you would need to know the size of the buffer you want to exploit **plus** the address of the function you want to exploit. How it works is once you exploit the buffer you want to the tell the program what address you want to access. 

In this case objdump would work, but a friend recommended I try ghidra. Had to open it up with Kali, as it was too difficult to install on M1. Anyways, with the guidance of a friend, I found that the actual size of the buffer was not 64 but actually "0x48" which is 73 in decimal. 

<img width="902" alt="Screenshot 2023-04-10 at 4 11 19 PM" src="https://user-images.githubusercontent.com/112781868/231016331-c9831d2d-5f00-484c-bd51-7e4bc35b819c.png">

As shown in the image, the actual size of the buffer was 73. So the input I needed to be shy of the size 73. Using Ghidra (or objdump), I was also able to find the address of the flag() function, which was at address, "0x0401146"

<img width="1062" alt="Screenshot 2023-04-10 at 4 14 14 PM" src="https://user-images.githubusercontent.com/112781868/231016637-ac1edaae-a041-4c19-a80f-e0737fff03ad.png">

Now its time for the hecking 😎. 
