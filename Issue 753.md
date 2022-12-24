# Issue 753: derivative alias for diff

archive/issues_000753.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor all polynomials and mpolynomials\n\nIssue created by migration from https://trac.sagemath.org/ticket/753\n\n",
    "created_at": "2007-09-25T18:30:04Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "derivative alias for diff",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/753",
    "user": "@robertwb"
}
```
Assignee: @williamstein

For all polynomials and mpolynomials

Issue created by migration from https://trac.sagemath.org/ticket/753





---

archive/issue_comments_004448.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T23:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4448",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004449.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-11-30T23:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4449",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_004450.json:
```json
{
    "body": "arrggh this is a bit of a mess currently. All the types seem to behave differently at the moment. Some standardisation is really needed here, and things pulled back closer to the base classes. Examples:\n\n\n```\nsage: x = var(\"x\")\nsage: type(x)\n<class 'sage.calculus.calculus.SymbolicVariable'>\nsage: x.diff()\n1\nsage: x.derivative()\n1\nsage: x.differentiate()\n1\n\nsage: R.<x> = PolynomialRing(ZZ)\nsage: x.derivative()\n1\nsage: x.diff()\n[boom]\n\nsage: R.<x> = PolynomialRing(QQ)\nsage: x.diff()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/dmharvey/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: diff() takes at least 2 arguments (1 given)\nsage: x.derivative()\n1\n```\n",
    "created_at": "2008-01-02T19:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4450",
    "user": "dmharvey"
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

archive/issue_comments_004451.json:
```json
{
    "body": "Attached patch revamps all derivative functions in sage, and also covers #756 and #1578.\n\nThis has been tested (sort of) on 2.10.2.\n\nI'm now going to try against mabshoff's pseudo-2.10.3.rc0.\n\nI'm not sure whether this should be targeted at 2.10.3 or 2.10.4.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4451",
    "user": "dmharvey"
}
```

Attached patch revamps all derivative functions in sage, and also covers #756 and #1578.

This has been tested (sort of) on 2.10.2.

I'm now going to try against mabshoff's pseudo-2.10.3.rc0.

I'm not sure whether this should be targeted at 2.10.3 or 2.10.4.



---

archive/issue_comments_004452.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4452",
    "user": "dmharvey"
}
```

Changing status from assigned to new.



---

archive/issue_comments_004453.json:
```json
{
    "body": "Changing assignee from @mwhansen to dmharvey.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4453",
    "user": "dmharvey"
}
```

Changing assignee from @mwhansen to dmharvey.



---

archive/issue_comments_004454.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-02-28T02:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4454",
    "user": "dmharvey"
}
```

Changing priority from minor to major.



---

archive/issue_comments_004455.json:
```json
{
    "body": "Attachment [derivative.patch](tarball://root/attachments/some-uuid/ticket753/derivative.patch) by dmharvey created at 2008-02-28 03:09:20",
    "created_at": "2008-02-28T03:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4455",
    "user": "dmharvey"
}
```

Attachment [derivative.patch](tarball://root/attachments/some-uuid/ticket753/derivative.patch) by dmharvey created at 2008-02-28 03:09:20



---

archive/issue_comments_004456.json:
```json
{
    "body": "Attachment [derivative2.patch](tarball://root/attachments/some-uuid/ticket753/derivative2.patch) by dmharvey created at 2008-03-02 01:55:27\n\nI've added an additional file derivative2.patch which incorporates a missing file (derivative.pyx)",
    "created_at": "2008-03-02T01:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4456",
    "user": "dmharvey"
}
```

Attachment [derivative2.patch](tarball://root/attachments/some-uuid/ticket753/derivative2.patch) by dmharvey created at 2008-03-02 01:55:27

I've added an additional file derivative2.patch which incorporates a missing file (derivative.pyx)



---

archive/issue_comments_004457.json:
```json
{
    "body": "Attachment [derivative-reviewer.patch](tarball://root/attachments/some-uuid/ticket753/derivative-reviewer.patch) by cwitty created at 2008-03-02 02:53:24\n\nLooks good to me!  \"sage -testall\" passes, code and doctests look good.  I added a patch that changes some indirect doctests to direct doctests, and fixes a 1-character typo.\n\nApply all three patches.",
    "created_at": "2008-03-02T02:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4457",
    "user": "cwitty"
}
```

Attachment [derivative-reviewer.patch](tarball://root/attachments/some-uuid/ticket753/derivative-reviewer.patch) by cwitty created at 2008-03-02 02:53:24

Looks good to me!  "sage -testall" passes, code and doctests look good.  I added a patch that changes some indirect doctests to direct doctests, and fixes a 1-character typo.

Apply all three patches.



---

archive/issue_comments_004458.json:
```json
{
    "body": "All doctests pass for me too.",
    "created_at": "2008-03-02T02:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4458",
    "user": "@mwhansen"
}
```

All doctests pass for me too.



---

archive/issue_comments_004459.json:
```json
{
    "body": "Merged all three patches in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T18:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4459",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 2.10.3.rc1



---

archive/issue_comments_004460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T18:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/753#issuecomment-4460",
    "user": "mabshoff"
}
```

Resolution: fixed
