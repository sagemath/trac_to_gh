# Issue 202: Elliptic curve point multiplication bug.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-21 03:41:49

Assignee: somebody

From Nick Alexander:

```
I don't know how to fix this one.
 
sage: E
Elliptic Curve defined by y^2 + x*y  = x^3 + 1543929847778604404998775606458319946*x + 4576785278558486524781594900057632159 over Finite Field of size 9067796676684828360396591155312024321
 
sage: P = E.random_element()
 
sage: n
9067796676684828360396591155344486080L
 
sage: P*n
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)
 
/Users/nalexand/Devel/sage-alpha8/devel/sage-ncalexan/sage/<ipython console> in <module>()
 
/Users/nalexand/Devel/sage-alpha8/local/lib/python2.5/site-packages/sage/schemes/generic/morphism.py in __mul__(self, n)
    381         if isinstance(n, (RingElement, int, long)):
    382             # [n]*P - multiplication by n.
--> 383             return AdditiveGroupElement._lmul_(self, Integer(n))
    384         else:
    385             # Function composition
 
/Users/nalexand/Devel/sage-alpha8/devel/sage-ncalexan/sage/element.pyx in element.ModuleElement._lmul_()
 
/Users/nalexand/Devel/sage-alpha8/devel/sage-ncalexan/sage/element.pyx in element.AdditiveGroupElement._lmul_c_impl()
 
<type 'exceptions.OverflowError'>: long int too large to convert to int
 
The offending code even says:
 
    cdef ModuleElement _lmul_c_impl(self, RingElement right):
        cdef int m
        m = int(right)  # a little worrisome.
 
Understatement of the year.
 
Nick
```



---

Comment by was created at 2007-01-23 23:34:57

Resolution: fixed


---

Comment by was created at 2007-01-23 23:34:57

Fixed for sage > 1.8.
