# Issue 9929: Additional test in is_even_hole_free

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-09-17 08:08:52

Assignee: jason, ncohen, rlm

This bug has been reported in #9925, and fixed by #9420. We just want to make sure it does not appear again ! `:-)`

Nathann


---

Comment by ncohen created at 2010-09-17 08:16:09

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2010-09-17 08:48:56

I tried the loop included in this patch with 100 000 instead of 100, and it still works.... Sounds like we are safe on this side `:-)`

Nathann


---

Comment by dimpase created at 2010-09-19 08:00:07

Replying to [comment:3 ncohen]:
> I tried the loop included in this patch with 100 000 instead of 100, and it still works.... Sounds like we are safe on this side `:-)`
> 
> Nathann

unless there is a probabilistic argument that with high probability we run into the cases we are interested in testing here,
this won't fly... Random tests don't prove much otherwise. And here you don't even know what to look for, right?


---

Comment by dimpase created at 2010-09-19 08:00:07

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2010-09-19 08:30:51

> unless there is a probabilistic argument that with high probability we run into the cases we are interested in testing here,
> this won't fly... Random tests don't prove much otherwise. And here you don't even know what to look for, right?

Well, there is a practical argument saying that the mistake appeared with a probability of 1%, as my comments on #9925 indicated (and which I tried on even longer sequences of tests). Besides, the graph I create from its sparse6_string is known to create a mistake on the current version of Sage. What do you think we could do besides that ?

Nathann


---

Comment by dimpase created at 2010-09-19 08:54:23


```
the graph I create from its sparse6_string is known to create a mistake on the current version of Sage. 
```

OK, this is fair enough. I'll give it a positive review as soon as it is marked as "needs review"


---

Comment by ncohen created at 2010-09-19 09:00:52

> OK, this is fair enough. I'll give it a positive review as soon as it is marked as "needs review" 

Then let it be ! `:-)`

Nathann


---

Comment by ncohen created at 2010-09-19 09:00:52

Changing status from needs_info to needs_review.


---

Comment by dimpase created at 2010-09-19 09:02:22

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-09-19 09:04:10

Thanksssssss !! And many other thanks for the review of subgraph_search `:-)`

Nathann


---

Comment by mpatel created at 2010-09-29 08:39:33

Resolution: fixed
