import pandas as pd
# data set folder
import pandas as pd
data_path = "C:\\Users\\shaok\\Documents\\pandas"
###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
# from ignore import pd                                       #
###############################################################

# Let's say I have a dictionary that maps guitar types
# to their colors
guitars_dict = {
    "Fender Telecaster": "Baby Blue",
    "Gibson Les Paul": "Sunburst",
    "ESP Eclipse": "Dark Green"
}

# Create a new Series object, passing in the guitars_dict dictionary as the data source.
# Assign the resulting Series to a "guitars" variable.
guitars = pd.Series(guitars_dict)
print(guitars)

# Access the value for the index position of 0 within the "guitars" Series.
# Assign the value to a "fender_color" variable.
print(guitars[0])
print(guitars["Fender Telecaster"])
guitars[0] = "fender_color"
print(guitars)




# Access the value for the index label of "Gibson Les Paul" in the "guitars" Series.
# Assign the value to a "gibson_color" variable.


# Access the value for the index label of "ESP Eclipse" in the "guitars" Series.
# Assign the value to a "esp_color" variable.
