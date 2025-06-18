import sys
def downcase_it(s):
    return s.lower()
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(downcase_it(arg))
else:
    print("none")