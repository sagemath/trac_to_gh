# Issue 4421: create an optional singular_surf.spkg

archive/issues_004421.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe have removed the Java binaries required for surf (which is part of Singular). Since there are optional doctests in sage/rings/polynomial/multi_polynomial_ideal.py that depend on it and since people have complained about it not being available we should add it back via an optional spkg.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4421\n\n",
    "created_at": "2008-11-02T02:31:43Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "create an optional singular_surf.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

We have removed the Java binaries required for surf (which is part of Singular). Since there are optional doctests in sage/rings/polynomial/multi_polynomial_ideal.py that depend on it and since people have complained about it not being available we should add it back via an optional spkg.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4421





---

archive/issue_comments_032451.json:
```json
{
    "body": "There is already a surf package so I think this can be closed. The surf package however doesn't build but we have #6316 for this. Putting up for review so someone else can look wether this can be closed.",
    "created_at": "2017-09-13T12:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4421#issuecomment-32451",
    "user": "https://github.com/koffie"
}
```

There is already a surf package so I think this can be closed. The surf package however doesn't build but we have #6316 for this. Putting up for review so someone else can look wether this can be closed.



---

archive/issue_comments_032452.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-13T12:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4421#issuecomment-32452",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032453.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2017-09-13T18:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4421#issuecomment-32453",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_004666.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2017-09-13T18:05:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4421",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4421#event-4666"
}
```
