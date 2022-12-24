# Issue 9940: faster multinomial_coefficients

archive/issues_009940.json:
```json
{
    "body": "Assignee: @aghitza\n\nWith the attached patch multinomial_coefficients(m,n) becomes faster\nthan the unpatched version as m increases\n\nSage-4.5.1\nsage: %timeit w = multinomial_coefficients(int(20),int(5))\n5 loops, best of 3: 4.91 s per loop\n\nwith patch:\nsage: %timeit w = multinomial_coefficients(int(20),int(5))\n5 loops, best of 3: 1.05 s per loop\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9941\n\n",
    "created_at": "2010-09-18T15:43:36Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "faster multinomial_coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9940",
    "user": "pernici"
}
```
Assignee: @aghitza

With the attached patch multinomial_coefficients(m,n) becomes faster
than the unpatched version as m increases

Sage-4.5.1
sage: %timeit w = multinomial_coefficients(int(20),int(5))
5 loops, best of 3: 4.91 s per loop

with patch:
sage: %timeit w = multinomial_coefficients(int(20),int(5))
5 loops, best of 3: 1.05 s per loop



Issue created by migration from https://trac.sagemath.org/ticket/9941





---

archive/issue_comments_098973.json:
```json
{
    "body": "Attachment [trac_9941_faster_multinomial_coefficients.patch](tarball://root/attachments/some-uuid/ticket9941/trac_9941_faster_multinomial_coefficients.patch) by ylchapuy created at 2010-09-21 08:05:04\n\nI think I got an even faster implementation.\nI'm sorry but I don't have a development Sage handy for the next days, so I just put the code here.\nIf you want to make a clean patch with this, go ahead; otherwise, I will do it in some days when I'm back home.\n\n\n```\ndef multinomial_coefficients(m, n):\n    if m == 2:\n        return binomial_coefficients(n)\n    t = [n] + [0] * (m - 1)\n    r = {tuple(t): 1}\n    if n:\n        p0 = 0 # leftmost nonzero position\n    else:\n        p0 = m\n    # enumerate tuples in co-lex order\n    while p0 < m - 1:\n        # compute next tuple\n        j = p0\n        tj = t[j]\n        t[j+1] += 1\n        if j:\n            t[0] = tj\n            t[j] = 0\n        if tj > 1:\n            p0 = 0\n            start = 1\n        else:\n            p0 += 1\n            start = p0\n        # compute the value\n        v = 0\n        for k in xrange(start, m):\n            if t[k]:\n                t[k] -= 1\n                v += r[tuple(t)]\n                t[k] += 1\n        t[0] -= 1\n        r[tuple(t)] = (v * tj) // (n - t[0])\n    return r\n```\n",
    "created_at": "2010-09-21T08:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98973",
    "user": "ylchapuy"
}
```

Attachment [trac_9941_faster_multinomial_coefficients.patch](tarball://root/attachments/some-uuid/ticket9941/trac_9941_faster_multinomial_coefficients.patch) by ylchapuy created at 2010-09-21 08:05:04

I think I got an even faster implementation.
I'm sorry but I don't have a development Sage handy for the next days, so I just put the code here.
If you want to make a clean patch with this, go ahead; otherwise, I will do it in some days when I'm back home.


```
def multinomial_coefficients(m, n):
    if m == 2:
        return binomial_coefficients(n)
    t = [n] + [0] * (m - 1)
    r = {tuple(t): 1}
    if n:
        p0 = 0 # leftmost nonzero position
    else:
        p0 = m
    # enumerate tuples in co-lex order
    while p0 < m - 1:
        # compute next tuple
        j = p0
        tj = t[j]
        t[j+1] += 1
        if j:
            t[0] = tj
            t[j] = 0
        if tj > 1:
            p0 = 0
            start = 1
        else:
            p0 += 1
            start = p0
        # compute the value
        v = 0
        for k in xrange(start, m):
            if t[k]:
                t[k] -= 1
                v += r[tuple(t)]
                t[k] += 1
        t[0] -= 1
        r[tuple(t)] = (v * tj) // (n - t[0])
    return r
```




---

archive/issue_comments_098974.json:
```json
{
    "body": "Attachment [trac9941-even_faster_multinomial_coefficients.patch](tarball://root/attachments/some-uuid/ticket9941/trac9941-even_faster_multinomial_coefficients.patch) by ylchapuy created at 2010-09-22 14:17:32",
    "created_at": "2010-09-22T14:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98974",
    "user": "ylchapuy"
}
```

Attachment [trac9941-even_faster_multinomial_coefficients.patch](tarball://root/attachments/some-uuid/ticket9941/trac9941-even_faster_multinomial_coefficients.patch) by ylchapuy created at 2010-09-22 14:17:32



---

archive/issue_comments_098975.json:
```json
{
    "body": "Apply only http://trac.sagemath.org/sage_trac/attachment/ticket/9941/trac9941-even_faster_multinomial_coefficients.patch .\nWith it applied, I got `260 ms` for the same test on my computer.",
    "created_at": "2010-09-22T14:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98975",
    "user": "ylchapuy"
}
```

Apply only http://trac.sagemath.org/sage_trac/attachment/ticket/9941/trac9941-even_faster_multinomial_coefficients.patch .
With it applied, I got `260 ms` for the same test on my computer.



---

archive/issue_comments_098976.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T14:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98976",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098977.json:
```json
{
    "body": "up... any chance someone review this ticket?",
    "created_at": "2010-10-11T06:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98977",
    "user": "ylchapuy"
}
```

up... any chance someone review this ticket?



---

archive/issue_comments_098978.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-14T11:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98978",
    "user": "fwclarke"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098979.json:
```json
{
    "body": "I've tested this, and confirmed that the \"even_faster\" patch is indeed significantly faster and delivers correct results.  It's *almost* a positive review, except for two minor things:\n\n1. Erroneous results are returned if `m` is zero. E.g.,\n\n   * \n\n```\nsage: multinomial_coefficients(0, 3)\n{(3,): 1}\n```\n\n\nTo be consistent with `multinomial([])`, which returns `1`, `multinomial_coefficients(0, n)` should return `{(), 1)}` if `n` is zero, and `{}` otherwise.\n\n2. I don't understand the comment \"`the very first step was mixed above\"`, the word *mixed* in particular.\n\nOne other thing that might be worth changing would be to allow `multinomial` to take a tuple as its argument.  Then `multinomial_coefficients` could have a doctest like\n\n\n```\nsage: r = multinomial_coefficients(4, 3)\nsage: all(multinomial(k) == v for k, v in r.items())\nTrue\n```\n",
    "created_at": "2010-11-14T11:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98979",
    "user": "fwclarke"
}
```

I've tested this, and confirmed that the "even_faster" patch is indeed significantly faster and delivers correct results.  It's *almost* a positive review, except for two minor things:

1. Erroneous results are returned if `m` is zero. E.g.,

   * 

```
sage: multinomial_coefficients(0, 3)
{(3,): 1}
```


To be consistent with `multinomial([])`, which returns `1`, `multinomial_coefficients(0, n)` should return `{(), 1)}` if `n` is zero, and `{}` otherwise.

2. I don't understand the comment "`the very first step was mixed above"`, the word *mixed* in particular.

One other thing that might be worth changing would be to allow `multinomial` to take a tuple as its argument.  Then `multinomial_coefficients` could have a doctest like


```
sage: r = multinomial_coefficients(4, 3)
sage: all(multinomial(k) == v for k, v in r.items())
True
```




---

archive/issue_comments_098980.json:
```json
{
    "body": "Attachment [trac9941-corrections.patch](tarball://root/attachments/some-uuid/ticket9941/trac9941-corrections.patch) by ylchapuy created at 2010-11-14 23:08:37\n\nI attached a patch to be applied after the 'even_faster' one.\n\nIt corrects the behavior for `m=0`. It also change the comment.\nI just wanted to say that the initialization of v (which is part of the computation of the value) is done within the code for enumerating the tuples.\n\nRegarding the modification of `multinomial`, I leave this for another ticket.",
    "created_at": "2010-11-14T23:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98980",
    "user": "ylchapuy"
}
```

Attachment [trac9941-corrections.patch](tarball://root/attachments/some-uuid/ticket9941/trac9941-corrections.patch) by ylchapuy created at 2010-11-14 23:08:37

I attached a patch to be applied after the 'even_faster' one.

It corrects the behavior for `m=0`. It also change the comment.
I just wanted to say that the initialization of v (which is part of the computation of the value) is done within the code for enumerating the tuples.

Regarding the modification of `multinomial`, I leave this for another ticket.



---

archive/issue_comments_098981.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-11-15T07:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98981",
    "user": "fwclarke"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_098982.json:
```json
{
    "body": "Fine now with these two patches. \u00a0Positive review.",
    "created_at": "2010-11-15T07:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98982",
    "user": "fwclarke"
}
```

Fine now with these two patches.  Positive review.



---

archive/issue_comments_098983.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-12-02T14:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98983",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_098984.json:
```json
{
    "body": "You should add an example/test for the last patch, i.e. for the case m = 0.",
    "created_at": "2010-12-02T14:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98984",
    "user": "@jdemeyer"
}
```

You should add an example/test for the last patch, i.e. for the case m = 0.



---

archive/issue_comments_098985.json:
```json
{
    "body": "Attachment [trac9941_second_review.patch](tarball://root/attachments/some-uuid/ticket9941/trac9941_second_review.patch) by ylchapuy created at 2010-12-02 19:46:33",
    "created_at": "2010-12-02T19:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98985",
    "user": "ylchapuy"
}
```

Attachment [trac9941_second_review.patch](tarball://root/attachments/some-uuid/ticket9941/trac9941_second_review.patch) by ylchapuy created at 2010-12-02 19:46:33



---

archive/issue_comments_098986.json:
```json
{
    "body": "Here it is. Apply in order:\n\n* trac9941-even_faster_multinomial_coefficients.patch\n* trac9941-corrections.patch\n* trac9941_second_review.patch",
    "created_at": "2010-12-02T19:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98986",
    "user": "ylchapuy"
}
```

Here it is. Apply in order:

* trac9941-even_faster_multinomial_coefficients.patch
* trac9941-corrections.patch
* trac9941_second_review.patch



---

archive/issue_comments_098987.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-02T19:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98987",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098988.json:
```json
{
    "body": "The new patch does the job.",
    "created_at": "2010-12-02T21:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98988",
    "user": "fwclarke"
}
```

The new patch does the job.



---

archive/issue_comments_098989.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-02T21:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98989",
    "user": "fwclarke"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9940#issuecomment-98990",
    "user": "@jdemeyer"
}
```

Resolution: fixed
