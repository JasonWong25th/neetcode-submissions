class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Any input validation needed?

        #is the output always guarneteed to fit in the results

        #Naive approch is we multiple the entire list
        #then for each element we divide it against the product

        #we can have a 2 pass approch
        #once where we are multipling everything before the element
        #and second where we are multipling after the current element

        #example:
        #[1,2,3,4]
        #[1, 1, 2,6] before
        #[24,12,4,1] after
        #[24,12,8,6] before and after

        pre_multiplication = [1]* len(nums)
        post_multiplication = [1] * len(nums)
        res = [1] * len(nums)
        #pre
        for i in range(1,len(nums)):
            pre_multiplication[i] = pre_multiplication[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1,-1):
            post_multiplication[i] = post_multiplication[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = pre_multiplication[i] * post_multiplication[i]
        return res
