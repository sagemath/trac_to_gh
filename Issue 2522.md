# Issue 2522: modify "sage -pkg" to not include OSX junk in spkgs

Issue created by migration from https://trac.sagemath.org/ticket/2522

Original creator: cwitty

Original creation time: 2008-03-14 23:54:05

Assignee: mabshoff

It looks like maybe we only need to set an environment variable to eliminate at least some of the junk; see http://norman.walsh.name/2008/02/22/tar for details.


---

Attachment

One just has to set

```
COPYFILE_DISABLE=true
```

on OS X.


---

Comment by mabshoff created at 2009-02-16 04:34:31

Yep, that does the trick.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 04:34:44

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 04:34:44

Resolution: fixed
