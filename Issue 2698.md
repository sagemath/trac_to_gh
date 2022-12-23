# Issue 2698: [with patch, needs review] Small improvements to integer lcm, gcd on lists and a new xlcm function

Issue created by migration from https://trac.sagemath.org/ticket/2698

Original creator: cremona

Original creation time: 2008-03-28 12:21:13

Assignee: somebody

The patch does the following:

   * gcd of a list returns as soon as the current gcd is 1
   * gcd and lcm of empty lists return 1 as a Sage Integer not a python integer
   * gcd and lcm of lists of length 1 apply abs():  before, we had


```
sage: l=(-3,)
sage: lcm(l)
-3
sage: gcd(l)
-3
```


while now we have

```
sage: l=(-3,)
sage: lcm(l)
3
sage: gcd(l)
3
```


   * A new extended xlcm funtion has been added to sage/rings/arith.py.  Under the name tidy_lcm() this has been stuck in sage/schemes/elliptic_curves/sll_finite_field.py but I moved it and renamed it since I need it for work I am doing on a whole lot of generic group algorithms.



---

Attachment


---

Comment by cremona created at 2008-03-28 12:25:50

I don't know why the patch is not viewable.  It was based on 2.11.alpha1.


---

Comment by mabshoff created at 2008-03-28 12:40:43

Replying to [comment:1 cremona]:
> I don't know why the patch is not viewable.  It was based on 2.11.alpha1.

Hi John,

the patch is only visible if the parent is in the repo on sagemath.org. That is 2.10.4 right now, so the parent is probably in 2.11.alpha0 or later.

Cheers,

Michael


---

Comment by cremona created at 2008-03-28 12:47:44

Hi Michael,

That's right, I based it on 2.11.alpha1.

Shall I repost a patch based on 2.10.4?

John


---

Comment by mabshoff created at 2008-03-28 12:54:54

Replying to [comment:3 cremona]:
> Hi Michael,
> 
> That's right, I based it on 2.11.alpha1.
> 
> Shall I repost a patch based on 2.10.4?
> 
> John

Nah, since the download works I think it isn't too much of a burden to review.

Cheers,

Michael


---

Attachment

apply after 9029.patch


---

Comment by AlexGhitza created at 2008-03-28 15:59:49

Looks mostly good, but:

I got a bunch of doctest failures in a variety of places.  They seem to be due to the line g = v[0].abs() in !__GCD_list, since v[0] is sometimes a Python int and so does not have an abs() method: for an example, try sage -t schemes/generic/algebraic_scheme.py, although there's a handful of other places this comes up.

Another failure comes from rings/polynomial/multi_polynomial_libsingular.pyx, where one can find the doctest


```
sage: GCD([x^3 - 3*x + 2, x^4 - 1, x^6 -1])
```


This now fails because v[0] is a polynomial, so it does not have an abs() method.

I have fixed these things in the patch 9029-2.patch as follows: if it's possible to coerce v[0] into Z, do that and take its abs(), otherwise just work with v[0] as before.

I have run sage -t * and everything seems fine, so unless John disagrees with my fix we should merge this.


---

Comment by cremona created at 2008-03-28 16:35:58

Hi Alex, thanks for checking this.

Here's an alternative suggestion which I thought of just after uploading the patch.



```
def __GCD_list(v):
     """
    EXAMPLES:
        sage: l = ()
        sage: gcd(l)
        0
        sage: gcd(srange(10))
        1
        sage: X=polygen(QQ)
        sage: gcd((2*X+4,2*X^2,2))
        1
        sage: X=polygen(ZZ)
        sage: gcd((2*X+4,2*X^2,2))
        2
    """
    if len(v) == 0:
        return integer_ring.ZZ(0)
    g = v[0].parent()(0)
    for vi in v:
        g = GCD(g, vi)
        if g == 1: return g
    return g
```


Surely any type for which this function makes sense will allow 0 to be coerced into the parent?
***actually no -- in the doctests above, gcd(range(10)) fails since the items in range(10) are python ints.  So that would again need a special case.  I think you might know how to test for that case?

Note also that (1) the value returned for an empty list is ZZ(0) and not ZZ(1) as before which was stupid;  in this case we have no parent structure anyway, and I guess that ZZ(0)  can be coerced into anything.  And (2) the way it is coded now, the first pairwise gcd done is gcd(0,v[0]) rather than gcd(v[0],v[0]).  Also this way we don't need to use abs() since we can assume that the pairwise gcd function does whatever normalization is appropriate.


---

Attachment

apply after 9029.patch, instead of 9029-2.patch


---

Comment by cremona created at 2008-03-28 17:04:18

The patch 8964.patch should be added after 9029.patch and *instead* of 9029-2.patch.


---

Attachment

Apply after previous patch


---

Comment by cremona created at 2008-03-28 17:47:36

Extra patch 8965.patch further improves lcm of lists, after more testing, and adds doctests.

Note: I still do not know why this works:

```
sage: R.<X>=QQ[]
sage: lcm(X-1,X+1)
X^2 - 1
```


but this fails:

```
sage: R.<X>=QQ[]
sage: lcm((X-1,X+1))
```


but I have spent enough time on this for one day and I think a new pair of eyes is needed.


---

Comment by AlexGhitza created at 2008-03-28 23:04:34

OK, I just looked at 8965.patch.  It breaks doctests in two places: coding/code_constructions.py and modules/free_module_element.pyx

I don't have time to look at this in detail right now, but the issue seems to be undesired interactions between the lcm code in arith.py and lcm methods elsewhere in Sage.  This means, in particular, that the problem is either in arith.py, or in the corresponding lcm methods but hasn't been noticed until now.


---

Comment by AlexGhitza created at 2008-03-29 13:51:57

The problem in free_module_element.pyx is that it calls LCM([+Infinity, +Infinity, +Infinity]).

In code_constructions.py, there is something that amounts to

```
sage: FF.<a> = GF(3^2,"a")                                                                                                       
sage: x = PolynomialRing(FF,"x").gen()                                                                                           
sage: L = [b.minpoly() for b in [a,a^2,a^3]]
sage: L
[x^2 + 2*x + 2, x^2 + 1, x^2 + 2*x + 2]
sage: LCM(L)
Boom!
```



---

Comment by cremona created at 2008-03-30 17:47:51

Apply INSTEAD of all previous patches!


---

Attachment

The new patch 9114.patch should be applied INSTEAD of all the earlier ones since it includes the earlier changes plus a couple of tweaks so that it passes all tests with 2.11.rc0.  [NB this patch is based on 2.11.rc0.]

Here's how I fixed the two problems:
   * in free_module_element.py I added a test so that if any of the elements has additive_order +Infinity then it returns +Infinity right away without calling lcm() at all.  This is also more efficient!
   * to get around the code_constructions.py problem I just changed the order of the lcm in arith.py.  This makes current tests pass but reveals another bug (*not* caused by this patch!):
`lcm(p,q)` fails if p and q are polynomials and p is constant.  I have reported this in another ticket.


---

Attachment

trivial fixes, apply after 9114.patch


---

Comment by AlexGhitza created at 2008-04-01 02:38:10

John,

Good work fixing all of this!  Everything looks fine, except for one minor glitch: line 1082 of arith.py should be

sage: LCM([1,2,3,4,5])

instead of

sage: LCM([1,2,3,4,5/3])

There was also a trivial typo in the docstring for lcm.

Since everything else was great and these things were trivial to fix, I did that and put up a small patch 9114-typos.patch.


---

Comment by cremona created at 2008-04-01 08:25:02

I'm quite happy with your extra patch.  Thanks!


---

Comment by mabshoff created at 2008-04-01 14:05:26

Yes, with the patches pass the doctests pass for me. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 14:05:49

Merged 9114.patch and 9114-typos.patch in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 14:05:49

Resolution: fixed
