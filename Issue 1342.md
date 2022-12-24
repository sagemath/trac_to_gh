# Issue 1342: very serious bug in number field residue_field

archive/issues_001342.json:
```json
{
    "body": "Assignee: was\n\nNotice that the parent of a changes below when you do a*a!!\n\n\n```\nsage: K.<z> = CyclotomicField(7)\nsage: P = K.factor_integer(17)[0][0]\nsage: ff = K.residue_field(P)\nsage: a = ff(z)\nsage: parent(a)\nResidue field of Fractional ideal (17)\nsage: parent(a*a)\nFinite Field in z of size 17^6\n```\n\n\nThis doesn't happen if 17 is replaced by something much smaller.\nThe problem is an optimization in finite field pari element, which\nhas two separate parent attributes. BAD.  \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1342\n\n",
    "created_at": "2007-11-30T09:16:28Z",
    "labels": [
        "number theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "very serious bug in number field residue_field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1342",
    "user": "was"
}
```
Assignee: was

Notice that the parent of a changes below when you do a*a!!


```
sage: K.<z> = CyclotomicField(7)
sage: P = K.factor_integer(17)[0][0]
sage: ff = K.residue_field(P)
sage: a = ff(z)
sage: parent(a)
Residue field of Fractional ideal (17)
sage: parent(a*a)
Finite Field in z of size 17^6
```


This doesn't happen if 17 is replaced by something much smaller.
The problem is an optimization in finite field pari element, which
has two separate parent attributes. BAD.  


Issue created by migration from https://trac.sagemath.org/ticket/1342





---

archive/issue_comments_008609.json:
```json
{
    "body": "Attachment [trac1342-part2.patch](tarball://root/attachments/some-uuid/ticket1342/trac1342-part2.patch) by was created at 2007-12-02 03:45:16",
    "created_at": "2007-12-02T03:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1342#issuecomment-8609",
    "user": "was"
}
```

Attachment [trac1342-part2.patch](tarball://root/attachments/some-uuid/ticket1342/trac1342-part2.patch) by was created at 2007-12-02 03:45:16



---

archive/issue_comments_008610.json:
```json
{
    "body": "Looks good to me. -- David Roe",
    "created_at": "2007-12-02T04:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1342#issuecomment-8610",
    "user": "roed"
}
```

Looks good to me. -- David Roe



---

archive/issue_comments_008611.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T04:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1342#issuecomment-8611",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008612.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T04:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1342",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1342#issuecomment-8612",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.
