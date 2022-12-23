# Issue 8008: Implement an rref() function which works over the fraction field of the base ring of a matrix

Issue created by migration from https://trac.sagemath.org/ticket/8008

Original creator: jason

Original creation time: 2010-01-20 05:01:34

Assignee: was

CC:  was rbeezer

This is a resolution to the issues at #3211.


---

Attachment


---

Comment by jason created at 2010-01-20 06:00:45

Changing status from new to needs_review.


---

Comment by spancratz created at 2010-01-20 09:11:38

- Perhaps a very short statement about what the row echelon form of matrices over fields look like would be nice.

- line 4035: instead of echelon_form, I think this should be ``echelon_form`` or :meth:`echelon_form`

- line 4085: I'd prefer if this was done in two lines 
    {{{
        F = R.fraction_field()
        return self.change_ring(F).echelon_form()
    }}}
   so that if an error occurs when creating the fraction field, the line number corresponds to the obvious problem.  (Of course, this would be clear from the traceback anyway...)

Sebastian


---

Comment by spancratz created at 2010-01-20 09:11:38

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-01-20 10:02:26

apply on top of previous patch


---

Attachment


---

Comment by jason created at 2010-01-20 10:02:48

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-01-20 10:03:13

The second patch fixes the issues Sebastian brought up.


---

Comment by spancratz created at 2010-01-20 10:55:41

I think this looks good now.


---

Comment by spancratz created at 2010-01-20 10:55:41

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 14:53:24

I got a hunk failure after applying [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch), then [trac-8008-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-fixes.patch):

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8008/trac-8008-rref.patch && hg qpush
adding trac-8008-rref.patch to series file
applying trac-8008-rref.patch
now at: trac-8008-rref.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8008/trac-8008-fixes.patch && hg qpush
adding trac-8008-fixes.patch to series file
applying trac-8008-fixes.patch
patching file sage/matrix/matrix2.pyx
Hunk #3 FAILED at 4273
1 out of 3 hunks FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-8008-fixes.patch
[mvngu@sage sage-main]$ cat sage/matrix/matrix2.pyx.rej
--- matrix2.pyx
+++ matrix2.pyx
@@ -4267,12 +4274,14 @@
         """
         Return the echelon form of self.
 
-        .. note:: This row reduction does not use division if the
-        matrix is not over a field (e.g., if the matrix is over the
-        integers).  If you want to calculate the echelon form using
-        division, then use :meth:`rref`, which assumes that the matrix
-        entries are in a field (specifically, the field of fractions
-        of the base ring of the matrix).
+        .. note:: 
+
+            This row reduction does not use division if the
+            matrix is not over a field (e.g., if the matrix is over
+            the integers).  If you want to calculate the echelon form
+            using division, then use :meth:`rref`, which assumes that
+            the matrix entries are in a field (specifically, the field
+            of fractions of the base ring of the matrix).
         
         INPUT:
```

Perhaps this ticket needs a rebase?


---

Comment by mvngu created at 2010-01-22 14:53:24

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-01-24 12:16:56

rebase of trac-8008-fixes.patch against Sage 4.3.1


---

Attachment

The attachment [trac_8008-fixes-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-fixes-rebase.patch) is a rebase of [trac-8008-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-fixes.patch) against Sage 4.3.1. So my rebase needs some review to ensure I didn't mess up anything. Only apply [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch) and [trac_8008-fixes-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-fixes-rebase.patch).


---

Comment by mvngu created at 2010-01-24 12:20:31

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-02-04 04:33:01

I think the rebase is fine.  But I wanted to add some doctests for more complicated rings, since sometimes echelon_form is not implemented but rref does work.  Anyone can review that review and then all is well.  Apply only rref.patch and rebase-plus-more.


---

Attachment


---

Comment by jason created at 2010-02-27 10:26:51

ping to whoever has time: this is an easy ticket to finish reviewing...


---

Comment by rbeezer created at 2010-02-27 22:44:45

Patches install fine, sage builds and runs, docs build without warnings and look fine, passes all tests.

Positive review.  Thanks for everybody's work on this one, my students will appreciate it.  6 lines of code, 4 reviewers.  Hmmm.

Release manager - two patches only, original "rref" and then "rebase-plus-more."  Should be able to kill #3211 also.


---

Comment by rbeezer created at 2010-02-27 22:44:45

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 21:52:55

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 21:52:55

Merged in this order:

 1. [trac-8008-rref.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac-8008-rref.patch)
 1. [trac_8008-rebase-plus-more.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8008/trac_8008-rebase-plus-more.patch)

Jason: You should put a sensible commit message in your patch, together with the ticket number.


---

Comment by jason created at 2010-03-02 22:03:33

Replying to [comment:12 mvngu]:

> Jason: You should put a sensible commit message in your patch, together with the ticket number.

You'll notice that my recent patches do that :).

I still think the trac ticket number should be automatically prepended to the commit message by the merge script to prevent mistakes and make it easier for patch authors.
