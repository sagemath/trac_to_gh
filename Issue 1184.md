# Issue 1184: OSX: moving sage breaks recompile of libcsage (--rpath issue)

archive/issues_001184.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is likely one the first issue to be reported and involves the use of --rpath linker option. On OSX that leads to trouble when moving a Sage installation and recompiling the Sage library. Symptoms are the linker complaining that it cannot find a libgmp.dylib, specifically that gmp symbols with triple underscores are missing.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1184\n\n",
    "created_at": "2007-11-16T03:39:13Z",
    "labels": [
        "component: relocation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "OSX: moving sage breaks recompile of libcsage (--rpath issue)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

This is likely one the first issue to be reported and involves the use of --rpath linker option. On OSX that leads to trouble when moving a Sage installation and recompiling the Sage library. Symptoms are the linker complaining that it cannot find a libgmp.dylib, specifically that gmp symbols with triple underscores are missing.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1184





---

archive/issue_comments_007288.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-27T00:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1184#issuecomment-7288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007289.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2007-11-27T00:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1184#issuecomment-7289",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_007290.json:
```json
{
    "body": "Attachment [Sage-2.8.15.alpha1-twiddle-with-link-order.patch](tarball://root/attachments/some-uuid/ticket1184/Sage-2.8.15.alpha1-twiddle-with-link-order.patch) by mabshoff created at 2007-12-02 02:55:56\n\nThe updated spkg is at \n\nhttp://sage.math.washington.edu/home/mabshoff/ntl-5.4.1.p7.spkg\n\nYou need to apply both the patch and add the ntl.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-02T02:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1184#issuecomment-7290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.15.alpha1-twiddle-with-link-order.patch](tarball://root/attachments/some-uuid/ticket1184/Sage-2.8.15.alpha1-twiddle-with-link-order.patch) by mabshoff created at 2007-12-02 02:55:56

The updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/ntl-5.4.1.p7.spkg

You need to apply both the patch and add the ntl.spkg.

Cheers,

Michael



---

archive/issue_comments_007291.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T04:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1184#issuecomment-7291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007292.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T04:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1184#issuecomment-7292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha2.



---

archive/issue_events_001316.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-02T04:13:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1184#event-1316"
}
```
