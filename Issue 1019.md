# Issue 1019: strange behavious in notebook with %octave

Issue created by migration from https://trac.sagemath.org/ticket/1019

Original creator: mabshoff

Original creation time: 2007-10-28 09:41:32

Assignee: boothby

The following was reported by David Galant:

```
In the notebook, starting a block with '%octave' does not produce a
result.
This has been consistent throughout all releases of sage 2.*
The behavior is consistent on MacOS and Ubuntu Linux.
A sample session showing this is:
 
sage: from math import *
sage: sin(1)
0.8414709848078965
sage: gp.sin(1)
0.8414709848078965066525023216
sage: octave.sin(1)
0.841471
sage: %gp
sage: sin(1)
0.8414709848078965066525023216
sage: %octave
sage: sin(1)
 
sage: 3+2
5
sage: quit
Exited sage process
```


See


---

Comment by mabshoff created at 2008-02-15 22:31:51

This is still an issue with 2.10.1 and when I now switch the Sage notebook at sagenb into octave mode it seems like only every second cell is evaluated.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 22:31:51

Changing priority from major to critical.


---

Comment by boothby created at 2008-03-05 07:14:28

Changing assignee from boothby to was.


---

Comment by mhansen created at 2008-09-03 00:54:03

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-09-03 00:54:03

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-01-22 09:21:38

It turns out that this is caused by the chdir command (which is run before each cell is evaluated) screwing up the syncronization.

This can also be fixed by improving the Octave interface to have better error detection.


---

Comment by jason created at 2009-01-22 17:11:36

This works for me.  Mike explained the patch and it sounds reasonable.  Positive Review.


---

Comment by mabshoff created at 2009-01-23 08:03:19

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 08:03:19

Resolution: fixed
