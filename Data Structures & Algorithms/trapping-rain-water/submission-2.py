class Solution:
    def trap(self, height: List[int]) -> int:
        #my thoughts
        # in order for us to determine how much water needs to be trapped we
        #need to consider what the left max and right max are for 
        #each specific index. Take the minimum value. that will the amount
        #of water in each puddle
        #this can be represented as 2 arrays tracking the running maxes
        #going both ways

        #ways we can optimize
        #we can use a two pointer approch
        #tracking the local maximums of the left and right 
        #Always picking the lower bounds of it
        

        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        water = 0
        while left <= right:
            min_height = min(left_max,right_max)

            if left_max < right_max:
                if height[left] > left_max:
                    left_max = max(left_max, height[left])
                else:
                    water += max((left_max - height[left]),0)
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += max((right_max - height[right]),0)
                right -= 1
        return water


