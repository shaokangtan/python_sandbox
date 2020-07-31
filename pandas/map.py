import pandas as pd
# data set folder
import pandas as pd
data_path = "C:\\Users\\shaok\\Documents\\pandas\\"
pokemon_names = pd.read_csv(data_path+"pokemon.csv", usecols = ["Pokemon"], squeeze = True)
print(pokemon_names.head(3))
pokemon_types = pd.read_csv(data_path+"pokemon.csv", index_col = "Pokemon", squeeze = True)
print(pokemon_types.head(3))

print(pokemon_names.map(pokemon_types))

pokemon_types.sort_index(inplace=True)
print(pokemon_types.head(3))
print(pokemon_names.map(pokemon_types))