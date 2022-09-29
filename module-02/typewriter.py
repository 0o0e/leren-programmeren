import string
import sys, time, os

os.system('cls')




def typewriter(string):
     for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.000000000000000000000000000000000000000000000000000000000000001)
        if char !="\n":
            time.sleep(0.03)
        else:
            time.sleep(1)





message = "hello world nice to meet you.\n\
"
typewriter(message)