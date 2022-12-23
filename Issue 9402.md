# Issue 9402: Extend dokchitser L-function package in Elliptic Curves to Number Fields

Issue created by migration from https://trac.sagemath.org/ticket/9402

Original creator: adam

Original creation time: 2010-07-01 16:24:25

Assignee: cremona

CC:  alexjbest

Keywords: Elliptic Curves, L-series,

This patch adds the attribute .dokchitser() to an elliptic_curve.lseries() over a number field (this capability is present over QQ). It also adds an attribute to .dokchitser(), namely get_coeffs(bound), which returns the first bound coefficients in the Dirichlet expansion of the associated L-series.


---

Comment by adam created at 2010-07-02 20:37:10

Use lseries_num_fields2.patch, the second one. This adds documentation and fixes a bug in the first one. 

The bug fixed is that the elliptic curve E was calling E.reduction(prime_ideal).count_points() where prime_ideal is a prime of good reduction but E is not minimal with respect to that ideal; i.e., that ideal's norm divides the conductor of E.

The fix first checks that E is minimal with respect to said ideal. If not, E.local_minimal_model(prime_ideal).reduction(prime_ideal).count_points() 
is calles.


---

Comment by was created at 2011-02-03 10:37:50

Hi,

1. If you want to get this code refereed you have to set it to "needs review" (under action below). 

2. You function to get the coefficients computes for all primes with residue characteristic up to a given bound.  Instead, it would make vastly more sense to compute for all primes with *norm* up to a given bound.    This is much easier, and in many cases means counting points in easier cases (e.g. over the prime subfield).


---

Comment by was created at 2011-02-03 10:40:16

I also implemented something like this in psage, but it's really just a little reference implementation of computing the Fourier coefficients a_I.     See 

   http://code.google.com/p/purplesage/source/detail?r=7c1e21eb34dbeada1ed0cd5d2011da1226ef5518

It's nice to separate computing the Fourier coefficients from the actual Dokchitser code, I think, since that makes using them much more flexible.


---

Comment by was created at 2011-02-03 12:28:30

I think my comment (2) above is wrong.  I just misunderstood your code.


---

Comment by adam created at 2011-02-03 15:11:24

Changing status from new to needs_review.


---

Comment by aly.deines created at 2011-05-11 16:16:22

Changing status from needs_review to needs_work.


---

Comment by aly.deines created at 2011-05-11 16:16:22

This patch failed to apply on sage-4.7.rc2 (Mac OS X, 10.6.7) and on sage-4.7.rc0.


---

Comment by aly.deines created at 2011-05-11 17:04:28

Nevermind.  I didn't catch that you need to apply the patches in order.  I'm playing with this code now.


---

Comment by aly.deines created at 2011-05-11 17:04:28

Changing status from needs_work to needs_review.


---

Comment by was created at 2011-06-28 19:17:19

Changing status from needs_review to needs_work.


---

Comment by was created at 2011-06-28 19:17:19

Clearly this needs substantial work.  I'm also deleting the two patches and putting one flattened patch.


---

Attachment

*WARNING*   Extensive improvements on this code (which is really a mess right now) are appearing in psage.  See, e.g., the file lseries_nf.py here:

http://code.google.com/p/purplesage/source/browse/#hg%2Fpsage%2Fellcurve%2Flseries

Having just written that code in psage (which involved going through the code on this ticket), I would definitely not recommend including the current code in Sage with a major rewrite.   For example, code like this in the patch:

```
    s = 'v = %s; a(k)=if(k>%s,0,v[k]);'%( coeffs, upper_limit) 
    L.init_coeffs('a(k)', pari_precode = s)    
```

is just masking confusion, since it's setting all Dirichlet coefficients above a certain bound to 0, which is nonsense.


---

Comment by chapoton created at 2013-09-21 12:12:36

Changing keywords from "Elliptic Curves, L-series," to "Elliptic Curves, L-series, dokchitser".


---

Comment by chapoton created at 2018-08-18 13:38:09

New commits:


---

Comment by git created at 2018-08-18 15:31:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-08-19 09:16:17

There are some failing doctests, namely one check of the functional equation does not pass. Maybe the list of coefficients is wrong in this case, or maybe some other bug is lurking around (or some wrong other Dokchitser parameters ?).


---

Comment by chapoton created at 2019-03-09 07:32:18

Changing keywords from "Elliptic Curves, L-series, dokchitser" to "Elliptic Curves, lseries, dokchitser".
