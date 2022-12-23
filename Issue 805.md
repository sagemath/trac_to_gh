# Issue 805: is_trivial() does not work for fractional ideals of number field

Issue created by migration from https://trac.sagemath.org/ticket/805

Original creator: dmharvey

Original creation time: 2007-10-03 14:12:24

Assignee: was


```
sage: F.<a> = QuadraticField(-5)
sage: I = F.ideal(3)
sage: I.is_trivial()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

/Users/david/sage-2.8.5/local/lib/python2.5/site-packages/sage/rings/ideal.py in is_trivial(self)
    229             return True
    230         elif self.is_principal():
--> 231             return self.gen().is_unit()
    232         raise NotImplementedError
    233 

<type 'exceptions.AttributeError'>: 'NumberFieldIdeal' object has no attribute 'gen'
```




---

Comment by robertwb created at 2007-11-04 02:35:38

Changing status from new to assigned.


---

Comment by robertwb created at 2007-11-04 02:35:38

Changing assignee from was to robertwb.


---

Attachment


---

Attachment

Both patches above should be applied: Robert's handles the special case of number fields; mine fixes a bug in multipolynomial ideals and makes generic ideals more robust.


---

Comment by was created at 2007-11-18 04:05:19

GOOD -- I especially like Nick's improvements.


---

Comment by mabshoff created at 2007-11-19 22:32:40

Merged in 2.8.13.alpha1.


---

Comment by mabshoff created at 2007-11-19 22:32:40

Resolution: fixed
