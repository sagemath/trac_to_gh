# Issue 691: .coefficients() for EisensteinSeries does not return requested coefficients

archive/issues_000691.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: e = G.gen()\nsage: E = EisensteinForms(e, 3)\nsage: v = E.eisenstein_series()\nsage: f = v[0]\nsage: f\n15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11 + q + (4*zeta10 + 1)*q^2 + (-9*zeta10^3 + 1)*q^3 + (16*zeta10^2 + 4*zeta10 + 1)*q^4 + (25*zeta10^3 - 25*zeta10^2 + 25*zeta10 - 24)*q^5 + O(q^6)\nsage: f.coefficients([0,1,2,3,4])\n\n[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,\n 1,\n 4*zeta10 + 1,\n -9*zeta10^3 + 1,\n 16*zeta10^2 + 4*zeta10 + 1]\nsage: f.coefficients([0,1,2,3,4])\n[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/691\n\n",
    "created_at": "2007-09-18T22:11:56Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": ".coefficients() for EisensteinSeries does not return requested coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/691",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein


```
sage: e = G.gen()
sage: E = EisensteinForms(e, 3)
sage: v = E.eisenstein_series()
sage: f = v[0]
sage: f
15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11 + q + (4*zeta10 + 1)*q^2 + (-9*zeta10^3 + 1)*q^3 + (16*zeta10^2 + 4*zeta10 + 1)*q^4 + (25*zeta10^3 - 25*zeta10^2 + 25*zeta10 - 24)*q^5 + O(q^6)
sage: f.coefficients([0,1,2,3,4])

[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,
 1,
 4*zeta10 + 1,
 -9*zeta10^3 + 1,
 16*zeta10^2 + 4*zeta10 + 1]
sage: f.coefficients([0,1,2,3,4])
[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11]
```


Issue created by migration from https://trac.sagemath.org/ticket/691





---

archive/issue_comments_003580.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-09-18T22:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3580",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_003581.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2007-09-18T22:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3581",
    "user": "https://github.com/mwhansen"
}
```

Patch attached.



---

archive/issue_comments_003582.json:
```json
{
    "body": "Actually, there is a problem with f._compute.  Ignore the above patch for now.",
    "created_at": "2007-09-19T00:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3582",
    "user": "https://github.com/mwhansen"
}
```

Actually, there is a problem with f._compute.  Ignore the above patch for now.



---

archive/issue_comments_003583.json:
```json
{
    "body": "Attachment [691.patch](tarball://root/attachments/some-uuid/ticket691/691.patch) by @mwhansen created at 2007-09-19 01:23:17",
    "created_at": "2007-09-19T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3583",
    "user": "https://github.com/mwhansen"
}
```

Attachment [691.patch](tarball://root/attachments/some-uuid/ticket691/691.patch) by @mwhansen created at 2007-09-19 01:23:17



---

archive/issue_comments_003584.json:
```json
{
    "body": "Attachment [691.2.patch](tarball://root/attachments/some-uuid/ticket691/691.2.patch) by @mwhansen created at 2007-09-19 01:24:18\n\nPatch attached which fixes the issues.",
    "created_at": "2007-09-19T01:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3584",
    "user": "https://github.com/mwhansen"
}
```

Attachment [691.2.patch](tarball://root/attachments/some-uuid/ticket691/691.2.patch) by @mwhansen created at 2007-09-19 01:24:18

Patch attached which fixes the issues.



---

archive/issue_comments_003585.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3585",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000757.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-21T00:28:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/691#event-757"
}
```
