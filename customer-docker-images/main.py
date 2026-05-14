import pandas as pd
import json

print("\nStarting Docker Application...\n")

# Read CSV Data
employees = pd.read_csv("data/employees.csv")

print("Employee Data:\n")
print(employees)

# Read Config File
with open("config/config.json") as file:
    config = json.load(file)

print("\nConfiguration Details:\n")
print(config)

print("\nDocker Application Completed Successfully.")