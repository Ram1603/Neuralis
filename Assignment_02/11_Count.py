def topKFrequent(nums, k):
    
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    sorted_nums = sorted(counts, key=counts.get, reverse=True)

    return sorted_nums[:k]