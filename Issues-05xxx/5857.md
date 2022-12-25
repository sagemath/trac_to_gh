# Issue 5857: [with patch, positive review] E.list() for E an elliptic curve over a finite field is broken

archive/issues_005857.json:
```json
{
    "body": "Assignee: @loefflerd\n\nE.list() doesn't work, but list(E) works fine.\n\n```\nsage: E = EllipticCurve(GF(11), [1,2])\nsage: E.list()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/teragon.local/15239/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.list (sage/structure/parent.c:5196)()\n\nAttributeError: 'EllipticCurve_finite_field' object has no attribute '__iter__'\nsage: list(E)\n\n[(0 : 1 : 0),\n (1 : 2 : 1),\n (1 : 9 : 1),\n (2 : 1 : 1),\n...\n```\n\nSee also #5856\n\nIssue created by migration from https://trac.sagemath.org/ticket/5857\n\n",
    "closed_at": "2009-08-23T02:11:00Z",
    "created_at": "2009-04-22T15:47:55Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] E.list() for E an elliptic curve over a finite field is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5857",
    "user": "https://github.com/williamstein"
}
```
Assignee: @loefflerd

E.list() doesn't work, but list(E) works fine.

```
sage: E = EllipticCurve(GF(11), [1,2])
sage: E.list()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/15239/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.list (sage/structure/parent.c:5196)()

AttributeError: 'EllipticCurve_finite_field' object has no attribute '__iter__'
sage: list(E)

[(0 : 1 : 0),
 (1 : 2 : 1),
 (1 : 9 : 1),
 (2 : 1 : 1),
...
```

See also #5856

Issue created by migration from https://trac.sagemath.org/ticket/5857





---

archive/issue_comments_046189.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46189",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_046190.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-21T08:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46190",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_046191.json:
```json
{
    "body": "Attachment [trac_5857-elliptic_curve_iterator.patch](tarball://root/attachments/some-uuid/ticket5857/trac_5857-elliptic_curve_iterator.patch) by @JohnCremona created at 2009-08-18 20:52:02\n\nApplies to 4.1.1",
    "created_at": "2009-08-18T20:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46191",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5857-elliptic_curve_iterator.patch](tarball://root/attachments/some-uuid/ticket5857/trac_5857-elliptic_curve_iterator.patch) by @JohnCremona created at 2009-08-18 20:52:02

Applies to 4.1.1



---

archive/issue_comments_046192.json:
```json
{
    "body": "I think this does what was wanted.",
    "created_at": "2009-08-18T20:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46192",
    "user": "https://github.com/JohnCremona"
}
```

I think this does what was wanted.



---

archive/issue_comments_046193.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-08-19T10:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46193",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_046194.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2009-08-23T02:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46194",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch



---

archive/issue_events_013782.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-23T02:11:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5857#event-13782"
}
```



---

archive/issue_comments_046195.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T02:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46195",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_046196.json:
```json
{
    "body": "Attachment [trac_5857-reviewer.patch](tarball://root/attachments/some-uuid/ticket5857/trac_5857-reviewer.patch) by mvngu created at 2009-08-23 02:11:00\n\nThe reviewer patch `trac_5857-reviewer.patch` fixes a trivial typo in ReST formatting. Merged patches in this order:\n\n1. `trac_5857-elliptic_curve_iterator.patch`\n2. `trac_5857-reviewer.patch`",
    "created_at": "2009-08-23T02:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5857#issuecomment-46196",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5857-reviewer.patch](tarball://root/attachments/some-uuid/ticket5857/trac_5857-reviewer.patch) by mvngu created at 2009-08-23 02:11:00

The reviewer patch `trac_5857-reviewer.patch` fixes a trivial typo in ReST formatting. Merged patches in this order:

1. `trac_5857-elliptic_curve_iterator.patch`
2. `trac_5857-reviewer.patch`
