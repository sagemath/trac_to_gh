# Issue 2029: adjust TIMEOUT for long and valgrinded doctests

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-02 04:30:56

Assignee: failure


```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.10.1.rc4$ ./sage -t -valgrind -long devel/sage/sage/calculus/calculus.py
sage -t -valgrind -long devel/sage-main/sage/calculus/calculus.py
Raising timeout to 1800 seconds due to '-long' option

Raising timeout to 1048576 seconds due to valgrind
```


Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 04:31:02

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-02 04:31:02

Changing assignee from failure to mabshoff.


---

Attachment

Patch applies cleanly. 
Tested that -long, -valgrind work as advertised.


---

Comment by mabshoff created at 2008-02-02 05:22:47

Resolution: fixed


---

Comment by mabshoff created at 2008-02-02 05:22:47

Merged in Sage 2.10.1.rc5


---

Comment by was created at 2008-02-02 08:06:52

another positive review.
