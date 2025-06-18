import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    cout = text.count(keyword)
    if cout == 0:
        print("none")
    else:
        print(cout)
        