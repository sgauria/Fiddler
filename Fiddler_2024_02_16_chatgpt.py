def longest_sequence():
    # Define the sequence of numbers
    numbers = [1, 2, 3, 4]

    # Initialize variables to keep track of the longest sequence and its length
    longest = []
    longest_length = 0

    # Dynamic programming table to keep track of the longest sequence for each sum
    dp = {}

    # Helper function to recursively find the longest sequence
    def find_longest_sequence(seq):
        nonlocal longest, longest_length
        # Check if the current sequence is longer than the longest found so far
        if len(seq) > longest_length:
            longest = seq.copy()
            longest_length = len(seq)

        # Base case: if the sequence length is 0 or 1, we can't continue
        if len(seq) <= 1:
            return

        # Iterate through each number in the sequence
        for num in numbers:
            # Check if adding the current number preserves the condition of no consecutive equal sums
            if len(seq) == 1 or seq[-1] + num != seq[-2] * 2:
                # Add the number to the sequence and recursively continue
                new_seq = seq + [num]
                find_longest_sequence(new_seq)

    # Start with all possible starting numbers and find the longest sequence
    for start_num in numbers:
        find_longest_sequence([start_num])

    return longest

# Find the longest sequence
result = longest_sequence()
print("Longest sequence with no successive subsequences with the same sum:", result)
