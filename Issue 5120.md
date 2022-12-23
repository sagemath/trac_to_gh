# Issue 5120: abstract class for unique representation

Issue created by migration from https://trac.sagemath.org/ticket/5120

Original creator: nthiery

Original creation time: 2009-01-28 19:47:27

Assignee: cwitty

CC:  sage-combinat

Implement a sage.structure.UniqueRepresentation class. 
Subclasses inherit from it a unique representation behavior for its elements.

Patch under construction, starting from sage.categories.category.uniq.


---

Comment by mhansen created at 2009-01-28 22:17:57

Resolution: duplicate


---

Comment by mhansen created at 2009-01-28 22:17:57

Duplicate of #5119


---

Comment by mabshoff created at 2009-01-28 23:06:29

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-01-28 23:06:29

Well, Nicolas closed #5119 as a dupe, so I am reopening this one since I assume one ticket ought to stay open :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 23:06:29

Resolution changed from duplicate to 


---

Comment by nthiery created at 2009-03-04 04:44:59

Changing assignee from cwitty to nthiery.


---

Comment by nthiery created at 2009-03-04 04:44:59

Changing priority from minor to major.


---

Comment by nthiery created at 2009-03-04 04:44:59

Changing status from reopened to new.


---

Comment by cremona created at 2009-03-14 20:48:20

I'm sure there are good reasons why this is needed, but I think it would be helpful to potential reviewers of you could give a real-life example where this class will be used!


---

Comment by was created at 2009-04-12 06:43:49

1) The first line of one of the files is:

```
ï»¿r""" 
```

I.e., lots of weird corrupted characters.

2) There are no doctests for any of the actual functions you defined.  Code can't go into sage without 100% doctest coverage of each new function.


---

Comment by nthiery created at 2009-04-13 19:48:51

Uploaded an updated patch which fixes 1) and 2)

Ok to abide to a rule, even in a corner case like this where the extra doc really does not add any strength to the test suite, while actually making the code less readable. But it's frustrating to get complained at about documentation for a patch which has a doc/code ratio of 15/1. Next time a please will work better than a gun. 

       Grumpy O' Pa :-)


---

Comment by bump created at 2009-04-24 20:56:26

The patch doesn't apply cleanly to sage-3.4.1 since the hunk in
sage/structure/all.py needs to be corrected by hand.


---

Comment by nthiery created at 2009-04-24 21:28:35

Replying to [comment:8 bump]:
> The patch doesn't apply cleanly to sage-3.4.1 since the hunk in
> sage/structure/all.py needs to be corrected by hand.
Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two
little other improvements.


---

Comment by nthiery created at 2009-04-24 23:20:34

Replying to [comment:9 nthiery]:
> Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two
> little other improvements.

I just updated the patch, rebased for 3.4.1, with description header, default implementation of copy/deepcopy, and pickling by reduce rather than getnewargs.

This later change is debatable. For some reason the reduce way was preferable for some application to categories, but I badly enough did not take notes about why


---

Comment by nthiery created at 2009-04-25 07:48:02

Replying to [comment:10 nthiery]:
> Replying to [comment:9 nthiery]:
> > Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two
> > little other improvements.
> 
> I just updated the patch, rebased for 3.4.1, with description header, default implementation of copy/deepcopy, and pickling by reduce rather than getnewargs.
> 
> This later change is debatable. For some reason the reduce way was preferable for some application to categories, but I badly enough did not take notes about why

Ah, I know why: keyword arguments. See updated, 100% doctested and proofread patch.


---

Comment by nthiery created at 2009-04-25 15:45:13

> Ah, I know why: keyword arguments. See updated, 100% doctested and proofread patch.

Oops trivial update to apply cleanly on 3.4.1. Thanks Dan for the notice.

Michael: could we change the milestone to 3.4.2?


---

Comment by mabshoff created at 2009-04-30 22:10:08

Replying to [comment:12 nthiery]:

I deleted the old patch.

> Michael: could we change the milestone to 3.4.2?

The assignment of milestones is generally insignificant (an exception is like right now when 3.4.2.rc0 was the last merge release and we are in blocker fixes only mode), but as long as this ticket would have gotten a positive review it would have had a chance to go into 3.4.2 regardless which milestone it would have been assigned to.

This patch is also a new design pattern which warrants to be mentioned on sage-devel. It seems to be very well documented and AFAIK it should be properly covered :)

Cheers,

Michael


---

Comment by bump created at 2009-05-02 20:32:04

Applies cleanly to sage-3.4.2.rc0 and passes all tests.


---

Comment by mabshoff created at 2009-05-08 00:43:22

Note that #5879 exposes a problem with this patch. To quote Anne:

```
I just talked to Nicolas about the pickling problem; this is a shortcoming 
of the current unique representation patch and he will try to find a solution 
to the problem in patch 5120.
```


I will mark this "needs work" until this issue is resolved. 

Cheers,

Michael


---

Comment by nthiery created at 2009-05-08 21:39:53

Changing keywords from "" to "unique representation".


---

Comment by nthiery created at 2009-05-08 21:41:45

I changed a bit the underlying implementation which fixes the code and should be more robust.
I also added 2 pages of doc, and extracted a trivial yet general purpose CallclassMetaclass (Florent will be interested).
Updated patch upload in a couple minutes.


---

Comment by nthiery created at 2009-05-19 06:15:44

Updated patch includes ReST fixes suggested by David Roe, as well as an example on how to handle properly default arguments.


---

Comment by nthiery created at 2009-05-19 06:23:24

Changing status from new to assigned.


---

Attachment


---

Comment by roed created at 2009-05-19 07:57:35

I'd like to see some more thought go into what use cases are best served by UniqueRepresentation and what by UniqueFactory.  But the code is well documented, does what it claims to do, and UniqueRepresentation is easier to use than UniqueFactory.  So positive review.


---

Comment by mabshoff created at 2009-05-21 00:59:10

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 00:59:10

Resolution: fixed
