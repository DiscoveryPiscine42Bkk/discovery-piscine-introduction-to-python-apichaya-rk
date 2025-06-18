import sys
args = sys.argv[1:]
if not args:
    print("none")
else:
    print("parameter:", len(args))
    for arg in args:
        print(f"{arg}: {len(arg)}")