# Issue 1069: find a way to savely enable inplace optimizations

Issue created by migration from https://trac.sagemath.org/ticket/1069

Original creator: mabshoff

Original creation time: 2007-11-02 19:10:13

Assignee: rbradshaw

See #1068 and also 

http://groups.google.com/group/sage-devel/t/175e1796069fd33c

The short version: if we enable in-place optimizations we cause problems with numpy and potentially other libraries.

Cheers,

Michael


---

Comment by malb created at 2008-01-29 12:09:10

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2015-03-13 10:20:50

Changing component from packages: standard to cython.


---

Comment by jdemeyer created at 2015-06-23 11:31:44

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-06-23 11:31:44

Wontfix, see #18772.


---

Comment by jdemeyer created at 2015-06-23 11:31:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-07-17 20:05:45

Resolution: wontfix
