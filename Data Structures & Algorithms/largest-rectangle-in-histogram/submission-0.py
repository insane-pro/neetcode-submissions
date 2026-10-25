class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        right=[n]*n
        left=[-1]*n
        stk=[]
        for i in range(n):
            while stk and heights[stk[-1]]>heights[i]:
                top=stk.pop()
                right[top]=i
            if stk:
                left[i]=stk[-1]
            stk.append(i)
        area=0
        for i in range(n):
            h=heights[i]
            w=right[i]-left[i]-1
            area=max(area,h*w)
        return area
        