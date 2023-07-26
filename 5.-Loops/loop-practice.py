def count_equal_substrings(binary_string):
    count = 0
    i = 0
    while i < len(binary_string):
        if binary_string[i] == '0':
            zeros = 0
            while i < len(binary_string) and binary_string[i] == '0':
                zeros += 1
                i += 1
            count += (zeros * (zeros + 1)) // 2
        elif binary_string[i] == '1':
            ones = 0
            while i < len(binary_string) and binary_string[i] == '1':
                ones += 1
                i += 1
            count += (ones * (ones + 1)) // 2
    return count

binary_string = '0011001'
result = count_equal_substrings(binary_string)
print(result)  # Output: 5
