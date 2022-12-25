# Issue 3108: implement additive_order for elliptic curve points

archive/issues_003108.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: E = EllipticCurve(GF(5),[1..5])\nsage: P = E.lift_x(0)\nsage: P\n(0 : 2 : 1)\nsage: P.additive_order()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/Users/was/papers/submitted/kolyconj/<ipython console> in <module>()\n\n/Users/was/papers/submitted/kolyconj/element.pyx in sage.structure.element.ModuleElement.additive_order()\n\n<type 'exceptions.NotImplementedError'>: \nsage: P.order()\n3\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3108\n\n",
    "created_at": "2008-05-06T01:53:51Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "implement additive_order for elliptic curve points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3108",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: E = EllipticCurve(GF(5),[1..5])
sage: P = E.lift_x(0)
sage: P
(0 : 2 : 1)
sage: P.additive_order()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/papers/submitted/kolyconj/<ipython console> in <module>()

/Users/was/papers/submitted/kolyconj/element.pyx in sage.structure.element.ModuleElement.additive_order()

<type 'exceptions.NotImplementedError'>: 
sage: P.order()
3
```

Issue created by migration from https://trac.sagemath.org/ticket/3108





---

archive/issue_comments_021432.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-05-06T01:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21432",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_021433.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21433",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_021434.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21434",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_021435.json:
```json
{
    "body": "Attachment [trac_3108-additive_order.patch](tarball://root/attachments/some-uuid/ticket3108/trac_3108-additive_order.patch) by @JohnCremona created at 2009-07-24 22:21:25",
    "created_at": "2009-07-24T22:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21435",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_3108-additive_order.patch](tarball://root/attachments/some-uuid/ticket3108/trac_3108-additive_order.patch) by @JohnCremona created at 2009-07-24 22:21:25



---

archive/issue_comments_021436.json:
```json
{
    "body": "Done: I defined additive_order to be a synonym for order (in 3 places) with relevant doctests.",
    "created_at": "2009-07-24T22:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21436",
    "user": "https://github.com/JohnCremona"
}
```

Done: I defined additive_order to be a synonym for order (in 3 places) with relevant doctests.



---

archive/issue_comments_021437.json:
```json
{
    "body": "Fine.\n\nMaybe David Loeffler, working on abelian groups, wants this differently. \nBy now, this should go in.\n\nchris.",
    "created_at": "2009-08-17T12:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21437",
    "user": "https://github.com/categorie"
}
```

Fine.

Maybe David Loeffler, working on abelian groups, wants this differently. 
By now, this should go in.

chris.



---

archive/issue_comments_021438.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-22T22:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3108#issuecomment-21438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007024.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-22T22:13:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3108",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3108#event-7024"
}
```
