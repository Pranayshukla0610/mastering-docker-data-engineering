from data_loader import load_data

if __name__ == "__main__":
    file_path = "data/employees.csv"

    df = load_data(file_path)

    print("\nApplication Executed Successfully")