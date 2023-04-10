#must manipulate...
def dec(x):
    return chr(ord(x) + 1)

def inc(x):
    return chr(ord(x) - 1)

# def check():
print(inc('g'))
        #         return False
print(dec('k'))
        #         return False
print(inc('b'))
        #         return False
print(dec('f'))
        #         return False
print(inc('|'))
        #         return False
print(dec('3'))        # if dec(password[5]) != '3':
        #         return False
print(inc('t'))        # if inc(password[6]) != 't':
        #         return False
print(dec('b'))        # if dec(password[7]) != 'b':
        #         return False
print(inc('2'))        # if inc(password[8]) != '2':
        #         return False
print(dec('0'))        # if dec(password[9]) != '0':
        #         return False
print(inc('`'))# if inc(password[10]) != '`':
        #         return False
print(dec('0'))        # if dec(password[11]) != '0':
        #         return False
print(inc('t'))        # if inc(password[12]) != 't':
        #         return False
print(dec('^'))        # if dec(password[13]) != '^':
        #         return False
print(inc('g'))        # if inc(password[14]) != 'g':
        #         return False
print(dec('t'))        # if dec(password[15]) != 't':
        #         return False
print(inc('o'))        # if inc(password[16]) != 'o':
        #         return False
print(dec('|'))        # if dec(password[17]) != '|':
        #         return False
        # return True


# password = input().rstrip('\n')

# if check(password):
# 	print("submit that as the flag!")
# else:
# 	print("not quite")
