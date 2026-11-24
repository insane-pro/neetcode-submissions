class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ret,sol=[],[]
        def bt_dfs(i):
            if i==n:
                ret.append(sol[:])
                return
            bt_dfs(i+1)
            sol.append(nums[i])
            bt_dfs(i+1)
            sol.pop()
        bt_dfs(0)
        return ret
        