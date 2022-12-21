# Issue 5216: Update bzip2 to 1.0.5 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-09 12:23:44

Assignee: mabshoff

This is a security issue:

```
Version 1.0.5 removes a potential security vulnerability (CERT-FI 20469 
as it applies to bzip2) in versions 1.0.4 and earlier, so all users are 
recommended to upgrade immediately.
```

and we have been shipping an vulnerable bzip2 release for a while. So upgrade :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 12:25:24

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-15 06:22:50

Changing status from assigned to new.


---

Comment by mhansen created at 2009-02-15 06:22:50

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-02-15 06:22:56

Changing status from new to assigned.


---

Attachment

This is Mike's patch slightly modified


---

Comment by mabshoff created at 2009-02-20 14:22:31

The new bzip2 tarball is at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/bzip2-1.0.5.tar.gz

Note that we should move the bzip2 code to an spkg soon.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 14:26:39

Positive review. Thanks Mike.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 14:26:59

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 14:26:59

Merged in Sage 3.3.r3.

Cheers,

Michael
