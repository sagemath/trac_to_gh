# Issue 9452: strip_automount_prefix() is useless

Issue created by migration from https://trac.sagemath.org/ticket/9452

Original creator: rlm

Original creation time: 2010-07-08 08:00:49

Assignee: tbd

CC:  was

> We wrote the strip_automount_prefix() function for
> sage-test to get around problems with automounted
> file system having wierd mount points.
> Unfotunately the strip_automount_prefix() does not
> work at all!
>
> Here is a patch:
>
> % diff sage-test.old sage-test.new
> 20c20
> <     return strip_automount_prefix(os.path.abspath(x))
> ---
>>     return os.path.abspath(x)
> 57c57
> <         f = g[len(SAGE_ROOT)+1:]
> ---
>>         f = g[g.find(SAGE_ROOT)+len(SAGE_ROOT)+1:]
> %
>
> You can remove - or deprecate - the function strip_automount_prefix().


---

Attachment


---

Comment by jason created at 2011-02-23 23:28:23

Changing status from new to needs_review.


---

Comment by was created at 2011-02-24 00:10:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-02-24 10:00:46

What exactly is the problem that this patch is supposed to fix?  The description is very unclear...


---

Comment by was created at 2011-02-24 17:11:48

This patch is undoing a mysterious "fix" from a long time ago, which was required on some obscure filesystem somewhere.


---

Comment by jdemeyer created at 2011-03-08 21:45:14

Resolution: fixed
