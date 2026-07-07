class Solution:
    #clarifying questions
    # are all the strings ascii characthers
    #what happens whens strs are empty
    #or it's full of empty strings?

    #Naive approch, append them all into a single string
    #using a non ascii character as a delimiter
    
    #If there are non ascii characters allowed
    #need to determine the length of each string in the encoded
    #string. Also when the length ends and the starts since numbers are allowed
    
    def encode(self, strs: List[str]) -> str:
        
        return ''.join([f'{len(s)}#{s}' for s in strs])
    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            length_int = int(s[i:j])
            start = j + 1
            results.append(s[start:start+length_int])
            i = start+length_int
        return results


