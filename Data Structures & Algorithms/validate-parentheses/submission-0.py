class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[0]*n
        top=-1
        i=0
        valid=0
        while(i<n):
            if (s[i]=='[' or s[i]=='{' or s[i]=='('):
                top+=1
                stack[top]=s[i]
            elif(s[i]==']' or s[i]=='}' or s[i]==')'):
                ch =stack[top]
                top-=1
                if((s[i]==']' and ch=='[') or (s[i]=='}' and ch=='{') or (s[i]==')' and ch=='(')):
                    valid=1
                else:
                    break;
            i+=1
                    
        if valid==1 and top==-1:
            return True
        else:
            return False
