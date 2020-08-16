from collections import defaultdict
from itertools import combinations


def convert_num_binary(num):
    return str(int(bin(num)[2:]))


n = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
convert_max_num_binary = str(int(bin(max_num)[2:]))
length_converted_max_num = len(convert_max_num_binary)
# print(length_converted_max_num)
converted_binary_nums = []
converted_binary_nums_hash = defaultdict(list)
binary_equivalent = []
for items in nums:
    len_convert_items = len(convert_num_binary(items))
    if length_converted_max_num == len_convert_items:
        converted_binary_nums.append(str(convert_num_binary(items)))
    else:
        calculate_how_many_zero = length_converted_max_num - len_convert_items
        add_zeros_to_items = '0' * calculate_how_many_zero + convert_num_binary(items)
        converted_binary_nums.append(add_zeros_to_items)

for binary in range(len(converted_binary_nums)):
    count_1 = converted_binary_nums[binary].count('1')
    count_0 = converted_binary_nums[binary].count('0')

    converted_binary_nums_hash[converted_binary_nums[binary]].append([count_1, count_0])

for i in range(len(nums)):
    keys = combinations(converted_binary_nums, i + 1)
    for all_binary_nums in keys:
        if len(list(all_binary_nums)) == 1:
            value = converted_binary_nums_hash[all_binary_nums[0]]
            if value[0][0] == value[0][1]:
                binary_equivalent.append(all_binary_nums)
        else:
            join_binary = "".join(all_binary_nums)
            if join_binary.count("1") == join_binary.count("0"):
                binary_equivalent.append(all_binary_nums)

answer = convert_num_binary(len(binary_equivalent))
if len(answer) == length_converted_max_num:
    print(answer)
else:
    calculate_zero = length_converted_max_num - len(answer)
    add_zeros = '0' * calculate_zero + answer
    print(add_zeros)

