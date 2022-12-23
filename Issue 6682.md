# Issue 6682: Support non-ASCII characters in Sage sources

Issue created by migration from https://trac.sagemath.org/ticket/6682

Original creator: robertwb

Original creation time: 2009-08-07 07:03:17

Assignee: tbd

CC:  mvngu kini

This involves at least fixing the documentation build process and trac to support utf-8. Possibly other components as well. 

Discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/ff129ae1c62d5a78


---

Comment by mpatel created at 2010-01-21 04:08:36

Script to prepend coding to .py(x) files.  Not a patch.


---

Attachment

From my brief experience with Unicode in SageNB sources (#7249 adds them to doctests), we may just need to

 * Prepend `# -*- coding: utf-8 -*-` to every .py file.  I assume we should do this for .pyx files, too.  I've attached a [attachment:prependify.py script] that can do this, although I'm sure there are more succinct ways.

 * Use `unicode` strings for docstrings that contain non-ASCII Unicode characters.  For example,

```python
def f(n):
    u"""
    Transmogrifies ``n``, heinously. ☺
    """
    return transmogrify(n, algorithm='heinous')
```


Note: At #8000, Minh suggested polling sage-devel about allowing non-ASCII characters in Sage library code.  I'll try to do this soon.


---

Comment by jdemeyer created at 2014-02-14 12:39:13

We already do support UTF-8 in Sage sources, nothing to see here...


---

Comment by jdemeyer created at 2014-02-14 12:39:13

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-02-14 12:39:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-19 18:56:05

Resolution: fixed
