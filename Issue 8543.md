# Issue 8543: EmptySet is Back !

Issue created by migration from https://trac.sagemath.org/ticket/8543

Original creator: hivert

Original creation time: 2010-03-15 17:27:20

Assignee: hivert

CC:  nborie sage-combinat

Keywords: empty set, Testsuite

There is currently no way to have an empty set which pass the category tests. Indeed the current specification says: for any set `S` there must be a method `S.an_element()` which returns an actual element `x` such that `x in S`:

```
an_element = self.an_element()
tester.assert_(an_element in self, "self.an_element() is not in self")
```

This tests should allows `S` to be empty.


---

Attachment


---

Comment by hivert created at 2010-03-23 09:52:46

Changing keywords from "empty set, Testsuite" to "empty set, Testsuite, EmptySetError".


---

Comment by hivert created at 2010-03-23 09:52:46

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-23 11:48:41

Patches from #8519 your patch apply fine on 4.3.4
All tests passed for each touched files, doc is OK too. This another empty problem is fixed...

Thanks for fixing this!

I give this patch a positive review...


---

Comment by nborie created at 2010-03-23 11:48:41

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-04-16 21:10:21

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2010-04-16 21:10:21

Nicolas: thanks for your review!

Florent: I made a quick reviewer patch fixing some trivial things. Please double check, and set back the positive review!


---

Attachment


---

Comment by nthiery created at 2010-04-16 21:15:05

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-04-17 00:10:09

The new changes are good to me => positive review.


---

Comment by hivert created at 2010-04-17 00:10:09

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-17 02:50:58

Merged in 4.4.alpha0:
 - trac_8543-empty_set_categories-fh.patch
 - trac_8543-empty_set_categories-review-nt.patch


---

Comment by jhpalmieri created at 2010-04-17 02:50:58

Resolution: fixed
