import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    z_chars = [char for char in input_string if char == 'z']
    if z_chars:
        print(''.join(z_chars))
    else:
        print("none")
