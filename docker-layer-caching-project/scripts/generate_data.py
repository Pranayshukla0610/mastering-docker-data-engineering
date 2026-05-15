import pandas as pd
import os

os.makedirs("data",exist_ok=True)

data = {
    "id":[1,2,3,4,5],
    "name":["A","B","C","D","E"],
    "salary":[50000,60000,70000,80000,90000]
}

df = pd.DataFrame(data)

df.to_csv("data/employees.csv",index=False)

print("Data Generated Successfully")