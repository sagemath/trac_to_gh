# Issue 6411: sdist makes sage unable to run without building

Issue created by migration from https://trac.sagemath.org/ticket/6411

Original creator: rlm

Original creation time: 2009-06-25 17:28:23

Assignee: craigcitro

CC:  was

William was complaining about being unable to reproduce this, so here's an easy way to reproduce it:

Take sage-4.1.alpha1, do an sdist, and try running sage. Boom.


---

Comment by mhansen created at 2009-06-25 20:19:52

I think if you run a "sage -br" afterward, it will work.  There are just a few things that get compiled when doing that.  Looking at those, it should be easy to trac down what changed.


---

Comment by mhansen created at 2010-01-17 01:52:29

This is because in spkg-dist, we do the following:


```
rm -rf c_lib/*.so c_lib/*.os c_lib/*/*.os c_lib/*/*/*.os
```


This causes libcsage to be built again.  What we should do instead is delete the files from the tmp directory that we copy things into.


---

Attachment


---

Comment by mhansen created at 2010-01-17 02:20:48

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-17 18:04:39

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2010-01-17 18:04:39

This looks good, and fixes the problem for me.


---

Comment by rlm created at 2010-01-18 22:20:09

Resolution: fixed
