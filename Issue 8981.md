# Issue 8981: Adding support for param attribute of GSL ode solver

Issue created by migration from https://trac.sagemath.org/ticket/8981

Original creator: Moredread

Original creation time: 2010-05-17 02:02:16

Assignee: tba

Currently it isn't possible to pass parameters to a compiled function used for the GSL ode solver. There are some comments in place to indicate what needs to be changed. I implemented those pieces.


---

Attachment


---

Comment by Moredread created at 2010-05-17 12:53:09

Changing status from new to needs_review.


---

Comment by wdj created at 2010-06-29 19:39:09

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2010-06-29 19:39:09

I don't see any examples in the patch. If you make a change in the code (even one I don't understand) you need to add examples to the docstring testing the new functionality.


---

Comment by Moredread created at 2010-06-29 22:13:05

There is an example of the usage. I changed the existing one so that I matches the new API, including an example how to use it. (See changes between left hand side line number 295 and 315) Is this not enough?


---

Comment by Moredread created at 2010-11-20 21:22:09

Changing status from needs_work to needs_review.


---

Comment by Moredread created at 2010-11-20 22:44:06

Changing status from needs_review to needs_work.


---

Comment by Moredread created at 2010-11-20 22:44:41

I'll check if the patch still works and maybe improve the documentation first.
