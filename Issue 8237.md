# Issue 8237: Sage does not recognize Maxima's complex ininity

archive/issues_008237.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  robert.marik\n\nAs subject says:\n\n```\nsage: maxima('inf').sage()\n+Infinity\nsage: maxima('infinity').sage()\n+Infinity\n```\n\n\nFrom Maxima manual\n\n```\nConstant: inf\n    inf represents real positive infinity.\n\nConstant: infinity\n    infinity represents complex infinity.\n\nConstant: minf\n    minf represents real minus (i.e., negative) infinity. \n```\n\nAs a cosequence, Sage fails to evaluate limit of 1/x at x=0. Maxima gives correct result (complex infinity)\n\n```\nsage: maxima('limit(1/x,x,0)')\ninfinity\nsage: maxima('limit(1/x,x,0)').sage()\n+Infinity\nsage: limit(1/x,x=0)\n+Infinity\nsage: maxima('limit(1/x,x,0,plus)')\ninf\nsage: maxima('limit(1/x,x,0,plus)').sage()\n+Infinity\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8237\n\n",
    "created_at": "2010-02-11T17:09:35Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "Sage does not recognize Maxima's complex ininity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8237",
    "user": "robert.marik"
}
```
Assignee: burcin

CC:  robert.marik

As subject says:

```
sage: maxima('inf').sage()
+Infinity
sage: maxima('infinity').sage()
+Infinity
```


From Maxima manual

```
Constant: inf
    inf represents real positive infinity.

Constant: infinity
    infinity represents complex infinity.

Constant: minf
    minf represents real minus (i.e., negative) infinity. 
```

As a cosequence, Sage fails to evaluate limit of 1/x at x=0. Maxima gives correct result (complex infinity)

```
sage: maxima('limit(1/x,x,0)')
infinity
sage: maxima('limit(1/x,x,0)').sage()
+Infinity
sage: limit(1/x,x=0)
+Infinity
sage: maxima('limit(1/x,x,0,plus)')
inf
sage: maxima('limit(1/x,x,0,plus)').sage()
+Infinity
```


Issue created by migration from https://trac.sagemath.org/ticket/8237





---

archive/issue_comments_072758.json:
```json
{
    "body": "reported on [sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/350697c3650a3b76)",
    "created_at": "2010-02-11T17:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72758",
    "user": "robert.marik"
}
```

reported on [sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/350697c3650a3b76)



---

archive/issue_comments_072759.json:
```json
{
    "body": "Changing assignee from burcin to robert.marik.",
    "created_at": "2010-02-11T18:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72759",
    "user": "robert.marik"
}
```

Changing assignee from burcin to robert.marik.



---

archive/issue_comments_072760.json:
```json
{
    "body": "Changing assignee from robert.marik to burcin.",
    "created_at": "2010-02-11T18:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72760",
    "user": "robert.marik"
}
```

Changing assignee from robert.marik to burcin.



---

archive/issue_comments_072761.json:
```json
{
    "body": "Right now, there doesn't seem to be a lot of distinction in Sage between unsigned and signed infinity, though of course as you point out there should be.  From sage.rings.infinity.py:\n\n```\n    Note: the shorthand oo is predefined in Sage to be the same as\n    +Infinity in the infinity ring. It is considered equal to, but not\n    the same as Infinity in the UnsignedInfinityRing::\n    \n        sage: oo\n        +Infinity\n        sage: oo is InfinityRing.0\n        True\n        sage: oo is UnsignedInfinityRing.0\n        False\n        sage: oo == UnsignedInfinityRing.0\n        True\n    \n```\n\nThere is unsigned_infinity, but the following seems problematic:\n\n```\nsage: unsigned_infinity\nInfinity\nsage: Infinity\n+Infinity\n```\n\nWhat the heck?",
    "created_at": "2010-02-11T19:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72761",
    "user": "kcrisman"
}
```

Right now, there doesn't seem to be a lot of distinction in Sage between unsigned and signed infinity, though of course as you point out there should be.  From sage.rings.infinity.py:

```
    Note: the shorthand oo is predefined in Sage to be the same as
    +Infinity in the infinity ring. It is considered equal to, but not
    the same as Infinity in the UnsignedInfinityRing::
    
        sage: oo
        +Infinity
        sage: oo is InfinityRing.0
        True
        sage: oo is UnsignedInfinityRing.0
        False
        sage: oo == UnsignedInfinityRing.0
        True
    
```

There is unsigned_infinity, but the following seems problematic:

```
sage: unsigned_infinity
Infinity
sage: Infinity
+Infinity
```

What the heck?



---

archive/issue_comments_072762.json:
```json
{
    "body": "Attachment [trac_8237-maxima_infinity.patch](tarball://root/attachments/some-uuid/ticket8237/trac_8237-maxima_infinity.patch) by burcin created at 2010-02-11 22:00:42\n\nfix conversion of different infinities back from maxima",
    "created_at": "2010-02-11T22:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72762",
    "user": "burcin"
}
```

Attachment [trac_8237-maxima_infinity.patch](tarball://root/attachments/some-uuid/ticket8237/trac_8237-maxima_infinity.patch) by burcin created at 2010-02-11 22:00:42

fix conversion of different infinities back from maxima



---

archive/issue_comments_072763.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-11T22:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72763",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072764.json:
```json
{
    "body": "I uploaded a patch, please review.",
    "created_at": "2010-02-11T22:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72764",
    "user": "burcin"
}
```

I uploaded a patch, please review.



---

archive/issue_comments_072765.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-12T02:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72765",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072766.json:
```json
{
    "body": "Looks good, but does it duplicate some of lines 1841ff of sage/calculus/calculus.py?\n\n```\nfrom sage.rings.infinity import infinity, minus_infinity\nregister_symbol(infinity, dict(maxima='inf'))\nregister_symbol(minus_infinity, dict(maxima='minf'))\n```\n\nSince \n\n```\nsage: type(infinity)\n<class 'sage.rings.infinity.PlusInfinity'>\nsage: type(SR(infinity))\n<type 'sage.symbolic.expression.Expression'>\n```\n\nmy guess is that, at least for completeness, calculus.py should also import unsigned_infinity and have a line added with \n\n```\nregister_symbol(unsigned_infinity, dict(maxima='infinity'))\n```\n\n\nAlso, my taste in doctests is to also include the original example, not (only) the underlying cause:\n\n```\nsage: limit(1/x,x=0)\nInfinity\nsage: limit(1/x,x=0,dir='above')\n+Infinity\nsage: limit(1/x,x=0,dir='below')\n-Infinity\n```\n\nwhich of course works great now.  These are very minor quibbles, of course, but might as well be done.\n\nAlso, in doctesting it doesn't like sage: sage: as the prefix (though one could argue this is a bug itself), and \n\n```\ndevel/sage/sage/calculus/functional.py\", line 313:\n    sage: lim(1/x, x=0)\nExpected:\n    +Infinity\nGot:\n    Infinity\n```\n",
    "created_at": "2010-02-12T02:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72766",
    "user": "kcrisman"
}
```

Looks good, but does it duplicate some of lines 1841ff of sage/calculus/calculus.py?

```
from sage.rings.infinity import infinity, minus_infinity
register_symbol(infinity, dict(maxima='inf'))
register_symbol(minus_infinity, dict(maxima='minf'))
```

Since 

```
sage: type(infinity)
<class 'sage.rings.infinity.PlusInfinity'>
sage: type(SR(infinity))
<type 'sage.symbolic.expression.Expression'>
```

my guess is that, at least for completeness, calculus.py should also import unsigned_infinity and have a line added with 

```
register_symbol(unsigned_infinity, dict(maxima='infinity'))
```


Also, my taste in doctests is to also include the original example, not (only) the underlying cause:

```
sage: limit(1/x,x=0)
Infinity
sage: limit(1/x,x=0,dir='above')
+Infinity
sage: limit(1/x,x=0,dir='below')
-Infinity
```

which of course works great now.  These are very minor quibbles, of course, but might as well be done.

Also, in doctesting it doesn't like sage: sage: as the prefix (though one could argue this is a bug itself), and 

```
devel/sage/sage/calculus/functional.py", line 313:
    sage: lim(1/x, x=0)
Expected:
    +Infinity
Got:
    Infinity
```




---

archive/issue_comments_072767.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-02-20T14:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72767",
    "user": "burcin"
}
```

apply only this patch



---

archive/issue_comments_072768.json:
```json
{
    "body": "Attachment [trac_8237-maxima_infinity.take2.patch](tarball://root/attachments/some-uuid/ticket8237/trac_8237-maxima_infinity.take2.patch) by burcin created at 2010-02-20 14:36:11\n\nI was trying to get the first patch out quickly, so it ended up being too sloppy. I hope attachment:trac_8237-maxima_infinity.take2.patch is cleaner. :)\n\nI think it's more natural to put the maxima conversions for different infinities in `sage/symbolic/constants.py` where all the other constants are declared, so I removed the lines in `calculus.py`. I also added doctests with `limit(1/x, ...)`.",
    "created_at": "2010-02-20T14:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72768",
    "user": "burcin"
}
```

Attachment [trac_8237-maxima_infinity.take2.patch](tarball://root/attachments/some-uuid/ticket8237/trac_8237-maxima_infinity.take2.patch) by burcin created at 2010-02-20 14:36:11

I was trying to get the first patch out quickly, so it ended up being too sloppy. I hope attachment:trac_8237-maxima_infinity.take2.patch is cleaner. :)

I think it's more natural to put the maxima conversions for different infinities in `sage/symbolic/constants.py` where all the other constants are declared, so I removed the lines in `calculus.py`. I also added doctests with `limit(1/x, ...)`.



---

archive/issue_comments_072769.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-20T14:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72769",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072770.json:
```json
{
    "body": "By exercising a number of arithmetic use cases, viz. \n\n```\nfor k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):\n    print k, k + Infinity , k + +Infinity, k + -Infinity\n\nfor k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):\n    print k, Infinity -k , +Infinity -k, -Infinity -k\n\nfor k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):\n    print k, k / Infinity , k / +Infinity, k / -Infinity\n\nfor k in (1, 1.0, 1/2, x, -1, -1.0, -1/2, -x):\n    print k, k * Infinity , k * +Infinity, k * -Infinity\n```\n\nthere were a small number of things to note\n\n\n(a) the same answer resulted, regardless of whether (unsigned) Infinity or +Infinity was used. Query: Just to make sure we are getting the results we designed for...  Currently +Infinity (or -Infinity) is being returned regardless of whether a signed or unsigned infinity is used. Should (unsigned) Infinity be returned when (unsigned) Infinity is used?\n\n\n(b) what seems to be an inconsistency occurs when mixing Infinity with complex numbers (same thing holds when we replace Infinity with +Infinity or with -Infinity)\n\n```\n# the following combinations of complex and infinity are ok\nI + Infinity # +Infinity\nI - Infinity # -Infinity\nI / Infinity # 0\n\n# the following crash with Arithmetic Error \nInfinity / I  \nInfinity * I\nI * Infinity\n\n# isnt I+Infinity (for example) just as meaningful/less as I*Infinity ? \n```\n\n\n(c) Im curious about the following expressions\n\n```\nx * Infinity\n-x * Infinity\n```\n\nThese return `+Infinity` and `-Infinity` respectively. But what if x is negative real? (should be opposite answers). The following tries to demonstrate this for two vars (z and x), both declared real in two different ways\n\n```\nsage: var('z',domain='real')\nz\nsage: assume(x,'real',x<0,z<0)\nsage: assumptions()\n[x is real, x < 0, z < 0]\nsage: x*+Infinity\n+Infinity\nsage: z*+Infinity\n+Infinity\n```\n\n(is this another ticket \"make Infinity work with assumptions/declarations\"?)",
    "created_at": "2010-02-24T12:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72770",
    "user": "rossk"
}
```

By exercising a number of arithmetic use cases, viz. 

```
for k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):
    print k, k + Infinity , k + +Infinity, k + -Infinity

for k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):
    print k, Infinity -k , +Infinity -k, -Infinity -k

for k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):
    print k, k / Infinity , k / +Infinity, k / -Infinity

for k in (1, 1.0, 1/2, x, -1, -1.0, -1/2, -x):
    print k, k * Infinity , k * +Infinity, k * -Infinity
```

there were a small number of things to note


(a) the same answer resulted, regardless of whether (unsigned) Infinity or +Infinity was used. Query: Just to make sure we are getting the results we designed for...  Currently +Infinity (or -Infinity) is being returned regardless of whether a signed or unsigned infinity is used. Should (unsigned) Infinity be returned when (unsigned) Infinity is used?


(b) what seems to be an inconsistency occurs when mixing Infinity with complex numbers (same thing holds when we replace Infinity with +Infinity or with -Infinity)

```
# the following combinations of complex and infinity are ok
I + Infinity # +Infinity
I - Infinity # -Infinity
I / Infinity # 0

# the following crash with Arithmetic Error 
Infinity / I  
Infinity * I
I * Infinity

# isnt I+Infinity (for example) just as meaningful/less as I*Infinity ? 
```


(c) Im curious about the following expressions

```
x * Infinity
-x * Infinity
```

These return `+Infinity` and `-Infinity` respectively. But what if x is negative real? (should be opposite answers). The following tries to demonstrate this for two vars (z and x), both declared real in two different ways

```
sage: var('z',domain='real')
z
sage: assume(x,'real',x<0,z<0)
sage: assumptions()
[x is real, x < 0, z < 0]
sage: x*+Infinity
+Infinity
sage: z*+Infinity
+Infinity
```

(is this another ticket "make Infinity work with assumptions/declarations"?)



---

archive/issue_comments_072771.json:
```json
{
    "body": "Hi Ross,\n\nIt's likely that there are inconsistencies in the way infinity is handled by pynac. For instance it definitely doesn't handle interactions with the complex `I` well. I implemented support for infinity in pynac to provide a basis for better series expansions and limit computations. However, I didn't have time to actually use it for anything later.\n\nI suggest we keep this issue focused on the conversion problem in the maxima interface so it can be reviewed and merged quickly. You can open separate tickets for the problems in pynac related to infinity. The fact that assumptions are not passed on to pynac should be yet another ticket.\n\nBTW, this article might help decide what behavior we expect w.r.t. arithmetic involving infinity.\n\nhttp://dx.doi.org/10.1016/j.jsc.2004.12.002",
    "created_at": "2010-02-24T16:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72771",
    "user": "burcin"
}
```

Hi Ross,

It's likely that there are inconsistencies in the way infinity is handled by pynac. For instance it definitely doesn't handle interactions with the complex `I` well. I implemented support for infinity in pynac to provide a basis for better series expansions and limit computations. However, I didn't have time to actually use it for anything later.

I suggest we keep this issue focused on the conversion problem in the maxima interface so it can be reviewed and merged quickly. You can open separate tickets for the problems in pynac related to infinity. The fact that assumptions are not passed on to pynac should be yet another ticket.

BTW, this article might help decide what behavior we expect w.r.t. arithmetic involving infinity.

http://dx.doi.org/10.1016/j.jsc.2004.12.002



---

archive/issue_comments_072772.json:
```json
{
    "body": "Burcin.\n\n\nI *did* think it unlikely all these issues would be addressed in one ticket ;-) I guess I was trying to be diligent in reviewing (and Im interested in getting involved in \"symbolics\" development some time, so the extended exercising of the symbolics module is part of my familiarization process - I even started looking at the code!)\n\n\nThe tests I did above (plus others involving limits) warrant a positive review vote from me. Ill let Karl-Dieter sign it off when he wants, as he has reviewed the code as well.",
    "created_at": "2010-02-25T07:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72772",
    "user": "rossk"
}
```

Burcin.


I *did* think it unlikely all these issues would be addressed in one ticket ;-) I guess I was trying to be diligent in reviewing (and Im interested in getting involved in "symbolics" development some time, so the extended exercising of the symbolics module is part of my familiarization process - I even started looking at the code!)


The tests I did above (plus others involving limits) warrant a positive review vote from me. Ill let Karl-Dieter sign it off when he wants, as he has reviewed the code as well.



---

archive/issue_comments_072773.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-04-12T08:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72773",
    "user": "burcin"
}
```

apply only this patch



---

archive/issue_comments_072774.json:
```json
{
    "body": "Attachment [trac_8237-maxima_infinity.take3.patch](tarball://root/attachments/some-uuid/ticket8237/trac_8237-maxima_infinity.take3.patch) by burcin created at 2010-04-12 08:35:08\n\nI rebased the patch so that it applies cleanly after #7661.\n\nThis ticket depends on #7661. Only attachment:trac_8237-maxima_infinity.take3.patch should be applied.",
    "created_at": "2010-04-12T08:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72774",
    "user": "burcin"
}
```

Attachment [trac_8237-maxima_infinity.take3.patch](tarball://root/attachments/some-uuid/ticket8237/trac_8237-maxima_infinity.take3.patch) by burcin created at 2010-04-12 08:35:08

I rebased the patch so that it applies cleanly after #7661.

This ticket depends on #7661. Only attachment:trac_8237-maxima_infinity.take3.patch should be applied.



---

archive/issue_comments_072775.json:
```json
{
    "body": "This looks wonderful to me, but unfortunately I don't have a current build of the alphas for 4.4, so I can't actually test it.  I'd give is a positive review if I could!",
    "created_at": "2010-04-23T16:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72775",
    "user": "kcrisman"
}
```

This looks wonderful to me, but unfortunately I don't have a current build of the alphas for 4.4, so I can't actually test it.  I'd give is a positive review if I could!



---

archive/issue_comments_072776.json:
```json
{
    "body": "Works for me, long tests passed on 4.4.rc0.\n\nSince also kcrisman wrote \"This looks wonderful to me .... I'd give is a positive review if I could!\" I think that the ticket deserves positive review.\n\nPositive review. Apply only trac_8237-maxima_infinity.take3.patch",
    "created_at": "2010-04-29T06:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72776",
    "user": "robert.marik"
}
```

Works for me, long tests passed on 4.4.rc0.

Since also kcrisman wrote "This looks wonderful to me .... I'd give is a positive review if I could!" I think that the ticket deserves positive review.

Positive review. Apply only trac_8237-maxima_infinity.take3.patch



---

archive/issue_comments_072777.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-29T06:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72777",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072778.json:
```json
{
    "body": "Merged [trac_8237-maxima_infinity.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8237/trac_8237-maxima_infinity.take3.patch).",
    "created_at": "2010-05-08T22:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72778",
    "user": "mvngu"
}
```

Merged [trac_8237-maxima_infinity.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8237/trac_8237-maxima_infinity.take3.patch).



---

archive/issue_comments_072779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8237#issuecomment-72779",
    "user": "mvngu"
}
```

Resolution: fixed
