nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]

result = [number for block in nice_list for inner_list in block for number in inner_list]

print(result)
