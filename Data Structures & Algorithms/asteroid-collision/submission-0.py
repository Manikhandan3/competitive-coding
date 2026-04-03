class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(a)
                elif stack[-1] == abs(a):
                    stack.pop()
            else:
                stack.append(a)
        return stack
                