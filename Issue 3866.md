# Issue 3866: Create a 2d locator interact widget

Issue created by migration from https://trac.sagemath.org/ticket/3866

Original creator: jason

Original creation time: 2008-08-15 03:46:33

Assignee: itolkov

This is a *very* *extremely* rough-cut of a 2d locator widget.  All the docstrings are blatantly wrong and the code is full of ugly things.  But it works, sort of.  It's a starting point for someone to finish.

An example:


```
@interact
def _(pos=locator(3)):
    print pos
```




---

Attachment


---

Comment by mabshoff created at 2008-08-15 05:07:01

Hi Jason,

does this patch need a review?

Cheers,

Michael


---

Comment by jason created at 2008-08-15 07:02:28

No, not yet; definitely not yet.  I'm embarrassed to post the patch as it was; I only posted it because I was more embarrassed by almost losing the patch (I just barely found it).


---

Comment by mhampton created at 2008-12-30 18:23:57

I am thinking of giving this to a student of mine for an independent study project.  To avoid duplication of effort I would appreciate being informed of any independent effort on it.

Thanks,
Marshall Hampton


---

Attachment

rebase against 4.0.1, along with some very minor cleanup


---

Comment by mhampton created at 2009-06-11 23:02:15

It looks like my student didn't get very far, unfortunately.  I will attempt to improve this further, but I am attaching a rebased (and slightly cleaned-up) patch in case other people want to move ahead faster.


---

Comment by jason created at 2010-08-13 04:38:30

There is a bounty for a feature like this:

http://groups.google.com/group/sage-devel/browse_thread/thread/4b52ee22e227370d/a5347db58d549c71?lnk=gst&q=locator#a5347db58d549c71


---

Comment by chapoton created at 2018-04-30 08:50:52

Given that the legacy-notebook is no longer maintained or developed, let us close that old ticket.


---

Comment by chapoton created at 2018-04-30 08:50:52

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2018-05-01 12:31:01

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
