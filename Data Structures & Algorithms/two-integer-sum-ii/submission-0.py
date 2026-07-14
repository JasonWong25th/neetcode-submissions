class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #are the numbers within the max integer size
        #are there going to be duplicates since
        # it's non-decreasing, not increaing
        #is the target within the max integrer size?

        #First thought is to construct a hashmap
        #and as we iterate we can try and find the element
        #complment
        #but we should take advantage of the fact that it's
        #sorted.

        #for each element we can apply binary search to find the complment
        #each time? that would still be nlogn though
        
        #apply a two pointer approch?
        #starting at the left and right most element
        #if it's larger than target move right and if larger move left
        #if there's no possible solution (guarnteed not true return -1)

        left, right = 0, len(numbers)- 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right +1]
            elif numbers[left] +numbers[right] < target:
                left += 1
            else:
                right -= 1
        return -1