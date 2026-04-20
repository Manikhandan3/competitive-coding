class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        count = Counter(nums)
        def backtracking():
            if len(temp) == len(nums):
                ans.append(temp.copy())
                return

            for c in count:
                if count[c] > 0:
                    temp.append(c)
                    count[c] -= 1
                    backtracking()
                    count[c] += 1
                    temp.pop()

                
        backtracking()

        return ans
