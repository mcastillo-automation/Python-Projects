import pandas

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_color = squirrel_data["Primary Fur Color"]
squirrel_color_count = squirrel_color.value_counts().to_dict()
squirrel_colors_df = pandas.DataFrame({"Fur Color": list(squirrel_color_count.keys()),
                                       "Count": list(squirrel_color_count.values())})
squirrel_colors_df.to_csv("./squirrel count.csv")
