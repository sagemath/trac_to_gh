# Issue 5805: numerical noise in "devel/sage/sage/modular/dirichlet.py"

Issue created by migration from https://trac.sagemath.org/ticket/5805

Original creator: jsp

Original creation time: 2009-04-16 21:02:12

Assignee: craigcitro

On Fedora 9, 32 bit:



```
sage -t  "devel/sage/sage/modular/dirichlet.py"             
**********************************************************************
File "/home/jaap/downloads/sage-3.4.1.rc0/devel/sage/sage/modular/dirichlet.py", line 1044:
    sage: e.kloosterman_sum_numerical()
Expected:
    7.21644966006e-16 + 1.73205080757*I
Got:
    6.66133814775e-16 + 1.73205080757*I
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_29
***Test Failed*** 1 failures.

```



Cheers,

Jaap




---

Comment by mabshoff created at 2009-04-17 10:18:41

Changing component from modular forms to doctest.


---

Comment by mabshoff created at 2009-04-17 10:18:41

Changing assignee from craigcitro to mabshoff.


---

Comment by mabshoff created at 2009-04-17 10:18:41

Another datapoint from 3.4.1.rc3 on Solaris 10/x86-64 running in 32 bit mode:

```
sage -t -long devel/sage/sage/modular/dirichlet.py
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/
devel/sage-main/sage/modular/dirichlet.py", line 10
44:
    sage: e.kloosterman_sum_numerical()
Expected:
    7.21644966006e-16 + 1.73205080757*I
Got:
    6.66133814775e-16 + 1.73205080757*I
**********************************************************************
```



---

Comment by mabshoff created at 2009-04-17 10:18:41

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-17 11:32:40

Add the Sage release, make it clear it is a blocker. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-17 11:32:40

Changing priority from major to blocker.


---

Attachment


---

Comment by cremona created at 2009-04-18 14:27:38

Patch looks good to me, applied ok to 3.4.1.rc3 and passed test on 32- and 64-bit.


---

Comment by mabshoff created at 2009-04-18 23:12:22

Resolution: fixed


---

Comment by mabshoff created at 2009-04-18 23:12:22

Merged in Sage 3.4.1.rc4.

Cheers,

Michael
