# Issue 2648: bug in octave version

Issue created by migration from https://trac.sagemath.org/ticket/2648

Original creator: was

Original creation time: 2008-03-22 18:10:02

Assignee: was


```
The octave.version() command is returning '.1.73' when it should
almost certainly be returning '2.1.73'

This has been verified on three systems:
-- Sage 2.10.1 running in the Windows VM
-- Sage 2.10.3 running in the Windows VM
-- sagenb.org

If this is in fact a bug, I wonder if it is a bug in this command
alone or a more general bug having to do with returning strings from
Octave

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: octave.min([1,2,3])
 1
sage: octave.version()
'.1.73'
```



---

Attachment


---

Comment by was created at 2008-03-22 18:13:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-22 19:07:16

Patch looks good to me. Positive review.


---

Comment by mabshoff created at 2008-03-22 19:08:31

Resolution: fixed


---

Comment by mabshoff created at 2008-03-22 19:08:31

Merged in Sage 2.11.alpha1
