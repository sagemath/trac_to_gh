# Issue 6804: Permutation.weak_excedences inconsistency

Issue created by migration from https://trac.sagemath.org/ticket/6804

Original creator: schilly

Original creation time: 2009-08-22 17:16:29

Assignee: mhansen

CC:  mjo

Either code or docstring is wrong in 4.1.1, "=" vs. ">=":


```
Returns all the numbers self[i] such that self[i] = i+1
```



```
if self[i] >= i + 1:
    res.append(self[i])
```



---

Attachment

Fix the docstring.


---

Comment by mjo created at 2012-01-09 05:25:44

I found a reference; the bug was in the docstring.


---

Comment by mjo created at 2012-01-09 05:25:44

Changing status from new to needs_review.


---

Comment by ncohen created at 2012-01-29 15:58:43

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2012-01-29 15:58:43

Well, then...`:-)`

Nathann


---

Comment by jdemeyer created at 2012-02-02 12:51:52

Resolution: fixed
