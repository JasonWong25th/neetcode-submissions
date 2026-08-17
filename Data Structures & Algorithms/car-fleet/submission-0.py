class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #imagining the high way
        #target 6
        #[0,2,3,4,5]
        #[3,4,2,1,1]

        #If they could overtake each other. Assuming it takes 1 hr to move
        # a position
        #Car 0 would be there in 2 hrs
        #Car 1 would be there in 1 hr
        #car 2 would be there in 1.5
        # Car 3 would be there in 2 hrs
        # car 4 would be there in 1 hr

        #since they have to join car fleets
        #the faster cars join the slowest current cars pace

        #solution is to sort them based on starting position
        #starting from closest to the target

        #start a stack to track the fleets
        #as we desecend down

        fleets = []
        for start, velocity in sorted(zip( position, speed), reverse= True):
            time = (target - start) / velocity
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)

