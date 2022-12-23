# Issue 9784: Simple Server API - wrong cell results

archive/issues_009784.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  jason\n\nUsing the Simple Server API I tried the following (after logging in of course):\n\nAt first I sent the code \"`sleep(10);5`\" to the server using the following URL:\n`http://localhost:port/simple/compute?session=theID&code=sleep(10)%3B5`\n\nThen, immediatly afterwards (this means command one was still computing) I sent the code \"`4+5`\" to the server using the URL\n`http://localhost:port/simple/compute?session=theID&code=4%2B5`\n\nThen, after 10 seconds, I looked at the results of both commands using\n`http://localhost:port/simple/status?session=theID&cell=2`\nand\n`http://localhost:port/simple/status?session=theID&cell=3`\n\nBoth cells had `5` as result, which should be only the result of the first\ncell.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9785\n\n",
    "created_at": "2010-08-23T10:45:49Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Simple Server API - wrong cell results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9784",
    "user": "dpoetzsch"
}
```
Assignee: jason, was

CC:  jason

Using the Simple Server API I tried the following (after logging in of course):

At first I sent the code "`sleep(10);5`" to the server using the following URL:
`http://localhost:port/simple/compute?session=theID&code=sleep(10)%3B5`

Then, immediatly afterwards (this means command one was still computing) I sent the code "`4+5`" to the server using the URL
`http://localhost:port/simple/compute?session=theID&code=4%2B5`

Then, after 10 seconds, I looked at the results of both commands using
`http://localhost:port/simple/status?session=theID&cell=2`
and
`http://localhost:port/simple/status?session=theID&cell=3`

Both cells had `5` as result, which should be only the result of the first
cell.

Issue created by migration from https://trac.sagemath.org/ticket/9785





---

archive/issue_comments_096036.json:
```json
{
    "body": "Attachment\n\nThis fixes the problem for me.",
    "created_at": "2011-12-24T22:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96036",
    "user": "mmanashirov"
}
```

Attachment

This fixes the problem for me.



---

archive/issue_comments_096037.json:
```json
{
    "body": "Sadly, the simple server does not work with the current notebook, and the [Sage cell server](https://github.com/sagemath/sagecell) has more or less superseded it.",
    "created_at": "2013-06-14T17:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96037",
    "user": "kcrisman"
}
```

Sadly, the simple server does not work with the current notebook, and the [Sage cell server](https://github.com/sagemath/sagecell) has more or less superseded it.



---

archive/issue_comments_096038.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-14T17:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96038",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096039.json:
```json
{
    "body": "Although we'll close this, I hope the code here will someday prove useful, though!",
    "created_at": "2013-06-14T17:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96039",
    "user": "kcrisman"
}
```

Although we'll close this, I hope the code here will someday prove useful, though!



---

archive/issue_comments_096040.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-14T17:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96040",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096041.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2013-06-14T18:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96041",
    "user": "kcrisman"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_096042.json:
```json
{
    "body": "Note that #11409 would remove this completely.",
    "created_at": "2013-06-14T18:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96042",
    "user": "kcrisman"
}
```

Note that #11409 would remove this completely.



---

archive/issue_comments_096043.json:
```json
{
    "body": "This has now been removed.",
    "created_at": "2014-09-17T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96043",
    "user": "kcrisman"
}
```

This has now been removed.



---

archive/issue_comments_096044.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2014-09-17T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96044",
    "user": "kcrisman"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_096045.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-09-18T17:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9784#issuecomment-96045",
    "user": "vbraun"
}
```

Resolution: wontfix
