# ------------------- Import Libraries ------------------
import pandas

# ------------------- Define Constants ------------------

PATH_TO_PROJECT ="./Projects/Intermediate/PandasDataAnalysis"

# ------------------- Main Program ------------------

try:
    data = pandas.read_csv(PATH_TO_PROJECT+"/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
except FileNotFoundError:
    print("Error - File Not Found")
else:
    #grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
    grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
    print(f"Grey Squirrels  : {grey_squirrel_count}")
    print(f"Red Squirrels   : {red_squirrel_count}")
    print(f"Black Squirrels : {black_squirrel_count}")

    data_dic = {
        "Fur Color": ["Grey", "Red", "Black"],
        "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count],
    }

    df = pandas.DataFrame(data_dic)
    df.to_csv(PATH_TO_PROJECT+"/squirrel_count.csv")

finally:
    pass
