# Issue 2233: [with patch] "valuation too large" in padics on 64bit

archive/issues_002233.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: K = Qp(19, 5, 'capped-rel','series')\nsage: K(5,3)^19\n<type 'exceptions.ValueError'>: Valuation too large\n```\n\n\nThis is caused by an int constant 1 being left-shifted by 62 and overflowing. Changing this constant to a long constant seems to fix it. See attached patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2233\n\n",
    "created_at": "2008-02-20T15:00:48Z",
    "labels": [
        "component: number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch] \"valuation too large\" in padics on 64bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2233",
    "user": "https://github.com/wjp"
}
```
Assignee: @williamstein


```
sage: K = Qp(19, 5, 'capped-rel','series')
sage: K(5,3)^19
<type 'exceptions.ValueError'>: Valuation too large
```


This is caused by an int constant 1 being left-shifted by 62 and overflowing. Changing this constant to a long constant seems to fix it. See attached patch.

Issue created by migration from https://trac.sagemath.org/ticket/2233





---

archive/issue_comments_014762.json:
```json
{
    "body": "Attachment [trac2233_padics.patch](tarball://root/attachments/some-uuid/ticket2233/trac2233_padics.patch) by @wjp created at 2008-02-20 15:02:34",
    "created_at": "2008-02-20T15:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14762",
    "user": "https://github.com/wjp"
}
```

Attachment [trac2233_padics.patch](tarball://root/attachments/some-uuid/ticket2233/trac2233_padics.patch) by @wjp created at 2008-02-20 15:02:34



---

archive/issue_comments_014763.json:
```json
{
    "body": "Attachment [trac2233_padics2.patch](tarball://root/attachments/some-uuid/ticket2233/trac2233_padics2.patch) by @wjp created at 2008-02-20 15:58:47",
    "created_at": "2008-02-20T15:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14763",
    "user": "https://github.com/wjp"
}
```

Attachment [trac2233_padics2.patch](tarball://root/attachments/some-uuid/ticket2233/trac2233_padics2.patch) by @wjp created at 2008-02-20 15:58:47



---

archive/issue_comments_014764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T17:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014765.json:
```json
{
    "body": "Attachment [trac2233_padics3.patch](tarball://root/attachments/some-uuid/ticket2233/trac2233_padics3.patch) by mabshoff created at 2008-02-20 17:20:03\n\nMerged all three patches in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T17:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac2233_padics3.patch](tarball://root/attachments/some-uuid/ticket2233/trac2233_padics3.patch) by mabshoff created at 2008-02-20 17:20:03

Merged all three patches in Sage 2.10.2.alpha2
