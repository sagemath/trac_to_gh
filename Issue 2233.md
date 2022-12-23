# Issue 2233: [with patch] "valuation too large" in padics on 64bit

archive/issues_002233.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: K = Qp(19, 5, 'capped-rel','series')\nsage: K(5,3)^19\n<type 'exceptions.ValueError'>: Valuation too large\n```\n\n\nThis is caused by an int constant 1 being left-shifted by 62 and overflowing. Changing this constant to a long constant seems to fix it. See attached patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2233\n\n",
    "created_at": "2008-02-20T15:00:48Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "title": "[with patch] \"valuation too large\" in padics on 64bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2233",
    "user": "wjp"
}
```
Assignee: was


```
sage: K = Qp(19, 5, 'capped-rel','series')
sage: K(5,3)^19
<type 'exceptions.ValueError'>: Valuation too large
```


This is caused by an int constant 1 being left-shifted by 62 and overflowing. Changing this constant to a long constant seems to fix it. See attached patch.

Issue created by migration from https://trac.sagemath.org/ticket/2233





---

archive/issue_comments_014793.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-20T15:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14793",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_014794.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-20T15:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14794",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_014795.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T17:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14795",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014796.json:
```json
{
    "body": "Attachment\n\nMerged all three patches in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T17:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2233#issuecomment-14796",
    "user": "mabshoff"
}
```

Attachment

Merged all three patches in Sage 2.10.2.alpha2
