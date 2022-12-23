# Issue 8816: Bug in CPS_height_bound

Issue created by migration from https://trac.sagemath.org/ticket/8816

Original creator: robertwb

Original creation time: 2010-04-29 05:59:24

Assignee: cremona

The documentation states that 


```
        Return the Cremona-Prickett-Siksek height bound. This is a
        floating point number B such that if P is a rational point on
        the curve, then `|h(P) - \hat{h}(P)| \leq B`, where `h(P)` is        the naive logarithmic height of `P` and `\hat{h}(P)` is the
        canonical height.
```


But


```
            sage: E = EllipticCurve("5077a")
            sage: E.CPS_height_bound()
            0.0
```


Clearly that can't be correct as the naive height is not exactly equal to the canonical height. Either the documentation is incorrect, or the function broken for higher rank curves (in which case we should raise an error of some sort.)


---

Comment by cremona created at 2010-04-29 09:25:37

It is the documentation which is wrong.  Although the difference h(P) - \hat{h}(P)  is bounded above and below, this function returns the upper bound (since that is the one most used), i.e. it returns B such that h(P) <= \hat{h}(P) + B.

In the example, the generators are (1,0), (2,0), (0,-3).  Naive heights are therefore 0, log(2)=0.693 and 0.  The canonical heights are 0.6682, 0.767, 0.99.  This is consistent with B=0 as that just says that h(P) is no more than \hat{h}(P).

Note that Magma agrees with the bound of 0 for this curve (which is not that surprising since I wrote the Magma code  as well as the C++ code used here!).  Magma calls it the SiksekBound, despite the paper which it is based on having 3 authors!  The paper does give the lower bound too, and over number fields, so if that is ever needed it could be implemented.

At #8799 I am working through the documentation for this and other mwrank/eclib related functions, and had already noticed that the documentation for the height bounds was wrong in this respect.  I may fix this one at the same time -- in which case I will come back here and cross-reference.

I have taken the liberty of correcting teh title and description on this ticket!  (Rank is irrelevant here).


---

Attachment


---

Comment by robertwb created at 2010-04-29 18:12:09

Ah, OK, that makes more sense. I suspected rank, as the first example I tried (and was surprised by) was 389a (which also has integral generators). 

I have implemented some of this (e.g. the computation of alpha) in my min-height stuff, and am hoping to get a ticket up for that soon.


---

Comment by robertwb created at 2010-04-29 18:12:09

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-29 19:03:22

Replying to [comment:2 robertwb]:
> Ah, OK, that makes more sense. I suspected rank, as the first example I tried (and was surprised by) was 389a (which also has integral generators). 
> 
> I have implemented some of this (e.g. the computation of alpha) in my min-height stuff, and am hoping to get a ticket up for that soon. 

Good!  I'll be waiting...


---

Comment by cremona created at 2010-04-30 20:38:30

Positive review.  (All the patch does is make a minor correction to a docstring.)


---

Comment by cremona created at 2010-04-30 20:38:30

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:54:23

Resolution: fixed
