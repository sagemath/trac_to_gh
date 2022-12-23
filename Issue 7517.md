# Issue 7517: improve documentation of xgcd command

Issue created by migration from https://trac.sagemath.org/ticket/7517

Original creator: was

Original creation time: 2009-11-23 06:47:33

Assignee: AlexGhitza


```


On Sun, Nov 22, 2009 at 4:57 PM, Ricky Farr <> wrote:
> Dear All,
>
> I'd like to sincerely thank you for your help before hand.  I'm having
> some issues that need to be straightened out.  I was under the
> impression that xgcd(a,b) returned (g,s,t) so that g = s*a + t*b,
> where g=gcd(a,b).  Please review the following code, and tell me why
> this happens:
>
> sage: Q.<x> = PolynomialRing(ZZ);
> sage: gcd(x-2,x^3+2*x^2);
> 1
> sage: g,s,t = xgcd(x-2,x^3+2*x^2);
> sage: g
> 16
> sage: s*(x-2)+t*(x^3+2*x^2)
> 16
>
> I was under the impression, like I said that g would have been equal
> to 1.  Why is g, 16?

The ring ZZ[x] is not a principal ideal domain (e.g., the ideal (2, x) isn't principal), so xgcd *can't* in general return polynomials s, t such that g = s*a+t*b.    A simple example is a=2*x and b=x^2. Then x is the gcd, but you can't write x as a ZZ[x] linear combination of 2*x and x^2, since the linear term of s*(2*x) + t*x^2 is even. 


What it does return is the next best thing, which is s, t such that 

   s*a + t*b = resultant(a,b), 

assuming a, b are coprime (if they aren't, rescale so they are, do the above, then multiply through). 

Note that Sage just calls the FLINT library, and this behavior of xgcd is documented there. 

I did just maybe (?) find a bug in FLINT though (and certainly one in sage):
sage: gcd(Q(2),x^2)
1
sage: xgcd(Q(2),x^2)
<hang forever> 

Doing the same using NTL works fine:
sage: Q.<x> = PolynomialRing(ZZ,implementation="NTL")
sage: type(x)
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
sage: gcd(Q(2),x^2)
1
sage: xgcd(Q(2),x^2)
(4, 2, 0)
sage: xgcd(x-2, x^3+2*x^2)
(16, -x^2 - 4*x - 8, 1)

--

So, the docs in Sage need to change to correctly define xgcd over a non-PID.  Also, there is maybe a serious bug in FLINT. 

 -- William
```



---

Comment by was created at 2009-11-23 07:00:34

I'm making the xgcd *hang* another ticket: #7518


---

Comment by was created at 2009-11-23 07:00:34

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2009-12-08 09:52:44

Changing keywords from "" to "xgcd docstring".


---

Comment by AlexGhitza created at 2009-12-08 09:52:44

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2009-12-09 02:51:44

Resolution: fixed
