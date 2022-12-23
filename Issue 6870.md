# Issue 6870: [with patch, needs review] Bug in binomial

archive/issues_006870.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: binomial\n\nHere are two cases where binomial fails. I think it is not\nproperly converting its arguments to Integers in all cases where\nit should.\n\n\n```\nsage: binomial(1/2,1/1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/hakan/.sage/temp/joker/27910/_home_hakan__sage_init_sage_0.py in <module>()\n\n/media/megadisk/sage-4.1.1/local/lib/python2.6/site-packages/sage/rings/arith.py in binomial(x, m)\n   2602             except AttributeError:\n   2603                 pass\n-> 2604             raise TypeError, 'Either m or x-m must be an integer'\n   2605     if isinstance(x, (int, long, integer.Integer)):\n   2606         if x >= 0 and (m < 0 or m > x):\n\nTypeError: Either m or x-m must be an integer\n```\n\n\n\n```\nsage: binomial(10^20+1/1,10^20) \n---------------------------------------------------------------------------\nOverflowError                             Traceback (most recent call last)\n\n/home/hakan/.sage/temp/joker/27910/_home_hakan__sage_init_sage_0.py in <module>()\n\n/media/megadisk/sage-4.1.1/local/lib/python2.6/site-packages/sage/rings/arith.py in binomial(x, m)\n   2625         from sage.functions.all import gamma\n   2626         return gamma(x+1)/gamma(P(m+1))/gamma(x-m+1)\n-> 2627     return misc.prod([x-i for i in xrange(m)]) / P(factorial(m))\n   2628 \n   2629 def multinomial(*ks):\n\nOverflowError: long int too large to convert to int\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6870\n\n",
    "created_at": "2009-09-02T20:20:20Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] Bug in binomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6870",
    "user": "hgranath"
}
```
Assignee: somebody

Keywords: binomial

Here are two cases where binomial fails. I think it is not
properly converting its arguments to Integers in all cases where
it should.


```
sage: binomial(1/2,1/1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/hakan/.sage/temp/joker/27910/_home_hakan__sage_init_sage_0.py in <module>()

/media/megadisk/sage-4.1.1/local/lib/python2.6/site-packages/sage/rings/arith.py in binomial(x, m)
   2602             except AttributeError:
   2603                 pass
-> 2604             raise TypeError, 'Either m or x-m must be an integer'
   2605     if isinstance(x, (int, long, integer.Integer)):
   2606         if x >= 0 and (m < 0 or m > x):

TypeError: Either m or x-m must be an integer
```



```
sage: binomial(10^20+1/1,10^20) 
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/hakan/.sage/temp/joker/27910/_home_hakan__sage_init_sage_0.py in <module>()

/media/megadisk/sage-4.1.1/local/lib/python2.6/site-packages/sage/rings/arith.py in binomial(x, m)
   2625         from sage.functions.all import gamma
   2626         return gamma(x+1)/gamma(P(m+1))/gamma(x-m+1)
-> 2627     return misc.prod([x-i for i in xrange(m)]) / P(factorial(m))
   2628 
   2629 def multinomial(*ks):

OverflowError: long int too large to convert to int
```



Issue created by migration from https://trac.sagemath.org/ticket/6870





---

archive/issue_comments_056699.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-02T20:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56699",
    "user": "hgranath"
}
```

Attachment



---

archive/issue_comments_056700.json:
```json
{
    "body": "This is a good idea, and somewhat surprisingly it speeds up very small binomials without slowing down biggish ones.  However, it does seem to slow down symbolic binomials:\n\nBefore:\n\n```\nsage: timeit('binomial(100,10)')\n625 loops, best of 3: 21.9 \u00b5s per loop\nsage: timeit('binomial(10^7,252525)')\n5 loops, best of 3: 1.35 s per loop\nsage: timeit('binomial(2*n,n)')\n625 loops, best of 3: 60.3 \u00b5s per loop\nsage: timeit('binomial(n+1,n)')\n625 loops, best of 3: 78.4 \u00b5s per loop\n```\n\n\nAfter:\n\n```\nsage: timeit('binomial(100,10)')\n625 loops, best of 3: 18.9 \u00b5s per loop\nsage: sage: timeit('binomial(10^7,252525)')\n5 loops, best of 3: 1.34 s per loop\nsage: timeit('binomial(2*n,n)')\n625 loops, best of 3: 76.2 \u00b5s per loop\nsage: timeit('binomial(n+1,n)')\n625 loops, best of 3: 137 \u00b5s per loop\n```\n\n\nI imagine that in some applications with a lot of symbolic stuff that could be a problem, but I'm not sure.  Is it possible to put a catch in for expressions that would keep things more or less as they were there, without making the numeric ones much slower?",
    "created_at": "2009-09-14T20:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56700",
    "user": "kcrisman"
}
```

This is a good idea, and somewhat surprisingly it speeds up very small binomials without slowing down biggish ones.  However, it does seem to slow down symbolic binomials:

Before:

```
sage: timeit('binomial(100,10)')
625 loops, best of 3: 21.9 µs per loop
sage: timeit('binomial(10^7,252525)')
5 loops, best of 3: 1.35 s per loop
sage: timeit('binomial(2*n,n)')
625 loops, best of 3: 60.3 µs per loop
sage: timeit('binomial(n+1,n)')
625 loops, best of 3: 78.4 µs per loop
```


After:

```
sage: timeit('binomial(100,10)')
625 loops, best of 3: 18.9 µs per loop
sage: sage: timeit('binomial(10^7,252525)')
5 loops, best of 3: 1.34 s per loop
sage: timeit('binomial(2*n,n)')
625 loops, best of 3: 76.2 µs per loop
sage: timeit('binomial(n+1,n)')
625 loops, best of 3: 137 µs per loop
```


I imagine that in some applications with a lot of symbolic stuff that could be a problem, but I'm not sure.  Is it possible to put a catch in for expressions that would keep things more or less as they were there, without making the numeric ones much slower?



---

archive/issue_comments_056701.json:
```json
{
    "body": "I think to some extent this is a correctness vs speed issue. Before\nthe patch there is an asymmetry in the checking of whether m and x-m\nis in ZZ. So e.g. binomial(3/2,1/2) works while binomial(3/2,1/1)\nfails, although the documentation indicates they should be equivalent.\nFor me it was very confusing when something like that happened.\nThe benchmark case binomial(n+1,n) benefits from this asymmetry. I\nhave thought about it, but so far I have not found a satisfactory\nsolution which will not affect the speed of binomial(n+1,n) while\ndoing the right thing in other cases.\n\nThe other thing my patch is doing is to check more carefully if x is\nan integer. As noted this will be an improvement when this succeeds.\nApart from the above benchmarks, try e.g. binomial(QQ(10**7),252525) or\nbinomial(SR(10**7),252525) with and without the patch applied. This\npart of the patch however is not as important to me, a user could\nalways use binomial(ZZ(x),m) when beneficial. Hence an alternative\npatch is to just do the first part. This will decrease the speed\nregression in the symbolic case.",
    "created_at": "2009-09-16T03:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56701",
    "user": "hgranath"
}
```

I think to some extent this is a correctness vs speed issue. Before
the patch there is an asymmetry in the checking of whether m and x-m
is in ZZ. So e.g. binomial(3/2,1/2) works while binomial(3/2,1/1)
fails, although the documentation indicates they should be equivalent.
For me it was very confusing when something like that happened.
The benchmark case binomial(n+1,n) benefits from this asymmetry. I
have thought about it, but so far I have not found a satisfactory
solution which will not affect the speed of binomial(n+1,n) while
doing the right thing in other cases.

The other thing my patch is doing is to check more carefully if x is
an integer. As noted this will be an improvement when this succeeds.
Apart from the above benchmarks, try e.g. binomial(QQ(10**7),252525) or
binomial(SR(10**7),252525) with and without the patch applied. This
part of the patch however is not as important to me, a user could
always use binomial(ZZ(x),m) when beneficial. Hence an alternative
patch is to just do the first part. This will decrease the speed
regression in the symbolic case.



---

archive/issue_comments_056702.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-16T03:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56702",
    "user": "hgranath"
}
```

Attachment



---

archive/issue_comments_056703.json:
```json
{
    "body": "No, we should be able to compute the second type too, so don't jettison that.  But can't you combine the two?  Checking type is not so bad to do, and then you can still always try to coerce later.  After all, at the bottom there is a special case check for reals and floats.  So maybe you could do something like\n\n```\nif isinstance(m or x-m,whatever.rational):\n   convert to integer if possible\n```\n\n\nI did check, and the slowdown for symbolic ones is because of that check.  Checking for an instance takes about 1/10 the time.\n\n```\nsage: def f():\n....:     try:\n....:         m=ZZ(a)\n....:     except:\n....:         pass\n....:     \nsage: timeit('f()')\n625 loops, best of 3: 34.4 \u00b5s per loop\nsage: def g():\n....:     isinstance(a,(int,long,Integer))\n....:     \nsage: timeit('g()')\n625 loops, best of 3: 2.57 \u00b5s per loop\n```\n\nwhere a = n+1\n\nI guess the point is that we should definitely have as many correct answers as possible, but that the slowdown should be on these admittedly unusual cases with rationals, which are less likely to come up than the usual cases.",
    "created_at": "2009-09-16T14:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56703",
    "user": "kcrisman"
}
```

No, we should be able to compute the second type too, so don't jettison that.  But can't you combine the two?  Checking type is not so bad to do, and then you can still always try to coerce later.  After all, at the bottom there is a special case check for reals and floats.  So maybe you could do something like

```
if isinstance(m or x-m,whatever.rational):
   convert to integer if possible
```


I did check, and the slowdown for symbolic ones is because of that check.  Checking for an instance takes about 1/10 the time.

```
sage: def f():
....:     try:
....:         m=ZZ(a)
....:     except:
....:         pass
....:     
sage: timeit('f()')
625 loops, best of 3: 34.4 µs per loop
sage: def g():
....:     isinstance(a,(int,long,Integer))
....:     
sage: timeit('g()')
625 loops, best of 3: 2.57 µs per loop
```

where a = n+1

I guess the point is that we should definitely have as many correct answers as possible, but that the slowdown should be on these admittedly unusual cases with rationals, which are less likely to come up than the usual cases.



---

archive/issue_comments_056704.json:
```json
{
    "body": "But I have a problem then. In the situation where x is of type SR and\nm of type Integer, consider the cases x is n+1 (case A) and x is\nSR(10**7) (case B).\n\nTo handle these cases correctly they have to be treated differently,\nbut how to distinguish between them using fast checks like\n\"isinstance\" and similar if using \"try: ZZ(x)\" is not allowed because\nit will slow down case A?",
    "created_at": "2009-09-17T06:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56704",
    "user": "hgranath"
}
```

But I have a problem then. In the situation where x is of type SR and
m of type Integer, consider the cases x is n+1 (case A) and x is
SR(10**7) (case B).

To handle these cases correctly they have to be treated differently,
but how to distinguish between them using fast checks like
"isinstance" and similar if using "try: ZZ(x)" is not allowed because
it will slow down case A?



---

archive/issue_comments_056705.json:
```json
{
    "body": "Maybe this?\n\n```\nsage: var('n')\nn\nsage: a = n+1\nsage: from sage.symbolic.expression import Expression\nsage: isinstance(a,Expression)\nTrue\nsage: def g():\n....:     isinstance(a,Expression)\n....:     \nsage: timeit('g()')\n625 loops, best of 3: 573 ns per loop\nsage: a=SR(10**7)\nsage: timeit('g()')\n625 loops, best of 3: 595 ns per loop\nsage: timeit('f()')\n625 loops, best of 3: 1.59 \u00b5s per loop\n```\n\nYou can still use try: ZZ(x), it just makes sense to check type first, since it adds only nanoseconds, and then if someone is silly enough to use SR(10**7) instead of 10**7, they'll have to pay the microsecond penalty.  I jest a little, but I think you should try something like this to see if it would work.  If not, the first patch is probably better than allowing rational things to get through.  You could also add a check for rationals instead:\n\n```\nsage: from sage.rings.rational import Rational\nsage: def g():\n....:     isinstance(a,Rational)\n....:     \nsage: timeit('g()')\n625 loops, best of 3: 1.23 \u00b5s per loop\nsage: a = 10**7-1/1\nsage: type(a)\n<type 'sage.rings.rational.Rational'>\nsage: timeit('g()')\n625 loops, best of 3: 570 ns per loop\n```\n\nSo even if a isn't rational, you lose very little time by checking that before you coerce.",
    "created_at": "2009-09-17T13:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56705",
    "user": "kcrisman"
}
```

Maybe this?

```
sage: var('n')
n
sage: a = n+1
sage: from sage.symbolic.expression import Expression
sage: isinstance(a,Expression)
True
sage: def g():
....:     isinstance(a,Expression)
....:     
sage: timeit('g()')
625 loops, best of 3: 573 ns per loop
sage: a=SR(10**7)
sage: timeit('g()')
625 loops, best of 3: 595 ns per loop
sage: timeit('f()')
625 loops, best of 3: 1.59 µs per loop
```

You can still use try: ZZ(x), it just makes sense to check type first, since it adds only nanoseconds, and then if someone is silly enough to use SR(10**7) instead of 10**7, they'll have to pay the microsecond penalty.  I jest a little, but I think you should try something like this to see if it would work.  If not, the first patch is probably better than allowing rational things to get through.  You could also add a check for rationals instead:

```
sage: from sage.rings.rational import Rational
sage: def g():
....:     isinstance(a,Rational)
....:     
sage: timeit('g()')
625 loops, best of 3: 1.23 µs per loop
sage: a = 10**7-1/1
sage: type(a)
<type 'sage.rings.rational.Rational'>
sage: timeit('g()')
625 loops, best of 3: 570 ns per loop
```

So even if a isn't rational, you lose very little time by checking that before you coerce.



---

archive/issue_comments_056706.json:
```json
{
    "body": "If we want to fix only the rational case, that is of course easy to\ndo. I have two alternative new patches: one for doing just that, and\none which is basically my first patch but reworked to not affect the\ncase of floating point input (which was an undesired side effect).\n\nWith the QQ patch, it is unfortunately still easy to construct cases\nthat will fail: e.g. binomial(1/2,SR(1)),\nbinomial(SR(10**20+1),10**20) and binomial(SR(10**7+1),10**7) (the\nlast one takes a looong time).",
    "created_at": "2009-09-21T16:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56706",
    "user": "hgranath"
}
```

If we want to fix only the rational case, that is of course easy to
do. I have two alternative new patches: one for doing just that, and
one which is basically my first patch but reworked to not affect the
case of floating point input (which was an undesired side effect).

With the QQ patch, it is unfortunately still easy to construct cases
that will fail: e.g. binomial(1/2,SR(1)),
binomial(SR(10**20+1),10**20) and binomial(SR(10**7+1),10**7) (the
last one takes a looong time).



---

archive/issue_comments_056707.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-21T16:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56707",
    "user": "hgranath"
}
```

Attachment



---

archive/issue_comments_056708.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-21T16:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56708",
    "user": "hgranath"
}
```

Attachment



---

archive/issue_comments_056709.json:
```json
{
    "body": "I think you misunderstood.  My point is that one can ALSO do a check for symbolic expressions, as outlined above (that's what I meant by \"they'll have to pay the microsecond penalty\".  We can't catch every case, of course, but we might as well try to get the ones we know about.  \n\nI hope that these comments are not frustrating; this is overall a good fix to a non-critical but nonetheless important bug.",
    "created_at": "2009-09-21T16:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56709",
    "user": "kcrisman"
}
```

I think you misunderstood.  My point is that one can ALSO do a check for symbolic expressions, as outlined above (that's what I meant by "they'll have to pay the microsecond penalty".  We can't catch every case, of course, but we might as well try to get the ones we know about.  

I hope that these comments are not frustrating; this is overall a good fix to a non-critical but nonetheless important bug.



---

archive/issue_comments_056710.json:
```json
{
    "body": "I really have no idea what to do. So assume we have something like\n\n\n```\nif isinstance(x,Expression):\n```\n\n\nthen what to do? We have no idea at this point if x happens to be something\nlike SR(10**7) or n+1, and we will not know until we try x=ZZ(x). If\nthat try should fail, it is already too late to avoid the time penalty\nthat is the point of this discussion.",
    "created_at": "2009-09-21T17:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56710",
    "user": "hgranath"
}
```

I really have no idea what to do. So assume we have something like


```
if isinstance(x,Expression):
```


then what to do? We have no idea at this point if x happens to be something
like SR(10**7) or n+1, and we will not know until we try x=ZZ(x). If
that try should fail, it is already too late to avoid the time penalty
that is the point of this discussion.



---

archive/issue_comments_056711.json:
```json
{
    "body": "Replying to [comment:8 hgranath]:\n> I really have no idea what to do. So assume we have something like\n> \n> {{{\n> if isinstance(x,Expression):\n> }}}\n> \n> then what to do? We have no idea at this point if x happens to be something\n> like SR(10**7) or n+1, and we will not know until we try x=ZZ(x). If\n> that try should fail, it is already too late to avoid the time penalty\n> that is the point of this discussion.\n\nUnderstood; I think I didn't catch what the salient point was in your earlier comment, but now I do, and I agree that there is no easy way around it.  My apologies.  \n\nHere is my last idea.  I think that the .pyobject() method of Expression can catch this - because it returns an error for anything which is not a bare coefficient:\n\n```\nsage: def h():\n    try:\n        a.pyobject()\n        return ZZ(a)\n    except:\n            return a\nsage: a = n+1\nsage: h()\nn + 1\nsage: timeit('h()')\n625 loops, best of 3: 5.98 \u00b5s per loop\nsage: a = SR(10^7)\nsage: timeit('h()')\n625 loops, best of 3: 1.89 \u00b5s per loop\n```\n\nThe docstring confirms this performs as advertised.  If that doesn't speed things up, then I guess it's not possible :(\n\nSo if that doesn't work, your original solution stands as a definite improvement, with the changes you noted - put the rational check inside the already existing not isinstance(m, int etc.) check, before trying m = ZZ(m), do the floating point fix where you have it.  Oh yeah, be sure to add doctests for the SR(10**7) etc. \n\nBecause in the long run, we should have more correct cases, I think.  If someone notices a really bad slowdown, we will have to write a very fast symbolic binomial or something.  But all of these are an improvement on before.  Thanks for all of it!",
    "created_at": "2009-09-21T18:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56711",
    "user": "kcrisman"
}
```

Replying to [comment:8 hgranath]:
> I really have no idea what to do. So assume we have something like
> 
> {{{
> if isinstance(x,Expression):
> }}}
> 
> then what to do? We have no idea at this point if x happens to be something
> like SR(10**7) or n+1, and we will not know until we try x=ZZ(x). If
> that try should fail, it is already too late to avoid the time penalty
> that is the point of this discussion.

Understood; I think I didn't catch what the salient point was in your earlier comment, but now I do, and I agree that there is no easy way around it.  My apologies.  

Here is my last idea.  I think that the .pyobject() method of Expression can catch this - because it returns an error for anything which is not a bare coefficient:

```
sage: def h():
    try:
        a.pyobject()
        return ZZ(a)
    except:
            return a
sage: a = n+1
sage: h()
n + 1
sage: timeit('h()')
625 loops, best of 3: 5.98 µs per loop
sage: a = SR(10^7)
sage: timeit('h()')
625 loops, best of 3: 1.89 µs per loop
```

The docstring confirms this performs as advertised.  If that doesn't speed things up, then I guess it's not possible :(

So if that doesn't work, your original solution stands as a definite improvement, with the changes you noted - put the rational check inside the already existing not isinstance(m, int etc.) check, before trying m = ZZ(m), do the floating point fix where you have it.  Oh yeah, be sure to add doctests for the SR(10**7) etc. 

Because in the long run, we should have more correct cases, I think.  If someone notices a really bad slowdown, we will have to write a very fast symbolic binomial or something.  But all of these are an improvement on before.  Thanks for all of it!



---

archive/issue_comments_056712.json:
```json
{
    "body": "Thanks for the tip, I did not know about the pyobject method. It\ndefinitely improved performance in the symbolic case.\n\nI hope I finally got everything right in version 5 of the patch!",
    "created_at": "2009-09-22T15:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56712",
    "user": "hgranath"
}
```

Thanks for the tip, I did not know about the pyobject method. It
definitely improved performance in the symbolic case.

I hope I finally got everything right in version 5 of the patch!



---

archive/issue_comments_056713.json:
```json
{
    "body": "Attachment\n\nUnfortunately my Sage upgrade croaked, so I can't check it immediately.   I will try to do so as soon as possible.\n\nHowever, what does this patch do with this?\n\n```\nsage: binomial(SR(3/2),SR(1/1))?\n```\n\nTrying x-m won't work on this.   Note that \n\n```\nsage: type(SR(1/1).pyobject())\n<type 'sage.rings.rational.Rational'>\n```\n\nwhich means you may still want a m=ZZ(m) or rational check once you have discovered you aren't in the n+1 case.   I may have that wrong, though, since I can't actually try the patch out.\n\nAs for a trivial point, there is a misspelling of \"coerce\" as well.",
    "created_at": "2009-09-22T15:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56713",
    "user": "kcrisman"
}
```

Attachment

Unfortunately my Sage upgrade croaked, so I can't check it immediately.   I will try to do so as soon as possible.

However, what does this patch do with this?

```
sage: binomial(SR(3/2),SR(1/1))?
```

Trying x-m won't work on this.   Note that 

```
sage: type(SR(1/1).pyobject())
<type 'sage.rings.rational.Rational'>
```

which means you may still want a m=ZZ(m) or rational check once you have discovered you aren't in the n+1 case.   I may have that wrong, though, since I can't actually try the patch out.

As for a trivial point, there is a misspelling of "coerce" as well.



---

archive/issue_comments_056714.json:
```json
{
    "body": "You are right, binomial(SR(3/2),SR(1/1)) actually worked (for other\nreasons) but not e.g. binomial(3/2,SR(1/1)). Fixed in new version.",
    "created_at": "2009-09-22T16:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56714",
    "user": "hgranath"
}
```

You are right, binomial(SR(3/2),SR(1/1)) actually worked (for other
reasons) but not e.g. binomial(3/2,SR(1/1)). Fixed in new version.



---

archive/issue_comments_056715.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-22T16:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56715",
    "user": "hgranath"
}
```

Attachment



---

archive/issue_comments_056716.json:
```json
{
    "body": "I get an odd doctest failure:\n\n\n```\n**********************************************************************\nFile \"/Users/.../crypto/boolean_function.pyx\", line 1013:\n    sage: B.nonlinearity()\nExpected:\n    222\nGot:\n    217\n**********************************************************************\n```\n\nOne might as well add a doctest for that last case you mentioned, too.  I'm rebasing your last patch to fix these, and putting positive review since I only changed the doctests so they pass.  I think we finally got it!",
    "created_at": "2009-09-22T18:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56716",
    "user": "kcrisman"
}
```

I get an odd doctest failure:


```
**********************************************************************
File "/Users/.../crypto/boolean_function.pyx", line 1013:
    sage: B.nonlinearity()
Expected:
    222
Got:
    217
**********************************************************************
```

One might as well add a doctest for that last case you mentioned, too.  I'm rebasing your last patch to fix these, and putting positive review since I only changed the doctests so they pass.  I think we finally got it!



---

archive/issue_comments_056717.json:
```json
{
    "body": "Attachment\n\nBased on 4.1.2.alpha2; apply this patch only.",
    "created_at": "2009-09-22T18:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56717",
    "user": "kcrisman"
}
```

Attachment

Based on 4.1.2.alpha2; apply this patch only.



---

archive/issue_comments_056718.json:
```json
{
    "body": "Incidentally, in the future you may want to name your patches by Trac number and replace ones that are outdated.  Not a big deal, but I know if I don't say it then Minh will :)",
    "created_at": "2009-09-22T18:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56718",
    "user": "kcrisman"
}
```

Incidentally, in the future you may want to name your patches by Trac number and replace ones that are outdated.  Not a big deal, but I know if I don't say it then Minh will :)



---

archive/issue_comments_056719.json:
```json
{
    "body": "set username to Hakan Granath",
    "created_at": "2009-09-24T11:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56719",
    "user": "mvngu"
}
```

set username to Hakan Granath



---

archive/issue_comments_056720.json:
```json
{
    "body": "Attachment\n\nThe patch `trac_6870-final-v2.patch` is the same as `trac_6870-final.patch`. The only difference is that I have set the username to Hakan Granath. This is because `trac_6870-final.patch` is a rebase of Hakan's previous patches.",
    "created_at": "2009-09-24T11:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56720",
    "user": "mvngu"
}
```

Attachment

The patch `trac_6870-final-v2.patch` is the same as `trac_6870-final.patch`. The only difference is that I have set the username to Hakan Granath. This is because `trac_6870-final.patch` is a rebase of Hakan's previous patches.



---

archive/issue_comments_056721.json:
```json
{
    "body": "With `trac_6870-final-v2.patch`, I got the following doctest failure:\n\n```\nsage -t -long devel/sage/sage/crypto/boolean_function.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/crypto/boolean_function.pyx\", line 1013:\n    sage: B.nonlinearity()\nExpected:\n    217\nGot:\n    222\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_36\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_boolean_function.py\n\t [5.3 s]\n```\n",
    "created_at": "2009-09-24T11:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56721",
    "user": "mvngu"
}
```

With `trac_6870-final-v2.patch`, I got the following doctest failure:

```
sage -t -long devel/sage/sage/crypto/boolean_function.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/crypto/boolean_function.pyx", line 1013:
    sage: B.nonlinearity()
Expected:
    217
Got:
    222
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_boolean_function.py
	 [5.3 s]
```




---

archive/issue_comments_056722.json:
```json
{
    "body": "I do not know what is happening with the file boolean_function.pyx, I can not find it in my version of sage (4.1.1).",
    "created_at": "2009-09-24T11:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56722",
    "user": "hgranath"
}
```

I do not know what is happening with the file boolean_function.pyx, I can not find it in my version of sage (4.1.1).



---

archive/issue_comments_056723.json:
```json
{
    "body": "Yeah, I saw that, but couldn't figure out where it came from.  I don't think it's from this, because I got it in a branch without this patch.  Can you try that in a clean branch, Minh?\n\n(Incidentally, this file is in 4.1.2.alpha2, at any rate.)",
    "created_at": "2009-09-24T12:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56723",
    "user": "kcrisman"
}
```

Yeah, I saw that, but couldn't figure out where it came from.  I don't think it's from this, because I got it in a branch without this patch.  Can you try that in a clean branch, Minh?

(Incidentally, this file is in 4.1.2.alpha2, at any rate.)



---

archive/issue_comments_056724.json:
```json
{
    "body": "And how do you DO that keeping the name the same thing?",
    "created_at": "2009-09-24T12:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56724",
    "user": "kcrisman"
}
```

And how do you DO that keeping the name the same thing?



---

archive/issue_comments_056725.json:
```json
{
    "body": "Minh, I tried this again in a branch with no binomial changes, and it is still there.  I am restoring positive review, and suggest that one looks at #6950 and friends for this.  \n\n(Actually, I think it's a true one-liner, because that function depends on the current random state in Sage, and probably somewhere that got reset or changed, so that the \"random\" output isn't really that random. But I leave it the release manager to verify this and open a ticket.)",
    "created_at": "2009-09-24T13:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56725",
    "user": "kcrisman"
}
```

Minh, I tried this again in a branch with no binomial changes, and it is still there.  I am restoring positive review, and suggest that one looks at #6950 and friends for this.  

(Actually, I think it's a true one-liner, because that function depends on the current random state in Sage, and probably somewhere that got reset or changed, so that the "random" output isn't really that random. But I leave it the release manager to verify this and open a ticket.)



---

archive/issue_comments_056726.json:
```json
{
    "body": "Attachment\n\nfix 32- vs. 64-bit issue",
    "created_at": "2009-09-26T05:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56726",
    "user": "mvngu"
}
```

Attachment

fix 32- vs. 64-bit issue



---

archive/issue_comments_056727.json:
```json
{
    "body": "Replying to [comment:20 kcrisman]:\n> Minh, I tried this again in a branch with no binomial changes, and it is still there.  I am restoring positive review, and suggest that one looks at #6950 and friends for this.  \nThe doctest failure I got above is due to a 32- vs. 64-bit issue. On a 32-bit system, it would report 217. But on a 64-bit system, it would report 222. These results are consistent for all the machines I have tested on. See my doctest reports for Sage 4.1.2.alpha2:\n\n* 32- and 64-bit [Ubuntu](http://groups.google.com/group/sage-devel/browse_thread/thread/ec8e2958f394eb5b)\n* 32- and 64-bit [Mandriva](http://groups.google.com/group/sage-devel/browse_thread/thread/e61bb57a2637ba2e)\n* 32- and 64-bit [Debian](http://groups.google.com/group/sage-devel/browse_thread/thread/55d756fb80c94780)\n* 32- and 64-bit [Fedora](http://groups.google.com/group/sage-devel/browse_thread/thread/ff85e2965dc9e59b), [Red Hat, CentOS](http://groups.google.com/group/sage-devel/browse_thread/thread/4ddf1b90690d4cfa)\n* 32- and 64-bit [openSUSE](http://groups.google.com/group/sage-devel/browse_thread/thread/792bb7c3d1f662ef)\n* 32- and 64-bit [Mac OS X 10.5.8](http://groups.google.com/group/sage-devel/browse_thread/thread/954ecbadeb7676a8)\n \nIn all of the above reports, the doctest in question pass on 64-bit platforms, but fail on 32-bit platforms. I have attached the patch `trac_6870-bitness-issue.patch` which takes care of this bitness issue. It should be applied on top of `trac_6870-final-v2.patch`. If my patch is good, then everything is ready to be merged.",
    "created_at": "2009-09-26T05:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56727",
    "user": "mvngu"
}
```

Replying to [comment:20 kcrisman]:
> Minh, I tried this again in a branch with no binomial changes, and it is still there.  I am restoring positive review, and suggest that one looks at #6950 and friends for this.  
The doctest failure I got above is due to a 32- vs. 64-bit issue. On a 32-bit system, it would report 217. But on a 64-bit system, it would report 222. These results are consistent for all the machines I have tested on. See my doctest reports for Sage 4.1.2.alpha2:

* 32- and 64-bit [Ubuntu](http://groups.google.com/group/sage-devel/browse_thread/thread/ec8e2958f394eb5b)
* 32- and 64-bit [Mandriva](http://groups.google.com/group/sage-devel/browse_thread/thread/e61bb57a2637ba2e)
* 32- and 64-bit [Debian](http://groups.google.com/group/sage-devel/browse_thread/thread/55d756fb80c94780)
* 32- and 64-bit [Fedora](http://groups.google.com/group/sage-devel/browse_thread/thread/ff85e2965dc9e59b), [Red Hat, CentOS](http://groups.google.com/group/sage-devel/browse_thread/thread/4ddf1b90690d4cfa)
* 32- and 64-bit [openSUSE](http://groups.google.com/group/sage-devel/browse_thread/thread/792bb7c3d1f662ef)
* 32- and 64-bit [Mac OS X 10.5.8](http://groups.google.com/group/sage-devel/browse_thread/thread/954ecbadeb7676a8)
 
In all of the above reports, the doctest in question pass on 64-bit platforms, but fail on 32-bit platforms. I have attached the patch `trac_6870-bitness-issue.patch` which takes care of this bitness issue. It should be applied on top of `trac_6870-final-v2.patch`. If my patch is good, then everything is ready to be merged.



---

archive/issue_comments_056728.json:
```json
{
    "body": "I believe you, though I have no way of testing this, as I don't plan to build a 64-bit Sage any time soon.  My point is that, as far as I can tell, it should be the subject of its own ticket, not this one.  \n\nIn any case, I an unable to review that part of your patch.  I'm sorry :(",
    "created_at": "2009-09-27T00:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56728",
    "user": "kcrisman"
}
```

I believe you, though I have no way of testing this, as I don't plan to build a 64-bit Sage any time soon.  My point is that, as far as I can tell, it should be the subject of its own ticket, not this one.  

In any case, I an unable to review that part of your patch.  I'm sorry :(



---

archive/issue_comments_056729.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> I believe you, though I have no way of testing this, as I don't plan to build a 64-bit Sage any time soon.  My point is that, as far as I can tell, it should be the subject of its own ticket, not this one.  \n> \n> In any case, I an unable to review that part of your patch.  I'm sorry :(\nWhat you can do is get the patch `trac_6870-final-v2.patch` and remove the hunk:\n\n```\n1011\t1011\t        sage: B.nvariables() \n1012\t1012\t        9 \n1013\t1013\t        sage: B.nonlinearity() \n1014\t \t        222 \n \t1014\t        217 \n1015\t1015\t    \"\"\" \n1016\t1016\t    from sage.misc.randstate import current_randstate \n1017\t1017\t    r = current_randstate().python_random() \n```\n\nfrom that patch. The new patch would be the same as the original, only with changes to the file `sage/rings/arith.py`. As for my patch, you could open another ticket and put the patch there. That way, the patch won't be lost to history, and you could still review Hakan's changes to `sage/rings/arith.py`. As for the doctest failure in `sage/crypto/boolean_function.pyx`, you reference the new ticket from this ticket. How does that sound?",
    "created_at": "2009-09-27T00:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56729",
    "user": "mvngu"
}
```

Replying to [comment:22 kcrisman]:
> I believe you, though I have no way of testing this, as I don't plan to build a 64-bit Sage any time soon.  My point is that, as far as I can tell, it should be the subject of its own ticket, not this one.  
> 
> In any case, I an unable to review that part of your patch.  I'm sorry :(
What you can do is get the patch `trac_6870-final-v2.patch` and remove the hunk:

```
1011	1011	        sage: B.nvariables() 
1012	1012	        9 
1013	1013	        sage: B.nonlinearity() 
1014	 	        222 
 	1014	        217 
1015	1015	    """ 
1016	1016	    from sage.misc.randstate import current_randstate 
1017	1017	    r = current_randstate().python_random() 
```

from that patch. The new patch would be the same as the original, only with changes to the file `sage/rings/arith.py`. As for my patch, you could open another ticket and put the patch there. That way, the patch won't be lost to history, and you could still review Hakan's changes to `sage/rings/arith.py`. As for the doctest failure in `sage/crypto/boolean_function.pyx`, you reference the new ticket from this ticket. How does that sound?



---

archive/issue_comments_056730.json:
```json
{
    "body": "Attachment\n\nThe final patch.  No, really.",
    "created_at": "2009-09-27T00:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56730",
    "user": "kcrisman"
}
```

Attachment

The final patch.  No, really.



---

archive/issue_comments_056731.json:
```json
{
    "body": "That seems reasonable.\n\nOkay, v2.2 should be it.  You can revert to positive review once you check it really does pass all tests - on my current machine, that would probably take 12 hours or so.\n\nNew ticket is #7020.",
    "created_at": "2009-09-27T00:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56731",
    "user": "kcrisman"
}
```

That seems reasonable.

Okay, v2.2 should be it.  You can revert to positive review once you check it really does pass all tests - on my current machine, that would probably take 12 hours or so.

New ticket is #7020.



---

archive/issue_comments_056732.json:
```json
{
    "body": "The patch looks good to me too. Tested on 32 and 64 bit systems.  ~ Adam",
    "created_at": "2009-09-30T07:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56732",
    "user": "awebb"
}
```

The patch looks good to me too. Tested on 32 and 64 bit systems.  ~ Adam



---

archive/issue_comments_056733.json:
```json
{
    "body": "Merged `trac_6870-final-v2.2.patch`.",
    "created_at": "2009-09-30T08:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56733",
    "user": "mvngu"
}
```

Merged `trac_6870-final-v2.2.patch`.



---

archive/issue_comments_056734.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-30T08:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6870#issuecomment-56734",
    "user": "mvngu"
}
```

Resolution: fixed
