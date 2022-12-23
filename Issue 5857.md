# Issue 5857: E.list() for E an elliptic curve over a finite field is broken

Issue created by migration from https://trac.sagemath.org/ticket/5857

Original creator: was

Original creation time: 2009-04-22 15:47:55

Assignee: was

E.list() doesn't work, but list(E) works fine.


```
sage: E = EllipticCurve(GF(11), [1,2])
sage: E.list()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/15239/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.list (sage/structure/parent.c:5196)()

AttributeError: 'EllipticCurve_finite_field' object has no attribute '__iter__'
sage: list(E)

[(0 : 1 : 0),
 (1 : 2 : 1),
 (1 : 9 : 1),
 (2 : 1 : 1),
...
```


See also #5856


---

Comment by davidloeffler created at 2009-07-21 08:14:53

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-21 08:14:53

Changing component from number theory to elliptic curves.


---

Attachment

Applies to 4.1.1


---

Comment by cremona created at 2009-08-18 20:53:22

I think this does what was wanted.


---

Comment by AlexGhitza created at 2009-08-19 10:34:53

Looks good.


---

Comment by mvngu created at 2009-08-23 02:07:34

reviewer patch


---

Comment by mvngu created at 2009-08-23 02:11:00

Resolution: fixed


---

Attachment

The reviewer patch `trac_5857-reviewer.patch` fixes a trivial typo in ReST formatting. Merged patches in this order:

 1. `trac_5857-elliptic_curve_iterator.patch`
 1. `trac_5857-reviewer.patch`
