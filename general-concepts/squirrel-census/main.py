import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

fur_color_count_dict = {
    "Fur Color":["gray", "red", "black"],
    "Count":[gray_count, red_count, black_count]
}

new_data_fur_color_count = pandas.DataFrame(fur_color_count_dict)
new_data_fur_color_count.to_csv("squirrel_count.csv")
