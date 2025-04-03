class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2" : "abc", "3" : "def", "4" : "ghi", "5" :"jkl", "6" :"mno", "7" :"pqrs", "8" :"tuv", "9" : "wxyz"}
        if not digits:
            return []
        n = len(digits)
        def backtrack(i, currPath):
            if len(currPath) == n:
                copy = "".join(currPath)
                ans.append(copy)
                return
            for letter in hashmap[digits[i]]:
                currPath.append(letter)
                backtrack(i + 1, currPath)
                currPath.pop()
        ans = []
        backtrack(0, [])
        return ans