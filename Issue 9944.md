# Issue 9944: partial_fraction_decomposition broken for FpT elements

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-09-18 23:41:19

Assignee: AlexGhitza


```
> sage: R.<x> = GF(3)[]
> sage: q = (x+1)/(x^3+x+1)
> sage: q.partial_fraction_decomposition()
```


See http://groups.google.com/group/sage-support/browse_thread/thread/5423a314227309b3#


---

Comment by robertwb created at 2010-09-19 00:11:51

Changing status from new to needs_review.


---

Attachment


---

Comment by zimmerma created at 2010-09-19 19:36:08

Two small comments: in line 115 of sage/categories/quotient_fields.py, "in-exact" should be
"inexact". Also I don't understand "what side effects would this have this be bad?" on line 166.

Paul


---

Comment by zimmerma created at 2010-09-19 19:36:08

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-09-19 21:00:11

in addition, 2 doctests fail (with 4.5.3):

```
The following tests failed:

        sage -t  devel/sage-9945/sage/rings/ring.pyx # 2 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 5056.9 seconds
```

Paul


---

Comment by robertwb created at 2010-09-21 06:27:34

Changing status from needs_work to needs_review.


---

Attachment

I was just moving code, but it doesn't hurt to clean it up as I do so (and I was the original author, so the criticism is just :) I removed the TODO, I was thinking about changing the factor command to group "equal" roots but that would be too invasive of a change to consider right now.


---

Comment by zimmerma created at 2010-09-21 07:51:58

Robert, sorry the original patch fails to apply to 4.6.alpha1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: 9945
sage: hg_sage.import_patch("/tmp/9945-part-frac-FpT.patch")
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg import   "/tmp/9945-part-frac-FpT.patch"
applying /tmp/9945-part-frac-FpT.patch
patching file sage/rings/fraction_field_element.pyx
Hunk #3 FAILED at 282
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/fraction_field_element.pyx.rej
abort: patch failed to apply
```

Please could you rebase it?
| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |
| Type notebook() for the GUI, and license() for information.        |
Paul


---

Comment by zimmerma created at 2010-09-21 07:51:58

Changing status from needs_review to needs_work.


---

Attachment

apply only this patch


---

Comment by robertwb created at 2010-09-22 03:46:21

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-09-22 10:03:20

The rebased patch works ok with 4.6.alpha1.


---

Comment by zimmerma created at 2010-09-22 10:03:20

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-29 09:19:56

Rebased against #8334 which should be in 4.6.alpha2.  Apply only this patch.


---

Attachment

I've attached a patch rebased for the queue in [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2).


---

Comment by mpatel created at 2010-09-29 10:48:12

Resolution: fixed
