# exercise data frame merge join
import pandas as pd
data_path = "C:\\Users\\shaok\\Documents\\pandas\\"
week1 = pd.read_csv(data_path + "Restaurant - Week 1 Sales.csv")
print(len(week1))
week2 = pd.read_csv(data_path + "Restaurant - Week 2 Sales.csv")
print(len(week2))
weeks = week1.merge(week2, how = "inner", on = ["Customer ID"])
print(len(weeks))
print(weeks)
merged = week1.merge(week2, how = "outer", on = "Customer ID", suffixes = [" - Week 1", " - Week 2"],
            indicator = True)
print(merged)
counts = merged["_merge"].value_counts()
print(counts)