
# Problem 1: Find Most Frequent Element

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return max(counts, key=counts.get)


"""
Time and Space Analysis for problem 1:
- Best-case: O(n), because we still check every number.
- Worst-case: O(n), because we go through the whole list.
- Average-case: O(n).
- Space complexity: O(n), because we store numbers in a dictionary.
- Why this approach? A dictionary makes it easy to count each number.
- Could it be optimized? We could sort the list first, but that
  would usually take more time. This way is simple and fast.
"""


# Problem 2: Remove Duplicates While Preserving Order

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
- Best-case: O(n), because we check every number.
- Worst-case: O(n) expected, using a set.
- Average-case: O(n).
- Space complexity: O(n), because we store the unique numbers.
- Why this approach? A set helps us find duplicates quickly,
  and the list keeps everything in the same order.
- Could it be optimized? We could use just a list, but checking
  for duplicates would be slower. Using a set is better for speed.
"""


# Problem 3: Return All Pairs That Sum to Target

# My original solution
def find_pairs_original(nums, target):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))

    return pairs


# My optimized solution
def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        needed = target - num

        if needed in seen:
            pairs.append((needed, num))

        seen.add(num)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n) expected for the optimized solution.
- Worst-case: O(n) expected with normal set performance.
- Average-case: O(n).
- Space complexity: O(n), because we use a set and a list.
- Why this approach? The set lets us find matching numbers
  without checking every possible pair.
- Could it be optimized? I already optimized this problem.

Original vs Optimized:
- My original solution used two loops to check every pair.
- The original time complexity was O(n^2).
- The original extra space was O(n) for the output pairs.
- My new solution uses a set and only needs one loop.
- The optimized time complexity is O(n) on average.
- The optimized space complexity is O(n).
- This makes it faster for larger lists.
- The trade-off is that it uses extra memory for the set.
"""


# Problem 4: Simulate List Resizing

def add_n_items(n):
    capacity = 2
    size = 0
    items = [None] * capacity

    for num in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print("Resizing from", capacity, "to", new_capacity)

            new_items = [None] * new_capacity

            for i in range(size):
                new_items[i] = items[i]

            items = new_items
            capacity = new_capacity

        items[size] = num
        size += 1

    return items[:size]


"""
Time and Space Analysis for problem 4:
- Best-case: O(1) for one append when there is space.
- Worst-case: O(n) for one append when resizing happens.
- Average-case: O(1) amortized per append.
- Total time: O(n) for adding n items.
- When do resizes happen? When the list becomes full.
- Space complexity: O(n), because the list grows with the data.
- Why this approach? Doubling the capacity means we don't
  have to resize the list every time we add something.
- Why does doubling help? It makes resizing happen less often,
  so adding lots of items is faster overall.
"""


# Problem 5: Compute Running Totals

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:
- Best-case: O(n), because we go through the list once.
- Worst-case: O(n), because we still go through the list once.
- Average-case: O(n).
- Space complexity: O(n), because we make a new list.
- Why this approach? Keeping a running total is easier than
  adding everything again for each position.
- Could it be optimized? We could change the original list
  instead of making a new one. That would save memory,
  but it would also change the original data.
"""


# Test Cases

def test_problems():
    # Problem 1
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3
    assert most_frequent([5, 5, 5]) == 5
    assert most_frequent([]) is None

    # Problem 2
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []

    # Problem 3
    assert sorted(find_pairs([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]
    assert find_pairs([1, 2, 3], 10) == []
    assert find_pairs([], 5) == []
    assert sorted(find_pairs_original([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]

    # Problem 4
    assert add_n_items(6) == [0, 1, 2, 3, 4, 5]
    assert add_n_items(0) == []
    assert add_n_items(1) == [0]

    # Problem 5
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([5]) == [5]
    assert running_total([]) == []
    assert running_total([-1, 2, -3]) == [-1, 1, -2]

    print("All tests passed!")


if __name__ == "__main__":
    test_problems()
