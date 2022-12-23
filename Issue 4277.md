# Issue 4277: [with patch, needs review] improve doctest coverage of ell_point.py

Issue created by migration from https://trac.sagemath.org/ticket/4277

Original creator: zimmerma

Original creation time: 2008-10-13 19:48:41

Assignee: was

The patch improves the doctest coverage of ell_point.py to 100%. However, a test is failing, with _magma_init_(), and I wasn't able to fix it, it seems the _magma_().name() implementation is buggy:

```
File "/usr/local/sage-3.1.2/sage/tmp/ell_point.py", line 1289:
    sage: P._magma_init_()
Expected:
    'EllipticCurve([GF(17)!1,GF(17)!16])![13,4]'
Got:
    '_sage_[2]![_sage_[3],_sage_[4]]'
```

Also, I believe ell_padic.py should be removed, since it is said it is deprecated, and it does
not seem to be used anywhere.


---

Attachment


---

Comment by robertwb created at 2008-10-14 20:52:55

I had to rebase this against 3.1.3, which involved removing one typo fix that had been fixed by someone else.


---

Comment by robertwb created at 2008-10-14 21:07:21

Nevermind, I get that same error...


---

Comment by robertwb created at 2008-10-14 21:11:47

This patch depends on #4288


---

Comment by mabshoff created at 2008-10-18 15:20:36

Replying to [comment:3 robertwb]:
> This patch depends on #4288

I assume #4289.

Cheers,

Michael


---

Comment by zimmerma created at 2008-10-18 15:36:36

Replying to [comment:4 mabshoff]:
> I assume #4289.

I guess Robert wanted to say that the _magma_init_ error
is now a separate ticket, namely #4288.


---

Comment by robertwb created at 2008-10-18 16:35:25

Yes, my intention was that the _magma_init_ error is a separate ticket, and needs to be fixed before this can go in (with all doctests passing). William recently changed how _magma_init_ works in some cases, so I'm going to cc him.


---

Comment by mabshoff created at 2008-10-18 19:15:34

Replying to [comment:5 zimmerma]:
> I guess Robert wanted to say that the _magma_init_ error
> is now a separate ticket, namely #4288.

Yep, I found that out, too. Let's hope was or someone else fixes this one soon.

Cheers,

Michael


---

Comment by cremona created at 2008-10-19 20:25:23

Replying to [comment:7 mabshoff]:
> Replying to [comment:5 zimmerma]:
> > I guess Robert wanted to say that the _magma_init_ error
> > is now a separate ticket, namely #4288.
> 
> Yep, I found that out, too. Let's hope was or someone else fixes this one soon.

It was someone else ;)

Someone who looked at this one earlier might like to to try it out along with my patch to #4288 since I think the two together work fine (this one needs to be applied before that one).

> 
> Cheers,
> 
> Michael


---

Comment by mabshoff created at 2008-10-20 14:02:55

Resolution: fixed


---

Comment by mabshoff created at 2008-10-20 14:02:55

Merged in Sage 3.2.alpha0
