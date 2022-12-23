# Issue 4624: Sage 3.2.1.a1: add ipy_profile_sage.py to list of files copied when sdisting

Issue created by migration from https://trac.sagemath.org/ticket/4624

Original creator: mabshoff

Original creation time: 2008-11-26 14:56:24

Assignee: mabshoff

CC:  mhansen

Sigh:

```
sage-3.2.1.alpha2/spkg/standard/sage_scripts-3.2.1.alpha1$ hg stat
! ipy_profile_sage.py
```



---

Comment by mabshoff created at 2008-11-26 15:02:34

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-26 15:02:34

One way to fix this is to rename the file sage-ipy_profile.py which is likely a lot less pain long term.

Mike: any thoughts?

Cheers,

Michael


---

Comment by mhansen created at 2008-11-26 15:09:58

This doesn't work because ipython wants it explictly named that way for looking up the profile.


---

Comment by mabshoff created at 2008-11-26 15:15:45

Replying to [comment:2 mhansen]:
> This doesn't work because ipython wants it explictly named that way for looking up the profile.

Yep, I looked at the file and I came to the same conclusion. I have "fixed" the issue by correcting the sage_scripts repo in the 3.2.1.a1 tarball manually for now, but will take care of this once I catch some sleep.

Cheers,

Michael


---

Attachment


---

Attachment

With the second patch this is good to go.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 02:06:45

Resolution: fixed


---

Comment by mabshoff created at 2008-11-27 02:06:45

Merged both patches in Sage 3.2.1.alpha2
