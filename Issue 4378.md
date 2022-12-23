# Issue 4378: 3.2.alpha1: -sdist does not copy html from template directory

Issue created by migration from https://trac.sagemath.org/ticket/4378

Original creator: mabshoff

Original creation time: 2008-10-28 18:31:17

Assignee: mabshoff

-sdist needs to copy the new html files in the template directory. Otherwise Sage does not start up and all the tests fail on "make check"

These html files need to be added to MANIFEST.in

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 18:31:25

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-31 23:36:57

With the html files added to MANIFEST.in the repo does not lack any files:

```
dist/sage-3.2.alpha2/spkg/standard/sage-3.2.alpha2$ hg stat
dist/sage-3.2.alpha2/spkg/standard/sage-3.2.alpha2$ 
```


Cheers,

Michael


---

Attachment

Looks good.


---

Comment by mabshoff created at 2008-10-31 23:47:46

Resolution: fixed


---

Comment by mabshoff created at 2008-10-31 23:47:46

Merged in Sage 3.2.alpha2
