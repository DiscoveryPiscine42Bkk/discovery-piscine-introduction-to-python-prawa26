import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]
    occurrences = re.findall(re.escape(keyword), string_to_search)
    print(len(occurrences)) 
else:
    print("none")    