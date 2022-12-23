# Issue 9392: Broken docstring in binpacking method

Issue created by migration from https://trac.sagemath.org/ticket/9392

Original creator: ncohen

Original creation time: 2010-06-30 05:46:10

Assignee: jason, jkantor

CC:  rlm leif

Not really broken, but subject to change of behaviours depending on the solver used.... ;-)

Nathann


---

Comment by ncohen created at 2010-06-30 05:47:05

Changing status from new to needs_review.


---

Attachment

Here it is !

Nathann


---

Comment by leif created at 2010-07-04 20:15:17

Nathann's patch fails on normal (non-optional) doctesting because of undefined variables/some sections _not_ marked "optional".


---

Comment by leif created at 2010-07-04 20:15:17

Changing status from needs_review to needs_work.


---

Attachment

Fixes non-optional doctesting. Apply on top of Nathann's patch.


---

Comment by leif created at 2010-07-04 20:25:14

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-07-04 20:25:14

With my reviewer patch applied, at least passes reasonable tests (`-long`, `-long` with `-only-optional=cbc,glpk` in `sage/numerical`) on a 32-bit system where the doctest previously did _not_ fail...

Leaving as "needs review" for further testing.


---

Comment by rlm created at 2010-07-05 21:27:51

Doesn't this depend on #9312?


---

Comment by ncohen created at 2010-07-05 21:33:14

Not really... Though if we say it depends on #9312, then we do not need to add these "optional" flags anymore :-D

Nathann


---

Comment by rlm created at 2010-07-05 22:32:46

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-05 22:33:49

Resolution: fixed


---

Comment by leif created at 2010-07-05 23:11:54

Well, if GLPK gets a standard package, we should *definitely* remove the `optional` tags, since otherwise these tests are omitted in the usual test process.

(We could just substitute `optional` by `standard` to make life easier in case the package is made optional again for some reason. Same for Nathann's patch at #9312.)


---

Comment by leif created at 2010-07-06 04:03:16

Replying to [comment:9 leif]:
> Well, if GLPK gets a standard package, we should *definitely* remove the `optional` tags, since otherwise these tests are omitted in the usual test process.

This is addressed at #9432.
