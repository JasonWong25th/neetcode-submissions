class Solution:
    #clarifying questions
    # are all the strings ascii characthers
    #what happens whens strs are empty
    #or it's full of empty strings?

    #Naive approch, append them all into a single string
    #using a non ascii character as a delimiter
    
    
    def encode(self, strs: List[str]) -> str:
        SEP = '\x1f'
        return ''.join([s + SEP for s in strs])
    def decode(self, s: str) -> List[str]:
        if s:
            return s.split('\x1f')[:-1]
        else:
            return []