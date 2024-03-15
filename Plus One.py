class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        rem = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += rem
            if digits[i] > 9:
                digits[i] = digits[i] % 10
            else:
                return digits
        digits.insert(0, 1)
        return digits
