# Issue 8793: clean up documentation of logic/boolformula.py

Issue created by migration from https://trac.sagemath.org/ticket/8793

Original creator: mvngu

Original creation time: 2010-04-28 06:50:43

Assignee: mvngu

As the subject says.


---

Attachment


---

Comment by knsam created at 2013-03-09 07:23:38

Changing keywords from "" to "beginner doctest documentation".


---

Comment by knsam created at 2013-03-24 11:34:35

Apply on top of v0.


---

Attachment

Apply on top of both v0 and doc_add_prep1


---

Comment by knsam created at 2013-03-24 11:39:13

Changing status from new to needs_review.


---

Comment by chapoton created at 2013-07-09 12:38:26

I have added one more patch, that removes whitespaces and makes some changes in import section.


---

Attachment


---

Comment by vbraun created at 2013-07-12 13:16:29

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-07-12 13:16:29

Please refrain from unnecessary whitespace changes in the future.


---

Comment by jdemeyer created at 2013-07-25 17:18:27

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-07-25 17:18:27

The documentation doesn't even build correctly:

```
dochtml.log:[logic    ] /mazur/release/merger/sage-5.11.rc0/local/lib/python2.7/site-packages/sage/logic/boolformula.py:docstring of sage.logic.boolformula:6: WARNING: Bullet list ends without a blank line; unexpected unindent.
dochtml.log:[logic    ] /mazur/release/merger/sage-5.11.rc0/local/lib/python2.7/site-packages/sage/logic/boolformula.py:docstring of sage.logic.boolformula:6: WARNING: Bullet list ends without a blank line; unexpected unindent.
dochtml.log:[logic    ] /mazur/release/merger/sage-5.11.rc0/local/lib/python2.7/site-packages/sage/logic/boolformula.py:docstring of sage.logic.boolformula.BooleanFormula.dist_not:11: WARNING: Inline literal start-string without end-string.
dochtml.log:[logic    ] /mazur/release/merger/sage-5.11.rc0/local/lib/python2.7/site-packages/sage/logic/boolformula.py:docstring of sage.logic.boolformula.BooleanFormula.dist_ors:11: WARNING: Inline literal start-string without end-string.
```



---

Comment by jdemeyer created at 2013-07-25 17:20:44

Why end lines with

```
.::
```


I think these would be rendered as `.:`

You probably want

```
. ::
```



---

Attachment

ok, here is patch that makes sure that the doc build.

It also changes `.::` into `. ::`

It also remove _self_ from the input in most functions

It also makes the code in pep8 standard

Needs review.


---

Comment by chapoton created at 2013-07-26 08:09:27

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2013-08-06 08:47:56

It all looks good to me now `:-)`

Nathann


---

Comment by ncohen created at 2013-08-06 08:47:56

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-17 07:55:28

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-08-17 07:55:28

This should be rebased to sage-5.12.beta1 + #14951.


---

Attachment


---

Comment by chapoton created at 2013-10-04 19:00:25

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-10-04 19:00:25

ok, here is a brand new patch, to be applied alone.

for the *patchbots* apply trac_8793_new_version_2013_10.patch​


---

Comment by chapoton created at 2013-10-04 19:02:06

apply trac_8793_new_version_2013_10.patch


---

Comment by ncohen created at 2013-11-27 16:41:11

Good to go !

Nathann


---

Comment by ncohen created at 2013-11-27 16:41:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-12-05 08:02:28

Resolution: fixed
