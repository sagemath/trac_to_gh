# Issue 8449: real_part? has an unescaped \r

Issue created by migration from https://trac.sagemath.org/ticket/8449

Original creator: jason

Original creation time: 2010-03-05 21:53:57

Assignee: mvngu

This docstring should be a raw string (i.e., r""" ... """)


---

Attachment

based on Sage 4.4.2.alpha0


---

Comment by mvngu created at 2010-05-09 23:36:21

Changing priority from minor to trivial.


---

Comment by mvngu created at 2010-05-09 23:36:21

Changing status from new to needs_review.


---

Attachment


---

Comment by burcin created at 2010-05-10 03:24:48

There were a few more docstrings in that file with the same problem. Positive review to Minh's patch. Someone needs to review mine now. :)


---

Comment by mvngu created at 2010-05-10 04:28:09

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-10 04:28:09

Looks good. Burcin's patch clearly takes care of the others I missed.


---

Comment by mvngu created at 2010-05-11 05:16:16

Merged in this order:

 1. [trac_8449.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8449/trac_8449.patch)
 1. [trac_8449.more_rs.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8449/trac_8449.more_rs.patch)


---

Comment by mvngu created at 2010-05-11 05:16:16

Resolution: fixed
