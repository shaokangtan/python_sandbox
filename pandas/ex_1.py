import pandas as pd
# data set folder
data_path = "C:\\Users\\shaok\\Documents\\pandas"
###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
# from unittest.mock import MagicMock                           #
# import  pandas as pd                                           #
# pd.Series = MagicMock()                                       #
###############################################################

# Assume the pandas library has already been imported and assigned
# the alias "pd".

# Create a list with 4 countries - United States, France, Germany, Italy
# Create a new Series by passing in the list of countries
# Assign the Series to a "countries" variable
countries_list = ["United States", "France", "Germany", "Italy"]
countries = pd.Series(countries_list)
print(countries)


# Create a list with 3 colors - red, green, blue
# Create a new Series by passing in the list of colors
# Assign the Series to a "colors" variable
color_list=["red", "green", "blue"]
color = pd.Series(color_list)
print(color)


# Given the "recipe" dictionary below,
# create a new Series by passing in the dictionary as the data source
# Assign the resulting Series to a "series_dict" variable
recipe = {
  "Flour": True,
  "Sugar": True,
  "Salt": False
}

series_dict = pd.Series(recipe)
print(series_dict)