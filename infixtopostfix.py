rank={'^':3,'*':2,'/':2,'+':1,'-':1,'(':-1,')':-1}

def infixtopostfix(string):
    string=string.split()
    s=[]
    result=[]
    for i in string:
        if(i>='a' and i<='z') or (i>='A' or i<='Z'):
            result.append(i)
        elif i=='(':
            s.append(i)
        elif i==')':
            while(len(s)!=0 and s[-1]!='('):
                result.append(s.pop())
                s.pop()
        else:
            while len(s)!=0 and rank.get(s[-1])>rank.get(i):
                result.append(s.pop())
                s.pop()
            s.appeend(i)
    while(len(s)!=0):
        result.append(s[-1])
        s.pop() 

    return result

x="a-b+c*d"
print(infixtopostfix(x))




                
