# Issue 239: x^(3/4) rounding issue

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-03 10:13:33

Assignee: somebody


```
> Can someone please add support for evaluating say 2^(3/4) or 7^(5/3).
>  
> > 
>  
 
About this I just found this bug:
 
sage: x=maxima('x')
 
sage: x^(3/4)
 x^3/4
 
sage: x=maxima('2')
 
sage: x^150
 1427247692705959881058285969449495136382746624
 
sage: x^(3/4)
 2
 
sage: maxima(3/4)
 3/4
 
Greg
```


Greg's problem is that the exponent is rounded maybe, since x^(3/4) should be the same as x^(maxima('3/4')).


---

Comment by was created at 2007-02-03 16:52:02


```
Is this the same bug?  The types involved seem very diverse, but the strange 
result appears remarkably similar.
 
sage: CF=CyclotomicField(3)
sage: two=CF(2)
sage: two^(1/3)
1
sage: me=two^(1/3)
sage: me.parent()
Cyclotomic Field of order 3 and degree 2
 
--
```



---

Comment by was created at 2007-02-03 17:33:16

Resolution: fixed


---

Comment by was created at 2007-02-03 17:33:16

This is now fixed for sage 2.1.   The fix involved making __pow__ more careful (to raise an error in many cases).
