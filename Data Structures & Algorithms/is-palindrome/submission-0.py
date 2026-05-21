class Solution:
    def isPalindrome(self, s: str) -> bool:
        san = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for x in range(len(san)):
            print(x,san[x], san[len(san) - x - 1])
            if san[x] != san[len(san) - x - 1]:
                return False
        return True
        