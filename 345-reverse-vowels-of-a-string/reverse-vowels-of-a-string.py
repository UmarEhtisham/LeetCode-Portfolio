class Solution:
    def reverseVowels(self, s: str) -> str:

        vow = "aeiouAEIOU"
        s_list = list(s)
        left, right = 0, len(s)-1
        while left < right:

            if s_list[left] in vow and s_list[right] not in vow:
                right -= 1

            elif s_list[left] not in vow and s_list[right] in vow:
                left += 1

            elif s_list[left] in vow and s_list[right] in vow:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            
            elif s_list[left] not in vow and s_list[right] not in vow:
                left += 1
                right -= 1
    
        return "".join(s_list)
            


        