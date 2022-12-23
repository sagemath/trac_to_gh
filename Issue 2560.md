# Issue 2560: serious inefficiency in order of points on elliptic curvews over finite fields

archive/issues_002560.json:
```json
{
    "body": "Assignee: was\n\nKeywords: elliptic curves\n\nIn sage/elliptic_curves/sll_points.py in the function ` EllipticCurvePoint_finite_field.order()` a tiny blunder causes a huge inefficiency.  The BSGS function is used to find a multiple of the order of the point (when the group order is not yet known), and the existing code\n\n```\n                M = self._bsgs(E(0),0,ub)\n```\n\nshould be\n\n```\n                M = self._bsgs(E(0),lb,ub)\n```\n\nsince there is a loution in the interval [lb..ub].  This changes the complexity from O(q^1/2) to O(q^1/4).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2560\n\n",
    "created_at": "2008-03-16T22:22:45Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "serious inefficiency in order of points on elliptic curvews over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2560",
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

since there is a loution in the interval [lb..ub].  This changes the complexity from O(q^1/2) to O(q^1/4).

Issue created by migration from https://trac.sagemath.org/ticket/2560





---

archive/issue_comments_017452.json:
```json
{
    "body": "delete - duplicate",
    "created_at": "2008-03-16T22:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2560#issuecomment-17452",
    "user": "cremona"
}
```

delete - duplicate



---

archive/issue_comments_017453.json:
```json
{
    "body": "Duplicate of #2561",
    "created_at": "2008-03-16T22:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2560#issuecomment-17453",
    "user": "mhansen"
}
```

Duplicate of #2561



---

archive/issue_comments_017454.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-16T22:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2560#issuecomment-17454",
    "user": "mhansen"
}
```

Resolution: duplicate
