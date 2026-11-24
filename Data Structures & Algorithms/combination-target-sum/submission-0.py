class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret,sol=[],[]
        nums.sort()
        def bt(start: int, rem: int) -> None:
            if rem == 0:                  # Fix 1: countdown hits 0
                ret.append(sol[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > rem:         # Fix 2: check current candidate nums[i]
                    break
                sol.append(nums[i])
                bt(i, rem - nums[i])      # Fix 3: pass 'i' for reuse + subtract nums[i]
                sol.pop()

        bt(0, target)
        return ret