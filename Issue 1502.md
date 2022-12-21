# Issue 1502: calculus -- bug in argument ordering for formal functions

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-14 05:41:19

Assignee: was

This is wrong:


```
sage: f = function('Gamma', var('z'), var('w')); f
Gamma(z, w)
sage: f(2)
Gamma(z, 2)
sage: f(2,5)
Gamma(5, 2)
```


It should be


```
sage: f = function('Gamma', var('z'), var('w')); f
Gamma(z, w)
sage: f(2)
Gamma(2, w)
sage: f(2,5)
Gamma(2, 5)
```


Note that this works:


```
sage: f(z,w) = function('Gamma'); f
(z, w) |--> Gamma(z, w)
sage: f(2)
Gamma(2, w)
sage: f(2,5)
Gamma(2, 5)
```



---

Attachment


---

Comment by mhansen created at 2007-12-14 06:42:52

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-14 06:42:52

Apply after #553 .


---

Comment by mhansen created at 2007-12-14 06:42:52

Changing assignee from was to mhansen.


---

Comment by mabshoff created at 2007-12-15 11:32:34

Was reviewed this positively in IRC during BD7. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-15 11:33:01

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 12:20:20

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 12:20:20

Merged in 2.9.rc0.
