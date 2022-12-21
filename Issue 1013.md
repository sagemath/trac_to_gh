# Issue 1013: Matrix_real_double_dense overrides parent numpy() method with less-functional version

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-27 22:40:12

Assignee: was

Matrix_real_double_dense and Matrix_complex_double_dense both define a numpy() method that turns the matrix into the appropriate kind of numpy matrix.  However, Matrix defines a numpy() method that takes an optional type argument, to say what kind of matrix to produce.  The specialized classes should also take this optional type argument, and fall back to the slow method defined by Matrix if the type is not 'd' or 'D', respectively.


---

Comment by jason created at 2008-11-14 05:09:08

Changing status from new to assigned.


---

Comment by jason created at 2008-11-14 05:09:08

Changing assignee from was to jason.


---

Comment by jason created at 2008-11-14 05:09:39

This should be a modification of Matrix_double_dense now.


---

Comment by mabshoff created at 2009-02-09 08:36:31

Jason,

did you already fix this in some other patch or is this still open?

Cheers,

Michael


---

Comment by jason created at 2009-02-09 13:09:36

No, I haven't fixed it.  It's one of those low-hanging, one-line fixes, though.


---

Attachment


---

Comment by mhansen created at 2010-08-26 20:11:50

Changing status from new to needs_review.


---

Attachment

Same patch as before but with trailing whitespace removed


---

Comment by davidloeffler created at 2012-03-14 15:31:50

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2012-03-14 15:31:50

Apply trac_1013-whitespace_removed.patch

Looks good and doctests pass. I'm frankly amazed that this patch has survived for so long without bitrotting.


---

Comment by jdemeyer created at 2012-03-23 16:30:31

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-03-23 16:30:31

This needs to be rebased to sage-5.0.beta9:

```
applying trac_1013-whitespace_removed.patch
patching file sage/matrix/matrix_double_dense.pyx
Hunk #1 succeeded at 3268 with fuzz 2 (offset 1875 lines).
```



---

Comment by davidloeffler created at 2012-03-25 13:31:11

Rebase to 5.0.beta10


---

Attachment

Apply trac_1013-rebase.patch

Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.


---

Comment by davidloeffler created at 2012-03-25 13:33:09

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-03-26 13:24:58

Replying to [comment:8 davidloeffler]:
> Apply trac_1013-rebase.patch
> 
> Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.
...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.


---

Comment by davidloeffler created at 2012-03-26 13:51:07

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 davidloeffler]:
> > Apply trac_1013-rebase.patch
> > 
> > Here's the rebase. Since I didn't actually do anything, just hg import / qpush / refresh / export, I think it's valid for me just to restate the positive review.
> ...provided you did a sanity check that the patch was applied correctly.  1875 lines of offset certainly should raise your eyebrows.

It did, and I did, and it was fine. :-)


---

Comment by jdemeyer created at 2012-03-28 10:02:20

Resolution: fixed
