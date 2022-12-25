# Issue 685: Make Eisenstein series code handle eisenstein series with character

archive/issues_000685.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe eisenstein_series_qexp function currently only handles eisenstein series for level 1. It wouldn't be hard to make this handle eisenstein series for higher level and with character. I'm going to take care of this soon, but this is here in case I forget. ;)\n\nIssue created by migration from https://trac.sagemath.org/ticket/685\n\n",
    "created_at": "2007-09-18T05:14:14Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make Eisenstein series code handle eisenstein series with character",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/685",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

The eisenstein_series_qexp function currently only handles eisenstein series for level 1. It wouldn't be hard to make this handle eisenstein series for higher level and with character. I'm going to take care of this soon, but this is here in case I forget. ;)

Issue created by migration from https://trac.sagemath.org/ticket/685





---

archive/issue_comments_003541.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-02T00:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3541",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003542.json:
```json
{
    "body": "Craig,\n\nisn't this implemented by now?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T18:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig,

isn't this implemented by now?

Cheers,

Michael



---

archive/issue_comments_003543.json:
```json
{
    "body": "Do we want any more functionality than in the following example?\n\n```\nsage: G=DirichletGroup(4)\nsage: chi=G[1]\nsage: E=EisensteinForms(chi,1)\nsage: f=E.eisenstein_series()[0]\nsage: f.q_expansion(40)\n1/4 + q + q^2 + q^4 + 2*q^5 + q^8 + q^9 + 2*q^10 + 2*q^13 + q^16 + 2*q^17 + q^18 + 2*q^20 + 3*q^25 + 2*q^26 + 2*q^29 + q^32 + 2*q^34 + q^36 + 2*q^37 + O(q^40)\n```\n\nIf not, maybe we can close this as fixed/wontfix/whatever_is_appropriate.",
    "created_at": "2014-04-24T20:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3543",
    "user": "https://github.com/pjbruin"
}
```

Do we want any more functionality than in the following example?

```
sage: G=DirichletGroup(4)
sage: chi=G[1]
sage: E=EisensteinForms(chi,1)
sage: f=E.eisenstein_series()[0]
sage: f.q_expansion(40)
1/4 + q + q^2 + q^4 + 2*q^5 + q^8 + q^9 + 2*q^10 + 2*q^13 + q^16 + 2*q^17 + q^18 + 2*q^20 + 3*q^25 + 2*q^26 + 2*q^29 + q^32 + 2*q^34 + q^36 + 2*q^37 + O(q^40)
```

If not, maybe we can close this as fixed/wontfix/whatever_is_appropriate.



---

archive/issue_comments_003544.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-24T20:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3544",
    "user": "https://github.com/pjbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_003545.json:
```json
{
    "body": "Yes, that leaves nothing to desire.",
    "created_at": "2014-06-06T06:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3545",
    "user": "https://github.com/rwst"
}
```

Yes, that leaves nothing to desire.



---

archive/issue_comments_003546.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-06T06:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3546",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_000753.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-06-06T11:01:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/685#event-753"
}
```



---

archive/issue_comments_003547.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-06T11:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/685#issuecomment-3547",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
