# Issue 7969: escaped backslash at end of line in notebook

archive/issues_007969.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following input in the notebook produces the wrong output:\n\n\n```\n%python\n2+2\nprint \"\"\"\\\na\\\\\nn\nc\n\"\"\"\n```\n\n\nIt should return\n\n\n```\na\\\nn\nc\n```\n\n\nbut instead prints\n\n\n```\na\n\nc\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7969\n\n",
    "created_at": "2010-01-17T21:21:38Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "escaped backslash at end of line in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7969",
    "user": "@wjp"
}
```
Assignee: @williamstein

The following input in the notebook produces the wrong output:


```
%python
2+2
print """\
a\\
n
c
"""
```


It should return


```
a\
n
c
```


but instead prints


```
a

c
```


Issue created by migration from https://trac.sagemath.org/ticket/7969





---

archive/issue_comments_069522.json:
```json
{
    "body": "Changing assignee from @williamstein to @TimDumol.",
    "created_at": "2010-01-17T21:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69522",
    "user": "@wjp"
}
```

Changing assignee from @williamstein to @TimDumol.



---

archive/issue_comments_069523.json:
```json
{
    "body": "Attachment [trac_7969-escaped-backslash.patch](tarball://root/attachments/some-uuid/ticket7969/trac_7969-escaped-backslash.patch) by @TimDumol created at 2010-01-17 21:23:49\n\nPrevents end-of-line backslashse from being replaced in sage and python systems.",
    "created_at": "2010-01-17T21:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69523",
    "user": "@TimDumol"
}
```

Attachment [trac_7969-escaped-backslash.patch](tarball://root/attachments/some-uuid/ticket7969/trac_7969-escaped-backslash.patch) by @TimDumol created at 2010-01-17 21:23:49

Prevents end-of-line backslashse from being replaced in sage and python systems.



---

archive/issue_comments_069524.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T09:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69524",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069525.json:
```json
{
    "body": "Fixes the example above and a few others I've tried.  SageNB doctests pass.",
    "created_at": "2010-01-19T11:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69525",
    "user": "@qed777"
}
```

Fixes the example above and a few others I've tried.  SageNB doctests pass.



---

archive/issue_comments_069526.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T11:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69526",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069527.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69527",
    "user": "@qed777"
}
```

Resolution: fixed
