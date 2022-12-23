# Issue 3326: trailing question marks in %html blocks are mistreated

Issue created by migration from https://trac.sagemath.org/ticket/3326

Original creator: jhpalmieri

Original creation time: 2008-05-28 20:01:47

Assignee: somebody

Keywords: %html

In the notebook:


```
sage: %html  How are you?
```

returns

```
No object 'you' currently defined.
```




---

Attachment


---

Comment by mhansen created at 2009-01-23 12:32:04

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-23 12:32:04

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2009-01-23 12:32:04

I'm fixing this by making sure that introspection is only done in a Sage cell.

Note that this depends on #5050.


---

Comment by jhpalmieri created at 2009-01-24 16:03:26

The patch fails to apply cleanly to 3.3.alpha1:

```
patching file sage/server/notebook/worksheet.py
Hunk #4 FAILED at 2575
1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/worksheet.py.rej
```

and I can't figure how to fix it by hand to test it out.


---

Comment by mhansen created at 2009-01-25 00:16:58

Sorry, I forgot to mention that this also depends on the patch at #3201.


---

Comment by jhpalmieri created at 2009-01-25 00:25:07

This fixes the problem for me.


---

Comment by mabshoff created at 2009-01-28 15:19:06

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 15:19:06

Merged in Sage 3.3.alpha3.

Cheers,

Michael
