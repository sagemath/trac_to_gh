# Issue 1119: EllipticCurve.random_element for char=2

archive/issues_001119.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis should work:\n\n```\nsage: k.<a> = GF(2^5)\nsage: E = EllipticCurve(k,[k.random_element() for _ in range(5)])\nsage: E\nElliptic Curve defined by y^2 + (a^3+1)*x*y + (a^4+a^3+a)*y = x^3 +\n(a^4+a^3+a^2+a)*x^2 + (a^4+a^2+a+1)*x + a^2 over Finite Field in a of\nsize 2^5\nsage: E.random_element()\nException (click to the left for traceback):\n...\nZeroDivisionError: division by zero in finite field.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1119\n\n",
    "created_at": "2007-11-07T15:46:20Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "EllipticCurve.random_element for char=2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1119",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

This should work:

```
sage: k.<a> = GF(2^5)
sage: E = EllipticCurve(k,[k.random_element() for _ in range(5)])
sage: E
Elliptic Curve defined by y^2 + (a^3+1)*x*y + (a^4+a^3+a)*y = x^3 +
(a^4+a^3+a^2+a)*x^2 + (a^4+a^2+a+1)*x + a^2 over Finite Field in a of
size 2^5
sage: E.random_element()
Exception (click to the left for traceback):
...
ZeroDivisionError: division by zero in finite field.
```


Issue created by migration from https://trac.sagemath.org/ticket/1119





---

archive/issue_comments_006740.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-11-08T16:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6740",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_006741.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-08T16:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6741",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006742.json:
```json
{
    "body": "The attached patch fixes this (probably in a too naive way).",
    "created_at": "2007-11-08T16:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6742",
    "user": "https://github.com/malb"
}
```

The attached patch fixes this (probably in a too naive way).



---

archive/issue_comments_006743.json:
```json
{
    "body": "Attachment [ell_gf2_random.patch](tarball://root/attachments/some-uuid/ticket1119/ell_gf2_random.patch) by mabshoff created at 2007-11-11 23:39:20",
    "created_at": "2007-11-11T23:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6743",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [ell_gf2_random.patch](tarball://root/attachments/some-uuid/ticket1119/ell_gf2_random.patch) by mabshoff created at 2007-11-11 23:39:20



---

archive/issue_comments_006744.json:
```json
{
    "body": "Attachment [ell_gf2_random2.patch](tarball://root/attachments/some-uuid/ticket1119/ell_gf2_random2.patch) by @robertwb created at 2007-11-29 22:03:37\n\nGiven E defined by f(x,y) = 0, the patch assumed that there were always exactly zero or two values of y for every x, which is not true. I've attached a patch fixing this issue. \n\nAlso, in the characteristic > 2 case, it never considered the 'negative' square-root. I changed this too. \n\nOtherwise, the patch looks good.",
    "created_at": "2007-11-29T22:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6744",
    "user": "https://github.com/robertwb"
}
```

Attachment [ell_gf2_random2.patch](tarball://root/attachments/some-uuid/ticket1119/ell_gf2_random2.patch) by @robertwb created at 2007-11-29 22:03:37

Given E defined by f(x,y) = 0, the patch assumed that there were always exactly zero or two values of y for every x, which is not true. I've attached a patch fixing this issue. 

Also, in the characteristic > 2 case, it never considered the 'negative' square-root. I changed this too. 

Otherwise, the patch looks good.



---

archive/issue_comments_006745.json:
```json
{
    "body": "#1119 looks good.  It is slow but I don't know if that can be helped.",
    "created_at": "2007-12-15T05:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6745",
    "user": "https://github.com/williamstein"
}
```

#1119 looks good.  It is slow but I don't know if that can be helped.



---

archive/issue_comments_006746.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T05:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6746",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_001245.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-15T05:50:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1119#event-1245"
}
```



---

archive/issue_comments_006747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T05:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1119#issuecomment-6747",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
