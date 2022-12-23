# Issue 4606: elliptic curves -- implement gross-Zagier L-functions

Issue created by migration from https://trac.sagemath.org/ticket/4606

Original creator: robertwb

Original creation time: 2008-11-24 22:59:03

Assignee: was

CC:  was craigcitro wuthrich

Make it so one can do:

```
sage: e = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0); A
Fractional ideal class (2, -1/2*a)
sage: L = e.lseries_gross_zagier(A)  
sage: L(2)
0
sage: L.taylor_series(2,5)
nobody has seen this!
```



---

Attachment


---

Comment by robertwb created at 2008-11-25 06:46:16

Still going to add some doctests right now, but here's the code. Note, however, the check \sum_A L_A(E,s) = L(E/K,s) fails. :(


---

Attachment


---

Attachment


---

Comment by craigcitro created at 2008-11-28 11:38:29

So I've attached a patch, which at least fixes a few issues. This patch fixes two definite bugs:

 * In `E.lseries_gross_zagier(A)`, you were caching the value -- no matter what value of `A` was getting passed in! That was an easy fix. :) Unfortunately, after fixing that, there were still issues. 

 * There was a subtle issue in `I.quadratic_form()`, for `I` an ideal in a quadratic number field. For instance, with just the first two patches above, taking `K = QuadraticField(-40)` and `I` the trivial element in the class group, the code returned `x^2 + 40*y^2` for `I.quadratic_form()`. The underlying issue was one of choice of generators: you were using `K.gen()` where you really needed `K.ring_of_integers().gen()`, because you needed to know that something generated all of `I` over `ZZ`, not just `QQ`. I'm *fairly* certain that the current code is correct, but it's after 2AM, so someone should double check me. 

So, now that those are fixed, we go back to the example Robert points out in the code: 

```
sage: E = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0)
sage: L = E.lseries_gross_zagier(A)
sage: LL = E.lseries_gross_zagier(A**2)
sage: L(2) + LL(2)
0.506799279512368

sage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)
0.502803417587467
```


So we're now quite close. In particular, I wonder if there isn't rounding going on:


```
sage: E.lseries().taylor_series(2,5) * E.quadratic_twist(-40).lseries().taylor_series(2,5)
0.50 + 0.38*z - 0.16*z^2 + 0.0078*z^3 + 0.070*z^4 - 0.039*z^5 + O(z^6)
```


That definitely seems to suggest small precision to me. In any event, we're getting close:


```
sage: L.taylor_series(2,5) + LL.taylor_series(2,5)
0.506799279512368 + 0.360199571567893*z - 0.122141848388581*z^2 - 0.00635398874570253*z^3 + 0.0383995215484257*z^4 + O(z^5)

sage: L.taylor_series(2,5) + LL.taylor_series(2,5) - (E.lseries().taylor_series(2,5) * E.quadratic_twist(-40).lseries().taylor_series(2,5))
-0.016*z + 0.035*z^2 - 0.014*z^3 - 0.031*z^4 + O(z^5)
```


I'll cook up a few more examples and post what I find.


---

Comment by robertwb created at 2008-11-28 18:12:14

Excellent. That's looking very good. I was very tired the day I was finishing that up, so I'm glad you caught these errors.


---

Comment by mabshoff created at 2008-11-28 18:25:37

Replying to [comment:3 robertwb]:
> Excellent. That's looking very good. I was very tired the day I was finishing that up, so I'm glad you caught these errors. 

Should this ticker be "[with patch, needs review]" ? 

Cheers,

Michael


---

Comment by robertwb created at 2008-11-28 18:28:40

No, I don't think so yet (but if Craig is happy with it, then sure).


---

Comment by davidloeffler created at 2009-07-20 19:50:53

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:50:53

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-10-09 09:12:22

Remove assignee davidloeffler.


---

Comment by chapoton created at 2013-09-19 19:54:38

for the *patchbots*:

apply only trac_4606_gross_zagier_lseries_rebased.patch


---

Attachment

folded all three patches and rebased on 5.12.beta5


---

Comment by chapoton created at 2013-10-15 19:25:36

apply trac_4606_gross_zagier_lseries_rebased.patch


---

Comment by chapoton created at 2014-01-09 19:34:53

Changing status from new to needs_info.


---

Comment by chapoton created at 2014-01-09 19:34:53

New commits:


---

Comment by chapoton created at 2014-01-09 19:35:06

Changing status from needs_info to needs_work.


---

Comment by git created at 2015-04-25 16:21:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-04-26 07:54:06

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-01 19:54:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-02 07:32:18

It seems that the Dirichlet coefficients of

- the product of Dirichlet series for E and its twists
- the sum of Dirichlet series for (E,A) over all classes A

do not quite exactly match. I have not been able to locate the error so far. It could be either in the quadratic form code implemented here or elsewhere. Quadratic forms theta series should be checked against the generic implementation of theta series.


---

Comment by chapoton created at 2015-05-02 07:40:06

Apparently, the theta series is good (but slower than the generic implementation).

So the problem must be in the Dirichlet convolution code


---

Comment by git created at 2015-05-02 14:00:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-02 14:22:47

Hum, here is the current state of affairs:

```
sage: E = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0)
sage: L = E.lseries_gross_zagier(A)
sage: LL = E.lseries_gross_zagier(A**2)
sage: L(2) + LL(2)
0.506799279512368
sage: E.lseries()(2) * E.quadratic_twist(-40).lseries()(2)
0.502803417587467
```

Not so good, in fact. Now let us compare Taylor expansions:

```
sage: L.taylor_series(2, 5)+LL.taylor_series(2, 5)
0.506799279512368 + 0.360199571567893*z - 0.122141848388581*z^2 - 0.00635398874570253*z^3 + 0.0383995215484257*z^4 + O(z^5)
sage: E.lseries().taylor_series(2,series_prec=5) * E.quadratic_twist(-40).lseries().taylor_series(2,series_prec=5)
0.502803417587467 + 0.374948906665456*z - 0.144641137632262*z^2 + 0.00702138852027905*z^3 + 0.0487513598755609*z^4 + O(z^5)
```

Not far, but definitely not good. Note that the syntax of taylor expansion differs.


---

Comment by git created at 2015-05-02 16:01:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-02 16:23:23

I think that I have checked fully the computation of the Dirichet coefficients.

So well... maybe something is wrong in the parameters given to Dokchitser program ?

```
sage: e = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-40)
sage: A = K.class_group().gen(0)
sage: from sage.modular.modform.l_series import GrossZagierLseries
sage: G = GrossZagierLseries(e, A)
sage: G._dokchister.check_functional_equation()
-80.1679727952639
sage: G = GrossZagierLseries(e, A**2)
sage: G._dokchister.check_functional_equation()
47.5616711441054
```



---

Comment by git created at 2015-05-02 18:23:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-02 18:29:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-02 18:53:59

This is now working

```
sage: sage: e = EllipticCurve('37a')
sage: sage: K.<a> = QuadraticField(-40)
sage: sage: A = K.class_group().gen(0)
sage: sage: from sage.modular.modform.l_series import GrossZagierLseries
sage: sage: G = GrossZagierLseries(e, A)
sage: sage: G._dokchister.check_functional_equation()
2.77555756156289e-17
sage: sage: G = GrossZagierLseries(e, A**2)
sage: sage: G._dokchister.check_functional_equation()
-3.64291929955129e-17
```

After six years !


---

Comment by cremona created at 2015-05-02 19:03:36

Congratulations! I will look at it, but at the moment I am rebuilding with #18340 (new Pari version), and this should surely be tested on top of that?


---

Comment by cremona created at 2015-05-04 12:04:28

I just wrote a report which trac swallowed and deleted as I was not logged in.  I am not going to rewrite it!  More after I have done some more testing.


---

Comment by cremona created at 2015-05-04 12:05:26

Why is this not "needs review"?


---

Comment by chapoton created at 2015-05-04 12:14:27

I see some remaining things that should be done:

- maybe use the generic theta function code if it is faster than the one provided here for binary quadratic forms (as it seems to be)

- make sure that the syntax is similar to the other L-functions we have

- test with many curves and many quadratic number fields

- have an expert say something about the conductor. I changed it using my very small understanding of Dokchister parameters and it worked. But I am not very sure if it is the right answer for all curves and all fields.


---

Comment by cremona created at 2015-05-04 13:33:26

Replying to [comment:33 chapoton]:
> I see some remaining things that should be done:
> 
> - maybe use the generic theta function code if it is faster than the one provided here for binary quadratic forms (as it seems to be)

Surely such a possible improvement can be noted for later work, and not delay this?

> 
> - make sure that the syntax is similar to the other L-functions we have

Good point.  

> 
> - test with many curves and many quadratic number fields
>

I tested with one curve and many fields.  This led to the one suggestion I have:

- somewhere, perhaps in the constructor for GrossZagierLseries, test that the ideal class is associated to an imaginary quadratic field.  If you construct it from an ideal in a real quadratic field there is a resulting error in the quadratic forms code, and this should be more graceful.

John
 
> - have an expert say something about the conductor. I changed it using my very small understanding of Dokchister parameters and it worked. But I am not very sure if it is the right answer for all curves and all fields.


---

Comment by git created at 2015-05-04 15:10:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2015-05-04 16:46:01

Thanks for the IQF patch.
We should have someone look at the conductor though.  I won't have time (and would have to look things up for sure). Who?


---

Comment by git created at 2015-05-04 19:52:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-13 09:59:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-13 12:16:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-13 12:18:40

Now working better, but not perfectly (some problems with trivial ideal classes)

```
sage: K=QuadraticField(-79)
sage: K.class_group()
Class group of order 5 with structure C5 of Number Field in a with defining polynomial x^2 + 79
sage: A=K.class_group().gen()
sage: E=EllipticCurve('433a1')
sage: sum(E.lseries_gross_zagier(A**i)(2) for i in range(5))
0.173957331997956
sage: E.lseries()(2)*E.quadratic_twist(-79).lseries()(2)
0.327922081982688
sage: lgz=E.lseries_gross_zagier(A)
sage: lgz._dokchister.check_functional_equation()
8.32667268468867e-17
sage: lgz=E.lseries_gross_zagier(A**2)
sage: lgz._dokchister.check_functional_equation()
-2.20309881449055e-16
sage: lgz=E.lseries_gross_zagier(A**3)
sage: lgz._dokchister.check_functional_equation()
-2.20309881449055e-16
sage: lgz=E.lseries_gross_zagier(A**4)
sage: lgz._dokchister.check_functional_equation()
8.32667268468867e-17
sage: lgz=E.lseries_gross_zagier(A**5)
sage: lgz._dokchister.check_functional_equation()
-1383.90668128107
```



---

Comment by chapoton created at 2015-05-13 12:30:04

Is the following thing normal ?

```
sage: K=QuadraticField(-79)
sage: A=K.class_group().gen()
sage: [(A**i).ideal().quadratic_form().discriminant() for i in range(5)]
[-316, -79, -79, -79, -79]
```



---

Comment by git created at 2015-05-13 13:39:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-13 13:48:22

Ok. Now everything seems to work fine. As far as I can tell.

There remains to add a little more doc.


---

Comment by git created at 2015-05-17 19:45:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-17 19:47:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-17 19:58:12

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2015-05-17 19:58:12

Anybody interested, please give me feed back. It seems to work.


---

Comment by chapoton created at 2015-06-26 11:31:51

ping ?


---

Comment by wuthrich created at 2015-06-28 20:15:39

... pong!

I added a little bit more to the documentation. Just pointing to the article is not enough.

I tested this (merged into 6.8.beta6) and all passed. 
----
New commits:


---

Comment by wuthrich created at 2015-06-28 20:15:39

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2015-06-28 20:17:03

oops, sorry, something went wrong. I should be able fix that..


---

Comment by wuthrich created at 2015-06-28 20:17:03

Changing status from positive_review to needs_work.


---

Comment by wuthrich created at 2015-06-29 07:52:34

done and retested.
----
New commits:


---

Comment by wuthrich created at 2015-06-29 07:52:34

Changing status from needs_work to positive_review.


---

Comment by wuthrich created at 2015-06-29 08:34:42

There is one thing, I should add here, although I am in favour of putting this into sage: It is unlikely that this code will be used much. I might be wrong.


---

Comment by cremona created at 2015-06-29 08:49:45

You may well be right, and the fact that nothing much happened to this code for 7 years tends to support that.  But surely that does not matter -- far better that the code be here, properly documented and tested for the future, than that it should wither and die!


---

Comment by vbraun created at 2015-06-29 22:31:25

Resolution: fixed
