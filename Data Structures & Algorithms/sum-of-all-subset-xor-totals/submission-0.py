class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(num: List[int], i: int) -> None:
            nonlocal res
         
            if i == len(nums):
                r = 0
                for n in num:
                    r ^= n
                res += r
                return
            num.append(nums[i])
            dfs(num, i+1)
            num.pop()
            dfs(num, i+1)
        dfs([],0)
        return res

