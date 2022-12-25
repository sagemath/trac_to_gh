# Issue 4253: polybori interface: equality operator for navigators

archive/issues_004253.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: polybori\n\n\n```\nsage: r.<x,y>=BooleanPolynomialRing(2)\n\nsage: p=r(\"0\")\nsage: p.navigation()==p.navigation()\nFalse\n```\n\nShould be True, probably `__eq__` not implemented.\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4253\n\n",
    "created_at": "2008-10-08T06:42:41Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "polybori interface: equality operator for navigators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4253",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```
Assignee: @malb

Keywords: polybori


```
sage: r.<x,y>=BooleanPolynomialRing(2)

sage: p=r("0")
sage: p.navigation()==p.navigation()
False
```

Should be True, probably `__eq__` not implemented.

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4253





---

archive/issue_comments_030875.json:
```json
{
    "body": "Attachment [pbori_navigator_eq.patch](tarball://root/attachments/some-uuid/ticket4253/pbori_navigator_eq.patch) by @malb created at 2008-10-08 14:17:07",
    "created_at": "2008-10-08T14:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4253#issuecomment-30875",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_navigator_eq.patch](tarball://root/attachments/some-uuid/ticket4253/pbori_navigator_eq.patch) by @malb created at 2008-10-08 14:17:07



---

archive/issue_comments_030876.json:
```json
{
    "body": "thanks, works :-)",
    "created_at": "2008-10-09T06:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4253#issuecomment-30876",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

thanks, works :-)



---

archive/issue_comments_030877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-11T06:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4253#issuecomment-30877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030878.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-11T06:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4253#issuecomment-30878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.rc0
