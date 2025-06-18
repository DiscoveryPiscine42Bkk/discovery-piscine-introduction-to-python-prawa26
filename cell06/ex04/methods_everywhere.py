import sys
def shrink(i):
    print(i[:8])
def enlarge(i):
    print(i + 'z' * (8 - len(i)))
if len(sys.argv) < 2:
    print