# Issue 7969: escaped backslash at end of line in notebook

archive/issues_007969.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following input in the notebook produces the wrong output:\n\n\n```\n%python\n2+2\nprint \"\"\"\\\na\\\\\nn\nc\n\"\"\"\n```\n\n\nIt should return\n\n\n```\na\\\nn\nc\n```\n\n\nbut instead prints\n\n\n```\na\n\nc\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7969\n\n",
    "created_at": "2010-01-17T21:21:38Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "escaped backslash at end of line in notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7969",
    "user": "https://github.com/wjp"
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

archive/issue_comments_069402.json:
```json
{
    "body": "Changing assignee from @williamstein to @TimDumol.",
    "created_at": "2010-01-17T21:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69402",
    "user": "https://github.com/wjp"
}
```

Changing assignee from @williamstein to @TimDumol.



---

archive/issue_comments_069403.json:
```json
{
    "body": "Attachment [trac_7969-escaped-backslash.patch](tarball://root/attachments/some-uuid/ticket7969/trac_7969-escaped-backslash.patch) by @TimDumol created at 2010-01-17 21:23:49\n\nPrevents end-of-line backslashse from being replaced in sage and python systems.",
    "created_at": "2010-01-17T21:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69403",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7969-escaped-backslash.patch](tarball://root/attachments/some-uuid/ticket7969/trac_7969-escaped-backslash.patch) by @TimDumol created at 2010-01-17 21:23:49

Prevents end-of-line backslashse from being replaced in sage and python systems.



---

archive/issue_comments_069404.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T09:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69404",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069405.json:
```json
{
    "body": "Fixes the example above and a few others I've tried.  SageNB doctests pass.",
    "created_at": "2010-01-19T11:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69405",
    "user": "https://github.com/qed777"
}
```

Fixes the example above and a few others I've tried.  SageNB doctests pass.



---

archive/issue_comments_069406.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T11:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69406",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069407.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7969#issuecomment-69407",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
