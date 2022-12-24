# Issue 9968: Update extension code for mpmath-0.16

archive/issues_009968.json:
```json
{
    "body": "Assignee: tbd\n\nThe patch adds fast Cython version of some more mpmath functions to sage.libs.mpmath.\n\nThis should wait to be merged until mpmath 0.16 gets released (I will do this soon). Right now, it can be tested with an svn trunk checkout of mpmath.\n\nIt can be tested with:\n\n```\nsage: import mpmath\nsage: mpmath.runtests()\nsage: mpmath.doctests()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9969\n\n",
    "created_at": "2010-09-22T13:16:04Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Update extension code for mpmath-0.16",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9968",
    "user": "fredrik.johansson"
}
```
Assignee: tbd

The patch adds fast Cython version of some more mpmath functions to sage.libs.mpmath.

This should wait to be merged until mpmath 0.16 gets released (I will do this soon). Right now, it can be tested with an svn trunk checkout of mpmath.

It can be tested with:

```
sage: import mpmath
sage: mpmath.runtests()
sage: mpmath.doctests()
```


Issue created by migration from https://trac.sagemath.org/ticket/9969





---

archive/issue_comments_099880.json:
```json
{
    "body": "Attachment [14600.patch](tarball://root/attachments/some-uuid/ticket9969/14600.patch) by fredrik.johansson created at 2010-09-22 13:16:39\n\nupdated mpmath Cython extension code",
    "created_at": "2010-09-22T13:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99880",
    "user": "fredrik.johansson"
}
```

Attachment [14600.patch](tarball://root/attachments/some-uuid/ticket9969/14600.patch) by fredrik.johansson created at 2010-09-22 13:16:39

updated mpmath Cython extension code



---

archive/issue_comments_099881.json:
```json
{
    "body": "Here is an spkg: http://sage.math.washington.edu/home/fredrik/mpmath-0.16.spkg\n\nIt should work fine together with the patch. Sorry for the very long delay!",
    "created_at": "2010-10-30T21:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99881",
    "user": "fredrik.johansson"
}
```

Here is an spkg: http://sage.math.washington.edu/home/fredrik/mpmath-0.16.spkg

It should work fine together with the patch. Sorry for the very long delay!



---

archive/issue_comments_099882.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-30T21:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99882",
    "user": "fredrik.johansson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099883.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-02T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99883",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099884.json:
```json
{
    "body": "REPORT:\n\n* All tests passon sage.math.\n\n*  Your code needs \"::\\n\\n\" before any sage sessions for sphinx to format it right.\nSee the template here and note rightafterwords: http://sagemath.blogspot.com/\nright now if somebody introspects one of your functions in the notebook, sphinx will butcher it.\n\n* You define \"isqrt\" but sage integers already have an isqrt method that is exactly the same.  Clarify in the documentation the distinction.\n\nBug me again by email or chat when you've posted another patch (or patch on top of the above) that fixes the above two little things.",
    "created_at": "2010-11-02T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99884",
    "user": "was"
}
```

REPORT:

* All tests passon sage.math.

*  Your code needs "::\n\n" before any sage sessions for sphinx to format it right.
See the template here and note rightafterwords: http://sagemath.blogspot.com/
right now if somebody introspects one of your functions in the notebook, sphinx will butcher it.

* You define "isqrt" but sage integers already have an isqrt method that is exactly the same.  Clarify in the documentation the distinction.

Bug me again by email or chat when you've posted another patch (or patch on top of the above) that fixes the above two little things.



---

archive/issue_comments_099885.json:
```json
{
    "body": "Oh, could you have at least a short comment explaining what every single function does.  E.g.,\n\n```\ncdef cy_exp_basecase(mpz_t y, mpz_t x, int prec):\n     # <what this function does>\n```\n",
    "created_at": "2010-11-02T22:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99885",
    "user": "was"
}
```

Oh, could you have at least a short comment explaining what every single function does.  E.g.,

```
cdef cy_exp_basecase(mpz_t y, mpz_t x, int prec):
     # <what this function does>
```




---

archive/issue_comments_099886.json:
```json
{
    "body": "Attachment [docstring-fixes.patch](tarball://root/attachments/some-uuid/ticket9969/docstring-fixes.patch) by fredrik.johansson created at 2010-11-19 14:57:54",
    "created_at": "2010-11-19T14:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99886",
    "user": "fredrik.johansson"
}
```

Attachment [docstring-fixes.patch](tarball://root/attachments/some-uuid/ticket9969/docstring-fixes.patch) by fredrik.johansson created at 2010-11-19 14:57:54



---

archive/issue_comments_099887.json:
```json
{
    "body": "Added second patch with docstring fixes.",
    "created_at": "2010-11-19T15:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99887",
    "user": "fredrik.johansson"
}
```

Added second patch with docstring fixes.



---

archive/issue_comments_099888.json:
```json
{
    "body": "Remove assignee tbd.",
    "created_at": "2010-11-19T15:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99888",
    "user": "fredrik.johansson"
}
```

Remove assignee tbd.



---

archive/issue_comments_099889.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-19T15:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99889",
    "user": "fredrik.johansson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099890.json:
```json
{
    "body": "If I understand correctly you need to apply 14600.patch first, then docstring-fixes.patch?\nThis goes in sage-on-gentoo tonight for testing.",
    "created_at": "2011-01-27T08:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99890",
    "user": "fbissey"
}
```

If I understand correctly you need to apply 14600.patch first, then docstring-fixes.patch?
This goes in sage-on-gentoo tonight for testing.



---

archive/issue_comments_099891.json:
```json
{
    "body": "I forgot, for it to go in sage proper a new spkg will be needed. Are you working on that?",
    "created_at": "2011-01-27T08:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99891",
    "user": "fbissey"
}
```

I forgot, for it to go in sage proper a new spkg will be needed. Are you working on that?



---

archive/issue_comments_099892.json:
```json
{
    "body": "Yes, the patches should be applied in that order.\n\nThe spkg was linked in a post above: http://sage.math.washington.edu/home/fredrik/mpmath-0.16.spkg",
    "created_at": "2011-01-27T09:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99892",
    "user": "fredrik.johansson"
}
```

Yes, the patches should be applied in that order.

The spkg was linked in a post above: http://sage.math.washington.edu/home/fredrik/mpmath-0.16.spkg



---

archive/issue_comments_099893.json:
```json
{
    "body": "I should get a reader since I am obviously blind :)\nI say we try to get it formally in 4.7, I rewrite the\ndescription a little bit.",
    "created_at": "2011-01-27T10:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99893",
    "user": "fbissey"
}
```

I should get a reader since I am obviously blind :)
I say we try to get it formally in 4.7, I rewrite the
description a little bit.



---

archive/issue_comments_099894.json:
```json
{
    "body": "I just saw your post about mpmath-0.17 release, are you planing to update this ticket\nfor mpmath 0.17?",
    "created_at": "2011-02-01T22:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99894",
    "user": "fbissey"
}
```

I just saw your post about mpmath-0.17 release, are you planing to update this ticket
for mpmath 0.17?



---

archive/issue_comments_099895.json:
```json
{
    "body": "Yes, I'll create an spkg for 0.17 immediately to replace the 0.16 one.\n\nNothing should have changed in the way of Sage compatibility, so the patches should still be fine.",
    "created_at": "2011-02-01T22:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99895",
    "user": "fredrik.johansson"
}
```

Yes, I'll create an spkg for 0.17 immediately to replace the 0.16 one.

Nothing should have changed in the way of Sage compatibility, so the patches should still be fine.



---

archive/issue_comments_099896.json:
```json
{
    "body": "By the way, I noticed (too late) that there are two failing doctests if you run mpmath.doctests() as per the instructions. These failures a trivial (output formatting) and can be ignored.",
    "created_at": "2011-02-01T22:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99896",
    "user": "fredrik.johansson"
}
```

By the way, I noticed (too late) that there are two failing doctests if you run mpmath.doctests() as per the instructions. These failures a trivial (output formatting) and can be ignored.



---

archive/issue_comments_099897.json:
```json
{
    "body": "Replying to [comment:11 fredrik.johansson]:\n> Yes, I'll create an spkg for 0.17 immediately to replace the 0.16 one.\n> \n> Nothing should have changed in the way of Sage compatibility, so the patches should still be fine.\n\nGood to know, that means I won't have to change anything to support mpmath-0.17 in sage-on-gentoo when 4.6.2 is released.",
    "created_at": "2011-02-01T22:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99897",
    "user": "fbissey"
}
```

Replying to [comment:11 fredrik.johansson]:
> Yes, I'll create an spkg for 0.17 immediately to replace the 0.16 one.
> 
> Nothing should have changed in the way of Sage compatibility, so the patches should still be fine.

Good to know, that means I won't have to change anything to support mpmath-0.17 in sage-on-gentoo when 4.6.2 is released.



---

archive/issue_comments_099898.json:
```json
{
    "body": "Fixed patch that should apply in sage-4.6.1",
    "created_at": "2011-02-17T10:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99898",
    "user": "fredrik.johansson"
}
```

Fixed patch that should apply in sage-4.6.1



---

archive/issue_comments_099899.json:
```json
{
    "body": "Attachment [mpmath_update_fixed_4.6.1.patch](tarball://root/attachments/some-uuid/ticket9969/mpmath_update_fixed_4.6.1.patch) by fredrik.johansson created at 2011-02-18 08:35:16\n\nPatch that fixes some mpmath test failures due to use of the truediv operator",
    "created_at": "2011-02-18T08:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99899",
    "user": "fredrik.johansson"
}
```

Attachment [mpmath_update_fixed_4.6.1.patch](tarball://root/attachments/some-uuid/ticket9969/mpmath_update_fixed_4.6.1.patch) by fredrik.johansson created at 2011-02-18 08:35:16

Patch that fixes some mpmath test failures due to use of the truediv operator



---

archive/issue_comments_099900.json:
```json
{
    "body": "Attachment [truediv_fix.patch](tarball://root/attachments/some-uuid/ticket9969/truediv_fix.patch) by fredrik.johansson created at 2011-02-18 08:36:42",
    "created_at": "2011-02-18T08:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99900",
    "user": "fredrik.johansson"
}
```

Attachment [truediv_fix.patch](tarball://root/attachments/some-uuid/ticket9969/truediv_fix.patch) by fredrik.johansson created at 2011-02-18 08:36:42



---

archive/issue_comments_099901.json:
```json
{
    "body": "The two new patches together are smaller than the two previous patches. Is docstring-fixes.patch really not needed anymore?",
    "created_at": "2011-02-18T08:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99901",
    "user": "fbissey"
}
```

The two new patches together are smaller than the two previous patches. Is docstring-fixes.patch really not needed anymore?



---

archive/issue_comments_099902.json:
```json
{
    "body": "Most of docstring-fixes.patch consisted of reformatting existing docstrings, and there's a lot of air in the diff format, so I think the numbers add up.",
    "created_at": "2011-02-18T08:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99902",
    "user": "fredrik.johansson"
}
```

Most of docstring-fixes.patch consisted of reformatting existing docstrings, and there's a lot of air in the diff format, so I think the numbers add up.



---

archive/issue_comments_099903.json:
```json
{
    "body": "Replying to [comment:17 fredrik.johansson]:\n> Most of docstring-fixes.patch consisted of reformatting existing docstrings, and there's a lot of air in the diff format, so I think the numbers add up.\n\nI thought it could be the case. I will try to review this quickly so we can have it included in 4.7.alpha.",
    "created_at": "2011-02-18T09:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99903",
    "user": "fbissey"
}
```

Replying to [comment:17 fredrik.johansson]:
> Most of docstring-fixes.patch consisted of reformatting existing docstrings, and there's a lot of air in the diff format, so I think the numbers add up.

I thought it could be the case. I will try to review this quickly so we can have it included in 4.7.alpha.



---

archive/issue_comments_099904.json:
```json
{
    "body": "tests are not looking good to me.\n\n```\nPython 2.6.6 (r266:84292, Jan 28 2011, 01:59:55) \n[GCC 4.5.2] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import mpmath\n>>> mpmath.runtests()\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/usr/lib64/python2.6/site-packages/mpmath/__init__.py\", line 413, in runtests\n    from .tests import runtests as tests\nImportError: No module named tests\n```\n\nI get pretty much the same thing from sage. \n\nBy the way that looks more like a procedure to do a spkg-check than a doctest.",
    "created_at": "2011-02-18T10:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99904",
    "user": "fbissey"
}
```

tests are not looking good to me.

```
Python 2.6.6 (r266:84292, Jan 28 2011, 01:59:55) 
[GCC 4.5.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import mpmath
>>> mpmath.runtests()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib64/python2.6/site-packages/mpmath/__init__.py", line 413, in runtests
    from .tests import runtests as tests
ImportError: No module named tests
```

I get pretty much the same thing from sage. 

By the way that looks more like a procedure to do a spkg-check than a doctest.



---

archive/issue_comments_099905.json:
```json
{
    "body": "Hmm... it doesn't seem like mpmath installed correctly for you.\n\nIs \"/usr/lib64/python2.6/site-packages\" actually the location of your Sage site-packages library, or is this a standalone installation of mpmath 0.17?",
    "created_at": "2011-02-18T10:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99905",
    "user": "fredrik.johansson"
}
```

Hmm... it doesn't seem like mpmath installed correctly for you.

Is "/usr/lib64/python2.6/site-packages" actually the location of your Sage site-packages library, or is this a standalone installation of mpmath 0.17?



---

archive/issue_comments_099906.json:
```json
{
    "body": "sorry for the noise I shouldn't post past 11pm. There is an issue in Gentoo and sage-on-gentoo but there shouldn't be any in a pure sage environment. It may take a little bit of time testing this on various hardware.",
    "created_at": "2011-02-19T08:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99906",
    "user": "fbissey"
}
```

sorry for the noise I shouldn't post past 11pm. There is an issue in Gentoo and sage-on-gentoo but there shouldn't be any in a pure sage environment. It may take a little bit of time testing this on various hardware.



---

archive/issue_comments_099907.json:
```json
{
    "body": "Something I have noticed in the gentoo ebuild. There is now an option to use matplotlib. Since matplotlib is shipped in sage mpmath may have to depend on it or configured not to use it.\n\nUsually people choose the first option in this case, unless there is major trouble. If you want to do that, the deps file in spkg/standard will need to be updated.",
    "created_at": "2011-02-19T09:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99907",
    "user": "fbissey"
}
```

Something I have noticed in the gentoo ebuild. There is now an option to use matplotlib. Since matplotlib is shipped in sage mpmath may have to depend on it or configured not to use it.

Usually people choose the first option in this case, unless there is major trouble. If you want to do that, the deps file in spkg/standard will need to be updated.



---

archive/issue_comments_099908.json:
```json
{
    "body": "I got a number of failing mpmath.doctests on my x86 box. A formatting issue really. Does any of the code interacts with ecl or maxima? The install I tested it on is based on 4.6.2.alpha4 with ecl-11.1.1 (#10766) and maxima-5.23.2 (#10773) and a couple of other patch that should be orthogonal (ppl #10039 and associated patches).\n\n```\nalmosteq 0.004\nfindroot **********************************************************************\nFile \"/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/calculus/optimization.py\", line 835, in NoName\nFailed example:\n    findroot(f, -10, solver='anewton', verbose=True)\nExpected:\n    x:     -9.88888888888888888889\n    error: 0.111111111111111111111\n    converging slowly\n    x:     -9.77890011223344556678\n    error: 0.10998877665544332211\n    converging slowly\n    x:     -9.67002233332199662166\n    error: 0.108877778911448945119\n    converging slowly\n    accelerating convergence\n    x:     -9.5622443299551077669\n    error: 0.107778003366888854764\n    converging slowly\n    x:     0.99999999999999999214\n    error: 10.562244329955107759\n    x:     1.0\n    error: 7.8598304758094664213e-18\n    1.0\nGot:\n    ('x:    ', -9.88888888888888888889)\n    ('error:', 0.111111111111111111111)\n    converging slowly\n    ('x:    ', -9.77890011223344556678)\n    ('error:', 0.10998877665544332211)\n    converging slowly\n    ('x:    ', -9.67002233332199662166)\n    ('error:', 0.108877778911448945119)\n    converging slowly\n    accelerating convergence\n    ('x:    ', -9.5622443299551077669)\n    ('error:', 0.107778003366888854764)\n    converging slowly\n    ('x:    ', 0.99999999999999999214)\n    ('error:', 10.562244329955107759)\n    ('x:    ', 1.0)\n    ('error:', 7.8598304758094664213e-18)\n    1.0\n0.132\n__name__ 0.001\n```\n\nand\n\n```\nsuperfac 0.05\nsecondzeta **********************************************************************\nFile \"/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/functions/zeta.py\", line 983, in NoName\nFailed example:\n    secondzeta(0.5 + 40j, error=True, verbose=True)\nExpected:\n    main term = (-30190318549.138656312556 - 13964804384.624622876523j)\n        computed using 19 zeros of zeta\n    prime term = (132717176.89212754625045 + 188980555.17563978290601j)\n        computed using 9 values of the von Mangoldt function\n    exponential term = (542447428666.07179812536 + 362434922978.80192435203j)\n    singular term = (512124392939.98154322355 + 348281138038.65531023921j)\n    ((0.059471043 + 0.3463514534j), 1.455191523e-11)\nGot:\n    ('main term =', (-30190318549.138656312556 - 13964804384.624622876523j))\n    ('    computed using', 19, 'zeros of zeta')\n    ('prime term =', (132717176.89212754625045 + 188980555.17563978290601j))\n    ('    computed using', 9, 'values of the von Mangoldt function')\n    ('exponential term =', (542447428666.07179812536 + 362434922978.80192435203j))\n    ('singular term =', (512124392939.98154322355 + 348281138038.65531023921j))\n    ((0.059471043 + 0.3463514534j), 1.455191523e-11)\n**********************************************************************\nFile \"/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/functions/zeta.py\", line 992, in NoName\nFailed example:\n    secondzeta(0.5 + 40j, a=0.04, error=True, verbose=True)\nExpected:\n    main term = (-151962888.19606243907725 - 217930683.90210294051982j)\n        computed using 9 zeros of zeta\n    prime term = (2476659342.3038722372461 + 28711581821.921627163136j)\n        computed using 37 values of the von Mangoldt function\n    exponential term = (178506047114.7838188264 + 819674143244.45677330576j)\n    singular term = (175877424884.22441310708 + 790744630738.28669174871j)\n    ((0.059471043 + 0.3463514534j), 1.455191523e-11)\nGot:\n    ('main term =', (-151962888.19606243907725 - 217930683.90210294051982j))\n    ('    computed using', 9, 'zeros of zeta')\n    ('prime term =', (2476659342.3038722372461 + 28711581821.921627163136j))\n    ('    computed using', 37, 'values of the von Mangoldt function')\n    ('exponential term =', (178506047114.7838188264 + 819674143244.45677330576j))\n    ('singular term =', (175877424884.22441310708 + 790744630738.28669174871j))\n    ((0.059471043 + 0.3463514534j), 1.455191523e-11)\n34.812\ninf 0.002\n```\n\nI am preparing a run on amd64 with a fresh 4.6.2.rc0 without any patches.",
    "created_at": "2011-02-21T08:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99908",
    "user": "fbissey"
}
```

I got a number of failing mpmath.doctests on my x86 box. A formatting issue really. Does any of the code interacts with ecl or maxima? The install I tested it on is based on 4.6.2.alpha4 with ecl-11.1.1 (#10766) and maxima-5.23.2 (#10773) and a couple of other patch that should be orthogonal (ppl #10039 and associated patches).

```
almosteq 0.004
findroot **********************************************************************
File "/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/calculus/optimization.py", line 835, in NoName
Failed example:
    findroot(f, -10, solver='anewton', verbose=True)
Expected:
    x:     -9.88888888888888888889
    error: 0.111111111111111111111
    converging slowly
    x:     -9.77890011223344556678
    error: 0.10998877665544332211
    converging slowly
    x:     -9.67002233332199662166
    error: 0.108877778911448945119
    converging slowly
    accelerating convergence
    x:     -9.5622443299551077669
    error: 0.107778003366888854764
    converging slowly
    x:     0.99999999999999999214
    error: 10.562244329955107759
    x:     1.0
    error: 7.8598304758094664213e-18
    1.0
Got:
    ('x:    ', -9.88888888888888888889)
    ('error:', 0.111111111111111111111)
    converging slowly
    ('x:    ', -9.77890011223344556678)
    ('error:', 0.10998877665544332211)
    converging slowly
    ('x:    ', -9.67002233332199662166)
    ('error:', 0.108877778911448945119)
    converging slowly
    accelerating convergence
    ('x:    ', -9.5622443299551077669)
    ('error:', 0.107778003366888854764)
    converging slowly
    ('x:    ', 0.99999999999999999214)
    ('error:', 10.562244329955107759)
    ('x:    ', 1.0)
    ('error:', 7.8598304758094664213e-18)
    1.0
0.132
__name__ 0.001
```

and

```
superfac 0.05
secondzeta **********************************************************************
File "/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/functions/zeta.py", line 983, in NoName
Failed example:
    secondzeta(0.5 + 40j, error=True, verbose=True)
Expected:
    main term = (-30190318549.138656312556 - 13964804384.624622876523j)
        computed using 19 zeros of zeta
    prime term = (132717176.89212754625045 + 188980555.17563978290601j)
        computed using 9 values of the von Mangoldt function
    exponential term = (542447428666.07179812536 + 362434922978.80192435203j)
    singular term = (512124392939.98154322355 + 348281138038.65531023921j)
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
Got:
    ('main term =', (-30190318549.138656312556 - 13964804384.624622876523j))
    ('    computed using', 19, 'zeros of zeta')
    ('prime term =', (132717176.89212754625045 + 188980555.17563978290601j))
    ('    computed using', 9, 'values of the von Mangoldt function')
    ('exponential term =', (542447428666.07179812536 + 362434922978.80192435203j))
    ('singular term =', (512124392939.98154322355 + 348281138038.65531023921j))
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
**********************************************************************
File "/home/francois/Work/sandbox/sage-4.6.2.alpha4/local/lib/python2.6/site-packages/mpmath/functions/zeta.py", line 992, in NoName
Failed example:
    secondzeta(0.5 + 40j, a=0.04, error=True, verbose=True)
Expected:
    main term = (-151962888.19606243907725 - 217930683.90210294051982j)
        computed using 9 zeros of zeta
    prime term = (2476659342.3038722372461 + 28711581821.921627163136j)
        computed using 37 values of the von Mangoldt function
    exponential term = (178506047114.7838188264 + 819674143244.45677330576j)
    singular term = (175877424884.22441310708 + 790744630738.28669174871j)
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
Got:
    ('main term =', (-151962888.19606243907725 - 217930683.90210294051982j))
    ('    computed using', 9, 'zeros of zeta')
    ('prime term =', (2476659342.3038722372461 + 28711581821.921627163136j))
    ('    computed using', 37, 'values of the von Mangoldt function')
    ('exponential term =', (178506047114.7838188264 + 819674143244.45677330576j))
    ('singular term =', (175877424884.22441310708 + 790744630738.28669174871j))
    ((0.059471043 + 0.3463514534j), 1.455191523e-11)
34.812
inf 0.002
```

I am preparing a run on amd64 with a fresh 4.6.2.rc0 without any patches.



---

archive/issue_comments_099909.json:
```json
{
    "body": "These two failures were noted in a previous comment. They can safely be ignored.",
    "created_at": "2011-02-21T09:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99909",
    "user": "fredrik.johansson"
}
```

These two failures were noted in a previous comment. They can safely be ignored.



---

archive/issue_comments_099910.json:
```json
{
    "body": "Replying to [comment:24 fredrik.johansson]:\n> These two failures were noted in a previous comment. They can safely be ignored.\n\nI didn't realise they were the same one. I guess I expected they were fixed but that would require a new version of mpmath, not just sage patch I imagine.\nOnce I have tested this at least on amd64 I can give a positive review.",
    "created_at": "2011-02-21T09:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99910",
    "user": "fbissey"
}
```

Replying to [comment:24 fredrik.johansson]:
> These two failures were noted in a previous comment. They can safely be ignored.

I didn't realise they were the same one. I guess I expected they were fixed but that would require a new version of mpmath, not just sage patch I imagine.
Once I have tested this at least on amd64 I can give a positive review.



---

archive/issue_comments_099911.json:
```json
{
    "body": "OK so I tested this on linux-amd64 and OS X (10.5). and the tests perform ok.\nAlthough there is some noise on OS X because the wrong version of freetype is detected. I am not sure that the spkg fault or not.\n\n```\ntest_visualization\n    axes                      dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib\n  Referenced from: /usr/X11/bin/fc-list\n  Reason: Incompatible library version: fc-list requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0\ndyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib\n  Referenced from: /usr/X11/bin/fc-list\n  Reason: Incompatible library version: fc-list requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0\nok        6.5380421 s\n\nfinished tests in 17.99 seconds\n```\n\nOn further inspection this test is run because matplotlib is present and I assume that this message originates from matplotlib. So the problem is probably in matplotlib.\n\nThe last thing is whether we make matplotlib a dependency of mpmath or not.\nI will post a patch making this the default. Voice any opposition then.",
    "created_at": "2011-02-21T21:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99911",
    "user": "fbissey"
}
```

OK so I tested this on linux-amd64 and OS X (10.5). and the tests perform ok.
Although there is some noise on OS X because the wrong version of freetype is detected. I am not sure that the spkg fault or not.

```
test_visualization
    axes                      dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib
  Referenced from: /usr/X11/bin/fc-list
  Reason: Incompatible library version: fc-list requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0
dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib
  Referenced from: /usr/X11/bin/fc-list
  Reason: Incompatible library version: fc-list requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0
ok        6.5380421 s

finished tests in 17.99 seconds
```

On further inspection this test is run because matplotlib is present and I assume that this message originates from matplotlib. So the problem is probably in matplotlib.

The last thing is whether we make matplotlib a dependency of mpmath or not.
I will post a patch making this the default. Voice any opposition then.



---

archive/issue_comments_099912.json:
```json
{
    "body": "Attachment [mpmath-deps.patch](tarball://root/attachments/some-uuid/ticket9969/mpmath-deps.patch) by fbissey created at 2011-02-21 21:19:24\n\npatch to deps to make mpmath depend on matplotlib",
    "created_at": "2011-02-21T21:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99912",
    "user": "fbissey"
}
```

Attachment [mpmath-deps.patch](tarball://root/attachments/some-uuid/ticket9969/mpmath-deps.patch) by fbissey created at 2011-02-21 21:19:24

patch to deps to make mpmath depend on matplotlib



---

archive/issue_comments_099913.json:
```json
{
    "body": "Fredrik, a question about mpmath behavior with regards to matplotlib. Is mpmath detecting matplotlib at compilation time or its presence at runtime?",
    "created_at": "2011-03-13T22:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99913",
    "user": "fbissey"
}
```

Fredrik, a question about mpmath behavior with regards to matplotlib. Is mpmath detecting matplotlib at compilation time or its presence at runtime?



---

archive/issue_comments_099914.json:
```json
{
    "body": "Runtime. In fact, it only attempts to import matplotlib from inside the plotting functions (which are pure Python).",
    "created_at": "2011-03-13T23:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99914",
    "user": "fredrik.johansson"
}
```

Runtime. In fact, it only attempts to import matplotlib from inside the plotting functions (which are pure Python).



---

archive/issue_comments_099915.json:
```json
{
    "body": "Thanks, that means we don't need to depend on it. I am giving this a positive review. Hopefully it will be picked up for 4.7.",
    "created_at": "2011-03-14T00:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99915",
    "user": "fbissey"
}
```

Thanks, that means we don't need to depend on it. I am giving this a positive review. Hopefully it will be picked up for 4.7.



---

archive/issue_comments_099916.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-14T00:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99916",
    "user": "fbissey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099917.json:
```json
{
    "body": "Please change the commit message (using `hg qrefresh -e`) such that the ticket number appears on the first line.",
    "created_at": "2011-03-27T13:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99917",
    "user": "jdemeyer"
}
```

Please change the commit message (using `hg qrefresh -e`) such that the ticket number appears on the first line.



---

archive/issue_comments_099918.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-03-27T13:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99918",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099919.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-04-11T13:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99919",
    "user": "jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_099920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-11T19:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99920",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_099921.json:
```json
{
    "body": "Sorry I meant to do the refresh but I was unable to get it working.",
    "created_at": "2011-04-13T02:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99921",
    "user": "fbissey"
}
```

Sorry I meant to do the refresh but I was unable to get it working.



---

archive/issue_comments_099922.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-05-04T09:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99922",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_099923.json:
```json
{
    "body": "The files `SPKG.txt` and `spkg-install` should be put under hg control.  Also, SPKG.txt should not be executable.  Please fix these trivial issues.",
    "created_at": "2011-05-04T09:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99923",
    "user": "jdemeyer"
}
```

The files `SPKG.txt` and `spkg-install` should be put under hg control.  Also, SPKG.txt should not be executable.  Please fix these trivial issues.



---

archive/issue_comments_099924.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-05-04T09:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99924",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_099925.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2011-05-04T09:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99925",
    "user": "jdemeyer"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_099926.json:
```json
{
    "body": "I can fix the permissions in the spkg. What is involved to put SPKG.txt and spkg-install under hg control?",
    "created_at": "2011-05-04T09:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99926",
    "user": "fredrik.johansson"
}
```

I can fix the permissions in the spkg. What is involved to put SPKG.txt and spkg-install under hg control?



---

archive/issue_comments_099927.json:
```json
{
    "body": "Replying to [comment:38 fredrik.johansson]:\n> I can fix the permissions in the spkg. What is involved to put SPKG.txt and spkg-install under hg control?\n\nNever mind.  I did it myself: [http://boxen.math.washington.edu/home/jdemeyer/spkg/mpmath-0.17.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/mpmath-0.17.spkg)",
    "created_at": "2011-05-04T12:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99927",
    "user": "jdemeyer"
}
```

Replying to [comment:38 fredrik.johansson]:
> I can fix the permissions in the spkg. What is involved to put SPKG.txt and spkg-install under hg control?

Never mind.  I did it myself: [http://boxen.math.washington.edu/home/jdemeyer/spkg/mpmath-0.17.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/mpmath-0.17.spkg)



---

archive/issue_comments_099928.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-04T12:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99928",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-06T07:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9968#issuecomment-99929",
    "user": "jdemeyer"
}
```

Resolution: fixed
