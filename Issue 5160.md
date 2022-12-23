# Issue 5160: Change name of misc/sagex_ds.pyx

Issue created by migration from https://trac.sagemath.org/ticket/5160

Original creator: kcrisman

Original creation time: 2009-02-02 18:58:33

Assignee: tba

Since #5094 is merged, I'll open this ticket.  It seems to be a worthwhile idea.  

It appears to only be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory to pull this off.  I'm putting this under "documentation" component because it's really just a nomenclature holdover.


---

Comment by mabshoff created at 2009-02-02 19:00:01

The deprecation policy might apply here.

Cheers,

Michael


---

Attachment


---

Comment by jdemeyer created at 2012-09-25 20:46:17

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-09-25 20:46:17

Changing type from task to enhancement.


---

Comment by kcrisman created at 2012-09-25 20:48:26

Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?  Who could we ask?


---

Comment by jdemeyer created at 2012-09-25 20:52:14

Replying to [comment:3 kcrisman]:
> Nice.  I'll try to review it if someone else doesn't get there first.  Do you think we'd need a deprecation period, or is it unlikely anyone would actually use this other than in the files in question?
I think it's unlikely, since it's barely used in Sage itself.  Besides, Sage code shouldn't be affected:

```
sage: BinaryTree()
```

should work just as before.

I don't even know how to deprecate a _module name_ (as opposed to a function).


---

Comment by kcrisman created at 2012-09-26 01:46:47

> I don't even know how to deprecate a _module name_ (as opposed to a function).
Good point, which is why I didn't do it before.

This looks good.  I guess at some point this was supposed to have a lot more than binary trees :)  Running irrelevant tests now, but the relevant ones were fine.  I'm getting some errors, but they seem unrelated - I'll look into it.


---

Comment by kcrisman created at 2012-09-26 02:44:37

Yeah, they seem to be unrelated - weird, but I must have done something wrong.  They occurred with and without the patch.


---

Comment by kcrisman created at 2012-09-26 02:44:37

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-09-28 07:46:46

Resolution: fixed
