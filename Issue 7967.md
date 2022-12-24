# Issue 7967: DeprecationWarning for popen3 in hg_sage

archive/issues_007967.json:
```json
{
    "body": "Assignee: tbd\n\nUsing `hg_sage` is raising a `DeprecationWarning`:\n\n\n```\n/data/sage/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.\n  x = os.popen3(s)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7967\n\n",
    "created_at": "2010-01-17T18:34:34Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "DeprecationWarning for popen3 in hg_sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7967",
    "user": "@wjp"
}
```
Assignee: tbd

Using `hg_sage` is raising a `DeprecationWarning`:


```
/data/sage/sage-4.3.1.rc0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
```


Issue created by migration from https://trac.sagemath.org/ticket/7967





---

archive/issue_comments_069511.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T18:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7967#issuecomment-69511",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069512.json:
```json
{
    "body": "Attachment [7967_popen3.patch](tarball://root/attachments/some-uuid/ticket7967/7967_popen3.patch) by @TimDumol created at 2010-01-17 19:19:07\n\nGood job; looks good.",
    "created_at": "2010-01-17T19:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7967#issuecomment-69512",
    "user": "@TimDumol"
}
```

Attachment [7967_popen3.patch](tarball://root/attachments/some-uuid/ticket7967/7967_popen3.patch) by @TimDumol created at 2010-01-17 19:19:07

Good job; looks good.



---

archive/issue_comments_069513.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T19:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7967#issuecomment-69513",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T00:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7967#issuecomment-69514",
    "user": "@rlmill"
}
```

Resolution: fixed
