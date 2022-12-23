# Issue 1147: change location of valgrind output files to something less obnoxious

archive/issues_001147.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen running \n\n``` \n  sage -valgrind\n```\n\n\nthe output files are all over in $HOME/.sage.  They should be put in a file \n\n```\n  $HOME/.sage/valgrind\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1147\n\n",
    "created_at": "2007-11-11T14:44:26Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "change location of valgrind output files to something less obnoxious",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1147",
    "user": "was"
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

archive/issue_comments_007000.json:
```json
{
    "body": ":) - will do once I add proper omega report for 2.8.13.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-11T15:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7000",
    "user": "mabshoff"
}
```

:) - will do once I add proper omega report for 2.8.13.

Cheers,

Michael



---

archive/issue_comments_007001.json:
```json
{
    "body": "At least these should be put in `$HOME/.sage/valgrind-memcheck`, `$HOME/.sage/valgrind-cachgrind` etc.",
    "created_at": "2007-11-11T15:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7001",
    "user": "malb"
}
```

At least these should be put in `$HOME/.sage/valgrind-memcheck`, `$HOME/.sage/valgrind-cachgrind` etc.



---

archive/issue_comments_007002.json:
```json
{
    "body": "Attachment\n\nApply this to the scripts repo!",
    "created_at": "2007-12-02T19:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7002",
    "user": "was"
}
```

Attachment

Apply this to the scripts repo!



---

archive/issue_comments_007003.json:
```json
{
    "body": "It fails to apply cleanly against 2.9. The patch itself is good, if I have some time later I will try to correct the issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-18T21:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7003",
    "user": "mabshoff"
}
```

It fails to apply cleanly against 2.9. The patch itself is good, if I have some time later I will try to correct the issue.

Cheers,

Michael



---

archive/issue_comments_007004.json:
```json
{
    "body": "I fixed the hunk that gets rejected. positive review now ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T19:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7004",
    "user": "mabshoff"
}
```

I fixed the hunk that gets rejected. positive review now ;)

Cheers,

Michael



---

archive/issue_comments_007005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7005",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007006.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1147#issuecomment-7006",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
