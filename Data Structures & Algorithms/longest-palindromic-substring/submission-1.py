class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        best_start = 0
        best_length = 1

        def expand(left: int, right: int) -> None:

            nonlocal best_start, best_length

            while(
                left >= 0 and right < len(s) and s[left] == s[right]
            ):
                current_length = right - left + 1

                if current_length > best_length:
                    best_start = left
                    best_length = current_length

                left -= 1 
                right += 1

        for i in range(len(s)):
            expand(i,i)

            expand(i, i+1)


        return s[best_start : best_start + best_length]
