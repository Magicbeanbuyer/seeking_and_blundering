def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
     after removing all the numbers greater than or equal to n, all the numbers remaining are smaller than n.
     If any number i appears, we add n to nums[i] which makes nums[i]>=n. Therefore, if nums[i]<n, it means i never
     appears in the array and we should return i.
    """
    nums.append(0)
    n = len(nums)
    for i in range(n):  # delete those useless elements
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(n):  # use the index as the hash to record the frequency of each number
        index = nums[i] % n
        nums[index] += n
    for i in range(1, n):
        if nums[i] / n == 0:
            return i
    return n


test_first()
