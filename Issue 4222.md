# Issue 4222: Building R fails due to problem with readline

archive/issues_004222.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: R, readline, .d-files\n\nUnder GNU/Linux i686, the built of R failed, and the complaint is\n`  making sys-std.d from sys-std.c`\n`  sys-std.c:401:33: error: readline/readline.h: No such file or directory`\n`  sys-std.c:431:32: error: readline/history.h: No such file or directory`\n\nmabshoff reportedly has hit that problem before, it seems to be a bug in R when doing processing on .d files, but it isn't fixed yet.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4222\n\n",
    "created_at": "2008-09-30T13:09:01Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Building R fails due to problem with readline",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4222",
    "user": "SimonKing"
}
```
Assignee: mabshoff

Keywords: R, readline, .d-files

Under GNU/Linux i686, the built of R failed, and the complaint is
`  making sys-std.d from sys-std.c`
`  sys-std.c:401:33: error: readline/readline.h: No such file or directory`
`  sys-std.c:431:32: error: readline/history.h: No such file or directory`

mabshoff reportedly has hit that problem before, it seems to be a bug in R when doing processing on .d files, but it isn't fixed yet.



Issue created by migration from https://trac.sagemath.org/ticket/4222





---

archive/issue_comments_030675.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/r-2.6.1.p20.spkg\n\nshould fix the issue by setting CPPFLAGS correctly. The issue I saw on another box is likely orthogonal.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T13:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30675",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/r-2.6.1.p20.spkg

should fix the issue by setting CPPFLAGS correctly. The issue I saw on another box is likely orthogonal.

Cheers,

Michael



---

archive/issue_comments_030676.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-30T13:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30676",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030677.json:
```json
{
    "body": "I tried to replace the old with the new package and did \"make\" again, but it did not help.",
    "created_at": "2008-09-30T13:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30677",
    "user": "SimonKing"
}
```

I tried to replace the old with the new package and did "make" again, but it did not help.



---

archive/issue_comments_030678.json:
```json
{
    "body": "The commonly used label is \"needs work\"\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T13:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30678",
    "user": "mabshoff"
}
```

The commonly used label is "needs work"

Cheers,

Michael



---

archive/issue_comments_030679.json:
```json
{
    "body": "The most recent version of that spkg (md5sum de0de83b25ca7b9e0a65246c067f0afa) works! Now R builds although the global readline headers are not present.\n\nSo, I guess this is a positive review.",
    "created_at": "2008-09-30T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30679",
    "user": "SimonKing"
}
```

The most recent version of that spkg (md5sum de0de83b25ca7b9e0a65246c067f0afa) works! Now R builds although the global readline headers are not present.

So, I guess this is a positive review.



---

archive/issue_comments_030680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-30T18:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30680",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030681.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-30T18:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4222#issuecomment-30681",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
