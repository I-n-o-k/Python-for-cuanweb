# Define the starting number and the number of rows for each suffix
start = 310137947151
suffixes = [
    (',V2', 300),
    (',VBM3X', 45),
    (',V9GB7DSUM', 45),
    (',V11GB30D', 3),
    (',V18GB', 3),
    (',VPM4', 30),
    (',VAON1', 9),
    (',VAON2', 9),
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
