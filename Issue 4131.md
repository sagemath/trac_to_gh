# Issue 4131: [with patch, needs review] unbreak sage-clone

archive/issues_004131.json:
```json
{
    "body": "Assignee: mabshoff\n\nSome bash code snuck into the python script sage-clone. This patch fixes it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4131\n\n",
    "created_at": "2008-09-16T01:37:36Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] unbreak sage-clone",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Some bash code snuck into the python script sage-clone. This patch fixes it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4131





---

archive/issue_comments_029894.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-16T01:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029895.json:
```json
{
    "body": "Attachment [trac_4131.patch](tarball://root/attachments/some-uuid/ticket4131/trac_4131.patch) by mabshoff created at 2008-09-16 01:39:10",
    "created_at": "2008-09-16T01:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29895",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4131.patch](tarball://root/attachments/some-uuid/ticket4131/trac_4131.patch) by mabshoff created at 2008-09-16 01:39:10



---

archive/issue_comments_029896.json:
```json
{
    "body": "Oops. :-)",
    "created_at": "2008-09-16T01:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29896",
    "user": "https://github.com/mwhansen"
}
```

Oops. :-)



---

archive/issue_comments_029897.json:
```json
{
    "body": "I'm confused:\n\n```\nwdj@hera:~/sagefiles/sage-3.1.2.rc4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.rc4, Release Date: 2008-09-15                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: hg_sage.apply(\"/home/wdj/sagefiles/trac_4131.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage\" && hg import   \"/home/wdj/sagefiles/trac_4131.patch\"\napplying /home/wdj/sagefiles/trac_4131.patch\nunable to find 'sage-clone' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage-clone.rej\nabort: patch failed to apply\nsage:                                                \n```\n\nI see sage-clone in /home/wdj/sagefiles/sage-3.1.2.rc4/local/bin,\nso what the heck is going on?",
    "created_at": "2008-09-16T01:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29897",
    "user": "https://github.com/wdjoyner"
}
```

I'm confused:

```
wdj@hera:~/sagefiles/sage-3.1.2.rc4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc4, Release Date: 2008-09-15                   |
| Type notebook() for the GUI, and license() for information.        |
sage: hg_sage.apply("/home/wdj/sagefiles/trac_4131.patch")
cd "/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage" && hg import   "/home/wdj/sagefiles/trac_4131.patch"
applying /home/wdj/sagefiles/trac_4131.patch
unable to find 'sage-clone' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage-clone.rej
abort: patch failed to apply
sage:                                                
```

I see sage-clone in /home/wdj/sagefiles/sage-3.1.2.rc4/local/bin,
so what the heck is going on?



---

archive/issue_comments_029898.json:
```json
{
    "body": "You use hg_scripts.apply() to apply this patch.",
    "created_at": "2008-09-16T01:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29898",
    "user": "https://github.com/mwhansen"
}
```

You use hg_scripts.apply() to apply this patch.



---

archive/issue_comments_029899.json:
```json
{
    "body": "Thanks. Applied fine now and sage -clone is working:-)",
    "created_at": "2008-09-16T01:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29899",
    "user": "https://github.com/wdjoyner"
}
```

Thanks. Applied fine now and sage -clone is working:-)



---

archive/issue_comments_029900.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-16T03:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29900",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009411.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-16T03:46:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4131#event-9411"
}
```



---

archive/issue_comments_029901.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc5",
    "created_at": "2008-09-16T03:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29901",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc5
