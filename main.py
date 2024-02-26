# def count_duplicates(input_string):
#     input_string = input_string.lower()
#     unique_chars = set()
#     duplicates_count = 0
#
#     for char in input_string:
#         if input_string.count(char) > 1 and char not in unique_chars:
#             duplicates_count += 1
#             unique_chars.add(char)
#
#     return duplicates_count
#
# test_strings = ["abcde", "aabbcde", "aabBcde", "indivisibility", "Indivisibilities", "aA11", "ABBA"]
#
# for test_string in test_strings:
#     print(f'"{test_string}" -> {count_duplicates(test_string)}')