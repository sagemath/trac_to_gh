# Issue 6250: [with patch, needs review] Standardize MatrixGroup_gap: by adding .cardinality, and deprecating __len__

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-06-08 23:23:10

Assignee: nthiery

CC:  sage-combinat wdjoyner@gmail.com

Keywords: cardinality, __len__, order, groups

Followup on #5308:
 - cardinality now returns the size of the group (was order)
 - order is a backward compatibility alias for cardinality
 - __len__ raises a deprecation error


---

Attachment


---

Comment by nthiery created at 2009-06-08 23:28:01

matrix_group_gap-cardinality_len-6250-nt.2.patch superceedes the previous one (should have replaced it)

#4326 depends on it


---

Comment by wdj created at 2009-06-08 23:38:41

I have not applied or tested this patch but upon reading the code a few lines struck me as odd. Can you please explain how, if F is a finite field, F.order() -> F.cardinality() is correct? Has the order method for finite fields been rewritten? Did I miss the discussion on sage-delev that order should be deprecated and replaced by cardinality?


---

Comment by nthiery created at 2009-06-08 23:43:31

As far as I remember, what was discussed on the list was about the order of an *element* of a field/group/...

Here this is about the order of the group itself, which is its cardinality.


---

Comment by wdj created at 2009-06-10 11:18:35

I don't agree with the suggestion in one of the docstrings that order might be deprecated. But that is just my (American) opinion, which might not be shared by the rest of the world:-) In any case, the patches do not apply cleanly to 4.0.rc0.


---

Comment by nthiery created at 2009-06-10 16:05:39

Changing status from new to assigned.


---

Comment by nthiery created at 2009-06-10 16:05:39

Replying to [comment:4 wdj]:
> I don't agree with the suggestion in one of the docstrings that order might be deprecated.
> But that is just my (American) opinion, which might not be shared by the rest of the world:-)

I am fine with both options. From discussions on sage-devel, it seems that in general aliases are somewhat frowned upon.
We definitely want .cardinality(). But yes, even in Europe, some users would certainly be trying G.order() to get the size
of the group. That's why I raised the issue.

I am happy to remove the comment if you think its better.


> In any case, the patches do not apply cleanly to 4.0.rc0. 

? I just retried, and it applies smoothly on sage 4.0.1. Did you only apply the second patch? (the first one should be deleted)


---

Comment by wdj created at 2009-06-11 10:08:31

The second patch applied cleanly to 4.0.rc0 but failed sage -testall. I think it was unrelated but I'll retry on another version of Sage.


---

Comment by wdj created at 2009-06-11 13:11:25

The second patch applied cleanly to 4.0.1.a0 but failed sage -testall. However, that failure (in "devel/sage/sage/misc/html.py") is a known unrelated failure. The patch reads fine and does as it claims.


---

Comment by ncalexan created at 2009-06-13 21:38:17

Resolution: fixed
