# Issue 2131: disable "padlock" support in libgcrypt

archive/issues_002131.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn some OS/compiler variants, the \"Padlock\" support fails to compile.\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/9d4b39e961c24e4f/89bfb1cd2822ffd2?lnk=gst&q=rijndael#89bfb1cd2822ffd2 for details.\n\nThe easy fix is to add \"--disable-padlock-support\" in the call to configure.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2131\n\n",
    "created_at": "2008-02-09T20:39:06Z",
    "labels": [
        "packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "disable \"padlock\" support in libgcrypt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2131",
    "user": "cwitty"
}
```
Assignee: mabshoff

On some OS/compiler variants, the "Padlock" support fails to compile.

See http://groups.google.com/group/sage-devel/browse_thread/thread/9d4b39e961c24e4f/89bfb1cd2822ffd2?lnk=gst&q=rijndael#89bfb1cd2822ffd2 for details.

The easy fix is to add "--disable-padlock-support" in the call to configure.

Issue created by migration from https://trac.sagemath.org/ticket/2131





---

archive/issue_comments_013978.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha0/libgcrypt-1.4.0.p0.spkg\n\nadds the option Paul suggested. It passes compile tests on 32 and 64 bit Linux boxen.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T11:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2131#issuecomment-13978",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha0/libgcrypt-1.4.0.p0.spkg

adds the option Paul suggested. It passes compile tests on 32 and 64 bit Linux boxen.

Cheers,

Michael



---

archive/issue_comments_013979.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-14T11:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2131#issuecomment-13979",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013980.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T11:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2131#issuecomment-13980",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0

Cheers,

Michael



---

archive/issue_comments_013981.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-14T11:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2131#issuecomment-13981",
    "user": "mabshoff"
}
```

Resolution: fixed
