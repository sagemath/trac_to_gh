# Issue 8111: gcd of rationals is trouble

Issue created by migration from Trac.

Original creator: pdehaye

Original creation time: 2010-01-28 15:04:16

Assignee: AlexGhitza

The GCD of rationals is still unclear (see trac 3214), and leads to definite problems with reduce(). 


```
K.<k>= QQ[];
print gcd(64,256)
print gcd(K(64),K(256))
print gcd(64*k^2+128,64*k^3+256)
frac = (64*k^2+128)/(64*k^3+256)
frac.reduce()
print frac
```

gives

```
64
1
1
(64*k^2 + 128)/(64*k^3 + 256)
```

The last line in particular is false, according to me.


---

Comment by burcin created at 2010-01-29 15:07:11

I think the trouble here is our generic fraction field code, not how we define the gcd of rational numbers.

For efficiency, we should represent QQ(x) as Frac(ZZ[x]), and do the necessary normalisation of the denominator (it should be monic) when the user accesses it with `.denominator()`.


---

Comment by kcrisman created at 2011-02-16 21:21:37

#10771 is probably related/same thing.


---

Comment by SimonKing created at 2011-02-17 07:35:58

Replying to [comment:2 kcrisman]:
> #10771 is probably related/same thing.

It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.


---

Comment by SimonKing created at 2011-02-17 07:43:21

Replying to [comment:3 SimonKing]:
> Replying to [comment:2 kcrisman]:
> > #10771 is probably related/same thing.
> 
> It may be related, but my patch from #10771 does not touch the gcd for `QQ['x']` (perhaps it should?). So far, the two tickets are about different issues.

PS: It seems to me that for changing gcd for univariate polynomials over the rationals, one has to dive into flint. I'll not do that, it'd be too far off topic for me. BTW, the doc string explicitly states that gcd in `QQ['x']` returns the _monic_ gcd.


---

Comment by kcrisman created at 2015-02-12 15:06:40

Possibly related: [this discussion](https://groups.google.com/forum/#!searchin/sage-devel/xgcd/sage-devel/JV8fCPUqTzo/FTGonGmYyCgJ).


---

Comment by @kliem created at 2020-05-27 19:04:18

Changing status from new to needs_review.


---

Comment by @kliem created at 2020-05-27 19:04:18

Changing keywords from "" to "sd109".


---

Comment by kcrisman created at 2020-05-27 19:15:41

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2020-05-27 19:15:41

If this is fixed, we should probably have a doctest then.  Unless it wasn't an error to begin with?  Or it's possible it was fixed elsewhere and doctested, which is fine too.


---

Comment by kcrisman created at 2020-05-27 19:15:41

Changing type from defect to task.


---

Comment by kcrisman created at 2020-05-27 19:15:41

Changing priority from major to minor.


---

Comment by @kliem created at 2020-05-27 19:22:01

New commits:


---

Comment by @kliem created at 2020-05-27 19:22:01

Changing status from needs_info to needs_review.


---

Comment by mkoeppe created at 2020-06-14 14:15:47

Changing status from needs_review to positive_review.


---

Comment by @kliem created at 2020-06-14 18:26:20

Thank you.


---

Comment by vbraun created at 2020-07-08 19:32:46

Resolution: fixed
