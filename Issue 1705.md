# Issue 1705: factorization of polynomials over non-prime finite fields is TOTALLY BROKEN in Sage (and Singular?!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-07 04:01:49

Assignee: malb

CC:  mabshoff


```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: f = (x-a)*(y-a)
sage: f.factor()
x*y + ( - a)*x + ( - a)*y + (a + 1)
sage: singular(f)
x*y+(-a)*x+(-a)*y+(a+1)
sage: singular(f).factorH()
[1]:
   _[1]=1
   _[2]=x*y+(-a)*x+(-a)*y+(a+1)
[2]:
   1,1
sage: f = (x-2)*(y-1)
sage: f.factor()
(y - 1) * (x + 1)
sage: singular(f).factorH()
[1]:
   _[1]=1
   _[2]=x+1
   _[3]=y-1
[2]:
   1,1,1
```


In Magma this works fine:

```
k<a> := GF(9);
R<x,y> := PolynomialRing(k, 2);
f := (x-a)*(y-a);
print Factorization(f);

[
<y + a^5, 1>,
<x + a^5, 1>
]
```



---

Comment by malb created at 2008-01-07 11:28:35

I can confirm this behaviour with official Singular binary:


```
> ring r = (3,a),(x,y),dp;
> minpoly = a^2 + 2*a + 2;
> poly f = (x-a)*(y-a);
> factorize(f);
[1]:
   _[1]=1
   _[2]=xy+(-a)*x+(-a)*y+(a+1)
[2]:
   1,1
```


Michael volunteered to report this upstream.


---

Comment by was created at 2008-01-07 16:13:16

This bug is *so* terrible, that I think it should be considered a blocker, and we should have a NOtImplementedError be raised any time somebody factors a poly over a finite field in n variables.   This is really bad.


---

Comment by mabshoff created at 2008-01-09 16:10:10

The Singular team is working on a fix for this issue. I will keep you updated.

Cheers,

Michael


---

Attachment

Merged trac_1705.patch. We are closing this ticket and will open a new one once the issue is fixed upstream.


---

Comment by mabshoff created at 2008-01-18 01:48:49

Merged in Sage 2.10.alpha4.


---

Comment by mabshoff created at 2008-01-18 01:48:49

Resolution: fixed
