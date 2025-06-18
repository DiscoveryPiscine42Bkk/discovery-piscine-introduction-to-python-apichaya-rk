import sys
if len(sys.argv) != 2:
    print("none")
else:
    pram = sys.argv[1]
    user_input = input("what was the parameter? ")
    if user_input == pram:
        print("Good job!")
    else:
        print("Nope, sorry...")