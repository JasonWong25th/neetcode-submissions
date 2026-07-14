class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #do i have to do any input validation
        #ex do all the numbers are guarenteed to fit in a single integer
        #are there duplicates
        #do they have to appear consecutivly in the array?
        
        #An example of an input would be 
        #[2,3,5,5,6] -> 2 (2,3)
        #[4,6,7,3,5] - > 5
        #[30, 23, 1, 4,8,6,7,5] -> 5

        #My first thought is to sort the array
        #after sorting we can create a sliding window tracking the longest
        #consectuive window. O(nlogn)

        #next thought would be to
        #create some sort of hashmap/set tracking the seen values. 
        #Then we iterate over the list again, checking if elem- 1 value
        #is seen. If so we ignore this value
        #if not we are going to create a loop to see if the elem +1 is present
        #and start a counter variable.
        #this way we are only going to count from the local minimums

        res = 0
        seen = set(nums)
        for elem in nums:
            if elem - 1 in seen:
                continue
            
            current = elem
            counter = 0
            while current in seen:
                counter += 1
                current += 1
            res = max(res, counter)
        return res

