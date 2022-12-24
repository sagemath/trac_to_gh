# Issue 4131: [with patch, needs review] unbreak sage-clone

archive/issues_004131.json:
```json
{
    "body": "Assignee: mabshoff\n\nSome bash code snuck into the python script sage-clone. This patch fixes it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4131\n\n",
    "created_at": "2008-09-16T01:37:36Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] unbreak sage-clone",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4131",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Some bash code snuck into the python script sage-clone. This patch fixes it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4131





---

archive/issue_comments_029953.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-16T01:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29953",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029954.json:
```json
{
    "body": "Attachment [trac_4131.patch](tarball://root/attachments/some-uuid/ticket4131/trac_4131.patch) by mabshoff created at 2008-09-16 01:39:10",
    "created_at": "2008-09-16T01:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29954",
    "user": "mabshoff"
}
```

Attachment [trac_4131.patch](tarball://root/attachments/some-uuid/ticket4131/trac_4131.patch) by mabshoff created at 2008-09-16 01:39:10



---

archive/issue_comments_029955.json:
```json
{
    "body": "Oops. :-)",
    "created_at": "2008-09-16T01:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29955",
    "user": "mhansen"
}
```

Oops. :-)



---

archive/issue_comments_029956.json:
```json
{
    "body": "I'm confused:\n\n\n```\nwdj@hera:~/sagefiles/sage-3.1.2.rc4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.rc4, Release Date: 2008-09-15                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: hg_sage.apply(\"/home/wdj/sagefiles/trac_4131.patch\")\ncd \"/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage\" && hg status\ncd \"/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage\" && hg import   \"/home/wdj/sagefiles/trac_4131.patch\"\napplying /home/wdj/sagefiles/trac_4131.patch\nunable to find 'sage-clone' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage-clone.rej\nabort: patch failed to apply\nsage:                                                \n```\n\n\nI see sage-clone in /home/wdj/sagefiles/sage-3.1.2.rc4/local/bin,\nso what the heck is going on?",
    "created_at": "2008-09-16T01:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29956",
    "user": "wdj"
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

archive/issue_comments_029957.json:
```json
{
    "body": "You use hg_scripts.apply() to apply this patch.",
    "created_at": "2008-09-16T01:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29957",
    "user": "mhansen"
}
```

You use hg_scripts.apply() to apply this patch.



---

archive/issue_comments_029958.json:
```json
{
    "body": "Thanks. Applied fine now and sage -clone is working:-)",
    "created_at": "2008-09-16T01:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29958",
    "user": "wdj"
}
```

Thanks. Applied fine now and sage -clone is working:-)



---

archive/issue_comments_029959.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-16T03:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29959",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029960.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc5",
    "created_at": "2008-09-16T03:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4131#issuecomment-29960",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc5
