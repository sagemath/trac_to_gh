# Issue 7685: integer.pyx: factor docstring lies about output -- fix this

Issue created by migration from https://trac.sagemath.org/ticket/7685

Original creator: was

Original creation time: 2009-12-15 18:08:01

Assignee: AlexGhitza

CC:  kcrisman

The docstring for n.factor (for n a Sage integer) says it returns a list of pairs.  Actually it returns a Factorization (which derives from list, but prints differently, has arithmetic support, etc.).

We should also have an OUTPUT: block. 


---

Comment by dsm created at 2012-05-26 05:08:08

minor doc edits


---

Attachment

Minor tweaks.


---

Comment by dsm created at 2012-05-26 05:10:07

Changing status from new to needs_review.


---

Comment by was created at 2012-05-26 06:14:48

LGTM!


---

Comment by was created at 2012-05-26 06:14:48

Changing status from needs_review to positive_review.


---

Comment by was created at 2012-05-26 06:14:48

Changing keywords from "" to "sd40.5".


---

Comment by jdemeyer created at 2012-06-05 06:43:39

Resolution: fixed
