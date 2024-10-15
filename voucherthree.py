# Define the starting number and the number of rows for each suffix
start = 310138086564
suffixes = [
    (',V5GB3D', 30),
    (',VBM3X', 30),
    (',VPM4', 15),
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
