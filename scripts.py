import os

# Step 1/3: Simple Text Extraction

# 1 Python Script to Return First Line:

# Construct the file path
file_path = os.path.join(os.getcwd(), "exam.log")


def get_first_line(file_path):
    with open(file_path, "r") as file:
        first_line = file.readline().strip()
    return first_line


print("first line:", get_first_line(file_path))

# Step 2/3: Counting

# 2 Python Script to Count Lines with Log Level ERROR:


def get_error_count(file_path):
    error_count = 0
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            log_level = parts[2]
            if log_level == "ERROR":
                error_count += 1
    return error_count


print("Number of errors:", get_error_count(file_path))


# 3 Python Script to Count Transactions:


def get_transaction_count(file_path):
    transaction_count = 0
    with open(file_path, "r") as file:
        for line in file:
            if "transaction done" in line:
                transaction_count += 1
    return transaction_count


print("Number of transactions:", get_transaction_count(file_path))

# Step 3/3: Math

# 4 Python Script to Find Fastest Transaction ID:

# transaction 17030 begun
# transaction done


def get_fastest_transection(file_path):
    # Initialize variables
    fastest_transaction_time = float("inf")
    fastest_transaction_id = None

    with open(file_path, "r") as file:
        transaction_start = None
        for line in file:
            parts = line.split()
            timestamp = parts[1]
            if ("transaction" in line) and ("begun") in line:
                transaction_start = (
                    parts[6],
                    int(timestamp.split(":")[0]),
                    int(timestamp.split(":")[1]),
                    int(timestamp.split(":")[2].split(".")[0]),
                    int(timestamp.split(":")[2].split(".")[1]),
                )
            elif "transaction done" in line:
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
    return fastest_transaction_id


print("Fastest transaction ID:", get_fastest_transection(file_path))

# 5 Python Script to Calculate average transaction time


def get_the_average_transaction_time(file_path):
    # Initialize variables
    total_transaction_time = 0
    transaction_count = 0

    with open(file_path, "r") as file:
        transaction_start = None
        for line in file:
            parts = line.split()
            timestamp = parts[1]
            if ("transaction" in line) and ("begun") in line:
                transaction_count += 1
                transaction_start = (
                    parts[6],
                    int(timestamp.split(":")[0]),
                    int(timestamp.split(":")[1]),
                    int(timestamp.split(":")[2].split(".")[0]),
                    int(timestamp.split(":")[2].split(".")[1]),
                )
            elif "transaction done" in line:
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
    return average_transaction_time


print("Average transaction time (ms):", get_the_average_transaction_time(file_path))
