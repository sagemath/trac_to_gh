# Issue 1785: bug in creating points on elliptic curves over extension fields

Issue created by migration from https://trac.sagemath.org/ticket/1785

Original creator: was

Original creation time: 2008-01-15 19:10:31

Assignee: was

CC:  alexghitza


```


On Jan 15, 2008 10:25 AM, John Cremona <john.cremona@gmail.com> wrote:
> 
> I like Robert's suggestion.  If the user wants n independent generic
> points, construct a large enough field (transcendence degree n) to
> contain them.
> 
> A useful change Magma made relatively recently (a couple of years or
> so ago) was to aloow points on an elliptic curve to have coordinates
> in an extension of the base field of the curve -- as one would when
> working mathematically.  e.g. given a curve defined over QQ you can
> define points on E(K) for e.g. K=a number field, or K=a function field
> (such as the function field of E, to get a generic point).  Of course,
> these points "know" what their curve is so you can do point arithmetic
> on them and so on.
> 
> I don't see why this should be workable in Sage too (maybe it is
> already?  if so I will retire shame-faced from the discussion...)

It's sort of half-way there.  You can do:

sage: K.<a> = NumberField(x^2 + x - (3^3-3))
sage: E = EllipticCurve('37a')
sage: X = E(K)

but stupidly X is wrong:

sage: X
Abelian group of points on Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

though:

sage: X.domain()
Spectrum of Number Field in a with defining polynomial x^2 + x - 24

However, 

sage: P = X([3,a]);
boom with a TypeError

So this obviously needs work.  In fact, this counts as a bug.

```



---

Attachment


---

Comment by AlexGhitza created at 2008-09-07 07:30:12

See the patch (made against 3.1.2.rc0).


---

Comment by cremona created at 2008-09-08 18:57:14

Review:  Amazing 2-line fix!  Patch applies fine and all doctests in sage.schemes.elliptic_curves pass.  This will be very useful.


---

Comment by mabshoff created at 2008-09-08 20:21:39

Resolution: fixed


---

Comment by mabshoff created at 2008-09-08 20:21:39

Merged in Sage 3.1.2.rc1
