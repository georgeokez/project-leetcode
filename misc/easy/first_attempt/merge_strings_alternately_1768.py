class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if (len(word1) == len(word2)):
            return mergeStrings(word1, word2)

        if (len(word1) > len(word2)):
            return mergeStrings(word1[:len(word2)],word2) + word1[-(len(word1) - len(word2)):]
        
        if (len(word2) > len(word1)):
            return mergeStrings(word1, word2[:len(word1)]) + word2[-(len(word2) - len(word1)):]


def mergeStrings(str1, str2):
    merged = ''
    for i in range(len(str1)):
            merged = merged + str1[i]
            merged = merged + str2[i]

    return merged
