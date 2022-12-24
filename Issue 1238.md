# Issue 1238: update the cremona spkg

archive/issues_001238.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n\nAttached bundle fixes the point below: now cerr is only used for\nprompts, hence not at all in the library functions.  Instead, the\nfatal error conditions which send output now to cout are followed by a\ncall to abort().  Clearly this should never happen except if there's a\nbug.\n\nRalf -- a lot of those error outputs were in the linalg code which you\nare going to refactor.\n\nSecondly, I fixed the unintended output of \"transposing...\" reported by William.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1238\n\n",
    "created_at": "2007-11-21T17:30:10Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "update the cremona spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1238",
    "user": "was"
}
```
Assignee: was


```


Attached bundle fixes the point below: now cerr is only used for
prompts, hence not at all in the library functions.  Instead, the
fatal error conditions which send output now to cout are followed by a
call to abort().  Clearly this should never happen except if there's a
bug.

Ralf -- a lot of those error outputs were in the linalg code which you
are going to refactor.

Secondly, I fixed the unintended output of "transposing..." reported by William.
```


Issue created by migration from https://trac.sagemath.org/ticket/1238





---

archive/issue_comments_007739.json:
```json
{
    "body": "Attachment [a(2).hg](tarball://root/attachments/some-uuid/ticket1238/a(2).hg) by was created at 2007-11-21 17:30:54",
    "created_at": "2007-11-21T17:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1238#issuecomment-7739",
    "user": "was"
}
```

Attachment [a(2).hg](tarball://root/attachments/some-uuid/ticket1238/a(2).hg) by was created at 2007-11-21 17:30:54



---

archive/issue_comments_007740.json:
```json
{
    "body": "This issue will also be closed by the spkg at #1247.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T10:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1238#issuecomment-7740",
    "user": "mabshoff"
}
```

This issue will also be closed by the spkg at #1247.

Cheers,

Michael



---

archive/issue_comments_007741.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-24T15:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1238#issuecomment-7741",
    "user": "mabshoff"
}
```

Resolution: fixed
