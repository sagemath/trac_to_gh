# Issue 9845: misspelled word in parallel help function info

Issue created by migration from Trac.

Original creator: negas

Original creation time: 2010-09-01 05:48:06

Assignee: mvngu

Keywords: help info parallel

sage: help(parallel)

help on function parallel in module sage.parallel.decorate:

parallel(p_iter='fork', ncpus=None, **kwds)
    This is a decorator that gives a function a parallel interface,
    allowing it to be called with a list of inputs, whose *_valuaes*_ will
    be computed in parallel.


---

Attachment


---

Comment by aapitzsch created at 2011-01-07 10:09:20

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2011-01-07 10:09:20

Also added an example for `__call__`.


---

Comment by aly.deines created at 2011-01-10 00:02:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:21:50

Resolution: fixed
