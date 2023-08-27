import os

# Step 1/3: Simple Text Extraction

# First Line: 2023-08-24 10:00:00 [INFO] Transaction start ID:123

# 1 Python Script to Return First Line:

# Construct the file path
file_path = os.path.join(os.getcwd(), "logfile.txt")

with open(file_path, "r") as file:
    first_line = file.readline().strip()
print("first line:", first_line)

# Step 2/3: Counting

# 2 Python Script to Count Lines with Log Level ERROR:

error_count = 0
with open(file_path, "r") as file:
    for line in file:
        if "[ERROR]" in line:
            error_count += 1
print("Number of errors:", error_count)


# 3 Python Script to Count Transactions:

transaction_count = 0
with open(file_path, "r") as file:
    for line in file:
        if "Transaction end" in line:
            transaction_count += 1
print("Number of transactions:", transaction_count)

# Step 3/3: Math

# 4 Python Script to Find Fastest Transaction ID:

# Initialize variables
fastest_transaction_time = float("inf")
fastest_transaction_id = None

with open(file_path, "r") as file:
    transaction_start = None
    for line in file:
        stripped_line = line.strip()  # Remove leading and trailing whitespace
        if not stripped_line:  # Skip empty lines
            continue
        parts = stripped_line.split()
        timestamp = parts[0]
        if "Transaction start" in line:
            transaction_start = (
                parts[4].split(":")[1],
                int(timestamp.split(":")[0]),
                int(timestamp.split(":")[1]),
                int(timestamp.split(":")[2].split(".")[0]),
                int(timestamp.split(":")[2].split(".")[1]),
            )
        elif "Transaction end" in line:
            transaction_end = (
                int(timestamp.split(":")[0]),
                int(timestamp.split(":")[1]),
                int(timestamp.split(":")[2].split(".")[0]),
                int(timestamp.split(":")[2].split(".")[1]),
            )
            transaction_time = (
                (
                    transaction_end[0] * 3600
                    + transaction_end[1] * 60
                    + transaction_end[2]
                )
                * 1000
                + transaction_end[3]
                - (
                    transaction_start[1] * 3600
                    + transaction_start[2] * 60
                    + transaction_start[3]
                )
                * 1000
                - transaction_start[4]
            )
            if transaction_time < fastest_transaction_time:
                fastest_transaction_time = transaction_time
                fastest_transaction_id = transaction_start[0]

print("Fastest transaction ID:", fastest_transaction_id)

# 5 Python Script to Calculate average transaction time

# Initialize variables
total_transaction_time = 0
transaction_count = 0

with open(file_path, "r") as file:
    transaction_start = None
    for line in file:
        stripped_line = line.strip()  # Remove leading and trailing whitespace
        if not stripped_line:  # Skip empty lines
            continue
        parts = line.split()
        timestamp = parts[0]
        if "Transaction start" in line:
            transaction_count += 1
            transaction_start = (
                parts[4].split(":")[1],
                int(timestamp.split(":")[0]),
                int(timestamp.split(":")[1]),
                int(timestamp.split(":")[2].split(".")[0]),
                int(timestamp.split(":")[2].split(".")[1]),
            )
        elif "Transaction end" in line:
            transaction_end = (
                int(timestamp.split(":")[0]),
                int(timestamp.split(":")[1]),
                int(timestamp.split(":")[2].split(".")[0]),
                int(timestamp.split(":")[2].split(".")[1]),
            )
            transaction_time = (
                (
                    transaction_end[0] * 3600
                    + transaction_end[1] * 60
                    + transaction_end[2]
                )
                * 1000
                + transaction_end[3]
                - (
                    transaction_start[1] * 3600
                    + transaction_start[2] * 60
                    + transaction_start[3]
                )
                * 1000
                - transaction_start[4]
            )
            total_transaction_time += transaction_time

average_transaction_time = total_transaction_time / transaction_count
print("Average transaction time (ms):", average_transaction_time)
