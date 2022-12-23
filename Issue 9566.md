# Issue 9566: [with patch, needs review] Allow sage.libs.mpmath.call(..., parent=something)

Issue created by migration from https://trac.sagemath.org/ticket/9566

Original creator: fredrik.johansson

Original creation time: 2010-07-21 17:49:51

Assignee: AlexGhitza

CC:  burcin

This can simplify code that needs to call mpmath in some places.


---

Attachment

does it make sense to also test for parent RDF ?


---

Attachment

works for me


---

Comment by schilly created at 2010-07-21 21:17:38

Changing type from defect to enhancement.


---

Comment by schilly created at 2010-07-21 21:17:38

Changing status from new to needs_review.


---

Comment by schilly created at 2010-07-21 21:17:54

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 02:58:46

Changing status from positive_review to needs_work.


---

Comment by ddrake created at 2010-07-22 02:58:46

Please include ticket numbers in commit messages! Please change back to positive review when both patches are fixed up. Thanks.


---

Attachment

fixed patch


---

Comment by fredrik.johansson created at 2010-07-22 20:55:52

Added mpmath_call_FIXED.patch

I fixed an error in the first patch (there shouldn't be a new kwarg in mpmath_to_sage) and included Harald's change with an extra line to also print the type of the output.


---

Comment by fredrik.johansson created at 2010-07-22 21:05:20

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-07-22 23:05:32

dear release manager, just merge mpmath_call_FIXED.patch and ignore the others.


---

Comment by schilly created at 2010-07-22 23:05:32

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 23:44:54

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 23:44:54

Replying to [comment:6 schilly]:
> dear release manager, just merge mpmath_call_FIXED.patch and ignore the others. 

Done. Thanks for fixing the commit messages!
