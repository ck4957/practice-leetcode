# Given two string s and t, if t is an anagram of s, return true else false
# Example: s: "anagram" t: nagaram, return true

# Solution 1: HashMap, Time Complexity: O(n), Memory:  O(S+T) building Hashaps
# Compare length of s and t
# Two hashMap for s and t, count occurance of each character

# Solution 2: less space complexity
# sorting both string

def isAnagram(self, s:str, t:str): bool
    return sorted(s) == sorted(t)
    
    # Counter is built-in python Data structure that helps in counting occurence of a char in string
    return Counter(s) == Counter(t)
    
    #Sol 1
    if len(s) != len(t):
        return False
    countS, countT: {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[s[i]] = 1 + countT.get(s[i],0)
        
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
        
        
    

