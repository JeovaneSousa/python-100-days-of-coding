numbers = [1, 2, 3]
new_lit = [number + 1 for number in numbers]
print(new_lit)
# ------------------------
name = "Angela"
new_name_list = [letter for letter in name]
print(new_name_list)
# -----------------------
range_list = [n * 2 for n in range(1, 5)]
print(range_list)
# -------------------------
list_of_names = ['Álex', 'Beth', "Caroline", 'Dave', 'Eleanor', 'Freddie']
list_of_uppercase = [name.upper() for name in list_of_names if len(name) >= 5]
print(list_of_uppercase)
#--------------------------
