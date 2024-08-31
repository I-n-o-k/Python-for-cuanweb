# Define the starting and ending numbers
start = 709301094984
end = 709301095003
suffix = ','

# Generate the list
numbers_with_suffix = [f"{i}{suffix}" for i in range(start, end + 1)]

# Print the list
for number in numbers_with_suffix:
    print(number)
