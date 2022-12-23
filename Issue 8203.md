# Issue 8203: misc doc fixes

Issue created by migration from https://trac.sagemath.org/ticket/8203

Original creator: jhpalmieri

Original creation time: 2010-02-07 03:48:02

Assignee: mvngu

The attached patch fixes several warnings when building the documentation.



---

Comment by mvngu created at 2010-02-07 04:06:50

The attachment [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) conflicts with the patch at #8190: 

```
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.2-sage.math/devel/sage-main
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8190/trac_8190-docbuild.patch && hg qpush
adding trac_8190-docbuild.patch to series file
applying trac_8190-docbuild.patch
now at: trac_8190-docbuild.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8203/trac_8203-doc.patch && hg qpush
adding trac_8203-doc.patch to series file
applying trac_8203-doc.patch
patching file sage/gsl/ode.pyx
Hunk #1 FAILED at 205
1 out of 3 hunks FAILED -- saving rejects to file sage/gsl/ode.pyx.rej
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 644
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/rings/quotient_ring.py
Hunk #1 FAILED at 527
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/quotient_ring.py.rej
patching file sage/schemes/elliptic_curves/ell_generic.py
Hunk #1 FAILED at 2155
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_generic.py.rej
patching file sage/symbolic/expression.pyx
Hunk #1 succeeded at 4978 with fuzz 2 (offset -957 lines).
patching file sage/symbolic/relation.py
Hunk #1 FAILED at 860
Hunk #2 FAILED at 925
Hunk #3 FAILED at 985
Hunk #4 FAILED at 1014
4 out of 4 hunks FAILED -- saving rejects to file sage/symbolic/relation.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8203-doc.patch
```

Do you want to rebase [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) on top of #8190?


---

Comment by mvngu created at 2010-02-07 04:06:50

Changing status from new to needs_work.


---

Comment by jhpalmieri created at 2010-02-07 05:37:23

Replying to [comment:1 mvngu]:
> Do you want to rebase [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) on top of #8190?

Do I _want_ to?  Not really.  But here's a new version of the patch.

By the way, can I add "delete `SAGE_ROOT/devel/sage/doc/en/reference/sage/misc/attach.rst`" to this ticket, since this didn't get done as part of #8022?


---

Comment by jhpalmieri created at 2010-02-07 05:37:23

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mhampton created at 2010-02-07 23:27:56

Looks good to me, seems pretty simple and docs build OK.  Positive review.


---

Comment by mhampton created at 2010-02-07 23:27:56

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 14:41:28

Resolution: fixed
