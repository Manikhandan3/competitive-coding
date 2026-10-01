class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[len(cost)-1]
        two = cost[len(cost)-2]

        for i in range(len(cost)-3,-1,-1):
            temp = two
            two = cost[i] + min(one,two)
            one = temp
        
        return min(one,two)