# Issue 9795: Add a "diagonal" method for matrices

Issue created by migration from https://trac.sagemath.org/ticket/9796

Original creator: jason

Original creation time: 2010-08-24 15:54:40

Assignee: jason, was

CC:  kcrisman

See http://ask.sagemath.org/question/54/how-to-get-the-diagonal-of-a-matrix


---

Attachment


---

Comment by rbeezer created at 2011-01-29 03:50:24

Changing status from new to needs_review.


---

Comment by rbeezer created at 2011-01-29 03:50:24

Changing keywords from "" to "beginner".


---

Comment by tomc created at 2011-02-04 22:13:46

Changing status from needs_review to positive_review.


---

Comment by tomc created at 2011-02-04 22:13:46

This looks good.  Running:

```
sage -testall -long
```

gives that all doctests pass except five unrelated tests (in sage/plot/plot3d/tachyon.py and sage/plot/plot3d/base.pyx) that also fail in an unpatched copy of Sage (version 4.6.1, built from source on 64-bit Linux).


---

Comment by rbeezer created at 2011-02-05 23:10:24

Replying to [comment:3 tomc]:

Thanks for the review, Tom - the help is appreciated.

Rob


---

Comment by kcrisman created at 2011-02-06 01:56:36

I hope it's okay that I 'guessed' the reviewer's name from the trac main page!


---

Comment by jdemeyer created at 2011-02-07 08:46:39

Replying to [comment:5 kcrisman]:
> I hope it's okay that I 'guessed' the reviewer's name from the trac main page!

I suppose so, I do that all the time.


---

Comment by jdemeyer created at 2011-02-16 08:49:58

Resolution: fixed
