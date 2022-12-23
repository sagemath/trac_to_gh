# Issue 200: elliptic curve formal group printing error

Issue created by migration from https://trac.sagemath.org/ticket/200

Original creator: dmharvey

Original creation time: 2007-01-19 13:50:59

Assignee: was


```
sage: E = EllipticCurve("37a")

sage: E.formal_group()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

[...]
/home/was/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/formal_group.py in __repr__(self)
     24 
     25     def __repr__(self):
---> 26         return "The formal group associated to the " + self.__E
     27 
     28     def curve(self):

<type 'exceptions.TypeError'>: cannot concatenate 'str' and 'EllipticCurve_rational_field' objects
 


---

Comment by was created at 2007-01-25 19:25:04

Resolution: fixed
