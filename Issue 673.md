# Issue 673: Solaris 10: rings/complex_double.pyx doctests failure: inf vs. Infinity

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 00:34:27

Assignee: was

Keywords: Solaris 10, doctest, real double


```
sage -t  rings/real_double.pyx                              **********************************************************************
File "real_double.pyx", line 952:
    sage: RDF(0).log()
Expected:
    -inf
Got:
    -Infinity
**********************************************************************
File "real_double.pyx", line 954:
    sage: RDF(-1).log()
Expected:
    nan
Got:
    -NaN
**********************************************************************
```



---

Comment by mabshoff created at 2007-09-17 01:24:19

Changing assignee from was to failure.


---

Comment by mabshoff created at 2007-09-17 01:24:19

Changing component from packages to doctest.


---

Comment by mabshoff created at 2008-04-15 00:02:10

Some of this might have been fixed by #848.

Cheers,

Michael


---

Attachment


---

Attachment

Positive review for both patches. This also makes the printing of NaN and Infinity consistent with CC. At the same time it fixes three more doctesting issues on Solaris where the libc caused different printouts.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 07:10:22

Merged both patches in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 07:10:22

Resolution: fixed
