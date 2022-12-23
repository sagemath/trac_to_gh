# Issue 9831: Invalid HTML in data/sage/html/login.html

Issue created by migration from https://trac.sagemath.org/ticket/9832

Original creator: timdumol

Original creation time: 2010-08-28 13:42:47

Assignee: jason, was

CC:  jason

The W3C validator gives errors about missing targets for the <label> elements.


---

Comment by timdumol created at 2010-08-28 13:43:47

Fixes the error.


---

Attachment


---

Comment by timdumol created at 2010-08-28 14:15:48

Changing status from new to needs_review.


---

Comment by jason created at 2010-10-08 20:49:39

Changing assignee from jason, was to jason.


---

Comment by jason created at 2010-10-08 20:50:33

This looks right, though I haven't applied it yet.


---

Comment by jdemeyer created at 2010-10-12 12:26:40

Looks fine.  Testing with W3C validator still gives an error though:


```
Line 29, Column 79: The align attribute on the img element is obsolete. Use CSS instead.
```


But I suppose this is for backwards compatibility?


---

Comment by jdemeyer created at 2010-10-12 12:26:40

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-11 19:37:23

Resolution: fixed
