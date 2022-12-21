# Issue 4592: new setup.py dependency checking does not handle Cython built-in pxd files

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-11-23 04:56:53

Assignee: craigcitro

CC:  robertwb

I can't get #4580 to compile, and I think this is why:

#4580 adds "`from python_int cimport PyInt_AS_LONG`" to a Sage library file.  I believe this is intended to refer to $SAGE_ROOT/local/lib/python2.5/site-packages/Cython/Includes/python_int.pxd, but the setup.py dependency checker doesn't know about these Cython built-in pxd files, so it fails with an error: 

```
IOError: [Errno 2] No such file or directory: 'sage/rings/polynomial/python_int.pxd'
```



---

Attachment


---

Comment by craigcitro created at 2008-11-23 08:46:49

Adds code to also check the Cython include directory for any included `.pxd` files. Raises an error if a file can't be found. (Note that sometimes, this will sneak through and be caught by Cython instead.)


---

Comment by craigcitro created at 2008-11-23 08:46:49

Changing status from new to assigned.


---

Comment by cwitty created at 2008-11-23 16:22:14

The patch looks good, and does fix a problem.

Positive review.


---

Comment by mabshoff created at 2008-11-23 23:47:35

Merged in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-23 23:47:35

Resolution: fixed
