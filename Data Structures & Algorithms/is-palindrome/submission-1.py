class Solution:
    def isPalindrome(self, s: str) -> bool:
        #is it guarenteed all of the string is ascii characters?
        #do we care about puncuation
        #do we care about spaces
        #uper or lower case?

        #racecar
        
        #first instinct is to iterate throughout the string
        #stringing nonalphanumeric characters
        #normalize the string (all lower or upper)
        #copy it then reverse it then compare with the orginal

        #second approch is to create left and right pointers
        #checking if it's alpha numeric, and if it's the same value
        #after normalizing it. Then escaping once left and right meet or 
        #pass each other

        left, right = 0, len(s)-1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1      
            if left >= right:
                return True
            
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True



