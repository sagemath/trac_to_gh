# Issue 691: .coefficients() for EisensteinSeries does not return requested coefficients

archive/issues_000691.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: e = G.gen()\nsage: E = EisensteinForms(e, 3)\nsage: v = E.eisenstein_series()\nsage: f = v[0]\nsage: f\n15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11 + q + (4*zeta10 + 1)*q^2 + (-9*zeta10^3 + 1)*q^3 + (16*zeta10^2 + 4*zeta10 + 1)*q^4 + (25*zeta10^3 - 25*zeta10^2 + 25*zeta10 - 24)*q^5 + O(q^6)\nsage: f.coefficients([0,1,2,3,4])\n\n[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11,\n 1,\n 4*zeta10 + 1,\n -9*zeta10^3 + 1,\n 16*zeta10^2 + 4*zeta10 + 1]\nsage: f.coefficients([0,1,2,3,4])\n[15/11*zeta10^3 - 9/11*zeta10^2 - 26/11*zeta10 - 10/11]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/691\n\n",
    "created_at": "2007-09-18T22:11:56Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": ".coefficients() for EisensteinSeries does not return requested coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/691",
    "user": "mhansen"
}
```
Assignee: was


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

archive/issue_comments_003593.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-09-18T22:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3593",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_003594.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2007-09-18T22:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3594",
    "user": "mhansen"
}
```

Patch attached.



---

archive/issue_comments_003595.json:
```json
{
    "body": "Actually, there is a problem with f._compute.  Ignore the above patch for now.",
    "created_at": "2007-09-19T00:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3595",
    "user": "mhansen"
}
```

Actually, there is a problem with f._compute.  Ignore the above patch for now.



---

archive/issue_comments_003596.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-19T01:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3596",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_003597.json:
```json
{
    "body": "Attachment\n\nPatch attached which fixes the issues.",
    "created_at": "2007-09-19T01:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3597",
    "user": "mhansen"
}
```

Attachment

Patch attached which fixes the issues.



---

archive/issue_comments_003598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/691#issuecomment-3598",
    "user": "was"
}
```

Resolution: fixed
