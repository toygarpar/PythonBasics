import sys


#slices
#che3ck for errors

if len(sys.argv) < 2:
    sys.exit("too fex arguments")

for arg in sys.argv[1:-1]:  # -1 is not inclusive
    print("hello, my name is ", arg)        