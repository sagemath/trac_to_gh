# Issue 4526: Can't multiply symmetric functions by 0

archive/issues_004526.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jbandlow sage-combinat\n\nKeywords: symmetric functions\n\nThe following, which should just return 0 in SFASchur(QQ), is really nasty:\n\nsage: s = SFASchur(QQ)\nsage: 0 * s([1])\nsage.bin: : Unknown error 155689240\n\nand sage quits.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4526\n\n",
    "created_at": "2008-11-14T20:00:43Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Can't multiply symmetric functions by 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4526",
    "user": "https://github.com/jbandlow"
}
```
Assignee: @mwhansen

CC:  @jbandlow sage-combinat

Keywords: symmetric functions

The following, which should just return 0 in SFASchur(QQ), is really nasty:

sage: s = SFASchur(QQ)
sage: 0 * s([1])
sage.bin: : Unknown error 155689240

and sage quits.

Issue created by migration from https://trac.sagemath.org/ticket/4526





---

archive/issue_comments_033540.json:
```json
{
    "body": "arg... I meant\n\nsage: s = SFASchur(QQ)\n\nsage: 0 * s([1])\n\nof course.",
    "created_at": "2008-11-14T20:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33540",
    "user": "https://github.com/jbandlow"
}
```

arg... I meant

sage: s = SFASchur(QQ)

sage: 0 * s([1])

of course.



---

archive/issue_comments_033541.json:
```json
{
    "body": "FYI: the error message comes out of symmertrica. And:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sage-ipython\nGNU gdb 6.4.90-debian\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"x86_64-linux-gnu\"...Using host libthread_db library \"/lib/libthread_db.so.1\".\n| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |\n| Type notebook() for the GUI, and license() for information.        |\n[Thread debugging using libthread_db enabled]\n[New Thread 47664905056096 (LWP 26555)]\nPython 2.5.2 (r252:60911, Nov 10 2008, 22:40:35) \n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n\nsage: s = SFASchur(QQ)\nsage: 0 * s([1]) \n/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/python: OWER_symmetrica: Operation not permitted\n\nProgram exited with code 0341.\n(gdb) bt\nNo stack.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33541",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: the error message comes out of symmertrica. And:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sage-ipython
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
[Thread debugging using libthread_db enabled]
[New Thread 47664905056096 (LWP 26555)]
Python 2.5.2 (r252:60911, Nov 10 2008, 22:40:35) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

sage: s = SFASchur(QQ)
sage: 0 * s([1]) 
/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/python: OWER_symmetrica: Operation not permitted

Program exited with code 0341.
(gdb) bt
No stack.
```


Cheers,

Michael



---

archive/issue_comments_033542.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-15T02:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33542",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033543.json:
```json
{
    "body": "Attachment [trac_4526.patch](tarball://root/attachments/some-uuid/ticket4526/trac_4526.patch) by @mwhansen created at 2008-11-15 02:15:27",
    "created_at": "2008-11-15T02:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33543",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4526.patch](tarball://root/attachments/some-uuid/ticket4526/trac_4526.patch) by @mwhansen created at 2008-11-15 02:15:27



---

archive/issue_comments_033544.json:
```json
{
    "body": "Works for me.  Thanks Mike!",
    "created_at": "2008-11-15T03:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33544",
    "user": "https://github.com/jbandlow"
}
```

Works for me.  Thanks Mike!



---

archive/issue_comments_033545.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-15T04:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_events_004770.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-15T04:48:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4526#event-4770"
}
```



---

archive/issue_comments_033546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T04:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4526#issuecomment-33546",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
