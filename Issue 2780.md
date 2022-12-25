# Issue 2780: factorisation over number field has wrong unit part

archive/issues_002780.json:
```json
{
    "body": "Assignee: somebody\n\nWhen factoring a multivariate polynomial over a number field, the unit part of the factorisation is reported incorrectly:\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: R.<y, z> = PolynomialRing(K)\nsage: f = 2*y^2 + 2*z^2\nsage: F = f.factor(); F\n2 * (y + (-a)*z) * (y + a*z)\nsage: F.unit_part()\n1\n```\n\n\nThe unit part should be 2.\n\nReported by Genya Zaytman.\n\nSee also: http://groups.google.com/group/sage-devel/browse_thread/thread/cc519fe6a67ff9e\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2780\n\n",
    "created_at": "2008-04-02T21:39:35Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "factorisation over number field has wrong unit part",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2780",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

When factoring a multivariate polynomial over a number field, the unit part of the factorisation is reported incorrectly:


```
sage: K.<a> = NumberField(x^2 + 1)
sage: R.<y, z> = PolynomialRing(K)
sage: f = 2*y^2 + 2*z^2
sage: F = f.factor(); F
2 * (y + (-a)*z) * (y + a*z)
sage: F.unit_part()
1
```


The unit part should be 2.

Reported by Genya Zaytman.

See also: http://groups.google.com/group/sage-devel/browse_thread/thread/cc519fe6a67ff9e


Issue created by migration from https://trac.sagemath.org/ticket/2780





---

archive/issue_comments_019055.json:
```json
{
    "body": "Changing component from basic arithmetic to factorization.",
    "created_at": "2008-04-03T08:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from basic arithmetic to factorization.



---

archive/issue_events_006420.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-03T08:54:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2780#event-6420"
}
```



---

archive/issue_comments_019056.json:
```json
{
    "body": "Changing assignee from somebody to tbd.",
    "created_at": "2008-04-03T08:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19056",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to tbd.



---

archive/issue_comments_019057.json:
```json
{
    "body": "Attachment [2780-factorization_unit.patch](tarball://root/attachments/some-uuid/ticket2780/2780-factorization_unit.patch) by @aghitza created at 2008-04-11 23:24:49\n\nSee the patch.",
    "created_at": "2008-04-11T23:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19057",
    "user": "https://github.com/aghitza"
}
```

Attachment [2780-factorization_unit.patch](tarball://root/attachments/some-uuid/ticket2780/2780-factorization_unit.patch) by @aghitza created at 2008-04-11 23:24:49

See the patch.



---

archive/issue_comments_019058.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-12T07:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19058",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_019059.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T11:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19059",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_events_006421.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-12T11:23:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2780#event-6421"
}
```



---

archive/issue_comments_019060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T11:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
