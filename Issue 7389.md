# Issue 7389: Fallback _point_morphism_class() has wrong signature

Issue created by migration from https://trac.sagemath.org/ticket/7389

Original creator: wjp

Original creation time: 2009-11-04 19:45:30

Assignee: AlexGhitza

The default `Scheme._point_morphism_class()` has a different signature than the versions in the subclasses of Scheme, causing a `TypeError` when it is called instead of the intended `NotImplementedError`.

Small nonsensical example to trigger it in sage 4.2:


```
sage: S = Spec(ZZ)
sage: f = S.identity_morphism()
sage: from sage.schemes.generic.glue import GluedScheme
sage: T = GluedScheme(f,f)
sage: S.hom([1],T)
TypeError: _point_morphism_class() takes exactly 1 non-keyword argument (3 given)
```


The attached patch should fix it.


---

Attachment


---

Comment by wjp created at 2009-11-04 19:48:05

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2009-11-15 10:07:53

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2009-11-15 10:07:53

Please add a doctest that illustrates the problem being fixed (so that if someone messes this up again we can catch it automatically).  Even what you call the "small nonsensical example" would do; of course if you can come up with a small sensical one, that would be even better :).


---

Comment by AlexGhitza created at 2010-01-01 23:25:36

apply after the previous patch


---

Comment by AlexGhitza created at 2010-01-01 23:36:42

Changing status from needs_work to needs_review.


---

Attachment

OK, I've put up a patch with the doctest given in the description of this ticket.

I'm happy with Willem's patch, now if someone can look at mine we're set.


---

Comment by AlexGhitza created at 2010-01-20 09:48:13

Willem, could you review my patch here?


---

Comment by wjp created at 2010-01-20 22:13:40

Sorry, I completely missed the trac email from your previous comment. Thanks for the review; your doctest patch looks good.


---

Comment by wjp created at 2010-01-20 22:13:40

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 18:02:09

Resolution: fixed
