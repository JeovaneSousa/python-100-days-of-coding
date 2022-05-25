# data = []
# with open("weather_data.csv")  as csv_data:
#         untreated_data = csv_data.readlines()
#         for line in untreated_data:
#             treated_line = line.strip()
#             data.append(treated_line)
# print(data)
# ----------------------------------------------------

# import csv
# with open("weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)
#     print(type(data))
#     temperatures = []
#     for line in data:
#         print(line)
#         if line[1] != "temp":
#             temperatures.append(int(line[1]))
# print(temperatures)
# ----------------------------------------------------

import pandas

""
data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
print(data["temp"].mean())
print(data_dict)
print(temp_list)
# ----------------------------------------------------
max_temp_row = data[data["temp"] == data["temp"].max()]
print(max_temp_row)

# ----------------------------------------------------
monday_data = data[data["day"] == "Monday"]
print(monday_data)

monday_temp = int(monday_data["temp"])
print(f"The monday's temperature in C is {monday_temp}")
monday_temp_in_fahrenheit = monday_temp * 1.8 + 32
print(f"The monday's temperature in Fahr is {monday_temp_in_fahrenheit}")



