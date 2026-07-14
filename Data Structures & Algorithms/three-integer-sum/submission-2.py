class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums validation
        #example
        #no duplicate triplets
        #[-1,0, 0, 0, 1] -> [[-1,0,1],[0,0,0]]

        #thoughts
        #sort the array to make it easier to calcuate permissions
        #then for each array element. Apply a 2 pointer approach
        #searching for values that allow for the total to be 0

        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            i += 1  # <-- moved here
        return res
            
