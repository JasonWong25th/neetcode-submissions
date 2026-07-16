class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #my first thoughts are to create a sliding window
        #the important thing to know is how many replacement
        #characters have been used in the string
        #this can be tracked using a hashmap tracking the occurences
        #we have to shrink the window once the differnce between
        #the window - the max character occurence is greater than k

        left = 0
        frequencies = defaultdict(int)
        max_res = 0
        for i in range(len(s)):
            frequencies[s[i]] += 1
            
            while i -left +1 - max(frequencies.values()) > k:
                frequencies[s[left]] -= 1
                if frequencies[s[left]] == 0:
                    del frequencies[s[left]]
                left += 1
            max_res = max(max_res, i -left +1)
            
        max_res = max(max_res, len(s) -left)
        return max_res
            