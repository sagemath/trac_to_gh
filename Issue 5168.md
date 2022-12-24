# Issue 5168: [with patch, needs review] matrix0.pyx: fix doctest for commutator

archive/issues_005168.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: matrix0, commutator\n\nHere is the extent of the docstring for the commutator method in matrix0.pyx:\n\n```\n        Return the commutator self*other - other*self.\n\n        EXAMPLES:\n            sage: A = Matrix(QQ[['t']], 2, 2, range(4))\n```\n\nFix the doctest so that it actually computes a commutator.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5168\n\n",
    "created_at": "2009-02-03T21:17:52Z",
    "labels": [
        "linear algebra",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] matrix0.pyx: fix doctest for commutator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5168",
    "user": "@jhpalmieri"
}
```
Assignee: @williamstein

Keywords: matrix0, commutator

Here is the extent of the docstring for the commutator method in matrix0.pyx:

```
        Return the commutator self*other - other*self.

        EXAMPLES:
            sage: A = Matrix(QQ[['t']], 2, 2, range(4))
```

Fix the doctest so that it actually computes a commutator.


Issue created by migration from https://trac.sagemath.org/ticket/5168





---

archive/issue_comments_039594.json:
```json
{
    "body": "Attachment [5168.patch](tarball://root/attachments/some-uuid/ticket5168/5168.patch) by @jhpalmieri created at 2009-02-03 21:18:25",
    "created_at": "2009-02-03T21:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5168#issuecomment-39594",
    "user": "@jhpalmieri"
}
```

Attachment [5168.patch](tarball://root/attachments/some-uuid/ticket5168/5168.patch) by @jhpalmieri created at 2009-02-03 21:18:25



---

archive/issue_comments_039595.json:
```json
{
    "body": "New doctests look good, and they pass.\n\n(Good catch on noticing the original bug, too.)\n\nPositive review.",
    "created_at": "2009-02-05T06:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5168#issuecomment-39595",
    "user": "cwitty"
}
```

New doctests look good, and they pass.

(Good catch on noticing the original bug, too.)

Positive review.



---

archive/issue_comments_039596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T11:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5168#issuecomment-39596",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039597.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T11:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5168#issuecomment-39597",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael
