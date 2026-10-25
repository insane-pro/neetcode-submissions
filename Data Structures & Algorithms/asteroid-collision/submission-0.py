class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for ast in asteroids:
            while stk and ast<0<stk[-1]:
                if -ast>stk[-1]:
                    stk.pop()
                    continue
                elif -ast==stk[-1]:
                    stk.pop()
                break
            else:
                stk.append(ast)
        return stk
        