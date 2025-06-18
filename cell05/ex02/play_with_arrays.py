original_arry = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for x in original_arry]
print("original array:", original_arry)
print("New array:", new_array)
filtered_array = [x for x in new_array if x > 5]
print("Filtered array (>5):", filtered_array)