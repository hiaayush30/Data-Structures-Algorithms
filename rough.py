def isAnagram(s, t):
        if not len(s) == len(t):
            return False
        
        mapping =  {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
        for char in t:  
            if mapping[char] == 0:
                return False
            else:
                mapping[char] -= 1

        return True


print(isAnagram("cta","cat"))