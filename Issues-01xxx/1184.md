# Issue 1184: OSX 10.4: moving sage breaks recompile -> NTL related

archive/issues_001184.json:
```json
{
    "body": "Assignee: mabshoff\n\nMoving a sage install on OSX 10.4 and then upgrading anything that is linked against NTL leads to link errors due to missing gmp symbols. The problem is the link mode with which the dynamic NTL is created. I have a fix, but I am currently verifying that it really fixes the issue. Everything that is linked against NTL needs to be recompiled, i.e. singular and cremona at the moment.\n\nTo add to the confusion: This is not an issue on OSX 10.5.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1184\n\n",
    "closed_at": "2007-12-02T04:13:49Z",
    "created_at": "2007-11-16T03:39:13Z",
    "labels": [
        "component: relocation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "OSX 10.4: moving sage breaks recompile -> NTL related",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Moving a sage install on OSX 10.4 and then upgrading anything that is linked against NTL leads to link errors due to missing gmp symbols. The problem is the link mode with which the dynamic NTL is created. I have a fix, but I am currently verifying that it really fixes the issue. Everything that is linked against NTL needs to be recompiled, i.e. singular and cremona at the moment.

To add to the confusion: This is not an issue on OSX 10.5.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1184





---

archive/issue_events_003165.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-26T19:56:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1184#event-3165"
}
```



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

archive/issue_events_003166.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T04:13:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1184",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1184#event-3166"
}
```
