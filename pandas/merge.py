import pandas as pd
data_path = "C:\\Users\\shaok\\Documents\\pandas\\"
week1 = pd.read_csv(data_path + "Restaurant - Week 1 Sales.csv")
week2 = pd.read_csv(data_path + "Restaurant - Week 2 Sales.csv")
customers = pd.read_csv(data_path + "Restaurant - Customers.csv")
foods = pd.read_csv(data_path + "Restaurant - Foods.csv")
satisfaction = pd.read_csv(data_path + "Restaurant - Week 1 Satisfaction.csv")
m = pd.merge(week1, customers, how = "left", left_on = "Customer ID", right_on = "ID")
print(m)