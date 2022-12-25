# Issue 7644: generic power series reversion

archive/issues_007644.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  fwclarke\n\nMake the following work over any base ring:\n\n```\nsage: R.<x> = QQ[[]]\nsage: f = 1/(1-x) - 1; f\nx + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11 + x^12\n+ x^13 + x^14 + x^15 + x^16 + x^17 + x^18 + x^19 + O(x^20)\nsage: g = f.reversion(); g\nx - x^2 + x^3 - x^4 + x^5 - x^6 + x^7 - x^8 + x^9 - x^10 + x^11 - x^12\n+ x^13 - x^14 + x^15 - x^16 + x^17 - x^18 + x^19 + O(x^20)\nsage: f(g)\nx + O(x^20)\n```\n\n\nMatt Bainbridge says about power series reversion, which uses pari in some cases, and maybe isn't there in others:\n\n```\nIts easy enough to code this in sage.  This seems to work over any\nfield:\n\n\ndef ps_inverse(f):\n   if f.prec() is infinity:\n       raise ValueError, \"series must have finite precision for\nreversion\"\n   if f.valuation() != 1:\n       raise ValueError, \"series must have valuation one for\nreversion\"\n   t = parent(f).gen()\n   a = 1/f.coefficients()[0]\n   g = a*t\n   for i in range(2, f.prec()):\n       g -=  ps_coefficient((f + O(t^(i+1)))(g),i)*a*t^i\n   g += O(t^f.prec())\n   return g\n\ndef ps_coefficient(f,i):\n   if i >= f.prec():\n       raise ValueError, \"that coefficient is undefined\"\n   else:\n       return f.padded_list(f.prec())[i]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7644\n\n",
    "created_at": "2009-12-09T20:20:14Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "generic power series reversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7644",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  fwclarke

Make the following work over any base ring:

```
sage: R.<x> = QQ[[]]
sage: f = 1/(1-x) - 1; f
x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11 + x^12
+ x^13 + x^14 + x^15 + x^16 + x^17 + x^18 + x^19 + O(x^20)
sage: g = f.reversion(); g
x - x^2 + x^3 - x^4 + x^5 - x^6 + x^7 - x^8 + x^9 - x^10 + x^11 - x^12
+ x^13 - x^14 + x^15 - x^16 + x^17 - x^18 + x^19 + O(x^20)
sage: f(g)
x + O(x^20)
```


Matt Bainbridge says about power series reversion, which uses pari in some cases, and maybe isn't there in others:

```
Its easy enough to code this in sage.  This seems to work over any
field:


def ps_inverse(f):
   if f.prec() is infinity:
       raise ValueError, "series must have finite precision for
reversion"
   if f.valuation() != 1:
       raise ValueError, "series must have valuation one for
reversion"
   t = parent(f).gen()
   a = 1/f.coefficients()[0]
   g = a*t
   for i in range(2, f.prec()):
       g -=  ps_coefficient((f + O(t^(i+1)))(g),i)*a*t^i
   g += O(t^f.prec())
   return g

def ps_coefficient(f,i):
   if i >= f.prec():
       raise ValueError, "that coefficient is undefined"
   else:
       return f.padded_list(f.prec())[i]
```


Issue created by migration from https://trac.sagemath.org/ticket/7644





---

archive/issue_comments_065217.json:
```json
{
    "body": "Lagrange inversion is significantly faster.  With\n\n```\ndef ps_inverse_Lagrange(f):\n   if f.valuation() != 1:\n       raise ValueError, \"series must have valuation one for reversion\"\n   if f.prec() is infinity:\n       raise ValueError, \"series must have finite precision for reversion\"\n   t = parent(f).gen()\n   h = t/f\n   k = 1\n   g = 0\n   for i in range(1, f.prec()):\n       k *= h\n       g += (1/i)*ps_coefficient(k, i - 1)*t^i\n   g += O(t^f.prec())\n   return g\n```\n\nI found\n\n```\nsage: R.<x> = QQ[[]]\nsage: f = exp(x) - 1\nsage: timeit('ps_inverse(f)')\n5 loops, best of 3: 552 ms per loop\nsage: timeit('ps_inverse_Lagrange(f)')\n5 loops, best of 3: 74 ms per loop\n```\n",
    "created_at": "2009-12-10T10:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65217",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Lagrange inversion is significantly faster.  With

```
def ps_inverse_Lagrange(f):
   if f.valuation() != 1:
       raise ValueError, "series must have valuation one for reversion"
   if f.prec() is infinity:
       raise ValueError, "series must have finite precision for reversion"
   t = parent(f).gen()
   h = t/f
   k = 1
   g = 0
   for i in range(1, f.prec()):
       k *= h
       g += (1/i)*ps_coefficient(k, i - 1)*t^i
   g += O(t^f.prec())
   return g
```

I found

```
sage: R.<x> = QQ[[]]
sage: f = exp(x) - 1
sage: timeit('ps_inverse(f)')
5 loops, best of 3: 552 ms per loop
sage: timeit('ps_inverse_Lagrange(f)')
5 loops, best of 3: 74 ms per loop
```




---

archive/issue_comments_065218.json:
```json
{
    "body": "\n```\nThe code doesn't quite run, since it references some other function\n(ps_coefficient); here's an updated version which uses only built-in\nfunctions:\n\ndef ps_inverse_Lagrange(f):\n  if f.valuation() != 1:\n      raise ValueError, \"series must have valuation one for\nreversion\"\n  if f.prec() is infinity:\n      raise ValueError, \"series must have finite precision for\nreversion\"\n  t = parent(f).gen()\n  h = t/f\n  k = 1\n  g = 0\n  for i in range(1, f.prec()):\n      k *= h\n      g += (1/i)*k.padded_list(i)[i - 1]*t^i\n  g += O(t^f.prec())\n  return g\n```\n",
    "created_at": "2009-12-25T18:09:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65218",
    "user": "https://github.com/williamstein"
}
```


```
The code doesn't quite run, since it references some other function
(ps_coefficient); here's an updated version which uses only built-in
functions:

def ps_inverse_Lagrange(f):
  if f.valuation() != 1:
      raise ValueError, "series must have valuation one for
reversion"
  if f.prec() is infinity:
      raise ValueError, "series must have finite precision for
reversion"
  t = parent(f).gen()
  h = t/f
  k = 1
  g = 0
  for i in range(1, f.prec()):
      k *= h
      g += (1/i)*k.padded_list(i)[i - 1]*t^i
  g += O(t^f.prec())
  return g
```




---

archive/issue_comments_065219.json:
```json
{
    "body": "What should we do with power series with coefficients in, say, ZZ?  Raise an error, or return a power series over the fraction field?",
    "created_at": "2010-01-29T11:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65219",
    "user": "https://github.com/aghitza"
}
```

What should we do with power series with coefficients in, say, ZZ?  Raise an error, or return a power series over the fraction field?



---

archive/issue_comments_065220.json:
```json
{
    "body": "Replying to [comment:4 AlexGhitza]:\n> What should we do with power series with coefficients in, say, ZZ?  Raise an error, or return a power series over the fraction field?\n\nIn general, return a power series over the fraction field.  But if the leading coefficient is a unit, then despite the fact that Lagrange inversion involves division, the inverse series has coefficients in the same ring as the original series.  E.g., with the function defined in [comment:3 was],\n\n```\nsage: PS.<t> = ZZ[[]]\nsage: f = t + t^2 + O(t^10)\nsage: ps_inverse_Lagrange(f)\nt - t^2 + 2*t^3 - 5*t^4 + 14*t^5 - 42*t^6 + 132*t^7 - 429*t^8 + 1430*t^9 + O(t^10)\n```\n\nthough\n\n```\nsage: ps_inverse_Lagrange(f).parent()\nPower Series Ring in t over Rational Field\n```\n\nOver a ring of finite characteristic, to use Lagrange inversion, you have to lift to a ring of characteristic zero, invert, and then project down to the original ring.",
    "created_at": "2010-01-30T10:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65220",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:4 AlexGhitza]:
> What should we do with power series with coefficients in, say, ZZ?  Raise an error, or return a power series over the fraction field?

In general, return a power series over the fraction field.  But if the leading coefficient is a unit, then despite the fact that Lagrange inversion involves division, the inverse series has coefficients in the same ring as the original series.  E.g., with the function defined in [comment:3 was],

```
sage: PS.<t> = ZZ[[]]
sage: f = t + t^2 + O(t^10)
sage: ps_inverse_Lagrange(f)
t - t^2 + 2*t^3 - 5*t^4 + 14*t^5 - 42*t^6 + 132*t^7 - 429*t^8 + 1430*t^9 + O(t^10)
```

though

```
sage: ps_inverse_Lagrange(f).parent()
Power Series Ring in t over Rational Field
```

Over a ring of finite characteristic, to use Lagrange inversion, you have to lift to a ring of characteristic zero, invert, and then project down to the original ring.



---

archive/issue_comments_065221.json:
```json
{
    "body": "I've uploaded a patch which implements ps_inverse_Lagrange from above.  For simplicity, I didn't implement over rings of positive characteristic, or in the case that the leading coefficient is not a unit.  Instead, I included examples of changing the base ring and carrying out the reversion there.\n\nNote:  the line\n\n```\ng += (1/i)*k....\n```\n\ngave me some trouble, since I didn't realize .pyx files use python's integer division; someone who understands the implicit conversions between sage and python might want to check I dealt with that correctly.  It now reads:\n\n```\ng += k.padded_list(i)[i - 1]/i*t**i\n```\n\nand works fine in all my tests.",
    "created_at": "2010-07-08T19:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65221",
    "user": "https://github.com/nilesjohnson"
}
```

I've uploaded a patch which implements ps_inverse_Lagrange from above.  For simplicity, I didn't implement over rings of positive characteristic, or in the case that the leading coefficient is not a unit.  Instead, I included examples of changing the base ring and carrying out the reversion there.

Note:  the line

```
g += (1/i)*k....
```

gave me some trouble, since I didn't realize .pyx files use python's integer division; someone who understands the implicit conversions between sage and python might want to check I dealt with that correctly.  It now reads:

```
g += k.padded_list(i)[i - 1]/i*t**i
```

and works fine in all my tests.



---

archive/issue_comments_065222.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-08T19:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65222",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065223.json:
```json
{
    "body": "Changing keywords from \"\" to \"lagrange, reversion\".",
    "created_at": "2010-08-01T16:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65223",
    "user": "https://github.com/nilesjohnson"
}
```

Changing keywords from "" to "lagrange, reversion".



---

archive/issue_comments_065224.json:
```json
{
    "body": "Replying to [comment:2 fwclarke]:\n\nHi Francis,\n\nYou may be interested in reviewing this patch since it's based on your code.  I believe it will be an easy review.\n\nbest,\nNiles",
    "created_at": "2010-08-01T16:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65224",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:2 fwclarke]:

Hi Francis,

You may be interested in reviewing this patch since it's based on your code.  I believe it will be an easy review.

best,
Niles



---

archive/issue_comments_065225.json:
```json
{
    "body": "The latest version of this patch applies cleanly to sage 4.6.1.alpha2 and passes all (-long) doctests.  It also adds `power_series_poly` to the sage documentation, and makes some minor changes so that all documentation builds cleanly.",
    "created_at": "2010-11-30T19:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65225",
    "user": "https://github.com/nilesjohnson"
}
```

The latest version of this patch applies cleanly to sage 4.6.1.alpha2 and passes all (-long) doctests.  It also adds `power_series_poly` to the sage documentation, and makes some minor changes so that all documentation builds cleanly.



---

archive/issue_comments_065226.json:
```json
{
    "body": "I've been looking at this.  One concern is that for power series with rational coefficients the existing method using pari is a great deal faster, so that at least in this case the pari method should be retained.  Strangely the existing method fails for integer power series, though pari handles them perfectly ok.\n\nOn investigation it turns out that it is the conversion to pari which is failing and that this problem is pointed out in modular/overconvergent/genus0.py, and raised as #4376. \u00a0I have produced a short patch (awaiting review) which extends the range of base rings over which pari conversion of a power series is possible.\n\nWhat I propose then is that a revised patch (depending on the #4376 patch) should try to use pari and that only if this fails should the Lagrange inversion code be used. \u00a0\u00a0\n\nI also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.",
    "created_at": "2010-11-30T21:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65226",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

I've been looking at this.  One concern is that for power series with rational coefficients the existing method using pari is a great deal faster, so that at least in this case the pari method should be retained.  Strangely the existing method fails for integer power series, though pari handles them perfectly ok.

On investigation it turns out that it is the conversion to pari which is failing and that this problem is pointed out in modular/overconvergent/genus0.py, and raised as #4376.  I have produced a short patch (awaiting review) which extends the range of base rings over which pari conversion of a power series is possible.

What I propose then is that a revised patch (depending on the #4376 patch) should try to use pari and that only if this fails should the Lagrange inversion code be used.   

I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.



---

archive/issue_comments_065227.json:
```json
{
    "body": "apply only this patch; tries to use pari first, then falls back to Lagrange inversion",
    "created_at": "2010-12-01T02:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65227",
    "user": "https://github.com/nilesjohnson"
}
```

apply only this patch; tries to use pari first, then falls back to Lagrange inversion



---

archive/issue_comments_065228.json:
```json
{
    "body": "Attachment [trac_7644_reversion_lagrange_3.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_3.patch) by @nilesjohnson created at 2010-12-01 02:44:53\n\nReplying to [comment:10 fwclarke]:\n> I've been looking at this.  \n\nThanks!\n\n> One concern is that for power series with rational coefficients the existing method using pari is a great deal faster, so that at least in this case the pari method should be retained.  \n\nYes, especially if there is work in progress to support converting more rings to pari.  I wrote a revised patch which first attempts to convert to pari and do reversion there, and then tries the Lagrange inversion if conversion to pari fails.  I think that implementation means that this patch can be independent of #4376 -- it will simply perform better when that patch is included.\n\n\n> I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.  \n\nYes, upon further consideration I agree.  I've made this and two other improvements:\n\n1. Given a power series with infinite precision and degree `deg`, it's reversion is computed with precision `deg + 1`.\n2. Given a power series whose leading coefficient is not a unit, the code tries to pass to the fraction field of the base ring and compute the reversion there.\n3. Given a power series over a base ring of positive characteristic, the code tries to lift to a characteristic zero base (using `.lift()`), compute the reversion, and then push back down to the positive characteristic base.  This works over finite fields and `Zmod(n)`, but fails over a base ring like `Zmod(n)[x]`.\n\nEach of these is demonstrated with an example.",
    "created_at": "2010-12-01T02:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65228",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_7644_reversion_lagrange_3.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_3.patch) by @nilesjohnson created at 2010-12-01 02:44:53

Replying to [comment:10 fwclarke]:
> I've been looking at this.  

Thanks!

> One concern is that for power series with rational coefficients the existing method using pari is a great deal faster, so that at least in this case the pari method should be retained.  

Yes, especially if there is work in progress to support converting more rings to pari.  I wrote a revised patch which first attempts to convert to pari and do reversion there, and then tries the Lagrange inversion if conversion to pari fails.  I think that implementation means that this patch can be independent of #4376 -- it will simply perform better when that patch is included.


> I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.  

Yes, upon further consideration I agree.  I've made this and two other improvements:

1. Given a power series with infinite precision and degree `deg`, it's reversion is computed with precision `deg + 1`.
2. Given a power series whose leading coefficient is not a unit, the code tries to pass to the fraction field of the base ring and compute the reversion there.
3. Given a power series over a base ring of positive characteristic, the code tries to lift to a characteristic zero base (using `.lift()`), compute the reversion, and then push back down to the positive characteristic base.  This works over finite fields and `Zmod(n)`, but fails over a base ring like `Zmod(n)[x]`.

Each of these is demonstrated with an example.



---

archive/issue_comments_065229.json:
```json
{
    "body": "Is it sensible to remove the first 3 patches - if so, I can do so, as I have admin rights. \n\nHave all the results been verified by independent means? If so, it would be useful to state how. If not, then I personally don't agree with such \"tests\", but as a minimum it should be documented if the results have not been verified. \n\nAs for the actual maths, I can't review that - this is well outside my level of maths, since none of my degrees are in maths\n\nDave",
    "created_at": "2010-12-01T02:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65229",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Is it sensible to remove the first 3 patches - if so, I can do so, as I have admin rights. 

Have all the results been verified by independent means? If so, it would be useful to state how. If not, then I personally don't agree with such "tests", but as a minimum it should be documented if the results have not been verified. 

As for the actual maths, I can't review that - this is well outside my level of maths, since none of my degrees are in maths

Dave



---

archive/issue_comments_065230.json:
```json
{
    "body": "Replying to [comment:12 drkirkby]:\n> Is it sensible to remove the first 3 patches - if so, I can do so, as I have admin rights. \n\nSure; thanks :)\n\n> \n> Have all the results been verified by independent means? If so, it would be useful to state how. If not, then I personally don't agree with such \"tests\", but as a minimum it should be documented if the results have not been verified. \n\nThe verifications are performed by checking that `f(g)` and `g(f)` both return `x + O(x^prec)`.  Actually just one of these is necessary to determine the reversion of f, so I view this as two different methods for verifying the answer.\n\n> \n> As for the actual maths, I can't review that - this is well outside my level of maths, since none of my degrees are in maths\n\nThanks for checking into it :)",
    "created_at": "2010-12-01T13:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65230",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:12 drkirkby]:
> Is it sensible to remove the first 3 patches - if so, I can do so, as I have admin rights. 

Sure; thanks :)

> 
> Have all the results been verified by independent means? If so, it would be useful to state how. If not, then I personally don't agree with such "tests", but as a minimum it should be documented if the results have not been verified. 

The verifications are performed by checking that `f(g)` and `g(f)` both return `x + O(x^prec)`.  Actually just one of these is necessary to determine the reversion of f, so I view this as two different methods for verifying the answer.

> 
> As for the actual maths, I can't review that - this is well outside my level of maths, since none of my degrees are in maths

Thanks for checking into it :)



---

archive/issue_comments_065231.json:
```json
{
    "body": "Replying to [comment:11 niles]:\n\n> Yes, especially if there is work in progress to support converting more rings to pari.  I wrote a revised patch which first attempts to convert to pari and do reversion there, and then tries the Lagrange inversion if conversion to pari fails.  I think that implementation means that this patch can be independent of #4376 -- it will simply perform better when that patch is included.\n\nA good point (but it would be nice if #4376 could be reviewed; it's very short).\n\n> > I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.\n> Yes, upon further consideration I agree.  I've made this and two other improvements:  1. Given a power series with infinite precision and degree `deg`, its reversion is computed with precision `deg + 1`.\n\nI don't see the logic for this.  I would suggest having a keyword `precision` with default `None`, and replacing\n\n\n```\n    if f.prec() is infinity:\n        out_prec = f.degree() + 1\n        f = f.add_bigoh(out_prec)\n    else:\n        out_prec = f.prec()\n```\n\nwith\n\n\n```\n    if f.prec() is infinity and precision is None:\n        precision = f.parent().default_prec()\n    if precision:\n        f = f.add_bigoh(precision)\n```\n\nThen one could do (to get some Catalan numbers):\n\n\n```\nsage: R.<x> = QQ[[]]\nsage: (x - x^2).reversion()\nx + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 \n+ 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 \n+ 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 \n+ 129644790*x^18 + 477638700*x^19 + O(x^20)\n```\n\nor\n\n\n```\nsage: (x - x^2).reversion(precision=8)\nx + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + O(x^8)\n```\n\nrather than\n\n\n```\nsage: (x - x^2).reversion()\nx + x^2 + O(x^3)\n```\n",
    "created_at": "2010-12-01T21:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65231",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:11 niles]:

> Yes, especially if there is work in progress to support converting more rings to pari.  I wrote a revised patch which first attempts to convert to pari and do reversion there, and then tries the Lagrange inversion if conversion to pari fails.  I think that implementation means that this patch can be independent of #4376 -- it will simply perform better when that patch is included.

A good point (but it would be nice if #4376 could be reviewed; it's very short).

> > I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.
> Yes, upon further consideration I agree.  I've made this and two other improvements:  1. Given a power series with infinite precision and degree `deg`, its reversion is computed with precision `deg + 1`.

I don't see the logic for this.  I would suggest having a keyword `precision` with default `None`, and replacing


```
    if f.prec() is infinity:
        out_prec = f.degree() + 1
        f = f.add_bigoh(out_prec)
    else:
        out_prec = f.prec()
```

with


```
    if f.prec() is infinity and precision is None:
        precision = f.parent().default_prec()
    if precision:
        f = f.add_bigoh(precision)
```

Then one could do (to get some Catalan numbers):


```
sage: R.<x> = QQ[[]]
sage: (x - x^2).reversion()
x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 
+ 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 
+ 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 
+ 129644790*x^18 + 477638700*x^19 + O(x^20)
```

or


```
sage: (x - x^2).reversion(precision=8)
x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + O(x^8)
```

rather than


```
sage: (x - x^2).reversion()
x + x^2 + O(x^3)
```




---

archive/issue_comments_065232.json:
```json
{
    "body": "apply only this patch; choice for default precision improved",
    "created_at": "2010-12-02T17:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65232",
    "user": "https://github.com/nilesjohnson"
}
```

apply only this patch; choice for default precision improved



---

archive/issue_comments_065233.json:
```json
{
    "body": "Attachment [trac_7644_reversion_lagrange_4.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_4.patch) by @nilesjohnson created at 2010-12-02 17:06:12\n\nReplying to [comment:14 fwclarke]:\n> Replying to [comment:11 niles]:\n> \n\n> A good point (but it would be nice if #4376 could be reviewed; it's very short).\n\nagreed -- I'll add it to my list\n\n> I don't see the logic for this.  I would suggest ...\n\nthat's a better idea; it's implemented in the new patch",
    "created_at": "2010-12-02T17:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65233",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_7644_reversion_lagrange_4.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_4.patch) by @nilesjohnson created at 2010-12-02 17:06:12

Replying to [comment:14 fwclarke]:
> Replying to [comment:11 niles]:
> 

> A good point (but it would be nice if #4376 could be reviewed; it's very short).

agreed -- I'll add it to my list

> I don't see the logic for this.  I would suggest ...

that's a better idea; it's implemented in the new patch



---

archive/issue_comments_065234.json:
```json
{
    "body": "This is looking good.  Some comments on the docstring:\n\n\n```\nIf f has infinite precision, then the precision \nof the reversion defaults to the default precision of \n``f.parent()``. \n```\n\nshould say \"unless precision is set\", or words to that effect.\n\nThe remark a few lines later that\n\n\n```\nself must have finite precision (i.e. this cannot be done \nfor polynomials).  \n```\n\nis no longer appropriate.  Nor is\n\n\n```\nUnder the current implementation, the leading \ncoefficient must be a unit in the base ring, and the base ring must \nhave characteristic zero. \n```\n\nI'm not sure that\n\n\n```\nIn positive characteristic, attempt first to lift to characteristic \nzero and perform the reversion there:\n```\n\nis in the right place; it's really to do with the algorithm.  Perhaps  better to say here that the function can handle some base rings of non-zero characteristic.",
    "created_at": "2010-12-02T18:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65234",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

This is looking good.  Some comments on the docstring:


```
If f has infinite precision, then the precision 
of the reversion defaults to the default precision of 
``f.parent()``. 
```

should say "unless precision is set", or words to that effect.

The remark a few lines later that


```
self must have finite precision (i.e. this cannot be done 
for polynomials).  
```

is no longer appropriate.  Nor is


```
Under the current implementation, the leading 
coefficient must be a unit in the base ring, and the base ring must 
have characteristic zero. 
```

I'm not sure that


```
In positive characteristic, attempt first to lift to characteristic 
zero and perform the reversion there:
```

is in the right place; it's really to do with the algorithm.  Perhaps  better to say here that the function can handle some base rings of non-zero characteristic.



---

archive/issue_comments_065235.json:
```json
{
    "body": "Replying to [comment:16 fwclarke]:\n> This is looking good.  Some comments on the docstring:\n> \n\n...\n\nSorry for not catching these before; fixed now.",
    "created_at": "2010-12-04T17:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65235",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:16 fwclarke]:
> This is looking good.  Some comments on the docstring:
> 

...

Sorry for not catching these before; fixed now.



---

archive/issue_comments_065236.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-17T09:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65236",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065237.json:
```json
{
    "body": "This is fine now, except for one little thing.  In the patch file, the line\n\n\n```\n+        most ``f.prec()).  If f has infinite precision, and the argument\n```\n\nshould read\n\n\n```\n+        most ``f.prec())``.  If ``f`` has infinite precision, and the argument\n```\n",
    "created_at": "2010-12-17T09:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65237",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

This is fine now, except for one little thing.  In the patch file, the line


```
+        most ``f.prec()).  If f has infinite precision, and the argument
```

should read


```
+        most ``f.prec())``.  If ``f`` has infinite precision, and the argument
```




---

archive/issue_comments_065238.json:
```json
{
    "body": "Thanks for catching that -- fixed now.",
    "created_at": "2010-12-17T11:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65238",
    "user": "https://github.com/nilesjohnson"
}
```

Thanks for catching that -- fixed now.



---

archive/issue_comments_065239.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-17T11:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65239",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065240.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-17T12:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65240",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065241.json:
```json
{
    "body": "Now it's perfect. Positive review.",
    "created_at": "2010-12-17T12:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65241",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Now it's perfect. Positive review.



---

archive/issue_comments_065242.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-13T06:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65242",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_065243.json:
```json
{
    "body": "You should change the commit message of the patch (use `hg qrefresh -e` for that).  Make sure you include the ticket number.",
    "created_at": "2011-01-13T06:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65243",
    "user": "https://github.com/jdemeyer"
}
```

You should change the commit message of the patch (use `hg qrefresh -e` for that).  Make sure you include the ticket number.



---

archive/issue_comments_065244.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2011-01-13T12:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65244",
    "user": "https://github.com/nilesjohnson"
}
```

apply only this patch



---

archive/issue_comments_065245.json:
```json
{
    "body": "Attachment [trac_7644_reversion_lagrange_5.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_5.patch) by @nilesjohnson created at 2011-01-13 12:02:45\n\ndone.",
    "created_at": "2011-01-13T12:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65245",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_7644_reversion_lagrange_5.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_5.patch) by @nilesjohnson created at 2011-01-13 12:02:45

done.



---

archive/issue_comments_065246.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T12:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65246",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T13:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65247",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065248.json:
```json
{
    "body": "commit message ok now",
    "created_at": "2011-01-13T13:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65248",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

commit message ok now



---

archive/issue_comments_065249.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-19T01:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65249",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_065250.json:
```json
{
    "body": "There are some formatting errors in the docstrings (a `::` should be followed by indented code, there are some places where this is violated).  I can fix these, but later.",
    "created_at": "2011-01-19T01:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65250",
    "user": "https://github.com/jdemeyer"
}
```

There are some formatting errors in the docstrings (a `::` should be followed by indented code, there are some places where this is violated).  I can fix these, but later.



---

archive/issue_comments_065251.json:
```json
{
    "body": "My apologies -- I'll upload a fixed version soon.",
    "created_at": "2011-01-19T12:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65251",
    "user": "https://github.com/nilesjohnson"
}
```

My apologies -- I'll upload a fixed version soon.



---

archive/issue_comments_065252.json:
```json
{
    "body": "Attachment [trac_7644_reversion_lagrange_6.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_6.patch) by @nilesjohnson created at 2011-01-19 13:24:56\n\napply only this patch",
    "created_at": "2011-01-19T13:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65252",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_7644_reversion_lagrange_6.patch](tarball://root/attachments/some-uuid/ticket7644/trac_7644_reversion_lagrange_6.patch) by @nilesjohnson created at 2011-01-19 13:24:56

apply only this patch



---

archive/issue_comments_065253.json:
```json
{
    "body": "The documentation issue is fixed now -- all documentation builds without warnings.",
    "created_at": "2011-01-19T13:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65253",
    "user": "https://github.com/nilesjohnson"
}
```

The documentation issue is fixed now -- all documentation builds without warnings.



---

archive/issue_comments_065254.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T13:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65254",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065255.json:
```json
{
    "body": "Replying to [comment:27 niles]:\n> The documentation issue is fixed now -- all documentation builds without warnings.\nAgreed.",
    "created_at": "2011-01-19T16:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65255",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:27 niles]:
> The documentation issue is fixed now -- all documentation builds without warnings.
Agreed.



---

archive/issue_comments_065256.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T16:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65256",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7644#issuecomment-65257",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
