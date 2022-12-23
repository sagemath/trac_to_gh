# Issue 8017: incorrect trailing digits for continued fraction

Issue created by migration from https://trac.sagemath.org/ticket/8017

Original creator: robertwb

Original creation time: 2010-01-21 00:12:58

Assignee: AlexGhitza

CC:  was


```
continued_fraction(sqrt(2))
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]
```


Followup to and depends on #5107, which documents the function better. 


---

Attachment


---

Comment by robertwb created at 2010-01-21 01:25:52

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-21 01:25:52

This does change the definition from "continued fraction expansion of a real approximation" to "truncation of continued fraction expansion." It also adds an nterms option to compute a specified number of terms.


---

Comment by zimmerma created at 2010-03-14 20:24:58

Robert, this seems to be great work! However a small question: for *exact* symbolic input,
the truncated continued fraction should not depend on the initial floating-point
approximation, and should be a truncation of the (finite or infinite) continued fraction:

```
sage: continued_fraction(22/7,bits=4)
[3, 4]
sage: continued_fraction(22/7,bits=5)
[3, 8]
```

I guess the above should give instead:

```
sage: continued_fraction(RealIntervalField(4)(22/7))
[3]
sage: continued_fraction(RealIntervalField(5)(22/7))
[3]
```

Can the same problem happen with say sqrt(2), or is it only for rationals?


---

Comment by zimmerma created at 2010-03-14 20:24:58

Changing status from needs_review to needs_info.


---

Attachment


---

Comment by robertwb created at 2010-03-15 20:07:47

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2010-03-15 20:07:47

Thank you for looking at this. As you can probably tell, the current behavior really bothers me ;). I've fixed the case above (yes, it only impacted rationals).


---

Comment by zimmerma created at 2010-03-16 07:57:25

while I'm running the doctests, a few comments: (1) maybe the documentation should say that the
terms of the truncated continued fraction are (now) guaranteed exact (using interval arithmetic);
(2) `If nterms is given, the precision is increased until the specified number of terms can be computed`: if possible, for example 22/7 will give only two terms.

I also suggest giving an additional example showing that we can give as input a floating-point
interval, and the difference with a floating-point number (where initial rounding error can
give an incorrect result):

```
sage: continued_fraction(RealField(39)(e))
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 2]
sage: continued_fraction(RealIntervalField(39)(e))
[2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10]
```


In the meantime the doctests finished, and I get two failures:

```
sage -t  core2/devel/sage-8017/sage/combinat/words/word_generators.py # 1 doctests failed
sage -t  core2/devel/sage-8017/sage/tests/book_stein_ent.py # 13 doctests failed
```



---

Comment by zimmerma created at 2010-03-16 07:57:25

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2010-07-29 05:21:11

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-07-29 09:24:24

positive review, good work, Robert! However I see as a side effect you had to change the doctests
in William's book, which has the consequence that those examples will not work any more as in the
book (but better now). This is a concern for me with the book we wrote about Sage (btw, the
doctest of the number theory chapter is ready for review, see #9395).

Paul


---

Comment by zimmerma created at 2010-07-29 09:24:24

Changing status from needs_review to positive_review.


---

Attachment

Thanks for being so quick to look at this after such a long wait. Yes, I was thinking about this when I made these changes. The answers are not substantially different, and should be clear to any user that the current behavior is correct (e.g. by computing things out to higher precision or consulting external sources). 

Most importantly, the commands used are not broken or semantically different, which would be really bad. I refreshed the patch just inserting a little note about the change (and, of course, it will be fully recorded in the revision control system).


---

Comment by mpatel created at 2010-08-01 23:29:07

Should the release manager merge all three patches?  By the way, the first patch is missing a Mercurial header and the second a descriptive commit string.


---

Comment by mpatel created at 2010-08-01 23:29:07

Changing status from positive_review to needs_info.


---

Attachment

apply only this patch


---

Comment by robertwb created at 2010-08-04 07:44:15

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2010-08-04 07:44:15

I have folded all three patches into 8017-all.patch, apply that one.


---

Comment by robertwb created at 2010-08-04 07:44:22

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:47:51

Resolution: fixed
