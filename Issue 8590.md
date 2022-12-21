# Issue 8590: `A` still using old coercion framework

Issue created by migration from Trac.

Original creator: vferay

Original creation time: 2010-03-23 17:40:36

Assignee: AlexGhitza

There is a failure in the test of the file

sage.categories.hopf_algebras_with_basis

The problem occurs during the test suite of an hopf algebra and returns the error


```
   RuntimeError: `A` still using old coercion framework
```


I am unfortunately not able to solve really this problem, but, if the competent people have no time right now, I can write a small patch predicting the error in the test so that the tests pass


---

Comment by mmezzarobba created at 2014-02-02 11:20:59

Changing status from new to needs_review.


---

Comment by tscrim created at 2014-02-02 15:55:42

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-02 20:43:01

Resolution: fixed
