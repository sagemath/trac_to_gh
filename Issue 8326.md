# Issue 8326: Sphinx warnings about posets and poset_example

Issue created by migration from https://trac.sagemath.org/ticket/8326

Original creator: mpatel

Original creation time: 2010-02-22 06:06:02

Assignee: sage-combinat

Sphinx warnings from building the HTML reference manual include: 

```
combinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object
combinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object
```



---

Comment by mpatel created at 2010-02-22 06:07:34

Work around Sphinx poset warnings.  sage repo.


---

Comment by mpatel created at 2010-02-22 06:12:19

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-22 06:12:19

Changing priority from minor to trivial.


---

Attachment

The patch appears to work, but feel free to reject it.


---

Comment by jhpalmieri created at 2010-02-24 23:25:37

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-02-24 23:25:37

Looks okay to me: the patch is pretty innocuous, and it fixes the docbuild problem.


---

Comment by mvngu created at 2010-03-02 21:47:12

Resolution: fixed
