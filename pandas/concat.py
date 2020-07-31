# exercise data frame concat, append
import pandas as pd
data_path = "C:\\Users\\shaok\\Documents\\pandas\\"
week1 = pd.read_csv(data_path + "Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv(data_path + "Restaurant - Week 2 Sales.csv")
customers = pd.read_csv(data_path + "Restaurant - Customers.csv")
foods = pd.read_csv(data_path + "Restaurant - Foods.csv")
sales = pd.concat([week1, week2], keys = ["A", "B"])
print(sales)
sales = pd.concat([week1, week2], ignore_index=False)
print(sales)
sales = pd.concat([week1, week2], ignore_index=True)
print(sales)
sales = week2.append(week1, ignore_index = True)
print(sales)