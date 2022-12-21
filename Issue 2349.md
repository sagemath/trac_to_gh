# Issue 2349: homogenize does different things in different contexts

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-02-28 21:54:09

Assignee: malb

CC:  ncalexan

Keywords: polynomial multi multivariate homogenize

Here are some examples:


```
sage: x = Zmod(3)['x'].gen(); x.homogenize('y')
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'
sage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y)
x^2 + x*y
sage: x, y = Zmod(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()
Multivariate Polynomial Ring in x, y, y over Ring of integers modulo 3
sage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y)
x^2 + x*y
sage: x, y = GF(3)['x', 'y'].gens(); (x + x^2).homogenize(y).parent()
Multivariate Polynomial Ring in x, y over Finite Field of size 3
```




---

Attachment


---

Comment by malb created at 2008-02-29 01:45:18

The attached patch unifies homogenize for the multivariate polynomials, but not the univariate yet.


---

Comment by ncalexan created at 2008-02-29 18:21:49

This patch fixes the code I was writing :)  It only applies to the multivariate case, see ticket #2352 for the univariate case.

Doctests are good.  I say apply.


---

Comment by mabshoff created at 2008-03-02 20:54:35

Resolution: fixed


---

Comment by mabshoff created at 2008-03-02 20:54:35

Merged in Sage 2.10.3.rc1
