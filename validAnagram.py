# Leetcode 242:

    # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    # Example 1:
    # Input: s = "anagram", t = "nagaram"
    # Output: true

    # Example 2:
    # Input: s = "rat", t = "car"
    # Output: false

# Solution:


# Algorithm:
# Option 1:
    # We sort the two strings and compare them to check for equality

# Option 2:
    # We create a hashmap and iterate through the first string to get a count of all characters in it. We then iterate through the second string and decrement the count if that character is found. We then loop through finally to check if all counts are 0 and if not, we return false.

# Code:

# Option 1:
def isAnagram(s: str, t: str) -> bool:
    return sorted(list(s)) == sorted(list(t))

# Option 2:
def isAnagram(s: str, t: str) -> bool:
    hashMap = {}

    for c in s:
        hashMap[c] = 1 + hashMap.get(c, 0)
    for c in t:
        hashMap[c] = hashMap.get(c, 0) - 1
    for c in hashMap:
        if hashMap[c] != 0:
            return False
    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("cat", "rac"))
print(isAnagram("rat", "tar"))