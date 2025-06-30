# Define the starting number and the number of rows for each suffix
start = 310319872151
suffixes = [
    (',V2', 200),
    (',VH2GB1D', 200),
    (',VH10GB7D', 50),
]

# Initialize a list to store the results
numbers_with_suffixes = []

# Generate the list
current_number = start
for suffix, count in suffixes:
    for _ in range(count):
        # Append the number with the current suffix to the list
        numbers_with_suffixes.append(f"{current_number}{suffix}")
        current_number += 1

# Print the list
for number in numbers_with_suffixes:
    print(number)
