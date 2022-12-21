# Issue 8379: add arithmetic for Boolean functions

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2010-02-26 13:21:45

Assignee: mvngu

CC:  malb

we define:

  * `~` : returns the complement Boolean function
  * `+`,`*` : corresponds to the same op. on the ANFs
  * `|` : concatenate the truth tables ( used for various constructions, e.g. http://eprint.iacr.org/2009/134.pdf )



---

Attachment


---

Comment by ylchapuy created at 2010-02-26 13:24:50

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-02-26 13:24:50

The provided patch also correct a bug in the computation of the algebraic immunity.


---

Comment by malb created at 2010-04-05 16:35:17

The patch looks good (I'll run doctests once my update is done) but we usually do not implement `__iadd__` and `__imul__` since objects in Sage are generally supposed to be immutable. There are some exceptions like matrices where this wouldn't make any sense.


---

Comment by malb created at 2010-04-05 18:33:03

Doctests pass. Thust for a positive review from me all that's needed would be to either remove `__iadd__` or to give a justification why this class should be an exception.


---

Comment by wdj created at 2010-04-28 20:16:26

Changing status from needs_review to needs_info.


---

Comment by wdj created at 2010-04-28 20:16:26

ylchapuy?


---

Attachment

apply only this one


---

Comment by ylchapuy created at 2010-05-04 12:55:06

Changing status from needs_info to needs_review.


---

Comment by ylchapuy created at 2010-05-04 12:55:06

Patch updated. I removed the inplace versions `__iadd__` and `__imul__`.

Apply only the last patch.

(and sorry for the delay, I'm quite busy those days...)


---

Comment by malb created at 2010-06-02 20:58:24

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-06-02 20:58:24

Patch looks good, applies cleanly, doctests pass on sage.math


---

Comment by mhansen created at 2010-06-06 08:32:40

Resolution: fixed
