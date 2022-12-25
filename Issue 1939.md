# Issue 1939: [with patch] Fix OSX rpy import issues: DYLD_LIBRARY_PATH fix

archive/issues_001939.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe latest r.spkg from \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc0/r-2.6.1.p13.spkg\n\nneeds the attached patch to properly import libR.dylib. `DYLD_LIBRARY_PATH` is properly set, but from some reason import fails. By adding the R's `lib` directory to `DY_LDLIBRARY_PATH` in `sage-env` the issue is resolved. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1939\n\n",
    "created_at": "2008-01-26T13:45:33Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch] Fix OSX rpy import issues: DYLD_LIBRARY_PATH fix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1939",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The latest r.spkg from 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc0/r-2.6.1.p13.spkg

needs the attached patch to properly import libR.dylib. `DYLD_LIBRARY_PATH` is properly set, but from some reason import fails. By adding the R's `lib` directory to `DY_LDLIBRARY_PATH` in `sage-env` the issue is resolved. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1939





---

archive/issue_comments_012277.json:
```json
{
    "body": "Attachment [Sage-2.10.1.rc0-fix-rpy-import-on-OSX.patch](tarball://root/attachments/some-uuid/ticket1939/Sage-2.10.1.rc0-fix-rpy-import-on-OSX.patch) by mabshoff created at 2008-01-26 13:45:46",
    "created_at": "2008-01-26T13:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1939#issuecomment-12277",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.1.rc0-fix-rpy-import-on-OSX.patch](tarball://root/attachments/some-uuid/ticket1939/Sage-2.10.1.rc0-fix-rpy-import-on-OSX.patch) by mabshoff created at 2008-01-26 13:45:46



---

archive/issue_comments_012278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-26T13:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1939#issuecomment-12278",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012279.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc0",
    "created_at": "2008-01-26T13:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1939",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1939#issuecomment-12279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc0
