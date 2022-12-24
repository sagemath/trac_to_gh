# Issue 5705: [with patch, needs review] homogenize() does not respect the rule that parents are unique

archive/issues_005705.json:
```json
{
    "body": "Assignee: malb\n\nso far `homogenize()` would always create a new parent if the variable was not in the current parent. It should make sure that it reuses a previously created parent if available.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5705\n\n",
    "created_at": "2009-04-07T11:33:45Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] homogenize() does not respect the rule that parents are unique",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5705",
    "user": "malb"
}
```
Assignee: malb

so far `homogenize()` would always create a new parent if the variable was not in the current parent. It should make sure that it reuses a previously created parent if available.

Issue created by migration from https://trac.sagemath.org/ticket/5705





---

archive/issue_comments_044582.json:
```json
{
    "body": "Attachment [mpoly_homogenize_parent.patch](tarball://root/attachments/some-uuid/ticket5705/mpoly_homogenize_parent.patch) by SimonKing created at 2009-04-07 15:38:59\n\nIndeed, without the patch, we have\n\n```\nsage: R=PolynomialRing(QQ,'x',5)\nsage: p=R.random_element()\nsage: q1=p.homogenize()\nsage: q2=p.homogenize()\nsage: q1.parent() is q2.parent()\nFalse\n```\n\n\nWith the patch, that cleanly applies, we have\n\n```\nsage: R=PolynomialRing(QQ,'x',5)\nsage: p=R.random_element()\nsage: q1=p.homogenize()\nsage: q2=p.homogenize()\nsage: q1.parent() is q2.parent()\nTrue\n```\n\n\nSo, I give it a positive review.",
    "created_at": "2009-04-07T15:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44582",
    "user": "SimonKing"
}
```

Attachment [mpoly_homogenize_parent.patch](tarball://root/attachments/some-uuid/ticket5705/mpoly_homogenize_parent.patch) by SimonKing created at 2009-04-07 15:38:59

Indeed, without the patch, we have

```
sage: R=PolynomialRing(QQ,'x',5)
sage: p=R.random_element()
sage: q1=p.homogenize()
sage: q2=p.homogenize()
sage: q1.parent() is q2.parent()
False
```


With the patch, that cleanly applies, we have

```
sage: R=PolynomialRing(QQ,'x',5)
sage: p=R.random_element()
sage: q1=p.homogenize()
sage: q2=p.homogenize()
sage: q1.parent() is q2.parent()
True
```


So, I give it a positive review.



---

archive/issue_comments_044583.json:
```json
{
    "body": "Hmm, I am happy to merge this provided someone post a doctest. With this patch applied doctests do pass. 3.4.1.rc2 will drop in about 18 hours, so there should be plenty of time.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T07:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44583",
    "user": "mabshoff"
}
```

Hmm, I am happy to merge this provided someone post a doctest. With this patch applied doctests do pass. 3.4.1.rc2 will drop in about 18 hours, so there should be plenty of time.

Cheers,

Michael



---

archive/issue_comments_044584.json:
```json
{
    "body": "Apply the new patch after the old one.  It just adds Simon's test as a doctest.",
    "created_at": "2009-04-09T08:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44584",
    "user": "AlexGhitza"
}
```

Apply the new patch after the old one.  It just adds Simon's test as a doctest.



---

archive/issue_comments_044585.json:
```json
{
    "body": "apply after the first patch",
    "created_at": "2009-04-09T08:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44585",
    "user": "AlexGhitza"
}
```

apply after the first patch



---

archive/issue_comments_044586.json:
```json
{
    "body": "Attachment [trac5705_doctest.patch](tarball://root/attachments/some-uuid/ticket5705/trac5705_doctest.patch) by mabshoff created at 2009-04-09 08:45:36\n\nMerged both patches in Sage 3.4.1.rc2. Thanks Alex.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T08:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44586",
    "user": "mabshoff"
}
```

Attachment [trac5705_doctest.patch](tarball://root/attachments/some-uuid/ticket5705/trac5705_doctest.patch) by mabshoff created at 2009-04-09 08:45:36

Merged both patches in Sage 3.4.1.rc2. Thanks Alex.

Cheers,

Michael



---

archive/issue_comments_044587.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T08:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44587",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044588.json:
```json
{
    "body": "Thanks Alex",
    "created_at": "2009-04-09T08:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5705#issuecomment-44588",
    "user": "malb"
}
```

Thanks Alex
