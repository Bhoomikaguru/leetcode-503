class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]

            if i < n:
                stack.append(idx)

        return res


# ── Test it locally ────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 1],          [2, -1, 2]),
        ([1, 2, 3, 4, 3],    [2, 3, 4, -1, 4]),
        ([5, 4, 3, 2, 1],    [-1, 5, 5, 5, 5]),
        ([1],                [-1]),
    ]

    for nums, expected in test_cases:
        result = sol.nextGreaterElements(nums)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{status} | Input: {nums} | Got: {result} | Expected: {expected}")