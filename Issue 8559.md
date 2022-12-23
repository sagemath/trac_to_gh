# Issue 8559: add Playfair cipher as a classical cryptosystem

Issue created by migration from https://trac.sagemath.org/ticket/8559

Original creator: mvngu

Original creation time: 2010-03-19 08:14:07

Assignee: mvngu

CC:  amca01@gmail.com

From Alasdair McAndrew:

```
Here is some code to implement the Playfair cipher.  Maybe you could take it and squeeze it into the Sage "Classical Cryptosystems" section - I don't know how to do this.

cheers,
Alasdair

-- 
Blog: http://amca01.wordpress.com
Web:  http://bit.ly/Alasdair
Facebook: http://www.facebook.com/alasdair.mcandrew
--
# Playfair cipher

def makePF(word): #creates 5 x 5 Playfair array beginning with "word"
    alph='ABCDEFGHIKLMNOPQRSTUVWXYZ'
    pf=''
    for ch in word:
        if (ch<>"J") & (pf.find(ch)==-1):  # ensures no letter is repeated
            pf+=ch
    for ch in alph:
        if pf.find(ch)==-1:  #only uses unused letters from alph
            pf+=ch
    PF=[[pf[5*i+j] for j in range(5)] for i in range(5)]
    return PF

def pf_encrypt(di,PF): # encrypts a digraph di with a Playfair array PF
    for i in range(5):
        for j in range(5):
            if PF[i][j]==di[0]:
                i0=i
                j0=j
            if PF[i][j]==di[1]:
                i1=i
                j1=j
    if (i0<>i1) & (j0<>j1):
        return PF[i0][j1]+PF[i1][j0]
    if (i0==i1) & (j0<>j1):
        return PF[i0][(j0+1)%5]+PF[i1][(j1+1)%5]
    if (i0<>i1) & (j0==j1):
        return PF[(i0+1)%5][j0]+PF[(i1+1)%5][j1]

def insert(ch,str,j):  # a helper function: inserts a character "ch" into
    tmp=''             # a string "str" at position j
    for i in range(j):
        tmp+=str[i]
    tmp+=ch
    for i in range(len(str)-j):
        tmp+=str[i+j]
    return tmp


def playfair(pl,word): # encrypts a plaintext "pl" with a Playfair cipher
    PF=makePF(word)    # using a keyword "word"
    pl2=makeDG(pl)
    tmp=''
    for i in range(len(pl2)//2):
        tmp+=pf_encrypt(pl2[2*i]+pl2[2*i+1],PF)
    return tmp

def makeDG(str): # creates digraphs with different values from a string "str"
    tmp=str.replace('J','I')  # replace all 'J's with 'I's
    c=len(tmp)
    i=0
    while (c>0) & (2*i+1<len(tmp)):
        if tmp[2*i]==tmp[2*i+1]:
            tmp=insert("X",tmp,2*i+1)
            c-=1
            i+=1
        else:
            c-=2
            i+=1
    if len(tmp)%2==1:
        tmp+='X'
    return tmp
```

