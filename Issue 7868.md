# Issue 7868: Factoring in fraction fields

Issue created by migration from Trac.

Original creator: spancratz

Original creation time: 2010-01-07 17:07:43

Assignee: AlexGhitza

CC:  cremona

Keywords: fraction field, factorization

The following is a quote from John Cremona, 

    http://groups.google.com/group/sage-devel/browse_thread/thread/3638a91c0438f439

I define a rational function in two variables over a finite field:


```
sage: R.<x,y> = GF(2)[]
sage: f = x*y/(x+y)
sage: f.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Finite
Field of size 2

```


I try to factor it, and get this error:


```
sage: f.factor()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/17587/_home_masgaj__sage_init_sage_0.py
in <module>()

/local/jec/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/rings/fraction_field_element.so
in sage.rings.fraction_field_element.FractionFieldElement.factor
(sage/rings/fraction_field_element.c:2972)()

/local/jec/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so
in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor
(sage/rings/polynomial/multi_polynomial_libsingular.cpp:22701)()

NotImplementedError: proof = True factorization not implemented.  Call
factor with proof=False.

```


So I do what I am told, but:


```
sage: f.factor(proof=False)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/17587/_home_masgaj__sage_init_sage_0.py
in <module>()

TypeError: factor() takes no keyword arguments

```




---

Attachment


---

Comment by spancratz created at 2010-01-07 18:36:25

Changing status from new to needs_review.


---

Comment by spancratz created at 2010-01-07 18:36:25

The patch I attached earlier changes the behaviour of the factoring method in fraction fields, passing on additional parameters to the factoring method of the underlying ring rather than ignoring them.

I've now tested the patch (without the ``long`` option), and this did not return any test failures.

Sebastian


---

Comment by spancratz created at 2010-01-07 18:36:41

Changing assignee from AlexGhitza to spancratz.


---

Comment by robertwb created at 2010-01-07 19:54:21

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-07 19:54:21

Looks good to me.


---

Comment by robertwb created at 2010-01-07 19:55:35

Well, the code looks good, but we need a test showing the behavior is fixed.


---

Comment by robertwb created at 2010-01-07 19:55:35

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-01-07 20:10:43

I agree with Robert's point, which I was going to make too.  But for me the code does not apply to either 4.3 or 4.3.1.apha1.  Sebastian, did you make the patch on top of your other changes to the fraction field code?  Robert, did you apply the patch?


---

Comment by robertwb created at 2010-01-07 20:39:03

No, I didn't actually apply it... (I've got a lot of fraction field changes that I needed to pop off first, and no, it's not applying for me either. I don't see why.) I've posted an updated one that should merge onto 4.3 fine, with the new doctest.


---

Comment by robertwb created at 2010-01-07 20:39:03

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-07 21:20:03

OOps, that second patch is empty!


---

Comment by cremona created at 2010-01-07 21:20:03

Changing status from needs_review to needs_work.


---

Attachment

replaces previous


---

Comment by robertwb created at 2010-01-07 21:38:44

Oops...


---

Comment by robertwb created at 2010-01-07 21:55:15

Changing status from needs_work to needs_review.


---

Attachment

replaces previous


---

Comment by cremona created at 2010-01-07 22:02:49

I deleted the lines sage: f.parent() in the patch since you omitted its output.  If this works for you: positive review.  Thanks!


---

Comment by cremona created at 2010-01-07 22:02:49

Changing status from needs_review to positive_review.


---

Comment by spancratz created at 2010-01-08 01:43:43

Great.  This all happened rather swiftly!

Sebastian

Replying to [comment:10 cremona]:
> I deleted the lines sage: f.parent() in the patch since you omitted its output.  If this works for you: positive review.  Thanks!


---

Comment by rlm created at 2010-01-13 08:20:37

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 08:20:37

Sorry, there's a conflict:

```
patching file sage/rings/fraction_field_element.pyx
Hunk #1 FAILED at 212
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/fraction_field_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 7868-fix.2.patch
```



---

Comment by spancratz created at 2010-01-19 12:49:41

Rebase to 4.3.1.rc0


---

Comment by rlm created at 2010-01-19 20:04:27

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by rlm created at 2010-01-19 20:05:13

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 20:06:57

Resolution: fixed
