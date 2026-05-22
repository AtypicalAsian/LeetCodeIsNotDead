class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l,r = 0,len(s)-1
        char_list = list(s)

        
        while l <= r:
            #increase left until we hit an alphabet letter
            while l < r and not char_list[l].isalpha():
                l+=1
            #decrease right until we hit an alphabet letter
            while l < r and not char_list[r].isalpha():
                r-=1
            #when both are alph letters -> swap then inc/dec both
            char_list[l],char_list[r] = char_list[r],char_list[l]
            l+=1
            r-=1
        
        return ''.join(char_list)