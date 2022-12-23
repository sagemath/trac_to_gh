# Issue 5367: bug in composition of power series

Issue created by migration from https://trac.sagemath.org/ticket/5367

Original creator: AlexGhitza

Original creation time: 2009-02-25 01:26:30

Assignee: tbd

Keywords: power series composition

The following returns an incorrect answer:


```
sage: S.<z> = QQ[[]]
sage: p = 1 + O(z)
sage: q = 1 + z
sage: p(q)          # should return O(z^0)
1
```


This was reported via "report a problem" from the notebook.



---

Comment by AlexGhitza created at 2009-02-25 22:45:52

As pointed out by Ralf Hemmecke on sage-devel, the correct behaviour is not to return 1, but rather to raise an error if q has a constant term.


---

Comment by davidloeffler created at 2009-04-30 11:24:26

I just came across this, which is presumably related:


```
sage: R.<x> = QQ[[]]
sage: f = 1 + 24*x^11 + 24*x^22 + O(x^33)
sage: f(x^2)
1 + 24*x^22 + 24*x^44 + O(x^86)
```


The answer should clearly be 1 + 24*x^22 + 24*x^44 + O(x^66). (This is causing some headaches in trying to sort out degeneracy maps for modular forms.)


---

Comment by robertwb created at 2010-01-14 05:20:10

See also #3979.


---

Comment by cremona created at 2010-05-19 08:18:51

Since this is a duplicate of #3979, I think this ticket should be closed.


---

Comment by fwclarke created at 2011-07-18 12:14:37

Replying to [comment:3 robertwb]:
> See also #3979.

Which now has a patch.


---

Comment by davidloeffler created at 2011-07-18 12:17:28

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2011-07-18 12:17:28

I concur that this should be closed as duplicate. I'll set it to "positive review" to bring this to the attention of the release manager.


---

Comment by davidloeffler created at 2011-07-18 12:17:40

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-07-19 17:37:31

Resolution: duplicate
