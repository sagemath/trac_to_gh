# Issue 4754: Merge minimum rank code

Issue created by migration from https://trac.sagemath.org/ticket/4754

Original creator: jason

Original creation time: 2008-12-11 04:15:52

Assignee: rlm

CC:  mvngu

Based on the discussion at http://groups.google.com/group/sage-support/browse_thread/thread/3ec4cc026e9c65bd, it would be great to merge the code found at http://arxiv.org/abs/0812.1616 into the Sage library.  Several functions should probably go into the main graph library (e.g., the edge clique cover function), while others probably ought to go into a minimum_rank.sage file.

I am one of the developers and hereby give my permission to incorporate the code into Sage.  I will ask the other developers as well.


---

Comment by jason created at 2008-12-11 04:15:59

Changing status from new to assigned.


---

Comment by jason created at 2008-12-11 04:15:59

Changing assignee from rlm to jason.


---

Comment by jason created at 2008-12-11 04:19:12

I also have a *much* faster Cython zero-forcing-set tester that I could donate to Sage.


---

Comment by was created at 2008-12-11 04:55:29

> while others probably ought to go into a minimum_rank.sage file. 

I don't think anything included in the core main sage library should go in a .sage file.  It should go in a .py file.

William


---

Comment by jason created at 2008-12-22 18:41:44

From personal email from Geoff Tims, 13 Dec 2008:


```
Hey Jason,
 
I don't know exactly how I feel.  I'm probably fine with it.
 
I agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later
 
Geoff
```



---

Comment by jason created at 2008-12-22 18:42:19

From personal email from Tracy McKay, 11 Dec 2008:


```
Hi Jason,

I agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later. 

Thanks,

Tracy McKay
```



---

Comment by jason created at 2008-12-22 18:43:44

From personal email from Laura DeLoss, 11 Dec 2008:


```
I agree to license the code available from http://arxiv.org/abs/0812.1616 as GPL version 2 or later and for the EGR group (Jason, Jason, Geoff, Tracy and myself) to be listed as the Sage contributors. 
```



---

Comment by mvngu created at 2009-06-27 00:49:27

CC'ing myself


---

Comment by jason created at 2010-01-05 04:16:53

Jason Smith also verbally gave me permission to license the code GPLv2 or later.


---

Attachment

apply on top of previous patch


---

Attachment

apply on top of previous patches


---

Attachment

Added rough versions of patches.


---

Comment by jason created at 2010-02-02 10:21:56

Changing status from new to needs_work.


---

Comment by dcoudert created at 2021-10-02 14:31:34

Is it best to merge the code or to make https://github.com/jasongrout/minimum_rank an optional package ?
