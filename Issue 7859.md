# Issue 7859: bug in QQbar (easy to fix!)

Issue created by migration from https://trac.sagemath.org/ticket/7859

Original creator: was

Original creation time: 2010-01-06 19:45:02

Assignee: AlexGhitza


```
The code

R.<x> = AA[]
v1 = QQbar.polynomial_root(AA.common_polynomial(x^4 + 3*x^2 + 1),\
 CIF(RIF(-RR(2.7018838812806391e-55), RR(2.5616917931009833e-55)),\
 RIF(RR(1.6180339887498947), RR(1.6180339887498949))))
v2 = (2/3*v1^3 + 2/3*v1^2 + 4/3*v1 + 1).norm()
sqrt(v2 - 1)

yields the error

NameError: global name 'AlgebriacNumber' is not defined

Apparently there is a small typo in line 3394 of the file qqbar.py

Best regards,

/Håkan
```



---

Comment by hgranath created at 2010-01-06 20:03:03

Changing status from new to needs_review.


---

Comment by was created at 2010-01-06 20:13:05


```

That's known.  And it was  fixed by an earlier version of the patch at
#6887 which was merged in 4.3.1.alpha1.  But I now see that that fix
has got lost, very strange.  It will need fixing again....

John
```



---

Comment by was created at 2010-01-06 20:13:31

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-01-06 20:13:31

Can you add a doctest to the patch to exercise this bit of code?


---

Comment by hgranath created at 2010-01-06 21:47:53

new version with doctest


---

Attachment


---

Comment by hgranath created at 2010-01-06 21:48:32

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-01-07 00:24:38

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 08:44:56

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 08:44:56


```
patching file sage/rings/qqbar.py
Hunk #2 FAILED at 3392
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/qqbar.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7859.patch
```



---

Comment by zimmerma created at 2010-02-05 21:27:12

This issue seems to be fixed already in 4.3.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = AA[]
sage: v1 = QQbar.polynomial_root(AA.common_polynomial(x^4 + 3*x^2 + 1),\
....:  CIF(RIF(-RR(2.7018838812806391e-55), RR(2.5616917931009833e-55)),\
....:  RIF(RR(1.6180339887498947), RR(1.6180339887498949))))
sage: 
sage: v2 = (2/3*v1^3 + 2/3*v1^2 + 4/3*v1 + 1).norm()
sage: sqrt(v2 - 1)
0
```



---

Comment by jason created at 2010-05-26 15:26:12

I agree.  This is fixed.  Possibly the doctest should be added, though.


```
~/sage/devel/sage/sage/rings% grep AlgebriacNumber *
~/sage/devel/sage/sage/rings%
```



---

Attachment

apply only this patch


---

Comment by davidloeffler created at 2010-06-29 09:29:35

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-06-29 09:29:35

Here's a tiny patch (based on 4.4.4 if it matters) containing just the doctest extracted from Håkan's patch, as Jason suggested.


---

Comment by robertwb created at 2010-06-30 07:24:36

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:19:44

I'm entering a guess in the Reviewer(s) field.  Please correct it, if I'm wrong.


---

Comment by mpatel created at 2010-07-20 09:19:44

Resolution: fixed
