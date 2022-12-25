# Issue 9646: Incorrect calculation of elliptic curve formal group law

archive/issues_009646.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @categorie\n\nKeywords: elliptic curve formal group law\n\nIf `F(t1, t2)` is a formal group law, then `F(t1, t2) = t1 + t2 (mod t1*t2)`.  So in particular, the coefficients of `t1^i` and `t2^i` are zero for all `i > 1`.  However the formal group law of an elliptic curve as returned by Sage includes (at least) the terms `-a1<sup>2*t1</sup>3` and `-a1<sup>2*t2</sup>2`, as the following example shows:\n\n```\nsage: P.<a1, a2, a3, a4, a6> = PolynomialRing(ZZ, 5)\nsage: E = EllipticCurve(list(P.gens()))\nsage: F = E.formal().group_law(prec = 4)\nsage: t2 = F.parent().gen()\nsage: t1 = F.parent().base_ring().gen()\nsage: F(t1, 0)\nt1 - a1^2*t1^3   # should be t1\nsage: F(0, t2)\nt2 - a1^2*t2^3\n```\n\nNote also that the coefficient of `t1^2*t2 + t1*t2^2` returned by sage is `-a1^2 - a2`, whereas, according to Silverman AEC IV.1, it should be simply `-a2`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9646\n\n",
    "created_at": "2010-07-30T15:06:26Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Incorrect calculation of elliptic curve formal group law",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9646",
    "user": "https://github.com/unzvfu"
}
```
Assignee: @JohnCremona

CC:  @categorie

Keywords: elliptic curve formal group law

If `F(t1, t2)` is a formal group law, then `F(t1, t2) = t1 + t2 (mod t1*t2)`.  So in particular, the coefficients of `t1^i` and `t2^i` are zero for all `i > 1`.  However the formal group law of an elliptic curve as returned by Sage includes (at least) the terms `-a1<sup>2*t1</sup>3` and `-a1<sup>2*t2</sup>2`, as the following example shows:

```
sage: P.<a1, a2, a3, a4, a6> = PolynomialRing(ZZ, 5)
sage: E = EllipticCurve(list(P.gens()))
sage: F = E.formal().group_law(prec = 4)
sage: t2 = F.parent().gen()
sage: t1 = F.parent().base_ring().gen()
sage: F(t1, 0)
t1 - a1^2*t1^3   # should be t1
sage: F(0, t2)
t2 - a1^2*t2^3
```

Note also that the coefficient of `t1^2*t2 + t1*t2^2` returned by sage is `-a1^2 - a2`, whereas, according to Silverman AEC IV.1, it should be simply `-a2`.

Issue created by migration from https://trac.sagemath.org/ticket/9646





---

archive/issue_comments_093371.json:
```json
{
    "body": "Added my Sage version and system info.",
    "created_at": "2010-07-30T15:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93371",
    "user": "https://github.com/unzvfu"
}
```

Added my Sage version and system info.



---

archive/issue_comments_093372.json:
```json
{
    "body": "The bug appears to be related to the precision in a regular way:\n\n```\nsage: for prec in srange(4, 7):\n....: E = EllipticCurve(list(P.gens()))\n....: F = E.formal_group()\n....: fg = F.group_law(prec)\n....: print prec, fg(0, fg.parent().gen())\n....: \n4 t2 - a1^2*t2^3\n5 t2 + (-a1^3 - a1*a2)*t2^4\n6 t2 + (-a1^4 - 2*a1^2*a2 - a1*a3)*t2^5\n```\n\nNote that the error is always of degree one less than the precision.  This might be related to the following issue, whereby the calculation dies when the precision is set to 2 or 3:\n\n```\nsage: E = EllipticCurve(list(P.gens()))\nsage: F = E.formal_group()\nsage: fg = F.group_law(2)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/hlaw/Dropbox/phd/thesis/<ipython console> in <module>()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in group_law(self, prec)\n    524         t3 = -t1 - t2 - \\\n    525              (a1*lam + a3*lam2 + a2*nu + 2*a4*lam*nu + 3*a6*lam2*nu)/  \\\n--> 526              (1 + a2*lam + a4*lam2 + a6*lam3)\n    527         inv = self.inverse(prec)\n    528 \n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()\n\nTypeError: unsupported operand parent(s) for '-': 'Power Series Ring in t2 over Power Series Ring in t1 over Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring' and 'Power Series Ring in t1 over Fraction Field of Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring'\nsage: fg = F.group_law(3)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/hlaw/Dropbox/phd/thesis/<ipython console> in <module>()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in group_law(self, prec)\n    524         t3 = -t1 - t2 - \\\n    525              (a1*lam + a3*lam2 + a2*nu + 2*a4*lam*nu + 3*a6*lam2*nu)/  \\\n--> 526              (1 + a2*lam + a4*lam2 + a6*lam3)\n    527         inv = self.inverse(prec)\n    528 \n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()\n\n/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()\n\nTypeError: unsupported operand parent(s) for '-': 'Power Series Ring in t2 over Power Series Ring in t1 over Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring' and 'Power Series Ring in t1 over Fraction Field of Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring'\n```\n",
    "created_at": "2010-07-30T16:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93372",
    "user": "https://github.com/unzvfu"
}
```

The bug appears to be related to the precision in a regular way:

```
sage: for prec in srange(4, 7):
....: E = EllipticCurve(list(P.gens()))
....: F = E.formal_group()
....: fg = F.group_law(prec)
....: print prec, fg(0, fg.parent().gen())
....: 
4 t2 - a1^2*t2^3
5 t2 + (-a1^3 - a1*a2)*t2^4
6 t2 + (-a1^4 - 2*a1^2*a2 - a1*a3)*t2^5
```

Note that the error is always of degree one less than the precision.  This might be related to the following issue, whereby the calculation dies when the precision is set to 2 or 3:

```
sage: E = EllipticCurve(list(P.gens()))
sage: F = E.formal_group()
sage: fg = F.group_law(2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/hlaw/Dropbox/phd/thesis/<ipython console> in <module>()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in group_law(self, prec)
    524         t3 = -t1 - t2 - \
    525              (a1*lam + a3*lam2 + a2*nu + 2*a4*lam*nu + 3*a6*lam2*nu)/  \
--> 526              (1 + a2*lam + a4*lam2 + a6*lam3)
    527         inv = self.inverse(prec)
    528 

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '-': 'Power Series Ring in t2 over Power Series Ring in t1 over Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring' and 'Power Series Ring in t1 over Fraction Field of Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring'
sage: fg = F.group_law(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/hlaw/Dropbox/phd/thesis/<ipython console> in <module>()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in group_law(self, prec)
    524         t3 = -t1 - t2 - \
    525              (a1*lam + a3*lam2 + a2*nu + 2*a4*lam*nu + 3*a6*lam2*nu)/  \
--> 526              (1 + a2*lam + a4*lam2 + a6*lam3)
    527         inv = self.inverse(prec)
    528 

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:11073)()

/Users/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6966)()

TypeError: unsupported operand parent(s) for '-': 'Power Series Ring in t2 over Power Series Ring in t1 over Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring' and 'Power Series Ring in t1 over Fraction Field of Multivariate Polynomial Ring in a1, a2, a3, a4, a6 over Integer Ring'
```




---

archive/issue_comments_093373.json:
```json
{
    "body": "There was indeed a precision error in the code and the patch that I attach should fix that. This is quite a bad bug as ALL the computations with formal groups happen to be wrong...",
    "created_at": "2010-11-14T16:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93373",
    "user": "https://github.com/categorie"
}
```

There was indeed a precision error in the code and the patch that I attach should fix that. This is quite a bad bug as ALL the computations with formal groups happen to be wrong...



---

archive/issue_comments_093374.json:
```json
{
    "body": "Attachment [trac_9646.patch](tarball://root/attachments/some-uuid/ticket9646/trac_9646.patch) by @categorie created at 2010-11-14 16:37:27\n\nexported against 4.6",
    "created_at": "2010-11-14T16:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93374",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9646.patch](tarball://root/attachments/some-uuid/ticket9646/trac_9646.patch) by @categorie created at 2010-11-14 16:37:27

exported against 4.6



---

archive/issue_comments_093375.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-14T16:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93375",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093376.json:
```json
{
    "body": "... and now to the other thing. As I played around with this, I found that I get different results than the [Errata](http://www.math.brown.edu/~jhs/AEC/AECErrata.pdf) of [Silverman](http://books.google.co.uk/books?id=Z90CA_EUCCkC&lpg=PR1&ots=3K8lmtWd1a&dq=silverman%20arithmetic%20of%20elliptic%20curves&pg=PA120#v=onepage&q&f=false). So I had to dig a little deeper and I found that the formula in Silverman are not correct.\n\nHere is an example. Let E be the elliptic curve `y^2 + y = x^3+1` Because `a1=a2=0`, the formula in the middle of page 120 of Silverman tells us that\n\n`F(t,t) = [2](t) = 2*t + t^4 + ... `\n\nBut I claim that it should be `2*t -7*t^4`. Here is an example. \n\n\n```\nsage: K = Qp(43,5)\nsage: E = EllipticCurve(K,[0,0,1,0,1])\nsage: Q = E(-779/43^2,-125945/43^3)\nsage: tQ =-Q[0]/Q[1]\nsage: tQ\n24*43 + 4*43^2 + 32*43^3 + 41*43^4 + 34*43^5 + O(43^6)\n```\n\n\nso the point lies in the formal group. We use the multiplication law on the curve and find\n\n```\nsage: ttwoQ = -(2*Q)[0]/(2*Q)[1]\nsage: ttwoQ\n5*43 + 9*43^2 + 21*43^3 + 38*43^4 + 37*43^5 + O(43^6)\n```\n\n\n\n```\nsage: sage: 2*tQ +tQ^4\n5*43 + 9*43^2 + 21*43^3 + 28*43^4 + 37*43^5 + O(43^6)\nsage: sage: 2*tQ -7*tQ^4\n5*43 + 9*43^2 + 21*43^3 + 38*43^4 + 37*43^5 + O(43^6)\n```\n\n\nshows that -7 is correct. I have added a docstring in `mult_by_n` to illustrate that our formula is correct, because this function is computed without using `group_law` if the base ring is a field of char 0 (instead it uses the multiplication on the curve). \n\nIn fact, the error appears as a sign error in the formula for `z_3`. The corrected formula should read\n\n`F(z_1,z_2) = z_1+z_2 -a_1 z_1z_2 -a_2(z_1^2 z_2+z_1 z_2^2) - 2a_3 z_1^3 z_2 +(a_1 a_2-3 a_3) z_1^2 z_2^2 - 2a_3 z_1 z_2^3 + ...`",
    "created_at": "2010-11-14T16:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93376",
    "user": "https://github.com/categorie"
}
```

... and now to the other thing. As I played around with this, I found that I get different results than the [Errata](http://www.math.brown.edu/~jhs/AEC/AECErrata.pdf) of [Silverman](http://books.google.co.uk/books?id=Z90CA_EUCCkC&lpg=PR1&ots=3K8lmtWd1a&dq=silverman%20arithmetic%20of%20elliptic%20curves&pg=PA120#v=onepage&q&f=false). So I had to dig a little deeper and I found that the formula in Silverman are not correct.

Here is an example. Let E be the elliptic curve `y^2 + y = x^3+1` Because `a1=a2=0`, the formula in the middle of page 120 of Silverman tells us that

`F(t,t) = [2](t) = 2*t + t^4 + ... `

But I claim that it should be `2*t -7*t^4`. Here is an example. 


```
sage: K = Qp(43,5)
sage: E = EllipticCurve(K,[0,0,1,0,1])
sage: Q = E(-779/43^2,-125945/43^3)
sage: tQ =-Q[0]/Q[1]
sage: tQ
24*43 + 4*43^2 + 32*43^3 + 41*43^4 + 34*43^5 + O(43^6)
```


so the point lies in the formal group. We use the multiplication law on the curve and find

```
sage: ttwoQ = -(2*Q)[0]/(2*Q)[1]
sage: ttwoQ
5*43 + 9*43^2 + 21*43^3 + 38*43^4 + 37*43^5 + O(43^6)
```



```
sage: sage: 2*tQ +tQ^4
5*43 + 9*43^2 + 21*43^3 + 28*43^4 + 37*43^5 + O(43^6)
sage: sage: 2*tQ -7*tQ^4
5*43 + 9*43^2 + 21*43^3 + 38*43^4 + 37*43^5 + O(43^6)
```


shows that -7 is correct. I have added a docstring in `mult_by_n` to illustrate that our formula is correct, because this function is computed without using `group_law` if the base ring is a field of char 0 (instead it uses the multiplication on the curve). 

In fact, the error appears as a sign error in the formula for `z_3`. The corrected formula should read

`F(z_1,z_2) = z_1+z_2 -a_1 z_1z_2 -a_2(z_1^2 z_2+z_1 z_2^2) - 2a_3 z_1^3 z_2 +(a_1 a_2-3 a_3) z_1^2 z_2^2 - 2a_3 z_1 z_2^3 + ...`



---

archive/issue_comments_093377.json:
```json
{
    "body": "I suggest that you write to Silverman, since he likes to keep his errata up to date!  And add something in the docstring here to explain why you use a formula different from that in Silverman.",
    "created_at": "2010-11-14T17:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93377",
    "user": "https://github.com/JohnCremona"
}
```

I suggest that you write to Silverman, since he likes to keep his errata up to date!  And add something in the docstring here to explain why you use a formula different from that in Silverman.



---

archive/issue_comments_093378.json:
```json
{
    "body": "Yes, I was typing my email as you wrote that :-). and yes, it is a good idea to add a comment in the code.",
    "created_at": "2010-11-14T17:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93378",
    "user": "https://github.com/categorie"
}
```

Yes, I was typing my email as you wrote that :-). and yes, it is a good idea to add a comment in the code.



---

archive/issue_comments_093379.json:
```json
{
    "body": "to be applied after the first patch",
    "created_at": "2010-11-14T17:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93379",
    "user": "https://github.com/categorie"
}
```

to be applied after the first patch



---

archive/issue_comments_093380.json:
```json
{
    "body": "Attachment [trac_9646_2.patch](tarball://root/attachments/some-uuid/ticket9646/trac_9646_2.patch) by @loefflerd created at 2010-12-16 12:07:21",
    "created_at": "2010-12-16T12:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93380",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9646_2.patch](tarball://root/attachments/some-uuid/ticket9646/trac_9646_2.patch) by @loefflerd created at 2010-12-16 12:07:21



---

archive/issue_comments_093381.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-16T12:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93381",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093382.json:
```json
{
    "body": "Is there a reason the milestone is sage-5.0?",
    "created_at": "2011-01-23T20:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93382",
    "user": "https://github.com/jdemeyer"
}
```

Is there a reason the milestone is sage-5.0?



---

archive/issue_comments_093383.json:
```json
{
    "body": "No, this can go in asap.",
    "created_at": "2011-01-23T21:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93383",
    "user": "https://github.com/categorie"
}
```

No, this can go in asap.



---

archive/issue_events_009782.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-26T22:26:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9646#event-9782"
}
```



---

archive/issue_comments_093384.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-26T22:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9646#issuecomment-93384",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
