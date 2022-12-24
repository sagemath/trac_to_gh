# Issue 1873: [with patch] elementary function expansion returns result in the wrong ring

archive/issues_001873.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nI'm using Sage 2.10 now. Expansion for elements in SFAElementary works\ngreat now, but there is another problem: the expansion lies in the\nwrong ring.\n\n```\nsage: e=SFAElementary(QQ)\nsage: f=e([2]).expand(2)\nsage: f\nx0*x1\nsage: f.parent()\nMultivariate Polynomial Ring in x0, x1, x2 over Rational Field\n```\n\n\nThe same code but for SFASchur results in:\n\n```\nsage: s=SFASchur(QQ)\nsage: f=s([2]).expand(2)\nsage: f\nx0^2 + x0*x1 + x1^2\nsage: f.parent()\nMultivariate Polynomial Ring in x0, x1 over Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1873\n\n",
    "created_at": "2008-01-20T22:22:55Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "title": "[with patch] elementary function expansion returns result in the wrong ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1873",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  sage-combinat

I'm using Sage 2.10 now. Expansion for elements in SFAElementary works
great now, but there is another problem: the expansion lies in the
wrong ring.

```
sage: e=SFAElementary(QQ)
sage: f=e([2]).expand(2)
sage: f
x0*x1
sage: f.parent()
Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
```


The same code but for SFASchur results in:

```
sage: s=SFASchur(QQ)
sage: f=s([2]).expand(2)
sage: f
x0^2 + x0*x1 + x1^2
sage: f.parent()
Multivariate Polynomial Ring in x0, x1 over Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/1873





---

archive/issue_comments_011861.json:
```json
{
    "body": "Attachment [1873.patch](tarball://root/attachments/some-uuid/ticket1873/1873.patch) by mhansen created at 2008-01-20 22:27:07",
    "created_at": "2008-01-20T22:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11861",
    "user": "mhansen"
}
```

Attachment [1873.patch](tarball://root/attachments/some-uuid/ticket1873/1873.patch) by mhansen created at 2008-01-20 22:27:07



---

archive/issue_comments_011862.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T22:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11862",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011863.json:
```json
{
    "body": "Looks fine to me, and appears to fix the ticket.\n\nmhansen has the super-commit-bit in this area anyway, in my opinion :)",
    "created_at": "2008-01-22T19:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11863",
    "user": "ncalexan"
}
```

Looks fine to me, and appears to fix the ticket.

mhansen has the super-commit-bit in this area anyway, in my opinion :)



---

archive/issue_comments_011864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-23T04:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11864",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011865.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-23T04:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1873#issuecomment-11865",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
