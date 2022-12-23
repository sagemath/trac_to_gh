# Issue 8118: split off Galois representations and modular parametrization from ell_rational_field.py

Issue created by migration from https://trac.sagemath.org/ticket/8118

Original creator: wuthrich

Original creation time: 2010-01-29 15:05:17

Assignee: AlexGhitza

CC:  cremona was robertwb roed

Keywords: elliptic curve, galois representation, modular parametrization

The file ell_rational_field.py is huge and should be split up further. This is especially important for the documentation, currently it is not very user-friendy to find a function in the reference.

I propose a first change.

* The modular paratrization class goes into a separate file. (maybe the modular_degree should mover there too ?)

* The functions concerning the Galois representation are moved to a separate field. I changed the functions like `is_surjective` and `is_irreducible` to deprecated. I believe for instance the latter clashes with the irreducibility of the scheme E.


---

Comment by wuthrich created at 2010-01-29 15:10:11

This patch is my first proposal for changes.

It will also allow me to work more on the Galois representation side. For instance I deleted the second output of non-surjective since it was not used anywhere. I will build this in later in a different way, while also improving the outputs.

Let me know if you think these changes go too far.

What was the decision on deprecation policy of sage ? Is my handling here the correct one ?

What is a ``TestSuite(s).run()` doctest.` ? Where do I find the information on that ?

I have first to test it myself, before I set it to "needs review".


---

Comment by wuthrich created at 2010-01-29 15:11:50

Changing assignee from AlexGhitza to cremona.


---

Comment by wuthrich created at 2010-01-29 15:11:50

Changing component from algebra to elliptic curves.


---

Comment by cremona created at 2010-01-29 16:07:01

I approve of this, though I don't have time to look at the patch right now.


---

Comment by wuthrich created at 2010-02-01 23:42:09

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-02-01 23:42:09

I don't understand this. I exported the patch after adding the two new files to hg. Then I apply it to a new clone.

 The patch applies fine and the tests pass. But when I do -docbuild reference html it tells me that it can not find the new files :


```
 /usr/local/sage/devel/sage/doc/en/reference/plane_curves.rst:7: (WARNING/2) toctree references unknown document u'sage/schemes/elliptic_curves/modular_parametrization'                                 
/usr/local/sage/devel/sage/doc/en/reference/plane_curves.rst:7: (WARNING/2) toctree references unknown document u'sage/schemes/elliptic_curves/gal_reps'     
```


 I must be doing something stupidly wrong. Help !


---

Comment by wuthrich created at 2010-02-01 23:43:03

updated.


---

Attachment

I applied the patch to 4.3.2.alpha1:  OK with some fuzz on hunk #7.

Tests in sage/schemes/elliptic_curves:  all tests (includng long) pass.

sage -docbuild reference html worked fine for me (it warned about 

```
/home/jec/sage-4.3.2.alpha1/devel/sage/doc/en/reference/sage/geometry/polytope.rst:: WARNING: document isn't included in any toctree
/home/jec/sage-4.3.2.alpha1/devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree
```

but that's not from this patch!)

I have not actually looked at the html docs for the new files yet, but will do so.  Meanwhile: positive review.


---

Comment by cremona created at 2010-02-02 09:54:27

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 11:53:14

My queue for 4.3.3.alpha0 is


```
trac_8219.patch
trac_3683-upgrade_moinmoin.patch
trac_8183-French_pdf.patch
trac_8190-docbuild.patch
trac_8184-eclib.patch
trac_8184-indentation.patch
trac_8155.patch
trac_8124-selmer-nf.review.patch
trac_7575.patch
trac_7575-followup.patch
trac_8189-hg.patch
trac_7935.patch
trac_7935b.2.patch
```


Could you let me know how I should apply #8118 and #4453?  Thanks!


---

Comment by mvngu created at 2010-02-13 05:55:47

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-02-13 05:55:47

I get hunk failures when applying [trac_8118.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8118/trac_8118.patch) to Sage 4.3.3.alpha0:

```
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.3.alpha0/devel/sage-main
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8118/trac_8118.patch && hg qpush
adding trac_8118.patch to series file
applying trac_8118.patch
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #2 FAILED at 45
Hunk #7 succeeded at 4141 with fuzz 2 (offset 99 lines).
Hunk #16 FAILED at 5294
Hunk #17 FAILED at 5327
Hunk #18 FAILED at 5367
Hunk #19 FAILED at 5381
Hunk #20 FAILED at 5576
Hunk #21 FAILED at 5589
Hunk #22 FAILED at 5610
Hunk #23 FAILED at 5620
Hunk #24 FAILED at 5692
Hunk #25 FAILED at 5702
Hunk #26 FAILED at 5717
Hunk #27 FAILED at 5728
13 out of 28 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8118.patch
```

Perhaps the attachment needs a rebase.


---

Attachment

exported against 4.3.3.alpha0


---

Comment by wuthrich created at 2010-02-13 18:58:11

No, that patch is not good. I will have to modify BSD.py, too.


---

Comment by wuthrich created at 2010-02-13 19:37:07

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-02-13 19:37:07

OK. so let's hope I did it correctly this time. The patch trac_8118_rebased.patch can be applied to 4.3.3.alpha0. Please apply it before any other patch for ell_rational_field, since it is likely to break again.


---

Comment by wuthrich created at 2010-02-13 21:42:41

Sorry, I tried to do things too quickly..


---

Comment by wuthrich created at 2010-02-13 21:42:41

Changing status from needs_review to needs_work.


---

Attachment

exported against 4.3.3.alpha0


---

Comment by wuthrich created at 2010-02-14 17:50:02

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-02-14 17:50:02

OK. This time, I think I got it right. The patch trac_8118_rebased.patch should apply fine to 4.3.3.alpha0. As said before, it should be applied before any other patch involving ell_rational_field, because I reordered the imports in the beginning of this file.

On my machine all tests pass. (Except for a problem in heegner.py which is already there on 4.3.3.alpha0.)

I don't know if I am allowed to set this back to positive review, since it is only a rebase. So I put a need_review instead. But it would be good if it gets in 4.3.3.


---

Comment by mvngu created at 2010-02-18 21:24:52

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 21:24:52

The rebase looks good. No drama when doctesting.


---

Comment by mvngu created at 2010-02-18 21:26:29

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 21:26:29

Merged [trac_8118_rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8118/trac_8118_rebased.patch).
