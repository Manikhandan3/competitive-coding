class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0 
        end_time = float('-inf')
        for a,t in customers:
            start_time = max(end_time,a)
            wait_time += t + (start_time - a)
            end_time = start_time + t
        return wait_time/len(customers)
