# Issue 2780: factorisation over number field has wrong unit part

archive/issues_002780.json:
```json
{
    "body": "Assignee: somebody\n\nWhen factoring a multivariate polynomial over a number field, the unit part of the factorisation is reported incorrectly:\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: R.<y, z> = PolynomialRing(K)\nsage: f = 2*y^2 + 2*z^2\nsage: F = f.factor(); F\n2 * (y + (-a)*z) * (y + a*z)\nsage: F.unit_part()\n1\n```\n\n\nThe unit part should be 2.\n\nReported by Genya Zaytman.\n\nSee also: http://groups.google.com/group/sage-devel/browse_thread/thread/cc519fe6a67ff9e\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2780\n\n",
    "created_at": "2008-04-02T21:39:35Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "factorisation over number field has wrong unit part",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2780",
    "user": "dmharvey"
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

archive/issue_comments_019095.json:
```json
{
    "body": "Changing component from basic arithmetic to factorization.",
    "created_at": "2008-04-03T08:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19095",
    "user": "mabshoff"
}
```

Changing component from basic arithmetic to factorization.



---

archive/issue_comments_019096.json:
```json
{
    "body": "Changing assignee from somebody to tbd.",
    "created_at": "2008-04-03T08:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19096",
    "user": "mabshoff"
}
```

Changing assignee from somebody to tbd.



---

archive/issue_comments_019097.json:
```json
{
    "body": "Attachment [2780-factorization_unit.patch](tarball://root/attachments/some-uuid/ticket2780/2780-factorization_unit.patch) by AlexGhitza created at 2008-04-11 23:24:49\n\nSee the patch.",
    "created_at": "2008-04-11T23:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19097",
    "user": "AlexGhitza"
}
```

Attachment [2780-factorization_unit.patch](tarball://root/attachments/some-uuid/ticket2780/2780-factorization_unit.patch) by AlexGhitza created at 2008-04-11 23:24:49

See the patch.



---

archive/issue_comments_019098.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-12T07:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19098",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_019099.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T11:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19099",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019100.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T11:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2780#issuecomment-19100",
    "user": "mabshoff"
}
```

Resolution: fixed
