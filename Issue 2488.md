# Issue 2488: unused/broken hanke and pari pxy files

Issue created by migration from https://trac.sagemath.org/ticket/2488

Original creator: gfurnish

Original creation time: 2008-03-12 09:34:44

Assignee: was

This file does not compile with cython currently but is in the tree. It is currently disabled in setup.py and should be removed or fixed. This is a significant priority as it makes the development of efficient(parallel) build systems problematic and wastes space, especially for files which have not been touched in ages. Code that does not build should not be in the main repository. 

```
Error converting Pyrex file to C:
------------------------------------------------------------
...
290 problem.
"""



include 'interrupt.pxi'
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/hanke/hanke.pyx:17:0: 'interrupt.pxi' not found


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o hanke.c hanke.pyx
```


```
Error converting Pyrex file to C:
------------------------------------------------------------
...
                ^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/pari/test.pxd:5:17: Special methods must be declared with 'def', not 'cdef'

Error converting Pyrex file to C:
------------------------------------------------------------
...
^
------------------------------------------------------------

/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main/sage/libs/pari/test.pyx:3:0: 'interrupt.pxi' not found


cython -I/home/x/build/build/pbuild/sage-2.10.3.rc1-build-cur/devel/sage-main --incref-local-binop --embed-positions -o test.c test.pyx
```



---

Comment by gfurnish created at 2008-03-13 02:00:56

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-13 02:00:56

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-13 02:03:14

This is not ready


---

Attachment


---

Comment by gfurnish created at 2008-03-13 02:08:17

This is now ready for a review.


---

Comment by mabshoff created at 2008-03-13 07:48:33

`sage -ba` and a `-testall -long` works after applying this patch. I would suggest contacting the authors of the various files we remove "just in case".

Cheers,

Michael


---

Comment by was created at 2008-03-13 17:01:06

Hanke's code has never worked, so it's safe to remove. He can add it back if he can get it to work.  It's a substantial amount of code, but it shouldn't be in sage until it works and has somebody who will maintain it. 

The other pari code -- test.pyx, e.g., was something I wrote and can safely be deleted.


---

Comment by mabshoff created at 2008-03-14 22:29:12


```
[23:00] <mabshoff> wstein: you are fine with the code removal by gfurnish?
[23:00] <mabshoff> Then I will apply those patches now. 
[23:00] <wstein> yes
```



---

Comment by mabshoff created at 2008-03-14 22:34:41

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 22:34:41

Merged in Sage 2.10.4.alpha0
