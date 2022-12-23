# Issue 8587: get rid of annoying warning in vector_space_dimension()

Issue created by migration from https://trac.sagemath.org/ticket/8587

Original creator: malb

Original creation time: 2010-03-23 13:46:54

Assignee: malb

CC:  burcin polybori

We pass a Groebner basis to `vdim()` of Singular but forgot to mention it to Singular.


---

Attachment


---

Comment by malb created at 2010-03-23 13:47:28

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-04 21:30:52

Looks good to me.

AFAICT, the message is printed to stderr, so there is no easy way to test this.


---

Comment by burcin created at 2010-05-04 21:30:52

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-05-04 21:32:12

apply only this patch


---

Attachment

attachment:trac_8587-vdim_warning.patch adds the ticket number in the log message.


---

Comment by mvngu created at 2010-05-08 21:46:13

Merged [trac_8587-vdim_warning.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8587/trac_8587-vdim_warning.patch).


---

Comment by mvngu created at 2010-05-08 21:46:13

Resolution: fixed
