#!/usr/bin/env python
# coding: utf-8

# In[10]:


# -*- coding : cp949 -*-
class Calc:
    def sum(self,a,b):
        result=a+b
        print("{0:d} + {1:d} = {2:d} 입니다".format(a,b,result))
    def sub(self,a,b):
        result=a-b
        print("{0:d} - {1:d} = {2:d} 입니다".format(a,b,result))
    def multi(self,a,b):
        result=a*b
        print("{0:d} * {1:d} = {2:d} 입니다".format(a,b,result))
    def divi(self,a,b):
        result=a/b
        print("{0:d} / {1:d} = {2:d} 입니다".format(a,b,int(result)))
calc=Calc()
calc.sum(1,2)
calc.sub(5,1)
calc.multi(2,3)
calc.divi(6,2)


# In[5]:


class myStack:
    def __init__(self,list):
        self.list=[]
    def push(self,a):
        self.list.append(a)
    def pop(self):
        if(self.list):
            a=self.list.pop()
            return a
        else:
            return
    def peek(self):
        if(self.list):
            a=self.list[-1]
            return a
        else:
            return
        
num=myStack("num")
op=myStack("op")

string=input("input: ")
element=string.split()

for x in element:
        if (x!="+" and x!="-" and x!="*" and x!="/"):
            num.push(x)
        if(op.peek()=="*" or op.peek()=="/"): #최상위 연산자가 곱셈/나눗셈 이라면 연산을 진행한다
                oper=op.pop()
                a=num.pop()
                b=num.pop()
                if(oper=="*"):
                    result=float(b)*float(a)
                elif(oper=="/"):
                    result=float(b)/float(a)
                num.push(str(result))
        if(x=="*" or x=="/"):
            op.push(x)
            continue
        if(x=="+" or x=="-"):
            op.push(x) 
            
#덧셈과 뺄셈으로만 이루어진 수식 계산 
i=0
answer=float(num.list[0])
for i in range(0,len(op.list)):
    if(op.list[i]=="+"):
        answer+=float(num.list[i+1])
    if(op.list[i]=="-"):
        answer-=float(num.list[i+1])

print("{0:s} = {1:f}".format(string,answer))


# In[ ]:




