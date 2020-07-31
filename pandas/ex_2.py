import pandas as pd
# data set folder
data_path = "C:\\Users\\shaok\\Documents\\pandas"
###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
# from unittest.mock import MagicMock                           #
# import pandas as pd                                           #
# pd.read_csv = MagicMock(spec = pd.read_csv)                   #
###############################################################

# Assume the pandas library has already been imported and assigned the alias "pd".

# Let's say we have a foods.csv CSV file with 3 columns: Item Number, Menu Item, Price
# The raw CSV data looks like this:
#
# Item Number,Menu Item,Price
# 1,Big Mac,4.99
# 2,McNuggets,7.99
# 3,Quarter Pounder,3.99
#
# Import the CSV file into a Pandas Series object
# The Series should have the standard Pandas numeric index
# The Series values should be the string values from the "Menu Item" column
# Assign the Series object to a "foods" variable
foods = pd.read_csv(data_path+"\\"+"Restaurant - Foods.csv", usecols=["Food Item", "Price"])
print(foods)