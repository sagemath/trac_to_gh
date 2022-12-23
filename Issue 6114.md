# Issue 6114: symbolics -- fix removal of constants.so

Issue created by migration from https://trac.sagemath.org/ticket/6114

Original creator: was

Original creation time: 2009-05-21 18:38:31

Assignee: burcin


```
Upgrading from alpha0 on Fedora 10 failed somehow. I had to remove constants.so
by hand.

$ rm devel/sage/build/sage/symbolic/constants.so

Now testing.

On Fedora 9 I'll do a fresh install.

```


I (=william) did remove enough constants.* files, which resulted in the above.  I will attach a patch to fix this.


---

Comment by mhansen created at 2009-05-28 02:59:37

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 02:59:37

Craig's sync-build at #5977 gives a cleaner way to do this.


---

Comment by mhansen created at 2009-05-28 02:59:37

Changing assignee from burcin to mhansen.


---

Comment by mhansen created at 2009-05-28 06:11:48

Actually, this won't work if there is a stale constants.cpp file sitting around in the directory.


---

Attachment


---

Comment by mhansen created at 2009-05-28 08:04:21

Resolution: fixed


---

Comment by mhansen created at 2009-05-28 08:04:21

Merged in 4.0.rc1.
