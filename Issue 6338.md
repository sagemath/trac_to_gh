# Issue 6338: make sage -sdist and -bdist take an existing tag name and verify that the tag name is valid

Issue created by migration from https://trac.sagemath.org/ticket/6338

Original creator: ncalexan

Original creation time: 2009-06-16 19:00:05

Assignee: tbd

It's annoying that one has to hg tag --remove VERSION by hand in a bunch of repos if one wants to rebundle a release.

Also, sage -sdist sage-VERSION instead of sage -sdist VERSION causes problems.  Check for this and raise an error.


---

Comment by jdemeyer created at 2012-05-18 13:48:24

Changing component from distribution to scripts.


---

Comment by jdemeyer created at 2012-05-18 13:48:24

Changing assignee from tbd to leif.


---

Comment by jdemeyer created at 2012-05-18 13:55:28

Changing priority from major to minor.


---

Comment by jdemeyer created at 2012-05-18 13:55:28

Changing status from new to needs_review.


---

Attachment


---

Comment by vbraun created at 2012-05-23 16:03:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2012-05-23 16:03:07

Looks good. I tripped over this more than once, thanks for fixing!


---

Comment by jdemeyer created at 2012-05-23 21:30:58

Resolution: fixed
