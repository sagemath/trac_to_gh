# Issue 753: [with patch, with positive review] derivative alias for diff

archive/issues_000753.json:
```json
{
    "body": "Assignee: dmharvey\n\nFor all polynomials and mpolynomials\n\nIssue created by migration from https://trac.sagemath.org/ticket/753\n\n",
    "closed_at": "2008-03-02T18:32:22Z",
    "created_at": "2007-09-25T18:30:04Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, with positive review] derivative alias for diff",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/753",
    "user": "https://github.com/robertwb"
}
```
Assignee: dmharvey

For all polynomials and mpolynomials

Issue created by migration from https://trac.sagemath.org/ticket/753





---

archive/issue_events_002050.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-26T21:19:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/753#event-2050"
}
```



---

archive/issue_comments_004433.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T23:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4433",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004434.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-11-30T23:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4434",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_events_002051.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-18T10:04:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/753#event-2051"
}
```



---

archive/issue_events_002052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-18T10:04:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/753#event-2052"
}
```



---

archive/issue_comments_004435.json:
```json
{
    "body": "arrggh this is a bit of a mess currently. All the types seem to behave differently at the moment. Some standardisation is really needed here, and things pulled back closer to the base classes. Examples:\n\n```\nsage: x = var(\"x\")\nsage: type(x)\n<class 'sage.calculus.calculus.SymbolicVariable'>\nsage: x.diff()\n1\nsage: x.derivative()\n1\nsage: x.differentiate()\n1\n\nsage: R.<x> = PolynomialRing(ZZ)\nsage: x.derivative()\n1\nsage: x.diff()\n[boom]\n\nsage: R.<x> = PolynomialRing(QQ)\nsage: x.diff()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/dmharvey/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: diff() takes at least 2 arguments (1 given)\nsage: x.derivative()\n1\n```",
    "created_at": "2008-01-02T19:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4435",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

arrggh this is a bit of a mess currently. All the types seem to behave differently at the moment. Some standardisation is really needed here, and things pulled back closer to the base classes. Examples:

```
sage: x = var("x")
sage: type(x)
<class 'sage.calculus.calculus.SymbolicVariable'>
sage: x.diff()
1
sage: x.derivative()
1
sage: x.differentiate()
1

sage: R.<x> = PolynomialRing(ZZ)
sage: x.derivative()
1
sage: x.diff()
[boom]

sage: R.<x> = PolynomialRing(QQ)
sage: x.diff()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

<type 'exceptions.TypeError'>: diff() takes at least 2 arguments (1 given)
sage: x.derivative()
1
```



---

archive/issue_comments_004436.json:
```json
{
    "body": "Attached patch revamps all derivative functions in sage, and also covers #756 and #1578.\n\nThis has been tested (sort of) on 2.10.2.\n\nI'm now going to try against mabshoff's pseudo-2.10.3.rc0.\n\nI'm not sure whether this should be targeted at 2.10.3 or 2.10.4.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4436",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attached patch revamps all derivative functions in sage, and also covers #756 and #1578.

This has been tested (sort of) on 2.10.2.

I'm now going to try against mabshoff's pseudo-2.10.3.rc0.

I'm not sure whether this should be targeted at 2.10.3 or 2.10.4.



---

archive/issue_comments_004437.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4437",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing status from assigned to new.



---

archive/issue_comments_004438.json:
```json
{
    "body": "Changing assignee from @mwhansen to dmharvey.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4438",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from @mwhansen to dmharvey.



---

archive/issue_comments_004439.json:
```json
{
    "body": "Attachment [derivative.patch](tarball://root/attachments/some-uuid/ticket753/derivative.patch) by dmharvey created at 2008-02-28 03:09:20",
    "created_at": "2008-02-28T03:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4439",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [derivative.patch](tarball://root/attachments/some-uuid/ticket753/derivative.patch) by dmharvey created at 2008-02-28 03:09:20



---

archive/issue_comments_004440.json:
```json
{
    "body": "Attachment [derivative2.patch](tarball://root/attachments/some-uuid/ticket753/derivative2.patch) by dmharvey created at 2008-03-02 01:55:27\n\nI've added an additional file derivative2.patch which incorporates a missing file (derivative.pyx)",
    "created_at": "2008-03-02T01:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4440",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [derivative2.patch](tarball://root/attachments/some-uuid/ticket753/derivative2.patch) by dmharvey created at 2008-03-02 01:55:27

I've added an additional file derivative2.patch which incorporates a missing file (derivative.pyx)



---

archive/issue_comments_004441.json:
```json
{
    "body": "Attachment [derivative-reviewer.patch](tarball://root/attachments/some-uuid/ticket753/derivative-reviewer.patch) by cwitty created at 2008-03-02 02:53:24\n\nLooks good to me!  \"sage -testall\" passes, code and doctests look good.  I added a patch that changes some indirect doctests to direct doctests, and fixes a 1-character typo.\n\nApply all three patches.",
    "created_at": "2008-03-02T02:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4441",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [derivative-reviewer.patch](tarball://root/attachments/some-uuid/ticket753/derivative-reviewer.patch) by cwitty created at 2008-03-02 02:53:24

Looks good to me!  "sage -testall" passes, code and doctests look good.  I added a patch that changes some indirect doctests to direct doctests, and fixes a 1-character typo.

Apply all three patches.



---

archive/issue_comments_004442.json:
```json
{
    "body": "All doctests pass for me too.",
    "created_at": "2008-03-02T02:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4442",
    "user": "https://github.com/mwhansen"
}
```

All doctests pass for me too.



---

archive/issue_comments_004443.json:
```json
{
    "body": "Merged all three patches in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T18:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 2.10.3.rc1



---

archive/issue_events_002053.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-02T18:32:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/753#event-2053"
}
```



---

archive/issue_comments_004444.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T18:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4444",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
