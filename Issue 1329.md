# Issue 1329: 2.8.14/Solaris: real_rqdf.pyx compile fixes

archive/issues_001329.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Solaris we need some of the following two patches to make it compile. Those aren't clean and would break compilation on other platforms.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1329\n\n",
    "created_at": "2007-11-28T22:28:35Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "2.8.14/Solaris: real_rqdf.pyx compile fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1329",
    "user": "mabshoff"
}
```
Assignee: mabshoff

On Solaris we need some of the following two patches to make it compile. Those aren't clean and would break compilation on other platforms.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1329





---

archive/issue_comments_008507.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-28T22:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8507",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_008508.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-30T03:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8508",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_008509.json:
```json
{
    "body": "The patch Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch includes all fixes from #1328 and #1329 in a cleaned up for. Apply that patch only.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T03:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8509",
    "user": "mabshoff"
}
```

The patch Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch includes all fixes from #1328 and #1329 in a cleaned up for. Apply that patch only.

Cheers,

Michael



---

archive/issue_comments_008510.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-30T03:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8510",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008511.json:
```json
{
    "body": "Patch passes compile test and testall on non-Solaris.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T07:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8511",
    "user": "mabshoff"
}
```

Patch passes compile test and testall on non-Solaris.

Cheers,

Michael



---

archive/issue_comments_008512.json:
```json
{
    "body": "Tested that it doesn't break anything on linux.",
    "created_at": "2008-01-30T07:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8512",
    "user": "jkantor"
}
```

Tested that it doesn't break anything on linux.



---

archive/issue_comments_008513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T07:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8513",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008514.json:
```json
{
    "body": "Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T07:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1329#issuecomment-8514",
    "user": "mabshoff"
}
```

Merged Sage-2.10.1.rc2-Solaris-build-fixes-for-sage.spkg.patch in Sage 2.10.1.rc3
