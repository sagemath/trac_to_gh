# Issue 8785: avoid subtle interaction between importing multiprocessing and twisted

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-27 20:54:37

Assignee: jason

It turns out that on some platforms, importing multiprocessing, then twisted, leads to an "int object is not callable" TypeError.  This breaks devel/sage/sage/all.py's quit_sage function, causing a big traceback at exit.   This could also cause great confusion for people writing a program that uses `@`parallel('multiprocessing') followed by anything involving twisted. 

A simple fix is to import the relevant part of twisted before using multiprocessing in `@`parallel.   The attached patch does this.


---

Attachment


---

Comment by was created at 2010-04-27 20:58:45

Changing status from new to needs_review.


---

Comment by mariah created at 2010-04-27 22:23:45

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2010-04-27 22:27:20

I tried it and it works!


---

Comment by was created at 2010-04-28 17:36:19

Resolution: fixed


---

Comment by vdelecroix created at 2016-01-10 23:21:51

Would be more informative to write explicitely on which hardware/OS it failed. "corporate settings" is more than vague. Was there any upstream report? This problem might have been solved since then!
