with open("file1.txt") as file1:
    list_file1 = file1.readlines()
    clean_list_1 = [int(number.strip()) for number in list_file1]
    print(clean_list_1)

with open("file2.txt") as file2:
    list_file2 = file2.readlines()
    clean_list_2 = [int(n.strip()) for n in list_file2]
    print(clean_list_2)


result = [n for n in clean_list_1 if n in clean_list_2]
print(result)