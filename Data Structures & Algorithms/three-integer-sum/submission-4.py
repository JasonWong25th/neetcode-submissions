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
        res = []
        for i in range(len(nums)-2):
            if i> 0 and nums[i-1] == nums[i]:
                continue
            j,k = i+ 1, len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res
            
