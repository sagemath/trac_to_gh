# Issue 4473: [with patch; needs review] loading file.sage that has a line "load foo.py" is broken due to a missing import

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-09 03:13:41

Assignee: was

CC:  mhansen




---

Attachment


---

Comment by was created at 2008-11-09 03:18:53

To test this, make a file foo.sage with

```
load a.py
```

in it, and make a.py an empty file.   Then try


```
sage: load foo.sage
```


and see that you don't get a big nasty printout.


---

Comment by mabshoff created at 2008-11-09 07:27:39

Nice catch. Positive review, we had to fix similar issues once we had updated to IPython 0.8.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-09 08:25:03

Merged in Sage 3.2.rc0


---

Comment by mabshoff created at 2008-11-09 08:25:03

Resolution: fixed
