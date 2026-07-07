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

        res = [1] * len(nums)
        #pre
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
        suffix = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
