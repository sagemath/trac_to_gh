# Issue 4996: OSX64: add proper libcsage build support

archive/issues_004996.json:
```json
{
    "body": "Assignee: mabshoff\n\nPatch coming up: We need to add \n\n```\n## We want the debug and optimization flags, since debug symbols are so useful, etc.\nenv.Append( CFLAGS=\"-O2 -g -m64\" )\nenv.Append( CXXFLAGS=\"-O2 -g -m64\" )\nenv.Append( LINKFLAGS=\"-m64 -single_module -flat_namespace -undefined dynamic_lookup\" )\n```\n\nin case we are building in 64 bit mode on OSX.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4996\n\n",
    "created_at": "2009-01-17T15:37:45Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "OSX64: add proper libcsage build support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4996",
    "user": "mabshoff"
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

archive/issue_comments_038117.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-17T15:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38117",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038118.json:
```json
{
    "body": "Attachment [trac_4996-OSX64-libcsage.patch](tarball://root/attachments/some-uuid/ticket4996/trac_4996-OSX64-libcsage.patch) by mabshoff created at 2009-01-22 19:07:34",
    "created_at": "2009-01-22T19:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38118",
    "user": "mabshoff"
}
```

Attachment [trac_4996-OSX64-libcsage.patch](tarball://root/attachments/some-uuid/ticket4996/trac_4996-OSX64-libcsage.patch) by mabshoff created at 2009-01-22 19:07:34



---

archive/issue_comments_038119.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T00:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38119",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038120.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T00:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38120",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038121.json:
```json
{
    "body": "+1 post-mortem...",
    "created_at": "2009-01-23T00:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38121",
    "user": "rlm"
}
```

+1 post-mortem...



---

archive/issue_comments_038122.json:
```json
{
    "body": "Yeah, sorry that I jumped the gun here ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T00:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4996#issuecomment-38122",
    "user": "mabshoff"
}
```

Yeah, sorry that I jumped the gun here ;)

Cheers,

Michael
