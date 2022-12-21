# Issue 7096: bug in dual isogeny computation

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-10-02 15:05:02

Assignee: davidloeffler

CC:  shumow@gmail.com

Keywords: elliptic curve isogeny


```
sage: p = 1019
sage: F = GF(p)
sage: E = EllipticCurve(F,[1,-1,0,1,1])
sage: psi = E.division_polynomial(7).factor()[3][0]
sage: phi = E.isogeny(kernel=psi)
sage: assert phi.degree()==7
sage: phi.dual()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/jec/.sage/temp/selmer/14232/_home_jec__sage_init_sage_0.py in <module>()

/home/jec/sage-4.1.2.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.pyc in dual(self)
   2998
   2999         phi_hat.set_pre_isomorphism(pre_isom)
-> 3000         phi_hat.set_post_isomorphism(post_isom)
   3001
   3002         self.__dual = phi_hat

/home/jec/sage-4.1.2.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.pyc in set_post_isomorphism(self, postWI)
   2627
   2628         if (self.__E2 != WIdom):
-> 2629             raise ValueError, "Invalid parameter: isomorphism must have domain curve equal to this isogenies'codomain."
   2630
   2631         if (None == self.__post_isomorphism):

ValueError: Invalid parameter: isomorphism must have domain curve equal to this isogenies' codomain.
```


This looks like something which should be easy to fix.


---

Comment by davidloeffler created at 2009-10-09 09:10:20

Remove assignee davidloeffler.


---

Comment by wuthrich created at 2009-10-09 09:24:56

While looking at the code of `{dual()`, I found a second bug in this


```
E = EllipticCurve(GF(7),[1,-1,1,-3,3])
phi = E.isogeny(E([1,0]))
phi.dual()
```


gives a ZeroDivisionError. Only separable isogenies are implented, so one can not possibly take the dual of this separable isogeny of degree 7 in chracteristic 7. A quick check should be introduced here.


---

Comment by wuthrich created at 2009-10-09 10:45:34

Yet another, bigger problem with dual() : Say E -> E' is an isogeny of degree d, then all the algorithm does is creating an isogeny E' -> E of degree d. This does not guarantee that it is the dual; it could be the dual composed with an automorphism, like [-1]. This probably happens quite often as it uses `WeierstrassIsomorphism(E,E')`. This returns one of the isomorphisms without any control of it, hence often the sign will be wrong.

The function dual definitely needs a lot of work.

Now, the actual bug reported in this ticket is not in dual but occurs as

```
E1 = EllipticCurve(GF(1013),[1,-1,0,288,19])
E2 = EllipticCurve(GF(1013),[7,970,0,363,464])
EllipticCurveIsogeny(E1,None,E2,7)
```



---

Comment by wuthrich created at 2009-10-09 11:52:50

Of course the field in the previous lines should be 1019. The output is


```
Isogeny of degree 7 from Elliptic Curve defined by y^2 + x*y = x^3 + 1018*x^2 + 288*x + 19 over Finite Field of size 1019 to Elliptic Curve defined by y^2 + 7*x*y + 850*y = x^3 + 970*x^2 + 445*x + 202 over Finite Field of size 1019
```


which has visibly the wrong, but an isomorphic codomain.
After 1 hour of chasing through the code, I was not able to find the error. I include the author as CC in the hope that he might have an idea.


---

Attachment

applies to 4.1.2. after trac #6886. this is only a provisional patch.


---

Comment by wuthrich created at 2009-10-17 23:13:38

I worked on the bugs for isogenies and I found two. They should be corrected with the above patch. But I have to do some more work and test it carefully, before it is ready for a review.


---

Comment by wuthrich created at 2009-10-23 09:08:44

I started implementing some more related to this ticket. Especially the `formal()` for isogeny. Then there are two ideas how to compute the dual.

 * I can take the implementation as it is now. This yields *a* isogeny of the correct degree
   in the opposite direction. Then I can compute the leading term of the composition in the 
   formal expansion (or simply check to what multiple the differential is pulled-back to). This 
   gives me the `WeierstrassIsomorphism` to use. I am not 100 % sure if this will work in
   all cases. Say the elliptic curve is defined over a finite field and has a cyclic isogeny of
   degree _n<sup>2</sup>_ to itself. It is certain that our current implementation gives back a cyclic 
   isogeny and not just _[n]_. I fear one could find counterexamples... I have to do some 
   testings.
 * Otherwise, I will try to implement the full computation of the dual via the formal group. I 
   believe that there is an algorithm with running time _O(n)_ for an isogeny of prime degree 
   _n_. Though I have not checked this in details. It would only involve to compute the first 
   _2n_ coefficients in _[n]_ and the `division_polynomial` in the formal expansion. The 
   one example I have computed so far by hand was a failure :(. One obstacle here will be the 
   fact that `.reversion()` is only defined for power-series with coefficients in *Q*.

à suivre.


---

Comment by wuthrich created at 2009-10-23 23:47:02

I found another issue with isogenies.


```
E = EllipticCurve('11a1')
E2 = EllipticCurve('11a2')
E2.isogeny(None,codomain=E1,degree=5)
```


fails with 


```
ValueError: Codomain parameter must be isomorphic to computed codomain isogeny
```


while `E.isogeny(None,codomain=E2,degree=5)` works fine. The reason is that the algorithm for computing the kernel polynomial in `compute_isogeny_starks` is only valid for *normalised* isogenies. 

Stark's algorithm is implemented in ell_curve_isogeny.py from scratch and so it contains the computation of the formal expansion of the Weierstrass p function. I wonder if we should add as another possible algorithm to do the same sort of computation, but using the already existing code for formal groups instead. ....


---

Comment by wuthrich created at 2009-10-24 17:29:47

Yet another bug with `dual`. I have to chase that. It does not look like being related to the previously reported bugs.


```
k = GF(103)
E = EllipticCurve(k,[1,0,0,1,-1])
P = E(60,85)
phi = E.isogeny(P)
phi.dual()
```


gives


```
IndexError: list index out of range
```


in  line 3789.

(I keep on adding these bugs here and I try to resolve as many as I can with the patch for this. Only then I will open new tickets for the remaining ones)


---

Comment by cremona created at 2009-10-24 19:19:31

Thanks for your work on this.  Perhaps we should make dual raise a NotImplementedError since it fails in so many different ways?

I think that when Dan Shumow implemented all the isogeny stuff he was mainly interested in certain kinds of isogenies (over finite fields?) so did not test as much in other situations.  Just guessing.  [For example, he added the model parameter on my request, over Q only;  I would have made that the default over Q.]


---

Comment by wuthrich created at 2009-10-24 20:22:33

The problem is that most errors go back to problems for the `EllipticCurveIsogeny` constructor itself. So they can be recreated without `dual`. Of course, I don't want `isogeny()` to raise a `NotImplementedError`. But I will include warnings in the documentation...


---

Attachment

Another preliminary version. Replaces the previous patch.


---

Comment by wuthrich created at 2009-11-01 14:28:15

OK. Here we go. That is a patch for this ticket that I would like to be reviewed.

I explain all the changes it introduces as it is quite a long and complicated patch. (I like the fact that the initial comment on the ticket was _"This looks like something which should be easy to fix."_ while it took me a month of quite hard work.)

 * I moved the computation of the weierstrass p-function into a seperate file ell_wp.py.
   I also completely clean it. It used to contain a lot of functions on power series that
   are already implemented in sage. There is an option now to call the pari version.
 * I added a `weierstrass_p` to ell_field.py.
 * Having redone all the weierstrass_p with laurent and power series rather than with 
   polynomials, also got rid of the `IndexError` mentioned above.
 * The dual is now correct and not just up to an automorphism.
 * When trying to give an isogeny with a codomain, it now checks if the algorithm fails
   (typically because there is no cyclic normalized isogeny of this degree). This eliminates a
   bad bug that was known in the code.
 * We can now take duals of non-normalized isogenies
 * There is a new function `formal` that computes the formal expansion of the isogeny.
 * This `formal` can be used to check if the isogeny is normalized; this simplifies and
   corrects the previous code (which is still there but deprecated).
 * I included a check to forbid `dual` of isogenies of degree divisible by the 
   charactersitic.
 * I updated a lot of the documentation of isogenies.
 * And I also changed the starting documentation of ell_generic.py to clarify what we mean by
   an elliptic curve in sage.
 
There is still a lot that should be done about isogenies for elliptic curves. I hope this patch corrects and clarifies what is possible right now. For further things that one could wish for in sage concerning isogenies and endomorphisms I opened ticket #7368 as a follow up.

Note that this ticket also includes the correction asked for in #7307.


---

Attachment

patch for this ticket exported against 4.2.alpha1. (in particular after #6886). This patch should be reviewed while the previously submitted should be ignored.


---

Comment by wuthrich created at 2009-11-01 14:30:15

Changing status from new to needs_review.


---

Comment by wuthrich created at 2009-11-01 14:33:07

Sorry I saw that the patch does not include the new file ell_wp.py.


---

Comment by wuthrich created at 2009-11-01 14:33:07

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2009-11-01 15:06:37

You have done a great job, and I look forward to studying it in detail.  Unfortunately other work prevents me from doing so for quite a while, so although I was the one who posted this (complete with under-estimation of the work involved) I would be very happy if someone else interested reviews it first.


---

Comment by cremona created at 2009-11-01 15:06:49

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-11-01 15:15:44

After writing the above I went ahead anyway and read the patch -- when ell_wp.py is added too I'll try test to test it as well.


---

Attachment

Replaces all previous patches.


---

Comment by wuthrich created at 2009-11-01 15:23:04

Ok that was easy. now it should be review-able.


---

Comment by cremona created at 2009-11-01 17:06:40

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2009-11-01 17:06:40

OK, I relented and have reviewed the patch.  It is great.  It applies fine to 4.2 and builds and tests ok.  (Even better, my not-yet-complete patch for #6887 applied OK on top of this, so a large piece of work which uses isogenies a lot still works fine;  that is a very good test, I think).  I also built and read through the documentation, which is good -- better than before in several respects.  I may have spotted a typo or too but did not note them down so will not delay things by hunting them down.

Positive review: and gives me a spur to finish #6887.


---

Comment by wuthrich created at 2009-11-01 17:37:35

That was quick ! Thanks a lot.

Chris.


---

Comment by mhansen created at 2009-11-02 04:49:07

Resolution: fixed
