# Issue 4180: magic pexpect logging switch

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-09-23 22:16:39

Assignee: was


```
Yeah, I think it would greatly help if users could send an env
variable that dumps the pexpect communication to a file. Currently I
have to debug some Singular vs. pexpect problems on Solaris, but I
guess with mhansen's help I will finally learn how to fix those
issues. But for random users out there a magic switch that gives us
logs and helps us hunt down "random" problems would be a great thing
IMHO.
```



---

Attachment


---

Comment by mhansen created at 2008-09-24 00:14:59

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-24 00:14:59

I've added a patch to do this which uses the SAGE_PEXPECT_LOG environment variable.


---

Comment by mhansen created at 2008-09-24 00:14:59

Changing assignee from was to mhansen.


---

Comment by mabshoff created at 2008-09-24 02:12:11

The patch looks very nice to me and will surely help us debug loads of Heisenbugs in the future. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 04:24:27

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-24 04:24:27

Resolution: fixed
