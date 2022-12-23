# Issue 4512: [with patch, needs review] sage path-related troubles

Issue created by migration from https://trac.sagemath.org/ticket/4512

Original creator: craigcitro

Original creation time: 2008-11-13 10:58:04

Assignee: craigcitro

Unfortunately, it seems that `sage -sh` doesn't ask the shell to avoid processing the `.profile` or equivalent. In particular, it can lead to things like this:


```
[craigcitro@sharma ~/new-three-two]  $ ./sage -version
Sage Version 3.2.rc0, Release Date: 2008-11-10
[craigcitro@sharma ~/new-three-two]  $ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

[craigcitro@sharma ~/new-three-two]  $ sage -version
SAGE Version 3.1.4, Release Date: 2008-10-16
[craigcitro@sharma ~/new-three-two]  $ which sage
/usr/local/bin/sage
```


This comes from the fact that I manually *prepend* certain things to my path in my `.bashrc`. Sadly, this leads to several small, subtle issues. I've attached a patch which turns several calls to `sage` into `$SAGE_ROOT/sage`.

However, something more serious is needed. I think that the right approach is to start the new shell without processing any login files, so that we know our path is correct. The patch does that. 

I'm listing this as a blocker, because it causes such subtle errors, and because a fix is attached.


---

Attachment


---

Comment by craigcitro created at 2008-11-13 10:59:49

This patch is for the `sage-scripts` repository, of course.


---

Comment by craigcitro created at 2008-11-13 10:59:49

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-13 12:41:48

Could we at least have a PS1 that includes the current directory?  I always hated it when I was on a machine where "sage -sh" didn't use my existing PS1.


---

Comment by craigcitro created at 2008-11-13 13:16:35

Yeah, that would be very reasonable.

Actually, we could go one further: have a specific place in `~/.sage/` where one can put `.profile` files and whatnot, with big warnings about paths. The point is really just that we don't want to grab the system-wide ones ...


---

Comment by mabshoff created at 2008-11-14 04:16:38

Craig,

I am not so sure this is a blocker, i.e. just because your .profile is misconfigured doesn't mean that as a consequence somebody else's config will not be broken by fixing it for you. I am inclined to merge this patch, but I need to think about it.

Cheers,

Michael


---

Attachment

trac-4512-pt2.patch addresses all my concerns even though it could be cleaner, i.e. via some special parameter. Craig will do so in a followup ticket, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-14 06:00:05

Merged both patch in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-14 06:00:05

Resolution: fixed
