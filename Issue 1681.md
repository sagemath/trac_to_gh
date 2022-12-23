# Issue 1681: serious bug when raising complex(0,1) to the power of the Sage integer 2.

Issue created by migration from https://trac.sagemath.org/ticket/1681

Original creator: was

Original creation time: 2008-01-04 17:42:31

Assignee: somebody

Notice getting +1 instead of -1:


```
sage: z = complex(0,1)
sage: z
1j
sage: z*z
(-1+0j)
sage: z^2
(1+1.973601453121677e-310j)
sage: z^float(2)
(-1+0j)
sage: z^int(2)
(-1+0j)
```



---

Comment by was created at 2008-01-04 17:46:43


```
mabshoff: is #1681 the fault of the maxime interface?
[09:44am] william_stein: no
[09:44am] william_stein: I don't know
[09:44am] mabshoff: ok
[09:44am] william_stein: It probably has nothing to do with maxima.
[09:44am] william_stein: complex(0,1) is built into python
[09:44am] william_stein: probably the problem is in __pow__ in integer.pyx
```



---

Comment by robertwb created at 2008-01-04 21:07:47

Changing assignee from somebody to robertwb.


---

Comment by robertwb created at 2008-01-04 21:07:47

This is a bug in Python 

```
sage: complex(0,1).__pow__(2r)
(1+2.0489322973043257e-310j)
```


I've changed the Integer.__pow__ function to use ** (which should be faster too).


---

Comment by robertwb created at 2008-01-04 21:07:47

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-01-05 02:36:49

positive review by was in IRC.


---

Comment by mabshoff created at 2008-01-05 02:36:58

Resolution: fixed


---

Comment by mabshoff created at 2008-01-05 02:36:58

Merged in 2.9.2.rc1.
