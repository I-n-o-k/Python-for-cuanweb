# Define the starting number and the number of rows for each suffix
start = 310115572767
suffixes = [
    (',VMINI2', 9),
    (',V5GB7D', 6),
    (',VAON1', 9),
    (',VAON6', 9)
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
