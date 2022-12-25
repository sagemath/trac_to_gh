# Issue 3998: [with patch, needs review] doctest the sage0 interface

archive/issues_003998.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3998\n\n",
    "created_at": "2008-08-29T21:59:57Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] doctest the sage0 interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3998",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/3998





---

archive/issue_comments_028662.json:
```json
{
    "body": "Attachment [trac_3998.patch](tarball://root/attachments/some-uuid/ticket3998/trac_3998.patch) by @mwhansen created at 2008-08-29 22:00:03",
    "created_at": "2008-08-29T22:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3998#issuecomment-28662",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3998.patch](tarball://root/attachments/some-uuid/ticket3998/trac_3998.patch) by @mwhansen created at 2008-08-29 22:00:03



---

archive/issue_comments_028663.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-08-29T23:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3998#issuecomment-28663",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_028664.json:
```json
{
    "body": "This looked very familiar and in fact the patch is already in 3.1.2.alpha2:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run -R < trac_3998.patch\\?format\\=raw \npatching file sage/interfaces/sage0.py\n```\n\nSo, this is a dupe of #3983.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T23:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3998#issuecomment-28664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This looked very familiar and in fact the patch is already in 3.1.2.alpha2:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run -R < trac_3998.patch\?format\=raw 
patching file sage/interfaces/sage0.py
```

So, this is a dupe of #3983.

Cheers,

Michael



---

archive/issue_events_009157.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-29T23:00:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3998#event-9157"
}
```
