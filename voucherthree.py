# Define the starting number and the number of rows for each suffix
start = 310320745904
suffixes = [
    (',VH4P5GB5D', 90),
    (',VH7GB28D', 30),
    (',VH42GB28D', 15),
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
