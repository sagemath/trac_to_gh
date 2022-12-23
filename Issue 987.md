# Issue 987: integrate(1/sqrt(9+x^2)) fails

archive/issues_000987.json:
```json
{
    "body": "Assignee: mhansen\n\nintegrate(1/sqrt(9+x^2))\nx/3\n\nI tried this at home and numerous times on sagenb.org.  Every other\nplausible syntax of this integral I tried (-1 power, more parentheses,\nswitch the summands, etc.) yields the same result\n\nHere's the reason\n\n```\n(%i1) integrate(1/sqrt(9+x^2),x)\n;\n                                         x\n(%o1)                              asinh(-)\n                                         3\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/987\n\n",
    "created_at": "2007-10-25T01:03:00Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "integrate(1/sqrt(9+x^2)) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/987",
    "user": "mhansen"
}
```
Assignee: mhansen

integrate(1/sqrt(9+x^2))
x/3

I tried this at home and numerous times on sagenb.org.  Every other
plausible syntax of this integral I tried (-1 power, more parentheses,
switch the summands, etc.) yields the same result

Here's the reason

```
(%i1) integrate(1/sqrt(9+x^2),x)
;
                                         x
(%o1)                              asinh(-)
                                         3


```


Issue created by migration from https://trac.sagemath.org/ticket/987





---

archive/issue_comments_006029.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-10-25T01:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6029",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_006030.json:
```json
{
    "body": "fixes this problem.",
    "created_at": "2007-10-25T01:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6030",
    "user": "was"
}
```

fixes this problem.



---

archive/issue_comments_006031.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-25T01:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6031",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_006032.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-25T02:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6032",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_006033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-25T06:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/987#issuecomment-6033",
    "user": "was"
}
```

Resolution: fixed
