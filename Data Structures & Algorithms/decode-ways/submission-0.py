class Solution:
    def numDecodings(self, s: str) -> int:
        #the first thing to note
        #if s is none
        #but it is guarneteed


        #do we need to do any input validation
        #assume not

        #Note if there's a 0, it has to be non-leading
        #special case to account for

        #breaking it down into the smaller problem
        #at each number I have to count both if I treat if as 
        #a single charcter and it's the start of a 2 letter combination
        #only if it's a 1 or 2
        #otherwise if it's 0,3-9 then it would be empty

        #I would probably want to use recursion in this case
        #and memoization caching the results as we go

        memo = {}
        memo[''] = 1

        def countWays(subString:str) -> int:
            if subString in memo:
                return memo[subString]
            #since we populate an empty string in memo
            #we can assume that it's not empty
            if subString[0] == '0':
                memo[subString] = 0
                return 0

            if subString[0] in ('1', '2') and len(subString) >= 2 and int(subString[:2]) < 27:
                memo[subString] =countWays(subString[1:]) + countWays(subString[2:])
            else:
                memo[subString] = countWays(subString[1:])

            return memo[subString]
        return countWays(s)
