#!/usr/local/bin/python
from os import system
inp = input("What's your first string?\n")
rep = '/' + input("What should you replace?\n") +  '/' 
print(rep)
new = input("What should it be now?\n")
cmd = 's' + rep + new + "/g"
print(cmd)
if "'" not in new:
	cmd += "'"
print("You actually said")

system("echo '" + inp + "' | sed '" +  cmd)
