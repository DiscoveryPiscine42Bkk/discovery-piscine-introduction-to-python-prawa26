

original_array = [2, 8, 9, 48, 8, 22, -12, 2]


new_array = list({num + 2 for num in original_array if num + 2 > 5})


new_array.sort()


print( original_array)
print( new_array)
