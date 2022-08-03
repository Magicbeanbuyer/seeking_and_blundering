# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        if len(digits) == 0:
            return res

        self.dfs(digits, 0, dic, "", res)
        return res

    def dfs(self, nums, index, dic, path, res):
        if index >= len(nums):
            res.append(path)
            return
        string1 = dic[nums[index]]
        for i in string1:
            self.dfs(nums, index + 1, dic, path + i, res)


if __name__ == "__main__":

    # solution = Solution()
    # a = solution.letterCombinations("234")
    # print(a)
    # print(len(a))
    z = 0
    for i in [1, 2, 3]:
        for j in [4, 5, 6]:
            for x in [7, 8, 9]:
                print(i, j, x)
                z += 1
                print(z)
