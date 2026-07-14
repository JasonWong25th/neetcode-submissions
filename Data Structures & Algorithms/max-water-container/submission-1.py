class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # are all the heights positive
        #Create a test case

        #[1,4, 2,3] -> 3*3 => 9

        #my first thought is to create two pointer approch
        #starting at the left and right
        #will have a running max_water
        #depending on whichever pointer is smaller
        #will move the point closer to the center
        #until the pointers meet

        left, right = 0, len(heights) -1
        max_water = 0

        while left < right:
            min_height = min(heights[left],heights[right])
            current_water = min_height * (right-left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            max_water = max(max_water, current_water)
        return max_water