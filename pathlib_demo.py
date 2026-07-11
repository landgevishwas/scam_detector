from pathlib import Path

# 1️⃣ Path of the current file
current_file = Path(__file__)
print("Current file:", current_file)

# 2️⃣ Get the parent directory
parent_dir = current_file.parent
parent_dir = Path(__file__).parent
print("Parent directory:", parent_dir)

# 3️⃣ Get absolute path
absolute_path = current_file.resolve()
print("Absolute path:", absolute_path)

# 4️⃣ Create a path to data.csv
data_file = parent_dir / "data.csv"
print("Data file path:", data_file)


# 5️⃣ Check if the file exists
print("Does file exist?", data_file.exists())