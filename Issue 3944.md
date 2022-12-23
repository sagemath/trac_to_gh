# Issue 3944: replace "sage -upgrade" by "sage -expert_upgrade" and upgrade() by "expert_upgrade()"

archive/issues_003944.json:
```json
{
    "body": "Assignee: mabshoff\n\nI'm sick of people thinking \"sage -upgrade\" is supposed to work if you're a newbie user.  That was absolutely never the intention with the current design, and there's no way we should suggest it is.\nNew users, or those not familiar with building from source, should have to redownload rather than upgrade.   Maybe someday we'll have binary upgrades, but \"sage -upgrade\" certainly isn't that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3944\n\n",
    "created_at": "2008-08-24T16:15:35Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "replace \"sage -upgrade\" by \"sage -expert_upgrade\" and upgrade() by \"expert_upgrade()\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3944",
    "user": "was"
}
```
Assignee: mabshoff

I'm sick of people thinking "sage -upgrade" is supposed to work if you're a newbie user.  That was absolutely never the intention with the current design, and there's no way we should suggest it is.
New users, or those not familiar with building from source, should have to redownload rather than upgrade.   Maybe someday we'll have binary upgrades, but "sage -upgrade" certainly isn't that.

Issue created by migration from https://trac.sagemath.org/ticket/3944





---

archive/issue_comments_028313.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-24T16:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3944#issuecomment-28313",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_028314.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-24T16:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3944#issuecomment-28314",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_028315.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-24T17:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3944#issuecomment-28315",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_028316.json:
```json
{
    "body": "to be honest, I don't like the name that much. If you insist on renaming the thing then maybe `dev_upgrade` or `developer_upgrade` could be a better choice than \"expert\". I wouldn't want to call myself an expert but I'll use that function.",
    "created_at": "2008-08-24T23:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3944#issuecomment-28316",
    "user": "malb"
}
```

to be honest, I don't like the name that much. If you insist on renaming the thing then maybe `dev_upgrade` or `developer_upgrade` could be a better choice than "expert". I wouldn't want to call myself an expert but I'll use that function.



---

archive/issue_comments_028317.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-11-22T22:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3944#issuecomment-28317",
    "user": "was"
}
```

Resolution: wontfix
