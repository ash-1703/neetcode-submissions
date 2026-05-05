class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        # text = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        # # print(text)  
        # text = text.lower()
        
        # return text[::].replace(" ","") == text[::-1].replace(" ","")
        # st=strr=""
        # for i in text[::]:
        #     st += i
        # for i in text[::-1]:
        #     strr += i
        # print(st)
        # print(strr.replace(" ",""))
        # return st.replace(" ", "") == strr.replace(" ","")

        l,r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l+=1
            while r > l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r=l+1,r-1
        return True

    def alphanum(self,c):
        return (ord("A") <= ord(c) <= ord('Z') or
            ord("a") <= ord(c) <= ord('z') or
            ord("0") <= ord(c) <= ord('9'))