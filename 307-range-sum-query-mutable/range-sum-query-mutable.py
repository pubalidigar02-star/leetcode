
class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i in range(self.n):
            self.add(i, nums[i])

    def add(self, index, val):
        index += 1

        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)

    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self.add(index, diff)

    def prefixSum(self, index):
        total = 0
        index += 1

        while index > 0:
            total += self.tree[index]
            index -= index & (-index)

        return total

    def sumRange(self, left, right):
        return self.prefixSum(right) - self.prefixSum(left - 1)
