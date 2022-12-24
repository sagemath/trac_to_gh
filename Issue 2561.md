# Issue 2561: serious inefficiency in order of points on elliptic curvews over finite fields

archive/issues_002561.json:
```json
{
    "body": "Assignee: was\n\nKeywords: elliptic curves\n\nIn sage/elliptic_curves/sll_points.py in the function ` EllipticCurvePoint_finite_field.order()` a tiny blunder causes a huge inefficiency.  The BSGS function is used to find a multiple of the order of the point (when the group order is not yet known), and the existing code\n\n```\n                M = self._bsgs(E(0),0,ub)\n```\n\nshould be\n\n```\n                M = self._bsgs(E(0),lb,ub)\n```\n\nsince there is a lsolution in the interval [lb..ub].  This changes the complexity from `O(q^1/2)` to `O(q^1/4)`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2561\n\n",
    "created_at": "2008-03-16T22:23:45Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "serious inefficiency in order of points on elliptic curvews over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2561",
    "user": "cremona"
}
```
Assignee: was

Keywords: elliptic curves

In sage/elliptic_curves/sll_points.py in the function ` EllipticCurvePoint_finite_field.order()` a tiny blunder causes a huge inefficiency.  The BSGS function is used to find a multiple of the order of the point (when the group order is not yet known), and the existing code

```
                M = self._bsgs(E(0),0,ub)
```

should be

```
                M = self._bsgs(E(0),lb,ub)
```

since there is a lsolution in the interval [lb..ub].  This changes the complexity from `O(q^1/2)` to `O(q^1/4)`.



Issue created by migration from https://trac.sagemath.org/ticket/2561





---

archive/issue_comments_017455.json:
```json
{
    "body": "Attachment [8866.patch](tarball://root/attachments/some-uuid/ticket2561/8866.patch) by cremona created at 2008-03-16 22:31:52",
    "created_at": "2008-03-16T22:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17455",
    "user": "cremona"
}
```

Attachment [8866.patch](tarball://root/attachments/some-uuid/ticket2561/8866.patch) by cremona created at 2008-03-16 22:31:52



---

archive/issue_comments_017456.json:
```json
{
    "body": "Looks fine to me, apply.",
    "created_at": "2008-03-16T23:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17456",
    "user": "ncalexan"
}
```

Looks fine to me, apply.



---

archive/issue_comments_017457.json:
```json
{
    "body": "Doctests pass with \"-long\", so another positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T23:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17457",
    "user": "mabshoff"
}
```

Doctests pass with "-long", so another positive review.

Cheers,

Michael



---

archive/issue_comments_017458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T23:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17458",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017459.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-16T23:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17459",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.final
