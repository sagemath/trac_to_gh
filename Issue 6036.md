# Issue 6036: a bug in polynomial()

Issue created by migration from https://trac.sagemath.org/ticket/6036

Original creator: klee

Original creation time: 2009-05-14 02:16:55

Assignee: Somebody

This works:


```
sage: R.<x,y>=PolynomialRing(QQ,2)
sage: a=x^2+x*y+y
sage: a.polynomial(x)
x^2 + y*x + y
```


But this does not work:


```
sage: R.<x,y>=PolynomialRing(GF(5),2)
sage: a=x^2+x*y+y
sage: a.polynomial(x)
Traceback (most recent call last):
...
TypeError: 'tuple' object cannot be interpreted as an index 
```


The bug is essentially in:

```
sage: B=QQ[x]
sage: print B({0:1,1:2})
2*x + 1
sage: print B({(0,):1,(1,):2})
2*x + 1
sage: B=GF(5)[x]
sage: print B({0:1,1:2})
2*x + 1
sage: print B({(0,):1,(1,):2})
Traceback (most recent call last):
...
TypeError: 'tuple' object cannot be interpreted as an index
}}

I think the second form is not acceptable. Then the function
remove_from_tuple() in sage.rings.polynomial.multi_polynomial.pyx
should be revised as it output (1,) from (1,2) for example


---

Comment by mabshoff created at 2009-05-14 05:27:44

Changing component from algebra to basic arithmetic.


---

Attachment


---

Attachment


---

Attachment

I attached a folded patch -- it should be applied instead of the other two.

Looks good to me.


---

Comment by mabshoff created at 2009-05-19 18:51:35

Merged trac_6036.patch in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 18:51:35

Resolution: fixed
