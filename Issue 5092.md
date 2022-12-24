# Issue 5092: Primes()?? gets hung in len call

archive/issues_005092.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5092\n\n",
    "created_at": "2009-01-25T02:11:19Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Primes()?? gets hung in len call",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5092",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/5092





---

archive/issue_comments_038802.json:
```json
{
    "body": "You don't need the first two lines below in __cmp__ anymore.\n\n```\n        if isinstance(right, Primes_class):\n            return 0\n        return cmp(type(self), type(right))\n```\n\n\nOtherwise, it's a positive review.",
    "created_at": "2009-01-25T02:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38802",
    "user": "saliola"
}
```

You don't need the first two lines below in __cmp__ anymore.

```
        if isinstance(right, Primes_class):
            return 0
        return cmp(type(self), type(right))
```


Otherwise, it's a positive review.



---

archive/issue_comments_038803.json:
```json
{
    "body": "This patch causes one doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/sets/set.py\"                 \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/sets/set.py\", line 278:\n    sage: Primes() < Set(QQ)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T18:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38803",
    "user": "mabshoff"
}
```

This patch causes one doctest failure:

```
sage -t -long "devel/sage/sage/sets/set.py"                 
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/sets/set.py", line 278:
    sage: Primes() < Set(QQ)
Expected:
    True
Got:
    False
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_038804.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> This patch causes one doctest failure:\n\nThis is a weird test. I'm not even sure that it says anything meaningful. In fact, according to the documentation of __cmp__ for Set, it doesn't:\n\n```\n        \\note{If $X < Y$ is true this does \\emph{not} necessarily mean\n        that $X$ is a subset of $Y$.  Also, any two sets can be\n        compared, which is a general Python philosophy.}\n```\n",
    "created_at": "2009-02-02T21:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38804",
    "user": "saliola"
}
```

Replying to [comment:5 mabshoff]:
> This patch causes one doctest failure:

This is a weird test. I'm not even sure that it says anything meaningful. In fact, according to the documentation of __cmp__ for Set, it doesn't:

```
        \note{If $X < Y$ is true this does \emph{not} necessarily mean
        that $X$ is a subset of $Y$.  Also, any two sets can be
        compared, which is a general Python philosophy.}
```




---

archive/issue_comments_038805.json:
```json
{
    "body": "See #5933, which brings the coverage to 100% and was merged in 3.4.2.rc0.",
    "created_at": "2009-04-30T12:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38805",
    "user": "AlexGhitza"
}
```

See #5933, which brings the coverage to 100% and was merged in 3.4.2.rc0.



---

archive/issue_comments_038806.json:
```json
{
    "body": "Well, there is still a potential bug fix in here, so can someone take a look and extra a potential fix?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T07:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38806",
    "user": "mabshoff"
}
```

Well, there is still a potential bug fix in here, so can someone take a look and extra a potential fix?

Cheers,

Michael



---

archive/issue_comments_038807.json:
```json
{
    "body": "Attachment [trac_5092.patch](tarball://root/attachments/some-uuid/ticket5092/trac_5092.patch) by mhansen created at 2009-10-19 19:25:44",
    "created_at": "2009-10-19T19:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38807",
    "user": "mhansen"
}
```

Attachment [trac_5092.patch](tarball://root/attachments/some-uuid/ticket5092/trac_5092.patch) by mhansen created at 2009-10-19 19:25:44



---

archive/issue_comments_038808.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-19T19:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38808",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_038809.json:
```json
{
    "body": "I've rebased the patch of #5933.",
    "created_at": "2009-10-19T19:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38809",
    "user": "mhansen"
}
```

I've rebased the patch of #5933.



---

archive/issue_comments_038810.json:
```json
{
    "body": "err, on top of #5933",
    "created_at": "2009-10-19T19:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38810",
    "user": "mhansen"
}
```

err, on top of #5933



---

archive/issue_comments_038811.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-20T07:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38811",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038812.json:
```json
{
    "body": "Positive review. Unless you can provide an easily accessible example of where Primes(False) isn't Primes(True), but perhaps the first place that happens is waaay down the road...",
    "created_at": "2009-10-20T07:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38812",
    "user": "kcrisman"
}
```

Positive review. Unless you can provide an easily accessible example of where Primes(False) isn't Primes(True), but perhaps the first place that happens is waaay down the road...



---

archive/issue_comments_038813.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T04:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5092#issuecomment-38813",
    "user": "mhansen"
}
```

Resolution: fixed
