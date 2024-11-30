# Define the starting number and the number of rows for each suffix
start = 309561008151
suffixes = [
    (',V1', 6),
    (',V5GB3D', 9),
    (',VMINI1', 15),
    (',VBM3X', 30),
    (',VMINI2', 3),
    (',V5GB7D', 3),
    (',V9GB7DSUM', 30),
    (',V7GB30D', 3),
    (',VAON1', 15),
    (',VAON2', 15),
    (',VAON6GB', 12),
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
