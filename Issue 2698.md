# Issue 2698: [with patch, needs review] Small improvements to integer lcm, gcd on lists and a new xlcm function

archive/issues_002698.json:
```json
{
    "body": "Assignee: somebody\n\nThe patch does the following:\n\n* gcd of a list returns as soon as the current gcd is 1\n* gcd and lcm of empty lists return 1 as a Sage Integer not a python integer\n* gcd and lcm of lists of length 1 apply abs():  before, we had\n\n\n```\nsage: l=(-3,)\nsage: lcm(l)\n-3\nsage: gcd(l)\n-3\n```\n\n\nwhile now we have\n\n```\nsage: l=(-3,)\nsage: lcm(l)\n3\nsage: gcd(l)\n3\n```\n\n\n* A new extended xlcm funtion has been added to sage/rings/arith.py.  Under the name tidy_lcm() this has been stuck in sage/schemes/elliptic_curves/sll_finite_field.py but I moved it and renamed it since I need it for work I am doing on a whole lot of generic group algorithms.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2698\n\n",
    "created_at": "2008-03-28T12:21:13Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Small improvements to integer lcm, gcd on lists and a new xlcm function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2698",
    "user": "cremona"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2698





---

archive/issue_comments_018594.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-28T12:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18594",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_018595.json:
```json
{
    "body": "I don't know why the patch is not viewable.  It was based on 2.11.alpha1.",
    "created_at": "2008-03-28T12:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18595",
    "user": "cremona"
}
```

I don't know why the patch is not viewable.  It was based on 2.11.alpha1.



---

archive/issue_comments_018596.json:
```json
{
    "body": "Replying to [comment:1 cremona]:\n> I don't know why the patch is not viewable.  It was based on 2.11.alpha1.\n\nHi John,\n\nthe patch is only visible if the parent is in the repo on sagemath.org. That is 2.10.4 right now, so the parent is probably in 2.11.alpha0 or later.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T12:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18596",
    "user": "mabshoff"
}
```

Replying to [comment:1 cremona]:
> I don't know why the patch is not viewable.  It was based on 2.11.alpha1.

Hi John,

the patch is only visible if the parent is in the repo on sagemath.org. That is 2.10.4 right now, so the parent is probably in 2.11.alpha0 or later.

Cheers,

Michael



---

archive/issue_comments_018597.json:
```json
{
    "body": "Hi Michael,\n\nThat's right, I based it on 2.11.alpha1.\n\nShall I repost a patch based on 2.10.4?\n\nJohn",
    "created_at": "2008-03-28T12:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18597",
    "user": "cremona"
}
```

Hi Michael,

That's right, I based it on 2.11.alpha1.

Shall I repost a patch based on 2.10.4?

John



---

archive/issue_comments_018598.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> Hi Michael,\n> \n> That's right, I based it on 2.11.alpha1.\n> \n> Shall I repost a patch based on 2.10.4?\n> \n> John\n\nNah, since the download works I think it isn't too much of a burden to review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T12:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18598",
    "user": "mabshoff"
}
```

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

archive/issue_comments_018599.json:
```json
{
    "body": "Attachment\n\napply after 9029.patch",
    "created_at": "2008-03-28T15:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18599",
    "user": "AlexGhitza"
}
```

Attachment

apply after 9029.patch



---

archive/issue_comments_018600.json:
```json
{
    "body": "Looks mostly good, but:\n\nI got a bunch of doctest failures in a variety of places.  They seem to be due to the line g = v[0].abs() in !__GCD_list, since v[0] is sometimes a Python int and so does not have an abs() method: for an example, try sage -t schemes/generic/algebraic_scheme.py, although there's a handful of other places this comes up.\n\nAnother failure comes from rings/polynomial/multi_polynomial_libsingular.pyx, where one can find the doctest\n\n\n```\nsage: GCD([x^3 - 3*x + 2, x^4 - 1, x^6 -1])\n```\n\n\nThis now fails because v[0] is a polynomial, so it does not have an abs() method.\n\nI have fixed these things in the patch 9029-2.patch as follows: if it's possible to coerce v[0] into Z, do that and take its abs(), otherwise just work with v[0] as before.\n\nI have run sage -t * and everything seems fine, so unless John disagrees with my fix we should merge this.",
    "created_at": "2008-03-28T15:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18600",
    "user": "AlexGhitza"
}
```

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

archive/issue_comments_018601.json:
```json
{
    "body": "Hi Alex, thanks for checking this.\n\nHere's an alternative suggestion which I thought of just after uploading the patch.\n\n\n\n```\ndef __GCD_list(v):\n     \"\"\"\n    EXAMPLES:\n        sage: l = ()\n        sage: gcd(l)\n        0\n        sage: gcd(srange(10))\n        1\n        sage: X=polygen(QQ)\n        sage: gcd((2*X+4,2*X^2,2))\n        1\n        sage: X=polygen(ZZ)\n        sage: gcd((2*X+4,2*X^2,2))\n        2\n    \"\"\"\n    if len(v) == 0:\n        return integer_ring.ZZ(0)\n    g = v[0].parent()(0)\n    for vi in v:\n        g = GCD(g, vi)\n        if g == 1: return g\n    return g\n```\n\n\nSurely any type for which this function makes sense will allow 0 to be coerced into the parent?\n***actually no -- in the doctests above, gcd(range(10)) fails since the items in range(10) are python ints.  So that would again need a special case.  I think you might know how to test for that case?\n\nNote also that (1) the value returned for an empty list is ZZ(0) and not ZZ(1) as before which was stupid;  in this case we have no parent structure anyway, and I guess that ZZ(0)  can be coerced into anything.  And (2) the way it is coded now, the first pairwise gcd done is gcd(0,v[0]) rather than gcd(v[0],v[0]).  Also this way we don't need to use abs() since we can assume that the pairwise gcd function does whatever normalization is appropriate.",
    "created_at": "2008-03-28T16:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18601",
    "user": "cremona"
}
```

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

archive/issue_comments_018602.json:
```json
{
    "body": "Attachment\n\napply after 9029.patch, instead of 9029-2.patch",
    "created_at": "2008-03-28T17:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18602",
    "user": "cremona"
}
```

Attachment

apply after 9029.patch, instead of 9029-2.patch



---

archive/issue_comments_018603.json:
```json
{
    "body": "The patch 8964.patch should be added after 9029.patch and *instead* of 9029-2.patch.",
    "created_at": "2008-03-28T17:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18603",
    "user": "cremona"
}
```

The patch 8964.patch should be added after 9029.patch and *instead* of 9029-2.patch.



---

archive/issue_comments_018604.json:
```json
{
    "body": "Attachment\n\nApply after previous patch",
    "created_at": "2008-03-28T17:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18604",
    "user": "cremona"
}
```

Attachment

Apply after previous patch



---

archive/issue_comments_018605.json:
```json
{
    "body": "Extra patch 8965.patch further improves lcm of lists, after more testing, and adds doctests.\n\nNote: I still do not know why this works:\n\n```\nsage: R.<X>=QQ[]\nsage: lcm(X-1,X+1)\nX^2 - 1\n```\n\n\nbut this fails:\n\n```\nsage: R.<X>=QQ[]\nsage: lcm((X-1,X+1))\n```\n\n\nbut I have spent enough time on this for one day and I think a new pair of eyes is needed.",
    "created_at": "2008-03-28T17:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18605",
    "user": "cremona"
}
```

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

archive/issue_comments_018606.json:
```json
{
    "body": "OK, I just looked at 8965.patch.  It breaks doctests in two places: coding/code_constructions.py and modules/free_module_element.pyx\n\nI don't have time to look at this in detail right now, but the issue seems to be undesired interactions between the lcm code in arith.py and lcm methods elsewhere in Sage.  This means, in particular, that the problem is either in arith.py, or in the corresponding lcm methods but hasn't been noticed until now.",
    "created_at": "2008-03-28T23:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18606",
    "user": "AlexGhitza"
}
```

OK, I just looked at 8965.patch.  It breaks doctests in two places: coding/code_constructions.py and modules/free_module_element.pyx

I don't have time to look at this in detail right now, but the issue seems to be undesired interactions between the lcm code in arith.py and lcm methods elsewhere in Sage.  This means, in particular, that the problem is either in arith.py, or in the corresponding lcm methods but hasn't been noticed until now.



---

archive/issue_comments_018607.json:
```json
{
    "body": "The problem in free_module_element.pyx is that it calls LCM([+Infinity, +Infinity, +Infinity]).\n\nIn code_constructions.py, there is something that amounts to\n\n```\nsage: FF.<a> = GF(3^2,\"a\")                                                                                                       \nsage: x = PolynomialRing(FF,\"x\").gen()                                                                                           \nsage: L = [b.minpoly() for b in [a,a^2,a^3]]\nsage: L\n[x^2 + 2*x + 2, x^2 + 1, x^2 + 2*x + 2]\nsage: LCM(L)\nBoom!\n```\n",
    "created_at": "2008-03-29T13:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18607",
    "user": "AlexGhitza"
}
```

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

archive/issue_comments_018608.json:
```json
{
    "body": "Apply INSTEAD of all previous patches!",
    "created_at": "2008-03-30T17:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18608",
    "user": "cremona"
}
```

Apply INSTEAD of all previous patches!



---

archive/issue_comments_018609.json:
```json
{
    "body": "Attachment\n\nThe new patch 9114.patch should be applied INSTEAD of all the earlier ones since it includes the earlier changes plus a couple of tweaks so that it passes all tests with 2.11.rc0.  [NB this patch is based on 2.11.rc0.]\n\nHere's how I fixed the two problems:\n* in free_module_element.py I added a test so that if any of the elements has additive_order +Infinity then it returns +Infinity right away without calling lcm() at all.  This is also more efficient!\n* to get around the code_constructions.py problem I just changed the order of the lcm in arith.py.  This makes current tests pass but reveals another bug (*not* caused by this patch!):\n`lcm(p,q)` fails if p and q are polynomials and p is constant.  I have reported this in another ticket.",
    "created_at": "2008-03-30T17:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18609",
    "user": "cremona"
}
```

Attachment

The new patch 9114.patch should be applied INSTEAD of all the earlier ones since it includes the earlier changes plus a couple of tweaks so that it passes all tests with 2.11.rc0.  [NB this patch is based on 2.11.rc0.]

Here's how I fixed the two problems:
* in free_module_element.py I added a test so that if any of the elements has additive_order +Infinity then it returns +Infinity right away without calling lcm() at all.  This is also more efficient!
* to get around the code_constructions.py problem I just changed the order of the lcm in arith.py.  This makes current tests pass but reveals another bug (*not* caused by this patch!):
`lcm(p,q)` fails if p and q are polynomials and p is constant.  I have reported this in another ticket.



---

archive/issue_comments_018610.json:
```json
{
    "body": "Attachment\n\ntrivial fixes, apply after 9114.patch",
    "created_at": "2008-04-01T02:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18610",
    "user": "AlexGhitza"
}
```

Attachment

trivial fixes, apply after 9114.patch



---

archive/issue_comments_018611.json:
```json
{
    "body": "John,\n\nGood work fixing all of this!  Everything looks fine, except for one minor glitch: line 1082 of arith.py should be\n\nsage: LCM([1,2,3,4,5])\n\ninstead of\n\nsage: LCM([1,2,3,4,5/3])\n\nThere was also a trivial typo in the docstring for lcm.\n\nSince everything else was great and these things were trivial to fix, I did that and put up a small patch 9114-typos.patch.",
    "created_at": "2008-04-01T02:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18611",
    "user": "AlexGhitza"
}
```

John,

Good work fixing all of this!  Everything looks fine, except for one minor glitch: line 1082 of arith.py should be

sage: LCM([1,2,3,4,5])

instead of

sage: LCM([1,2,3,4,5/3])

There was also a trivial typo in the docstring for lcm.

Since everything else was great and these things were trivial to fix, I did that and put up a small patch 9114-typos.patch.



---

archive/issue_comments_018612.json:
```json
{
    "body": "I'm quite happy with your extra patch.  Thanks!",
    "created_at": "2008-04-01T08:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18612",
    "user": "cremona"
}
```

I'm quite happy with your extra patch.  Thanks!



---

archive/issue_comments_018613.json:
```json
{
    "body": "Yes, with the patches pass the doctests pass for me. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T14:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18613",
    "user": "mabshoff"
}
```

Yes, with the patches pass the doctests pass for me. 

Cheers,

Michael



---

archive/issue_comments_018614.json:
```json
{
    "body": "Merged 9114.patch and 9114-typos.patch in Sage 3.0.alpha0",
    "created_at": "2008-04-01T14:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18614",
    "user": "mabshoff"
}
```

Merged 9114.patch and 9114-typos.patch in Sage 3.0.alpha0



---

archive/issue_comments_018615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T14:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2698#issuecomment-18615",
    "user": "mabshoff"
}
```

Resolution: fixed
