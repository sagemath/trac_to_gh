# Issue 864: Asymptotically slow pari <--> python long conversions

archive/issues_000864.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: pari\n\nThis is really a leftover from ticket #467, split because I wanted the first half of the fix to make it into 2.8.7. Here's a summary of the badness:\n\n\n```\nsage: x = 10^100000\n\nsage: time y = pari(x)\nCPU times: user 1.18 s, sys: 0.01 s, total: 1.19 s\nWall time: 1.26\n\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.02\n\nsage: time u = int(y)\nCPU times: user 1.94 s, sys: 1.33 s, total: 3.27 s\nWall time: 3.58\n\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.03\n\n\nsage: x = 10^1000000\n\nsage: time y = pari(x)\nCPU times: user 105.12 s, sys: 1.26 s, total: 106.38 s\nWall time: 121.86\n\nsage: time z = Integer(y)\nCPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s\nWall time: 0.09\n\nsage: time u = int(y)\nCPU times: user 188.17 s, sys: 145.12 s, total: 333.28 s\nWall time: 364.80\n\nsage: time u = int(Integer(y))\nCPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s\nWall time: 0.07\n```\n\n\nAnd here's the state of affairs after the first patch:\n\n\n```\nsage: x = 10^100000\n\nsage: time y = pari(x)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time u = int(y)\nCPU times: user 1.64 s, sys: 1.09 s, total: 2.73 s\nWall time: 2.79\n\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: x = 10^1000000\n\nsage: time y = pari(x)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n\nsage: time u = int(y)\nCPU times: user 220.90 s, sys: 137.34 s, total: 358.24 s\nWall time: 408.11\n\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n\n```\n\n\nClearly that third function call needs to be fixed, and it will be within a few days.\n\nIssue created by migration from https://trac.sagemath.org/ticket/864\n\n",
    "created_at": "2007-10-12T19:47:59Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.13",
    "title": "Asymptotically slow pari <--> python long conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/864",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

Keywords: pari

This is really a leftover from ticket #467, split because I wanted the first half of the fix to make it into 2.8.7. Here's a summary of the badness:


```
sage: x = 10^100000

sage: time y = pari(x)
CPU times: user 1.18 s, sys: 0.01 s, total: 1.19 s
Wall time: 1.26

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.02

sage: time u = int(y)
CPU times: user 1.94 s, sys: 1.33 s, total: 3.27 s
Wall time: 3.58

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.03


sage: x = 10^1000000

sage: time y = pari(x)
CPU times: user 105.12 s, sys: 1.26 s, total: 106.38 s
Wall time: 121.86

sage: time z = Integer(y)
CPU times: user 0.03 s, sys: 0.02 s, total: 0.05 s
Wall time: 0.09

sage: time u = int(y)
CPU times: user 188.17 s, sys: 145.12 s, total: 333.28 s
Wall time: 364.80

sage: time u = int(Integer(y))
CPU times: user 0.04 s, sys: 0.02 s, total: 0.06 s
Wall time: 0.07
```


And here's the state of affairs after the first patch:


```
sage: x = 10^100000

sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time u = int(y)
CPU times: user 1.64 s, sys: 1.09 s, total: 2.73 s
Wall time: 2.79

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: x = 10^1000000

sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01

sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00

sage: time u = int(y)
CPU times: user 220.90 s, sys: 137.34 s, total: 358.24 s
Wall time: 408.11

sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01

```


Clearly that third function call needs to be fixed, and it will be within a few days.

Issue created by migration from https://trac.sagemath.org/ticket/864





---

archive/issue_comments_005331.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-12T19:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5331",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005332.json:
```json
{
    "body": "Hi Craig,\n\nthis has been open a while. The current timings from sage.math:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: x = 10^100000\nsage: time y = pari(x)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: time z = Integer(y)\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: time u = int(y)\nCPU times: user 0.48 s, sys: 0.00 s, total: 0.48 s\nWall time: 0.48 s\nsage: time u = int(Integer(y))\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n```\n",
    "created_at": "2008-12-13T11:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5332",
    "user": "mabshoff"
}
```

Hi Craig,

this has been open a while. The current timings from sage.math:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x = 10^100000
sage: time y = pari(x)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time z = Integer(y)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time u = int(y)
CPU times: user 0.48 s, sys: 0.00 s, total: 0.48 s
Wall time: 0.48 s
sage: time u = int(Integer(y))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```




---

archive/issue_comments_005333.json:
```json
{
    "body": "Changing component from interfaces to performance.",
    "created_at": "2013-09-09T18:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5333",
    "user": "@pjbruin"
}
```

Changing component from interfaces to performance.



---

archive/issue_comments_005334.json:
```json
{
    "body": "I am uploading a patch that implements conversion from PARI `t_INT` to Python long via an intermediate `mpz_t`, so `long(y)` essentially does `long(Integer(y))`.\n\nSome timings:\n\n```\nsage: x = 10^1000000\nsage: %timeit y=pari(x)\n10000 loops, best of 3: 197 us per loop\nsage: %timeit z=Integer(y)\n100 loops, best of 3: 4.11 ms per loop\nsage: %timeit u=long(y)\n100 loops, best of 3: 13 ms per loop\nsage: %timeit u=long(Integer(y))\n100 loops, best of 3: 13.8 ms per loop\n\nsage: x = 10^10000000\nsage: %timeit y=pari(x)                                                         \n100 loops, best of 3: 5.57 ms per loop\nsage: %timeit z=Integer(y)\n100 loops, best of 3: 2.94 ms per loop\nsage: %timeit u=long(y)\n100 loops, best of 3: 13.9 ms per loop\nsage: %timeit u=long(Integer(y))\n100 loops, best of 3: 13.8 ms per loop\n```\n",
    "created_at": "2013-09-09T18:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5334",
    "user": "@pjbruin"
}
```

I am uploading a patch that implements conversion from PARI `t_INT` to Python long via an intermediate `mpz_t`, so `long(y)` essentially does `long(Integer(y))`.

Some timings:

```
sage: x = 10^1000000
sage: %timeit y=pari(x)
10000 loops, best of 3: 197 us per loop
sage: %timeit z=Integer(y)
100 loops, best of 3: 4.11 ms per loop
sage: %timeit u=long(y)
100 loops, best of 3: 13 ms per loop
sage: %timeit u=long(Integer(y))
100 loops, best of 3: 13.8 ms per loop

sage: x = 10^10000000
sage: %timeit y=pari(x)                                                         
100 loops, best of 3: 5.57 ms per loop
sage: %timeit z=Integer(y)
100 loops, best of 3: 2.94 ms per loop
sage: %timeit u=long(y)
100 loops, best of 3: 13.9 ms per loop
sage: %timeit u=long(Integer(y))
100 loops, best of 3: 13.8 ms per loop
```




---

archive/issue_comments_005335.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-09-09T18:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5335",
    "user": "@pjbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_005336.json:
```json
{
    "body": "Attachment [trac_864-pari_long_conversion.patch](tarball://root/attachments/some-uuid/ticket864/trac_864-pari_long_conversion.patch) by @pjbruin created at 2013-09-09 18:40:22",
    "created_at": "2013-09-09T18:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5336",
    "user": "@pjbruin"
}
```

Attachment [trac_864-pari_long_conversion.patch](tarball://root/attachments/some-uuid/ticket864/trac_864-pari_long_conversion.patch) by @pjbruin created at 2013-09-09 18:40:22



---

archive/issue_comments_005337.json:
```json
{
    "body": "Replying to [comment:4 pbruin]:\n> so `long(y)` essentially does `long(Integer(y))`.\nWhy not literally do `long(Integer(y))` then and save many lines of code?",
    "created_at": "2013-10-29T07:45:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5337",
    "user": "@jdemeyer"
}
```

Replying to [comment:4 pbruin]:
> so `long(y)` essentially does `long(Integer(y))`.
Why not literally do `long(Integer(y))` then and save many lines of code?



---

archive/issue_comments_005338.json:
```json
{
    "body": "Note that this works:\n\n```\nsage: Integer(pari(\"Mod(2,7)\"))\n2\n```\n\nso you would get these cases for free...",
    "created_at": "2013-10-29T07:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5338",
    "user": "@jdemeyer"
}
```

Note that this works:

```
sage: Integer(pari("Mod(2,7)"))
2
```

so you would get these cases for free...



---

archive/issue_comments_005339.json:
```json
{
    "body": "Replying to [comment:5 jdemeyer]:\n> Replying to [comment:4 pbruin]:\n> > so `long(y)` essentially does `long(Integer(y))`.\n> Why not literally do `long(Integer(y))` then and save many lines of code?\nI thought that the penalty for creating an `Integer` was quite heavy in some cases; for example, with the current patch applied, I get\n\n```\nsage: y=pari(10^10000)\nsage: %timeit -c -r 1 u=long(y)\n100000 loops, best of 1: 12.2 us per loop\nsage: %timeit -c -r 1 u=long(Integer(y))\n10000 loops, best of 1: 19.6 us per loop\n```\n\nHowever, I just tried implementing `gen.__long__(self)` as `return long(Integer(self))`, and it is just as fast, thanks to Cython I guess.  I also agree that `long(pari(\"Mod(2,7)\"))` is nice to get for free.  New patch coming soon.",
    "created_at": "2013-10-29T11:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5339",
    "user": "@pjbruin"
}
```

Replying to [comment:5 jdemeyer]:
> Replying to [comment:4 pbruin]:
> > so `long(y)` essentially does `long(Integer(y))`.
> Why not literally do `long(Integer(y))` then and save many lines of code?
I thought that the penalty for creating an `Integer` was quite heavy in some cases; for example, with the current patch applied, I get

```
sage: y=pari(10^10000)
sage: %timeit -c -r 1 u=long(y)
100000 loops, best of 1: 12.2 us per loop
sage: %timeit -c -r 1 u=long(Integer(y))
10000 loops, best of 1: 19.6 us per loop
```

However, I just tried implementing `gen.__long__(self)` as `return long(Integer(self))`, and it is just as fast, thanks to Cython I guess.  I also agree that `long(pari("Mod(2,7)"))` is nice to get for free.  New patch coming soon.



---

archive/issue_comments_005340.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-10-29T11:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5340",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_005341.json:
```json
{
    "body": "Attachment [trac_864-pari_int_long_conversion.patch](tarball://root/attachments/some-uuid/ticket864/trac_864-pari_int_long_conversion.patch) by @pjbruin created at 2013-10-29 12:13:23",
    "created_at": "2013-10-29T12:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5341",
    "user": "@pjbruin"
}
```

Attachment [trac_864-pari_int_long_conversion.patch](tarball://root/attachments/some-uuid/ticket864/trac_864-pari_int_long_conversion.patch) by @pjbruin created at 2013-10-29 12:13:23



---

archive/issue_comments_005342.json:
```json
{
    "body": "apply trac_864-pari_int_long_conversion.patch",
    "created_at": "2013-10-29T12:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5342",
    "user": "@pjbruin"
}
```

apply trac_864-pari_int_long_conversion.patch



---

archive/issue_comments_005343.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-10-29T12:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5343",
    "user": "@pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_005344.json:
```json
{
    "body": "Looks good!",
    "created_at": "2013-10-31T08:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5344",
    "user": "@jdemeyer"
}
```

Looks good!



---

archive/issue_comments_005345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-31T08:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/864#issuecomment-5345",
    "user": "@jdemeyer"
}
```

Resolution: fixed
