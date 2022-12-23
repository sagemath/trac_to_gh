# Issue 5512: CombinatorialSpeciesStructures with different labels are equal

Issue created by migration from https://trac.sagemath.org/ticket/5512

Original creator: saliola

Original creation time: 2009-03-13 17:31:47

Assignee: mhansen

CC:  sage-combinat

Keywords: species


```
sage: T = species.BinaryTreeSpecies()
sage: t = T.structures([1,2,3])[0]; t
1*(2*3)
sage: t[0], t[1][0]
1, 2
sage: t[0] == t[1][0]
True
```



---

Comment by mhansen created at 2011-01-24 23:12:33

Changing status from new to needs_review.


---

Comment by elnorreip created at 2011-02-08 11:12:37

Changing status from needs_review to positive_review.


---

Comment by elnorreip created at 2011-02-08 13:17:02

Added reviewers.


---

Comment by jdemeyer created at 2011-03-11 22:24:28

Moving to sage-feature as long as #10227 does not have a positive_review.


---

Comment by hivert created at 2011-06-10 18:16:43

Hi Jeroen,

Thanks for pointing that #10227 is still awaiting for review. 

One question concerning sage-wait: if someone (eg: me this week end if I find the time) review #10227, am I supposed to change the milestone of this one ? 

Florent


---

Comment by jdemeyer created at 2011-06-14 17:26:29

Replying to [comment:9 hivert]:
> Hi Jeroen,
> 
> Thanks for pointing that #10227 is still awaiting for review. 
> 
> One question concerning sage-wait: if someone (eg: me this week end if I find the time) review #10227, am I supposed to change the milestone of this one ? 

I would say: yes, you can do that, at least if you are sufficient familiar with _this_ ticket to be sure that there is no further obstruction.


---

Comment by mhansen created at 2012-07-31 22:01:00

Checking the patch, there is no hard dependency on #10227.


---

Comment by mhansen created at 2012-07-31 22:06:55

Apply trac_5512-species_equality.patch


---

Attachment


---

Comment by jdemeyer created at 2012-08-03 10:28:48

Rebased to sage-5.3.beta0.


---

Comment by jdemeyer created at 2012-08-12 18:58:28

Resolution: fixed
