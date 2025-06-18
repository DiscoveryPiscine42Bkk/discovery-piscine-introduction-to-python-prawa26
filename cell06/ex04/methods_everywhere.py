import sys
def shrink(i):
    print(i[:8])
def enlarge(i):
    print(i + 'z' * (8 - len(i)))
if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)