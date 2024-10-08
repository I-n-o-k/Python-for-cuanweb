# Define the starting number and the number of rows for each suffix
start = 310130761401
suffixes = [
    (',VMINI1', 15),
    (',VBM3X', 15),
    (',V7GB30D', 6),
    (',VPM4', 9),
    (',VAON1', 6),
    (',VAON2', 6),
    (',VAON6GB', 9),
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
