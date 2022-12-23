# Issue 9339: Notebook fails to print result of last expression if there is a line break

Issue created by migration from https://trac.sagemath.org/ticket/9339

Original creator: nbruin

Original creation time: 2010-06-25 20:04:50

Assignee: jason, was

Consider the following two notebook cells. Semantically, the input is the same in both examples. The only difference is that the second one has a line break inside a bracket.

First one prints the result of the last expression (line) in the cell:

```
(x+1)
///
x + 1
```


But the second one doesn't:

```
(x+
1)
///
```




---

Comment by acleone created at 2010-06-25 20:50:14

Should be fixed by #7997


---

Comment by kcrisman created at 2014-12-19 04:53:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-12-19 04:53:58

This is really the same as http://trac.sagemath.org/ticket/8503 and https://github.com/sagemath/sagenb/issues/301 - note that some examples _do_ work.


---

Comment by kcrisman created at 2014-12-19 04:54:12

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-13 01:17:18

Resolution: duplicate
