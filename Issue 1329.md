# Issue 1329: 2.8.14/Solaris: real_rqdf.pyx compile fixes

archive/issues_001329.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Solaris we need some of the following two patches to make it compile. Those aren't clean and would break compilation on other platforms.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1329\n\n",
    "created_at": "2007-11-28T22:28:35Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "2.8.14/Solaris: real_rqdf.pyx compile fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1329",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On Solaris we need some of the following two patches to make it compile. Those aren't clean and would break compilation on other platforms.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1329





---

archive/issue_comments_008483.json:
```json
{
    "body": "Attachment [Sage-2.8.14-rqdf_fix.h-on-Solaris-unclean.patch](tarball://root/attachments/some-uuid/ticket1329/Sage-2.8.14-rqdf_fix.h-on-Solaris-unclean.patch) by mabshoff created at 2007-11-28 22:29:19",
    "created_at": "2007-11-28T22:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8483",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.14-rqdf_fix.h-on-Solaris-unclean.patch](tarball://root/attachments/some-uuid/ticket1329/Sage-2.8.14-rqdf_fix.h-on-Solaris-unclean.patch) by mabshoff created at 2007-11-28 22:29:19



---

archive/issue_comments_008484.json:
```json
{
    "body": "Attachment [Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch](tarball://root/attachments/some-uuid/ticket1329/Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch) by mabshoff created at 2008-01-30 03:19:11",
    "created_at": "2008-01-30T03:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8484",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch](tarball://root/attachments/some-uuid/ticket1329/Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch) by mabshoff created at 2008-01-30 03:19:11



---

archive/issue_comments_008485.json:
```json
{
    "body": "The patch Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch includes all fixes from #1328 and #1329 in a cleaned up for. Apply that patch only.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T03:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch includes all fixes from #1328 and #1329 in a cleaned up for. Apply that patch only.

Cheers,

Michael



---

archive/issue_comments_008486.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-30T03:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8486",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008487.json:
```json
{
    "body": "Patch passes compile test and testall on non-Solaris.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T07:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8487",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch passes compile test and testall on non-Solaris.

Cheers,

Michael



---

archive/issue_comments_008488.json:
```json
{
    "body": "Tested that it doesn't break anything on linux.",
    "created_at": "2008-01-30T07:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8488",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Tested that it doesn't break anything on linux.



---

archive/issue_comments_008489.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T07:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8489",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008490.json:
```json
{
    "body": "Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T07:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch in Sage 2.10.1.rc3



---

archive/issue_events_001469.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-30T07:55:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1329#event-1469"
}
```
