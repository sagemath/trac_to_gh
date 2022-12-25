# Issue 1147: change location of valgrind output files to something less obnoxious

archive/issues_001147.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen running \n\n``` \n  sage -valgrind\n```\n\n\nthe output files are all over in $HOME/.sage.  They should be put in a file \n\n```\n  $HOME/.sage/valgrind\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1147\n\n",
    "created_at": "2007-11-11T14:44:26Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "change location of valgrind output files to something less obnoxious",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1147",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

When running 

``` 
  sage -valgrind
```


the output files are all over in $HOME/.sage.  They should be put in a file 

```
  $HOME/.sage/valgrind
```



Issue created by migration from https://trac.sagemath.org/ticket/1147





---

archive/issue_comments_006978.json:
```json
{
    "body": ":) - will do once I add proper omega report for 2.8.13.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-11T15:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

:) - will do once I add proper omega report for 2.8.13.

Cheers,

Michael



---

archive/issue_comments_006979.json:
```json
{
    "body": "At least these should be put in `$HOME/.sage/valgrind-memcheck`, `$HOME/.sage/valgrind-cachgrind` etc.",
    "created_at": "2007-11-11T15:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6979",
    "user": "https://github.com/malb"
}
```

At least these should be put in `$HOME/.sage/valgrind-memcheck`, `$HOME/.sage/valgrind-cachgrind` etc.



---

archive/issue_comments_006980.json:
```json
{
    "body": "Attachment [trac-1147.patch](tarball://root/attachments/some-uuid/ticket1147/trac-1147.patch) by @williamstein created at 2007-12-02 19:53:19\n\nApply this to the scripts repo!",
    "created_at": "2007-12-02T19:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6980",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1147.patch](tarball://root/attachments/some-uuid/ticket1147/trac-1147.patch) by @williamstein created at 2007-12-02 19:53:19

Apply this to the scripts repo!



---

archive/issue_comments_006981.json:
```json
{
    "body": "It fails to apply cleanly against 2.9. The patch itself is good, if I have some time later I will try to correct the issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-18T21:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6981",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It fails to apply cleanly against 2.9. The patch itself is good, if I have some time later I will try to correct the issue.

Cheers,

Michael



---

archive/issue_comments_006982.json:
```json
{
    "body": "I fixed the hunk that gets rejected. positive review now ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T19:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed the hunk that gets rejected. positive review now ;)

Cheers,

Michael



---

archive/issue_comments_006983.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006984.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-6984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
