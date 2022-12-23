# Issue 2053: creating symbolic matrices is insanely slow

archive/issues_002053.json:
```json
{
    "body": "Assignee: was\n\nOn the fastest modern hardware we have:\n\n\n```\nsage: time m = matrix(SR, 20, [1..20^2])\nCPU times: user 0.34 s, sys: 0.12 s, total: 0.45 s\nWall time: 1.05\n```\n\nwhich is frickin' slow.  And the time isn't just in coercion, since\n\n```\nsage: time v = [SR(a) for a in [1..20^2]]\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2053\n\n",
    "created_at": "2008-02-05T14:28:48Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "creating symbolic matrices is insanely slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2053",
    "user": "was"
}
```
Assignee: was

On the fastest modern hardware we have:


```
sage: time m = matrix(SR, 20, [1..20^2])
CPU times: user 0.34 s, sys: 0.12 s, total: 0.45 s
Wall time: 1.05
```

which is frickin' slow.  And the time isn't just in coercion, since

```
sage: time v = [SR(a) for a in [1..20^2]]
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
```


Issue created by migration from https://trac.sagemath.org/ticket/2053





---

archive/issue_comments_013289.json:
```json
{
    "body": "The attached patch fixes this problem.  Now the following works and speeds\nup the above benchmark by a huge amount:\n\n```\nsage: time m = matrix(SR, 20, [1..20^2])\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.07\nsage: time m = matrix(SR, 50, [1..50^2])\nCPU times: user 0.07 s, sys: 0.02 s, total: 0.09 s\nWall time: 0.46\nsage: time m = matrix(SR, 100, [1..100^2])\nCPU times: user 0.26 s, sys: 0.02 s, total: 0.27 s\nWall time: 0.49\n```\n\n\nEven a 500x500 matrix is possible, which used to be out\nof the question. \n\n```\nsage: time m = matrix(SR, 500, [1..500^2])\nCPU times: user 6.79 s, sys: 0.39 s, total: 7.17 s\nWall time: 13.32\n```\n",
    "created_at": "2008-02-05T14:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13289",
    "user": "was"
}
```

The attached patch fixes this problem.  Now the following works and speeds
up the above benchmark by a huge amount:

```
sage: time m = matrix(SR, 20, [1..20^2])
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.07
sage: time m = matrix(SR, 50, [1..50^2])
CPU times: user 0.07 s, sys: 0.02 s, total: 0.09 s
Wall time: 0.46
sage: time m = matrix(SR, 100, [1..100^2])
CPU times: user 0.26 s, sys: 0.02 s, total: 0.27 s
Wall time: 0.49
```


Even a 500x500 matrix is possible, which used to be out
of the question. 

```
sage: time m = matrix(SR, 500, [1..500^2])
CPU times: user 6.79 s, sys: 0.39 s, total: 7.17 s
Wall time: 13.32
```




---

archive/issue_comments_013290.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-05T14:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13290",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_013291.json:
```json
{
    "body": "I cannot apply this due to a failed hunk with the docstring in set_from_list.",
    "created_at": "2008-02-06T04:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13291",
    "user": "mhansen"
}
```

I cannot apply this due to a failed hunk with the docstring in set_from_list.



---

archive/issue_comments_013292.json:
```json
{
    "body": "Attachment\n\napply this *INSTEAD*!",
    "created_at": "2008-02-06T19:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13292",
    "user": "was"
}
```

Attachment

apply this *INSTEAD*!



---

archive/issue_comments_013293.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-07T07:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13293",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_013294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T10:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13294",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013295.json:
```json
{
    "body": "Merged the second patch only in Sage 2.10.2.alpha2",
    "created_at": "2008-02-07T10:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2053",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2053#issuecomment-13295",
    "user": "mabshoff"
}
```

Merged the second patch only in Sage 2.10.2.alpha2
