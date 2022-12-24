# Issue 3870: bug in find_root

archive/issues_003870.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @jasongrout\n\n\n```\nIt appears that find_root give the wrong result in the following\nexample:\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.5, Release Date: 2008-07-11                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: var('av')\nav\nsage: f=2.00000000000000*av - (10*sqrt(36.0000000000000*(av^4 - 2*av^3\n+ av^2) + 207.360000000000*(-4*av^4 + 8*av^3 - 4*av^2) +\n365*(51.8400000000000*(4*av^3 - 4*av) + 9.00000000000000*(2*av -\n2*av^2)) + 133225*(2.25000000000000 - 51.8400000000000*av)) +\n60.0000000000000*(av - av^2) + 5475.00000000000)/(720.000000000000*(2\n- 2*av) + 131400.000000000)\nsage: find_root(f,0,0.1)\n0.0\nsage: plot(f,0,0.1)\n\nThe last command will plot f and reveal that the root is somewhere\nnear to 0.05, but certainly not 0.0. No matter what I use for xtol or\nrtol, I always get 0.0 as a result. Can anyone help?\n\nThanks!\n\nStan\n```\n\n\nI don't what is going on yet.  It may be a bug in scipy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3870\n\n",
    "created_at": "2008-08-15T09:30:54Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in find_root",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3870",
    "user": "@williamstein"
}
```
Assignee: @garyfurnish

CC:  @jasongrout


```
It appears that find_root give the wrong result in the following
example:

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
sage: var('av')
av
sage: f=2.00000000000000*av - (10*sqrt(36.0000000000000*(av^4 - 2*av^3
+ av^2) + 207.360000000000*(-4*av^4 + 8*av^3 - 4*av^2) +
365*(51.8400000000000*(4*av^3 - 4*av) + 9.00000000000000*(2*av -
2*av^2)) + 133225*(2.25000000000000 - 51.8400000000000*av)) +
60.0000000000000*(av - av^2) + 5475.00000000000)/(720.000000000000*(2
- 2*av) + 131400.000000000)
sage: find_root(f,0,0.1)
0.0
sage: plot(f,0,0.1)

The last command will plot f and reveal that the root is somewhere
near to 0.05, but certainly not 0.0. No matter what I use for xtol or
rtol, I always get 0.0 as a result. Can anyone help?

Thanks!

Stan
```


I don't what is going on yet.  It may be a bug in scipy.

Issue created by migration from https://trac.sagemath.org/ticket/3870





---

archive/issue_comments_027584.json:
```json
{
    "body": "Stan Schymanski points out that:\n\n\n```\n\nI just found out that the problem can be solved using maxima's\nfind_root:\n\nsage: maxima.find_root(f,0,0.1)\n.03134446907530818\n\nIt's great that sage offers multiple ways of doing the same thing. :)\n\nStan\n```\n",
    "created_at": "2008-08-26T09:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3870#issuecomment-27584",
    "user": "@williamstein"
}
```

Stan Schymanski points out that:


```

I just found out that the problem can be solved using maxima's
find_root:

sage: maxima.find_root(f,0,0.1)
.03134446907530818

It's great that sage offers multiple ways of doing the same thing. :)

Stan
```




---

archive/issue_comments_027585.json:
```json
{
    "body": "I don't know if that is the cause, but I don't think find_root is prepared to deal with complex numbers:\n\n\n```\nsage: var('av')\nav\nsage: f=2.00000000000000*av - (10*sqrt(36.0000000000000*(av^4 - 2*av^3\n+ av^2) + 207.360000000000*(-4*av^4 + 8*av^3 - 4*av^2) +\n365*(51.8400000000000*(4*av^3 - 4*av) + 9.00000000000000*(2*av -\n2*av^2)) + 133225*(2.25000000000000 - 51.8400000000000*av)) +\n60.0000000000000*(av - av^2) + 5475.00000000000)/(720.000000000000*(2\n- 2*av) + 131400.000000000)\nsage: f(0.1).n()\n0.158699584011575 - 0.0475301543661689*I\n```\n",
    "created_at": "2008-09-08T20:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3870#issuecomment-27585",
    "user": "anakha"
}
```

I don't know if that is the cause, but I don't think find_root is prepared to deal with complex numbers:


```
sage: var('av')
av
sage: f=2.00000000000000*av - (10*sqrt(36.0000000000000*(av^4 - 2*av^3
+ av^2) + 207.360000000000*(-4*av^4 + 8*av^3 - 4*av^2) +
365*(51.8400000000000*(4*av^3 - 4*av) + 9.00000000000000*(2*av -
2*av^2)) + 133225*(2.25000000000000 - 51.8400000000000*av)) +
60.0000000000000*(av - av^2) + 5475.00000000000)/(720.000000000000*(2
- 2*av) + 131400.000000000)
sage: f(0.1).n()
0.158699584011575 - 0.0475301543661689*I
```




---

archive/issue_comments_027586.json:
```json
{
    "body": "Continuing from the previous block:\n\n```\nsage: ff = sage.ext.fast_eval.fast_float(f, av)\nsage: ff\n<sage.ext.fast_eval.FastDoubleFunc object at 0x8a7a8f0>\nsage: ff(0)\n-0.082429990966576328\nsage: ff(0.1)\nnan\nsage: ff(0.05)\nnan\nsage: ff(0.04)\n0.02790669038508465\nsage: find_root(f, 0, 0.04)\n0.031344469075307836\n```\n\n\nYeah, it is clearly not prepared.  I don't know why maxima works.",
    "created_at": "2008-09-08T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3870#issuecomment-27586",
    "user": "anakha"
}
```

Continuing from the previous block:

```
sage: ff = sage.ext.fast_eval.fast_float(f, av)
sage: ff
<sage.ext.fast_eval.FastDoubleFunc object at 0x8a7a8f0>
sage: ff(0)
-0.082429990966576328
sage: ff(0.1)
nan
sage: ff(0.05)
nan
sage: ff(0.04)
0.02790669038508465
sage: find_root(f, 0, 0.04)
0.031344469075307836
```


Yeah, it is clearly not prepared.  I don't know why maxima works.



---

archive/issue_comments_027587.json:
```json
{
    "body": "Changing keywords from \"\" to \"scipy\".",
    "created_at": "2008-11-14T06:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3870#issuecomment-27587",
    "user": "@jasongrout"
}
```

Changing keywords from "" to "scipy".



---

archive/issue_comments_027588.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-20T06:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3870#issuecomment-27588",
    "user": "@jasongrout"
}
```

Resolution: invalid



---

archive/issue_comments_027589.json:
```json
{
    "body": "Yep.  In the scipy documentation, it assumes the function is continuous (from context, it seems over the reals).  So this function fails, as allowed by the documentation.",
    "created_at": "2010-01-20T06:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3870#issuecomment-27589",
    "user": "@jasongrout"
}
```

Yep.  In the scipy documentation, it assumes the function is continuous (from context, it seems over the reals).  So this function fails, as allowed by the documentation.
