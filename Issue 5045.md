# Issue 5045: sage's "make check" should check that the sage build flags (in sage-flags.txt) are right

Issue created by migration from https://trac.sagemath.org/ticket/5045

Original creator: was

Original creation time: 2009-01-21 06:00:52

Assignee: mabshoff

Some people do "make check" but never even try to run sage.  Thus it is stupid that make check can run without ever verifying that sage-flags.txt is valid.  If it isn't, just stop the check.


---

Attachment


---

Comment by was created at 2009-01-22 10:11:48

To test this, edit SAGE_ROOT/local/lib/sage-flags.txt and add some madeup flags like x.  Then test by doing, e.g., 

```
make check
```

and seeing that the build process properly stops.


---

Comment by mabshoff created at 2009-01-22 10:38:14

Nice.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 08:47:53

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 08:47:53

Resolution: fixed
