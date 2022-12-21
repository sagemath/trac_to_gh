# Issue 203: more elliptic curve n*P problems

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-21 03:44:16

Assignee: was


```
Argh!  Curves over extension fields don't work?
 
sage: E
Elliptic Curve defined by y^2  = x^3 + x over Finite Field in a of size 5^2
 
sage: P
(a : 2*a + 4 : 1)
 
sage: P+P+P+P+P
(2*a + 3 : 2*a : 1)
 
sage: 5*P
(0 : 1 : 0)

 
sage: 5*P
(0 : 1 : 0)
 
sage: P*5
(2*a + 3 : 2*a : 1)
```



---

Comment by was created at 2007-01-23 22:05:53

This is caused because

  P.parent().base() 

is the finite field instead of ZZ.  But that base is supposed to be
the base ring for the module that P is in!  Ouch.

William


---

Comment by was created at 2007-01-23 23:30:33

Fixed for sage > 1.8.  Actually pretty subtle to fix...


---

Comment by was created at 2007-01-23 23:30:33

Resolution: fixed
