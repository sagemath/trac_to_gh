# Issue 6435: misformatted docstrings in sage.misc.abstract_method (easy fix)

Issue created by migration from https://trac.sagemath.org/ticket/6435

Original creator: davidloeffler

Original creation time: 2009-06-27 19:03:05

Assignee: tba

CC:  nthiery

Keywords: ReST docstring formatting

Building the documentation for 4.1.alpha2, there is a warning:

```
WARNING: /home/david/sage-4.1.alpha2/local/lib/python2.6/site-packages/sage/misc/abstract_method.py:docstring of sage.misc.abstract_method.abstract_method:19: (WARNING/2) Literal block expected; none found.
```

This is due to a rogue "::" in a docstring introduced by #6097.


---

Attachment

Here's a patch.


---

Comment by nthiery created at 2009-06-27 21:27:29

Oops, sorry for introducing this, and thanks for fixing it! Positive review.


---

Comment by rlm created at 2009-07-02 23:43:48

Resolution: fixed
