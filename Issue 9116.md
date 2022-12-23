# Issue 9116: sage-4.4.3.alpha1 fails to build on OS X due to png library issue

Issue created by migration from https://trac.sagemath.org/ticket/9116

Original creator: was

Original creation time: 2010-06-02 23:25:49

Assignee: GeorgSWeber




---

Attachment


---

Comment by was created at 2010-06-02 23:28:34

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-03 05:28:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-03 05:28:03

Looks good to me.


---

Comment by was created at 2010-06-03 15:34:13

Resolution: fixed


---

Comment by leif created at 2010-06-03 16:20:45

So Cygwin currently needs _two different_ versions of `libpng`?

Shouldn't that be fixed "upstream", i.e. in Cygwin or `pbori`?
