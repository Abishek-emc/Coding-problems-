nums = [2, 7, 11, 15]  # List of numbers
target = 9  # Target sum
nummap = {}  # Dictionary to store numbers and their indices

# Iterate through the list
for i in range(len(nums)):
    com = target - nums[i]  # Calculate the complement
    # Check if the complement is in the dictionary
    if com in nummap:
        print([i, nummap[com]])  # Output the indices
    # Add the current number and its index to the dictionary
    nummap[nums[i]] = i
