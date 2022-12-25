# Issue 2561: [with patch, with positive review] serious inefficiency in order of points on elliptic curvews over finite fields

archive/issues_002561.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: elliptic curves\n\nIn sage/elliptic_curves/sll_points.py in the function ` EllipticCurvePoint_finite_field.order()` a tiny blunder causes a huge inefficiency.  The BSGS function is used to find a multiple of the order of the point (when the group order is not yet known), and the existing code\n\n```\n                M = self._bsgs(E(0),0,ub)\n```\nshould be\n\n```\n                M = self._bsgs(E(0),lb,ub)\n```\nsince there is a lsolution in the interval [lb..ub].  This changes the complexity from `O(q^1/2)` to `O(q^1/4)`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2561\n\n",
    "closed_at": "2008-03-16T23:56:35Z",
    "created_at": "2008-03-16T22:23:45Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, with positive review] serious inefficiency in order of points on elliptic curvews over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2561",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

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

archive/issue_comments_017418.json:
```json
{
    "body": "Attachment [8866.patch](tarball://root/attachments/some-uuid/ticket2561/8866.patch) by @JohnCremona created at 2008-03-16 22:31:52",
    "created_at": "2008-03-16T22:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17418",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8866.patch](tarball://root/attachments/some-uuid/ticket2561/8866.patch) by @JohnCremona created at 2008-03-16 22:31:52



---

archive/issue_comments_017419.json:
```json
{
    "body": "Looks fine to me, apply.",
    "created_at": "2008-03-16T23:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17419",
    "user": "https://github.com/ncalexan"
}
```

Looks fine to me, apply.



---

archive/issue_comments_017420.json:
```json
{
    "body": "Doctests pass with \"-long\", so another positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T23:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests pass with "-long", so another positive review.

Cheers,

Michael



---

archive/issue_comments_017421.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T23:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005988.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T23:56:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2561#event-5988"
}
```



---

archive/issue_comments_017422.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-16T23:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2561#issuecomment-17422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.final
