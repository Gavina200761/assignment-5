# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None
    
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    
    return max(freq, key=freq.get)

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) - iterate through all elements to count frequencies.
- Worst-case: O(n) - pass through entire list
- Average-case: O(n) - no variance and always linear
- Space complexity: O(k) k is the number of unique elements
- Why this approach? This is optimal because we  must examine each element at least once. This approach achieves that.
- Could it be optimized? Space could be saved by tracking max during counting (one pass with O(1) extra space), but time remains O(n).
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - iterate through all elements to ensure order
- Worst-case: O(n) - same iteration through entire list
- Average-case: O(n) - linear regardless of duplicate
- Space complexity: O(n) - worst case when all elements are unique
- Why this approach? Using a set provides O(1) lookup time for duplicates. We must examine each element to preserve order, making O(n) optimal.
- Could it be optimized? Space is necessary to preserve order, so not in terms of time complexity. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Refactored approach: sort + two pointers.
    # Trade-off: This uses O(n log n) time due to sorting but requires O(1)
    # extra space (ignoring the cost of copying the input for safety).
    # Original approach: O(n) time and O(n) extra space using a hash set.
    
    if not nums:
        return []

    # Work on a copy so we don't mutate the caller's list
    arr = sorted(nums)
    left, right = 0, len(arr) - 1
    pairs = []

    # Two-pointer scan finds all unique pairs summing to target.
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) - must examine all elements even if no pairs exist
- Worst-case: O(n) - iterate through entire list
- Average-case: O(n) - independent of pair count
- Space complexity: O(n) - seen set stores up to n unique elements
- Why this approach? By checking if complement is in `seen`, we ensure each pair is added exactly once without duplicates.
- Could it be optimized? O(n) is optimal since we must examine each element. Space can't be reduced if we want to collect all pairs.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2  # Initial fixed capacity
    items = []
    
    for i in range(n):
        # Check if we need to resize
        if len(items) == capacity:
            print(f"Resizing: capacity {capacity} -> {capacity * 2}, copying {len(items)} items")
            capacity *= 2
        
        items.append(i)
    
    print(f"Final: {len(items)} items in list with capacity {capacity}")
    return items

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes occur at positions 2, 4, 8, 16, ... (powers of 2)
- What is the worst-case for a single append? When a resize occurs, meaning it must copy all n-1 existing items.
- What is the amortized time per append overall? Total work for n appends is O(n), so average per append is O(1)
- Space complexity: Capacity grows to accommodate n items
- Why does doubling reduce the cost overall? Doubling amortizes the cost by spreading it. Each resize at size k costs k work but enables k more O(1) appends.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) - must iterate through all elements
- Worst-case: O(n) - always iterate through entire list
- Average-case: O(n) - no variance, always linear
- Space complexity: O(n) - output list stores n cumulative sums
- Why this approach? Single pass with O(1) work per element is optimal. Maintains running total to avoid redundant recalculation.
- Could it be optimized? O(n) is optimal since we must process each element. Output space is inevitable to store results.
"""


# TEST CASES

def run_tests():
    print("PROBLEM 1: Find Most Frequent Element")
    
    # Test 1.1: Example from problem
    result = most_frequent([1, 3, 2, 3, 4, 1, 3])
    assert result == 3, f"Expected 3, got {result}"
    print("Test 1.1 passed: [1, 3, 2, 3, 4, 1, 3] → 3")
    
    # Test 1.2: Single element
    result = most_frequent([5])
    assert result == 5, f"Expected 5, got {result}"
    print("Test 1.2 passed: [5] → 5")
    
    print()
    print("PROBLEM 2: Remove Duplicates While Preserving Order")
    
    # Test 2.1: Example from problem
    result = remove_duplicates([4, 5, 4, 6, 5, 7])
    assert result == [4, 5, 6, 7], f"Expected [4, 5, 6, 7], got {result}"
    print("Test 2.1 passed: [4, 5, 4, 6, 5, 7] → [4, 5, 6, 7]")
    
    # Test 2.2: No duplicates
    result = remove_duplicates([1, 2, 3])
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"
    print("Test 2.2 passed: [1, 2, 3] → [1, 2, 3]")
    
    print()
    print("PROBLEM 3: Return All Pairs That Sum to Target")
    
    # Test 3.1: Example from problem
    result = find_pairs([1, 2, 3, 4], 5)
    result_set = set(result)
    expected_set = {(1, 4), (2, 3)}
    assert result_set == expected_set, f"Expected {expected_set}, got {result_set}"
    print("Test 3.1 passed: find_pairs([1, 2, 3, 4], 5) → {(1, 4), (2, 3)}")
    
    # Test 3.2: No pairs
    result = find_pairs([1, 2, 3], 10)
    assert result == [], f"Expected [], got {result}"
    print("Test 3.2 passed: find_pairs([1, 2, 3], 10) → []")
    
    print()
    print("PROBLEM 4: Simulate List Resizing (Amortized Cost)")
    
    # Test 4.1: Example from problem (n=6)
    print("Test 4.1: add_n_items(6)")
    result = add_n_items(6)
    assert result == [0, 1, 2, 3, 4, 5], f"Expected [0, 1, 2, 3, 4, 5], got {result}"
    print("Test 4.1 passed: Correct items added")
    
    # Test 4.2: Zero items
    print("\nTest 4.2: add_n_items(0)")
    result = add_n_items(0)
    assert result == [], f"Expected [], got {result}"
    print("Test 4.2 passed: Correct items added")
    
    print()
    print("PROBLEM 5: Compute Running Totals")
    
    # Test 5.1: Example from problem
    result = running_total([1, 2, 3, 4])
    assert result == [1, 3, 6, 10], f"Expected [1, 3, 6, 10], got {result}"
    print("Test 5.1 passed: [1, 2, 3, 4] → [1, 3, 6, 10]")
    
    # Test 5.2: Negative numbers
    result = running_total([1, -2, 3, -1])
    assert result == [1, -1, 2, 1], f"Expected [1, -1, 2, 1], got {result}"
    print("Test 5.2 passed: [1, -2, 3, -1] → [1, -1, 2, 1]")
    
    print()
    print("ALL TESTS PASSED!")


if __name__ == "__main__":
    run_tests()