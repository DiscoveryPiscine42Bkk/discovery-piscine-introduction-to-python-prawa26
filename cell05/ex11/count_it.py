import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{args}: {len(arg)}")