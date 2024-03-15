class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for word in s.split(' ')[::-1]:
            if word != '':
                return len(word)
