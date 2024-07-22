# Question 2

#  Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated.
#  Write a Python script to remove duplicates and display the unique customer IDs.

# Solution

# List of customer IDs with duplicates
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to remove duplicates
unique_customer_ids = set(customer_ids)

# Display the unique customer IDs
print(unique_customer_ids)