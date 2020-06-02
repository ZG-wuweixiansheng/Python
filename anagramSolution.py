# _*_ coding:utf-8 _*_
import time
def anagramSolution1(s1,s2):
    lists1=list(s1)
    post1=0
    stillOK=True
    while post1<len(lists1) and stillOK:
        lists2=list(s2)
        post2=0
        found=False
        while post2<len(lists2) and not found:
            if lists1[post1]==lists2[post2]:
                found=True
            else:
                post2=post2+1
        if found:
            lists2[post2]=None
        else:
            stillOK=False
        post1+=1
    return stillOK


def anagramSolution2(s1,s2):
    lists1=list(s1)
    lists2=list(s2)
    lists1=sorted(lists1)
    lists2=sorted(lists2)
    pos=0
    match=True
    while pos<len(lists1) and match:
        if lists1[pos]==lists2[pos]:
            pos+=1
        else:
             match=False
        return match


def anagramSolution3(s1,s2):
    c1=[0]*26
    c2=[0]*26
    for i in s1:
        pos=ord(i)-ord('a')
        c1[pos]+=1
    for i in s2:
        pos=ord(i)-ord('a')
        c2[pos]+=1
    j=0
    stillOK=True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j+=1
        else:
            stillOK=False
    return stillOK

print(anagramSolution1('abfdcghaakmr','raamkhcdfbag'))
print(anagramSolution2('abfdcghaakmr','raamkhcdfbag'))
print(anagramSolution3('abfdcghaakmr','raamkhcdfbag'))