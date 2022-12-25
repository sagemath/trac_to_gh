# Issue 4996: [with patch, positive review] OSX64: add proper libcsage build support

archive/issues_004996.json:
```json
{
    "body": "Assignee: mabshoff\n\nPatch coming up: We need to add \n\n```\n## We want the debug and optimization flags, since debug symbols are so useful, etc.\nenv.Append( CFLAGS=\"-O2 -g -m64\" )\nenv.Append( CXXFLAGS=\"-O2 -g -m64\" )\nenv.Append( LINKFLAGS=\"-m64 -single_module -flat_namespace -undefined dynamic_lookup\" )\n```\nin case we are building in 64 bit mode on OSX.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4996\n\n",
    "closed_at": "2009-01-23T00:30:47Z",
    "created_at": "2009-01-17T15:37:45Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] OSX64: add proper libcsage build support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Patch coming up: We need to add 

```
## We want the debug and optimization flags, since debug symbols are so useful, etc.
env.Append( CFLAGS="-O2 -g -m64" )
env.Append( CXXFLAGS="-O2 -g -m64" )
env.Append( LINKFLAGS="-m64 -single_module -flat_namespace -undefined dynamic_lookup" )
```
in case we are building in 64 bit mode on OSX.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4996





---

archive/issue_comments_038045.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-17T15:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38045",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038046.json:
```json
{
    "body": "Attachment [trac_4996-OSX64-libcsage.patch](tarball://root/attachments/some-uuid/ticket4996/trac_4996-OSX64-libcsage.patch) by mabshoff created at 2009-01-22 19:07:34",
    "created_at": "2009-01-22T19:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38046",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4996-OSX64-libcsage.patch](tarball://root/attachments/some-uuid/ticket4996/trac_4996-OSX64-libcsage.patch) by mabshoff created at 2009-01-22 19:07:34



---

archive/issue_events_011555.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T00:30:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4996#event-11555"
}
```



---

archive/issue_comments_038047.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T00:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038048.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T00:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038049.json:
```json
{
    "body": "+1 post-mortem...",
    "created_at": "2009-01-23T00:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38049",
    "user": "https://github.com/rlmill"
}
```

+1 post-mortem...



---

archive/issue_comments_038050.json:
```json
{
    "body": "Yeah, sorry that I jumped the gun here ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T00:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38050",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yeah, sorry that I jumped the gun here ;)

Cheers,

Michael
