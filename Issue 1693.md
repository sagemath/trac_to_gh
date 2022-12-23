# Issue 1693: jmol stubles over browser caching

Issue created by migration from https://trac.sagemath.org/ticket/1693

Original creator: schilly

Original creation time: 2008-01-05 20:20:07

Assignee: boothby

CC:  malb

applet is invoked by

```
jmol_applet(500, "/home/harri/5/cells/204/sage0-size500.jmol")
```

but does not get the new jmol file. possibly just needs a ?"number" as with plots/images


---

Comment by schilly created at 2008-01-05 20:21:27

Changing priority from major to blocker.


---

Attachment


---

Comment by robertwb created at 2008-01-08 23:06:45

Yes, this is the right fix.


---

Comment by mabshoff created at 2008-01-08 23:24:28

Resolution: fixed


---

Comment by mabshoff created at 2008-01-08 23:24:28

Merged in Sage 2.10.alpha1.


---

Comment by was created at 2008-01-09 04:28:16

looks good to me too.
