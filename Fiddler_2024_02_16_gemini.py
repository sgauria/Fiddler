def longest_sequence(numbers):
    """
    Finds the longest sequence drawn from the given numbers that has no successive subsequences with the same sum.

    Args:
        numbers: A list of integers.

    Returns:
        The longest sequence that satisfies the condition.
    """

    # Initialize variables
    current_seq = []
    max_seq = []

    # Iterate through each number in the input
    for num in numbers:
        # Check if adding the current number creates a new sum
        new_sum = sum(current_seq) + num
        if new_sum not in [sum(current_seq[-i:]) for i in range(1, len(current_seq) + 1)]:
            current_seq.append(num)
        else:
            # If not, update the max sequence if necessary and reset the current sequence
            max_seq = max(max_seq, current_seq, key=len)
            current_seq = []

    # Update max sequence if the current sequence is longer
    max_seq = max(max_seq, current_seq, key=len)

    return max_seq

# Example usage
numbers = [1, 2, 3, 4]
longest_seq = longest_sequence(numbers)
print(f"Longest sequence: {longest_seq}")
