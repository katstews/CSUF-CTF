#!/usr/local/bin/python
#flag{b4sh_1n_pyth0n}
from os import system

inp = input("What's your first string?\n")
rep = '/' + input("What should you replace?\n") +  '/' 
new = input("What should it be now?\n")
cmd = 's' + rep + new + "/g"
if "'" not in new:
	cmd += "'"
print("You actually said")

system("echo '" + inp + "' | sed '" +  cmd)

# '; cat flag.txt; #