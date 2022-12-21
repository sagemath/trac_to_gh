# Issue 7711: integral() does not reduce coefficients in finite field

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2009-12-16 12:21:31

Assignee: malb

Consider the following example:

```
sage: P.<x,z> = PolynomialRing(GF(2147483647))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z   
sage: p.integral()
1/2*y^2 + (x + z)*y
```

Note the leading coefficient 1/2 is not reduced mod 2147483647.

For smaller p this seems to work:

```
sage: P.<x,z> = PolynomialRing(GF(2147483629))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z
sage: p.integral()
-1073741814*y^2 + (x + z)*y
```

It works also when the smaller ring P has only one variable:

```
sage: P.<x> = PolynomialRing(GF(2147483647))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y
sage: p.integral()
1073741824*y^2 + x*y
```



---

Comment by was created at 2009-12-24 07:07:56

I'm declaring a total feature freeze on sage-4.3.


---

Comment by AlexGhitza created at 2010-01-02 11:14:53

Note also that in Paul's first example we have:


```
sage: p.integral().parent()
Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in x, z over Finite Field of size 2147483647
```


whereas in the second:


```
sage: p.integral().parent()
Univariate Polynomial Ring in y over Multivariate Polynomial Ring in x, z over Finite Field of size 2147483629
```


This is probably where the issue is.


---

Comment by zimmerma created at 2010-02-05 20:19:00

The bug is still there in 4.3.1.


---

Comment by jen created at 2012-03-19 18:28:17

Changing status from new to needs_review.


---

Comment by jen created at 2012-03-19 18:28:17

Changing keywords from "" to "rd2".


---

Comment by jen created at 2012-03-19 18:28:17

This is no longer an issue:


```
sage: P.<x,z> = PolynomialRing(GF(2147483647))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z   
sage: p.integral()
-1073741823*y^2 + (x + z)*y
sage: P(-1073741823*2)
1
```



---

Comment by jen created at 2012-03-19 18:28:49

Changing status from needs_review to positive_review.


---

Comment by dsm created at 2012-03-19 18:37:47

I don't agree that this has been fixed.  In 5.0.beta8, I only have to go up to the next prime:



```

sage: def f(N):
....:     P.<x,z> = PolynomialRing(GF(N))
....:     Q.<y> = PolynomialRing(P)
....:     p=x+y+z   
....:     return p.integral()
....: 
sage: N = 2147483647
sage: f(N)
-1073741823*y^2 + (x + z)*y
sage: N = next_prime(N)
sage: N
2147483659
sage: f(N)
1/2*y^2 + (x + z)*y

```



---

Comment by jen created at 2012-03-19 18:50:23

Good catch. I'll change it back to "needs work."


---

Comment by jen created at 2012-03-19 18:50:23

Changing keywords from "rd2" to "".


---

Comment by jen created at 2012-03-19 18:50:23

Changing status from positive_review to needs_work.


---

Comment by AlexGhitza created at 2012-03-24 05:24:02

For large primes, Sage uses polydicts for representing multivariate polynomials, instead of using Singular.  The trouble here is that dividing a polydict by another polydict automatically creates the fraction field, even when the denominator is actually an element of the coefficient ring.

The attached patch tries to detect this (relatively common) special case and perform the division in the coefficient ring instead of going to the fraction field of the ring of polynomials.  This fixes the problems with `integral()` reported here.


---

Comment by AlexGhitza created at 2012-03-24 05:25:24

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2012-03-24 08:59:58

Alex,

there is something I don't understand with your patch. You check that `right` is in the base
ring, but not `1/right`, thus what happens the base ring is not a field? Compare for example:

```
sage: P.<x,z> = PolynomialRing(ZZ)
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z
sage: t=p/2
sage: t.parent()
Univariate Polynomial Ring in y over Multivariate Polynomial Ring in x, z over Rational Field
sage: u=p.integral()
sage: u.parent()
Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in x, z over Integer Ring
```

Why do t and u have different parents?

Paul


---

Comment by zimmerma created at 2012-03-24 09:00:40

Changing status from needs_review to needs_info.


---

Comment by AlexGhitza created at 2012-03-24 09:08:16

I guess I always found the following strange:


```
sage: type(3)
<type 'sage.rings.integer.Integer'>
sage: type(3/1)
<type 'sage.rings.rational.Rational'>
```


and that influenced me in writing this patch.  I don't however have a strong opinion about this, and I'm happy to change it to make things more consistent by working in the fraction field of base_ring.  I'll replace the patch with one having this behavior soon.


---

Comment by AlexGhitza created at 2012-03-24 09:28:11

By the way, the issue you point out with ZZ coefficients is apparently orthogonal to this patch.  Multivariate polynomials over ZZ are handled by Singular, and the patch does not touch them.  It only modifies the behavior for multivariate polynomials that are implemented as polydict's, such as the ones over finite fields of huge characteristic that this ticket started with.

Your ZZ example behaves the same with or without this patch.  If you find it really bothersome, maybe it can be on a new ticket.


---

Comment by AlexGhitza created at 2012-03-24 09:39:23

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2012-03-24 09:52:44

Alex, can you add an example where your patch is called with coefficients in a ring?

About `3/1` giving a rational, this is ok for me. Indeed, you don't want the type of the result
to differ when the division is exact or not: `3/2` and `3/1` should give both rationals.

Paul


---

Comment by AlexGhitza created at 2012-03-24 10:42:36

Changing status from needs_review to needs_info.


---

Comment by AlexGhitza created at 2012-03-24 10:42:36

Alright, I'm starting to see what you are objecting to, and I agree with you.  Just to make sure I get this right: even the documented examples from the docstring of integral are inconsistent in this way


```
        EXAMPLES::
        
            sage: R.<x> = ZZ[]
            sage: R(0).integral()
            0
            sage: f = R(2).integral(); f
            2*x
        
        Note that since the integral is defined over the same base ring the
        integral is actually in the base ring.
        
        ::
        
            sage: f.parent()
            Univariate Polynomial Ring in x over Integer Ring
        
        If the integral isn't defined over the same base ring, then the
        base ring is extended::
        
            sage: f = x^3 + x - 2
            sage: g = f.integral(); g
            1/4*x^4 + 1/2*x^2 - 2*x
            sage: g.parent()
            Univariate Polynomial Ring in x over Rational Field
```


We want Sage to be less clever and more consistent, so the integral of 2 should be 2x in QQ[x] rather than in ZZ[x].

Of course, this is fun to implement, because you might have something like:


```
sage: A.<a, b> = PolynomialRing(ZZ)
sage: C.<c> = PolynomialRing(A)
sage: D.<d> = PowerSeriesRing(C)
sage: R.<x> = PolynomialRing(D)
sage: f = a*x^2 + c*x
sage: f.parent()
Univariate Polynomial Ring in x over Power Series Ring in d over 
Univariate Polynomial Ring in c over Multivariate Polynomial Ring 
in a, b over Integer Ring
```


What I would like to do is have f.integral() live in

```
Univariate Polynomial Ring in x over Power Series Ring in d over 
Univariate Polynomial Ring in c over Multivariate Polynomial Ring 
in a, b over Rational Field
```


So I want to change to the fraction field at the very bottom of the chain of extensions.  This means starting with R and going down to ZZ step by step, then changing ZZ to QQ and walking back up, changing all the intermediate rings along the way.  It can get expensive, but I guess that's the price to pay for working with such monstrosities.

If my outline agrees with what you had in mind, I'll produce a new patch based on it.


---

Comment by zimmerma created at 2012-03-24 11:03:37

Alex,

in fact I guess your initial patch did what we want. Indeed with your latest example:

```
sage: g=f/2
sage: g.parent()
Univariate Polynomial Ring in x over Power Series Ring in d over Univariate Polynomial Ring in c over Multivariate Polynomial Ring in a, b over Rational Field
```

thus the fact of dividing f by an element of the base ring automatically extends it to the corresponding
fraction field if necessary.

Thus I suggest you revert to your first patch (sorry) and add the above example as test.

Paul


---

Comment by was created at 2012-03-24 11:54:33

Does this patch break a major fundamental design decision in both Sage and Magma, namely that / is a constructor for elements of the fraction field.   E.g.,  3/1 has parent QQ.


---

Comment by zimmerma created at 2012-03-24 14:08:13

William, I don't think this patch (still not ready) will break anything, since I believe it will just
return f/c where f is a polynomial and c an element of the base ring.

Anyway your advice how to best solve this problem is welcome.

Paul


---

Comment by AlexGhitza created at 2012-03-24 21:17:27

Replying to [comment:20 was]:
> Does this patch break a major fundamental design decision in both Sage and Magma, namely that / is a constructor for elements of the fraction field.   E.g.,  3/1 has parent QQ.

Hi William, can you have a look at the docstring for p.integral() as it stands now and tell me whether you think it complies with this design decision?  Here is an example:


```
sage: S.<x> = ZZ[]
sage: p = 2*x
sage: p.integral()
x^2
sage: p.integral().parent()
Univariate Polynomial Ring in x over Integer Ring
```


Behind the scenes Sage performed 2/2 and decided that the answer was 1 in ZZ rather than 1 in QQ, so this seems to break the convention.  Also, the answer has a different parent than (3*x).integral(), which is the type of inconsistency that Paul was pointing out before.  So should this stay the way it is, or should this be changed to be more consistent?

But it gets a tiny bit more complicated than this.  Suppose your coefficients are not ZZ, but rather ZZ[y], where y is a vector of 200 variables.  The integral of 2*x is still `x^2`, but where do we want this `x^2` to live?  Possible answers are (a) ZZ[y][x], (b) Frac(ZZ[y])[x], (c) QQ[y][x].
The current behavior is (a) for 2*x and (b) for 3*x, and I am currently leaning toward changing both to (c).  Here's why: you have p in R[x], where R is some coefficient ring.  When you do p.integral(), you are not really dividing p by integers n, but rather the coefficients of p by integers n.  So maybe we should look at what division by n in the coefficient ring R does:


```
sage: R.<y0,y1,y2,y3> = ZZ[]
sage: S.<x> = R[]
sage: p = 2*y0
sage: p.parent()
Multivariate Polynomial Ring in y0, y1, y2, y3 over Integer Ring
sage: (p/2).parent()
Multivariate Polynomial Ring in y0, y1, y2, y3 over Rational Field
sage: p = 3*y0
sage: (p/2).parent()
Multivariate Polynomial Ring in y0, y1, y2, y3 over Rational Field
```


So p/2 is not in the fraction field of R.  This is what I would like integral() to do as well.

Thoughts?


---

Comment by AlexGhitza created at 2012-03-24 23:17:14

OK, I have changed the patch to a new one that achieves objective (c) in the previous comment.  It is also simpler and cleaner than the previous patches.  `integral` now relies on the coefficient rings to do the right thing.  They mostly do, except for polydict, whose behavior is fixed by the patch as well.


---

Comment by AlexGhitza created at 2012-03-24 23:23:06

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2012-03-26 07:49:49

Alex, I tried to apply your patch to sage-5.0.beta9 but it failed:

```

sage: hg_sage.import_patch("trac7711.patch")
cd "/localdisk/tmp/sage-5.0.beta9/devel/sage" && sage --hg import   "/localdisk/tmp/sage-5.0.beta9/trac7711.patch"
applying /localdisk/tmp/sage-5.0.beta9/trac7711.patch
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #1 FAILED at 2369
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
abort: patch failed to apply
```

For which version is this patch?

Paul


---

Comment by AlexGhitza created at 2012-03-26 07:55:51

> For which version is this patch?

It's based on sage-4.8.  I have a sage-5.0.beta10 somewhere, I'll rebase it on that soon.


---

Comment by zimmerma created at 2012-03-26 07:57:22

it seems my sage-5.0.beta9 was corrupted. I'll compile sage-5.0.beta10 from source and try
again.

Paul


---

Comment by AlexGhitza created at 2012-03-26 08:10:53

I tried on a clean sage-5.0.beta10 and the previous version of the patch did not apply correctly.  I have rebased it now and it should work.


---

Comment by zimmerma created at 2012-03-26 15:04:59

replying to comment [comment:22]: I guess we should just return `p/2` and let the coercion
mechanism decide the corresponding parent. In such a way it will ensure that `p.integral()` and `p/2` have the same type.

Paul


---

Comment by zimmerma created at 2012-03-26 16:00:34

I confirm the rebased patch applies cleanly to sage-5.0.beta10.

However there is still an issue:

```
sage: R.<x> = ZZ[]
sage: R(0).integral().parent()
Univariate Polynomial Ring in x over Integer Ring
sage: R(3).integral().parent()
Univariate Polynomial Ring in x over Rational Field
```

Why do we get a different parent for zero?

Paul


---

Comment by zimmerma created at 2012-03-26 16:00:34

Changing status from needs_review to needs_info.


---

Attachment


---

Comment by AlexGhitza created at 2012-03-26 21:46:19

Ah, that's because the degree of R(0) is negative.  Sorry.  It's fixed in the new patch, and I've added `R(0).integral().parent()` to the doctests.


---

Comment by AlexGhitza created at 2012-03-26 21:46:19

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2012-03-27 11:41:00

I get only one doctest failure, but it also fails with vanilla sage-5.0.beta10 and seems
unrelated:

```
sage -t  "devel/sage-7711/sage/misc/sagedoc.py"             

**********************************************************************
File "/localdisk/tmp/sage-5.0.beta10/devel/sage-7711/sage/misc/sagedoc.py", line 566:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /localdisk/tmp/sage-5.0.beta10/devel/sage/doc/output/html/de/tutorial
...
```


This patch not only fixes the original issue, but improves the coherence of Sage results.
Good job Alex!

Paul


---

Comment by zimmerma created at 2012-03-27 11:41:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-02 15:23:49

Resolution: fixed
