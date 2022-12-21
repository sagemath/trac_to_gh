# Issue 5012: Solaris 10/x86: Numerical noise in sage/rings/qqbar.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-18 06:50:40

Assignee: mabshoff

CC:  cwitty

Here we go:

```
[4:36pm] mabs: cwitty: I have another interesting bug for you:
[4:36pm] mabs: File "/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/qqbar.py", line 3826:
[4:36pm] mabs:     sage: cp.complex_roots(30, 1)
[4:36pm] mabs: Expected:
[4:36pm] mabs:     [1.189207115002721?,
[4:36pm] mabs:     -1.189207115002721?,
[4:36pm] mabs:     1.189207115002721?*I,
[4:36pm] mabs:     -1.189207115002721?*I]
[4:36pm] mabs: Got:
[4:36pm] mabs:     [1.189207115002721?, -1.189207115002722?, 1.189207115002721?*I, -1.189207115002721?*I]
[4:37pm] mabs: Notice that the second and third entries are different?
[4:37pm] mabs: Ehh, the second only
[4:38pm] cwitty: Yes.  It's probably not a bug; complex_roots doesn't guarantee to find the tightest possible 
interval, and it depends on ATLAS which doesn't guarantee identical results.
[4:38pm] mabs: ok
[4:38pm] mabs: Should I use "..." then?
[4:38pm] cwitty: Yes.
```


Patch coming up. Credit is shared with cwitty.


---

Comment by mabshoff created at 2009-01-18 06:50:55

Changing status from new to assigned.


---

Attachment

Patch looks pretty good, with one exception: guaranteed is misspelled in the patch. Once that is fixed, this looks good.


---

Comment by mabshoff created at 2009-01-18 14:01:05

I fixed the spelling issue in the patch I applied.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 14:01:15

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 14:01:15

Merged in Sage 3.3.alpha0
