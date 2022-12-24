# Issue 1600: another weird coercion bug

archive/issues_001600.json:
```json
{
    "body": "Assignee: somebody\n\nHaven't even started trying to track this one down yet:\n\n\n```\nsage: S.<s> = LaurentSeriesRing(GF(5))\nsage: T.<t> = PowerSeriesRing(pAdicRing(5))\nsage: \nsage: S(t)\n(1 + O(5^20))*s\nsage: parent(S(t))\nLaurent Series Ring in s over Finite Field of size 5\nsage: parent(S(t)[1])\n5-adic Ring with capped relative precision 20\n```\n\n\nPretty nasty.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1600\n\n",
    "created_at": "2007-12-26T17:29:30Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "another weird coercion bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1600",
    "user": "dmharvey"
}
```
Assignee: somebody

Haven't even started trying to track this one down yet:


```
sage: S.<s> = LaurentSeriesRing(GF(5))
sage: T.<t> = PowerSeriesRing(pAdicRing(5))
sage: 
sage: S(t)
(1 + O(5^20))*s
sage: parent(S(t))
Laurent Series Ring in s over Finite Field of size 5
sage: parent(S(t)[1])
5-adic Ring with capped relative precision 20
```


Pretty nasty.


Issue created by migration from https://trac.sagemath.org/ticket/1600





---

archive/issue_comments_010170.json:
```json
{
    "body": "Attachment [craigcitro-1600.patch](tarball://root/attachments/some-uuid/ticket1600/craigcitro-1600.patch) by craigcitro created at 2008-01-21 09:36:56",
    "created_at": "2008-01-21T09:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10170",
    "user": "craigcitro"
}
```

Attachment [craigcitro-1600.patch](tarball://root/attachments/some-uuid/ticket1600/craigcitro-1600.patch) by craigcitro created at 2008-01-21 09:36:56



---

archive/issue_comments_010171.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T09:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10171",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010172.json:
```json
{
    "body": "Changing assignee from somebody to craigcitro.",
    "created_at": "2008-01-21T09:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10172",
    "user": "craigcitro"
}
```

Changing assignee from somebody to craigcitro.



---

archive/issue_comments_010173.json:
```json
{
    "body": "Actually, this one turned out to be low-hanging fruit. The issue was that if the object being passed in to __call__ was already a power series, it didn't bother to try and coerce it -- obviously this is silly, since whenever the base_rings are different, some coercion needs to happen.",
    "created_at": "2008-01-21T09:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10173",
    "user": "craigcitro"
}
```

Actually, this one turned out to be low-hanging fruit. The issue was that if the object being passed in to __call__ was already a power series, it didn't bother to try and coerce it -- obviously this is silly, since whenever the base_rings are different, some coercion needs to happen.



---

archive/issue_comments_010174.json:
```json
{
    "body": "patch looks good, does what it is supposed to do, is documented. I say apply.",
    "created_at": "2008-01-26T11:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10174",
    "user": "malb"
}
```

patch looks good, does what it is supposed to do, is documented. I say apply.



---

archive/issue_comments_010175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-26T11:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10175",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010176.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc0",
    "created_at": "2008-01-26T11:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1600#issuecomment-10176",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc0
