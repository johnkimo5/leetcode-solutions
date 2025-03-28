class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # think normal brute force then optimize
        # use a hashmap
        if not digits:
            return []
        mapping = {"1" : "", "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        ans, currString = [], []
        # parameters of function should be currString, i
        def backtrack(currString, i):
            if i == len(digits):
                ans.append("".join(currString))
                return
            numbers = mapping[digits[i]]
            for num in numbers:
                currString.append(num)
                backtrack(currString, i + 1)
                currString.pop()
        backtrack(currString, 0)
        return ans
            