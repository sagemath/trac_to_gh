# Issue 164: doctests dependence thing

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-10-29 23:07:46

Assignee: was

It would be nice if, when one line of a doctest fails, then the doctest doesn't run the rest of that "example block". What tends to happen is e.g. one line fails, so then a bunch of variables aren't defined, and then you get tons of garbage in your doctest output, which is hard to sift through. After the first failure, it would be good if it would just stop there, and move onto the next example. (Or at least if there was an option for this behaviour.)


---

Comment by was created at 2006-11-06 06:46:27

Doctest is a completely standard Python module.  I didn't write it.  Maybe you
should look at the documentation and see if it has the feature you want already.
If not, you could propose it to the Python people (e.g., as a PEP).  This 
isn't really a SAGE question.


---

Comment by kcrisman created at 2013-01-29 20:31:41

Does [nose](http://trac.sagemath.org/sage_trac/ticket/9921) have a better way of handling this (not that we could switch to that anytime soon)?  I thought about, but decided against, making this "wontfix" after six years - it WOULD be nice.  Comments?


---

Comment by jdemeyer created at 2013-06-13 12:20:26

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-13 12:20:26

The new doctest option `sage -t --initial` sort of does this: it shows only the first failure in a doctest block. It's an _option_ which needs to be specified explicitly but I think that's sufficient.


---

Comment by jdemeyer created at 2013-06-13 12:20:26

Changing component from user interface to doctest framework.


---

Comment by jdemeyer created at 2013-06-13 12:20:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:21:45

Resolution: worksforme
