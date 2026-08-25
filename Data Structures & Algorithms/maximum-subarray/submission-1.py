class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadnes algrothim
        #create a sliding window tracking the growing sum
        #create another variable tracking the max_sum
        #if the window ever goes negative 
        #start a new window at current index

        if not nums:
            return 0
        max_sum = nums[0]
        cur_sum = nums[0]
        for right in range(1,len(nums),1):
            if cur_sum < 0:
                cur_sum = nums[right]
            else:
                cur_sum += nums[right]

            max_sum = max(max_sum,cur_sum)
        return max_sum