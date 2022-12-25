# Issue 1154: lost precision in RQDF -> RealField conversion

archive/issues_001154.json:
```json
{
    "body": "Assignee: jkantor\n\n\n```\nsage: R = RealField(206)\nsage: a = R(5292635226105886036954352397762172773270339156347702272822435/2^205)\nsage: b = RQDF(a)\nsage: c = R(b)\nself= 0.102925468350634334254648605229306925849343943655945448198193123\nsage: a - c\n1.215432671457254239676575010503930515740283626703352955683812e-63\n```\n\n\nI checked with b.get_doubles() that b == a, but was unable to find the routine which performs\nthe conversion from b (RQDF) to c (RealField). It seems R._set_from_qd is not used.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1154\n\n",
    "created_at": "2007-11-12T14:36:07Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "lost precision in RQDF -> RealField conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1154",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: jkantor


```
sage: R = RealField(206)
sage: a = R(5292635226105886036954352397762172773270339156347702272822435/2^205)
sage: b = RQDF(a)
sage: c = R(b)
self= 0.102925468350634334254648605229306925849343943655945448198193123
sage: a - c
1.215432671457254239676575010503930515740283626703352955683812e-63
```


I checked with b.get_doubles() that b == a, but was unable to find the routine which performs
the conversion from b (RQDF) to c (RealField). It seems R._set_from_qd is not used.

Issue created by migration from https://trac.sagemath.org/ticket/1154





---

archive/issue_comments_007024.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-12-02T06:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1154#issuecomment-7024",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: duplicate



---

archive/issue_comments_007025.json:
```json
{
    "body": "This is one of the issues that's covered by the patch at #1162.",
    "created_at": "2007-12-02T06:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1154#issuecomment-7025",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This is one of the issues that's covered by the patch at #1162.
