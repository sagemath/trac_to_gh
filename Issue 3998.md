# Issue 3998: [with patch, needs review] doctest the sage0 interface

archive/issues_003998.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3998\n\n",
    "created_at": "2008-08-29T21:59:57Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] doctest the sage0 interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3998",
    "user": "mhansen"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/3998





---

archive/issue_comments_028720.json:
```json
{
    "body": "Attachment [trac_3998.patch](tarball://root/attachments/some-uuid/ticket3998/trac_3998.patch) by mhansen created at 2008-08-29 22:00:03",
    "created_at": "2008-08-29T22:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3998#issuecomment-28720",
    "user": "mhansen"
}
```

Attachment [trac_3998.patch](tarball://root/attachments/some-uuid/ticket3998/trac_3998.patch) by mhansen created at 2008-08-29 22:00:03



---

archive/issue_comments_028721.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-08-29T23:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3998#issuecomment-28721",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_028722.json:
```json
{
    "body": "This looked very familiar and in fact the patch is already in 3.1.2.alpha2:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run -R < trac_3998.patch\\?format\\=raw \npatching file sage/interfaces/sage0.py\n```\n\nSo, this is a dupe of #3983.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T23:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3998#issuecomment-28722",
    "user": "mabshoff"
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
