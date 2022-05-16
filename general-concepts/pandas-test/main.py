# data = []
# with open("weather_data.csv")  as csv_data:
#         untreated_data = csv_data.readlines()
#         for line in untreated_data:
#             treated_line = line.strip()
#             data.append(treated_line)
# print(data)


# import csv
# with open("weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)
#     temperatures = []
#     for line in data:
#         print(line)
#         if line[1] != "temp":
#             temperatures.append(int(line[1]))
# print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data["temp"].mean())
print(data_dict)
temp_list = data["temp"].to_list()
max_temp = data["temp"].max()
print(temp_list)
print(max_temp)
max_temp_logical_vector = data["temp"] == max_temp
max_temp_row = data[max_temp_logical_vector]

print (max_temp_row)