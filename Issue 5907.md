# Issue 5907: [with patch; needs review] incorrect fast_float evaluation of constant polynomials

archive/issues_005907.json:
```json
{
    "body": "Assignee: tornaria\n\nKeywords: fast_float\n\nA constant polynomial `a` is incorrectly `_fast_float_`- evaluated as `a*x`:\n\n```\nsage: R.<t> = QQ[]\nsage: f = t + 2 - t\nsage: ff = f._fast_float_()\nsage: ff(3)\n6.0\nsage: list(ff)\n['load 0', 'push 2.0', 'mul']\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5907\n\n",
    "created_at": "2009-04-27T01:10:19Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] incorrect fast_float evaluation of constant polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5907",
    "user": "tornaria"
}
```
Assignee: tornaria

Keywords: fast_float

A constant polynomial `a` is incorrectly `_fast_float_`- evaluated as `a*x`:

```
sage: R.<t> = QQ[]
sage: f = t + 2 - t
sage: ff = f._fast_float_()
sage: ff(3)
6.0
sage: list(ff)
['load 0', 'push 2.0', 'mul']
```


Issue created by migration from https://trac.sagemath.org/ticket/5907





---

archive/issue_comments_046689.json:
```json
{
    "body": "Fix fast_float evaluation of constant polynomials",
    "created_at": "2009-04-27T01:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46689",
    "user": "tornaria"
}
```

Fix fast_float evaluation of constant polynomials



---

archive/issue_comments_046690.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-27T16:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46690",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_046691.json:
```json
{
    "body": "Attachment\n\nPositive review for the original patch (code looks good, doctests pass).  Unfortunately _fast_callable_ copied the buggy code; seems like we might as well fix both bugs on the same ticket, so I've added a second patch to fix the _fast_callable_ bug.  (So this second patch needs review.)",
    "created_at": "2009-04-27T16:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46691",
    "user": "cwitty"
}
```

Attachment

Positive review for the original patch (code looks good, doctests pass).  Unfortunately _fast_callable_ copied the buggy code; seems like we might as well fix both bugs on the same ticket, so I've added a second patch to fix the _fast_callable_ bug.  (So this second patch needs review.)



---

archive/issue_comments_046692.json:
```json
{
    "body": "Positive review for cwitty's change.",
    "created_at": "2009-05-19T05:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46692",
    "user": "mhansen"
}
```

Positive review for cwitty's change.



---

archive/issue_comments_046693.json:
```json
{
    "body": "Merged both patches in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T19:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46693",
    "user": "mabshoff"
}
```

Merged both patches in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_046694.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T19:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5907#issuecomment-46694",
    "user": "mabshoff"
}
```

Resolution: fixed
