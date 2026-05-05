class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        text = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        # print(text)  
        text = text.lower()
        
        return text[::].replace(" ","") == text[::-1].replace(" ","")
        # st=strr=""
        # for i in text[::]:
        #     st += i
        # for i in text[::-1]:
        #     strr += i
        # print(st)
        # print(strr.replace(" ",""))
        # return st.replace(" ", "") == strr.replace(" ","")