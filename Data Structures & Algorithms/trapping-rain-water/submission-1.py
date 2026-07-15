class Solution:
    def trap(self, height: List[int]) -> int:
        #my thoughts
        # in order for us to determine how much water needs to be trapped we
        #need to consider what the left max and right max are for 
        #each specific index. Take the minimum value. that will the amount
        #of water in each puddle
        #this can be represented as 2 arrays tracking the running maxes
        #going both ways

        left_maxes = []
        right_maxes = [0]* len(height)
        left_max = 0
        for h in height:
            left_max = max(left_max, h)
            left_maxes.append(left_max)

        right_max = 0
        for i in range(len(height)-1, -1, -1):
            right_max = max(right_max, height[i])
            right_maxes[i] =right_max

        # print(left_maxes)
        # print(right_maxes)
        water = 0
        for i in range(len(height)):
            local_min = min(left_maxes[i], right_maxes[i])
            # print(i, max(local_min - height[i],0))
            water += max(local_min - height[i],0)
        return water

