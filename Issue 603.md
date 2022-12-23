# Issue 603: add documentation/tutorial on how to valgrind Sage

archive/issues_000603.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  mvngu\n\nSee http://www.sagemath.org:9001/ValgrindingSage for a working copy of the document. Once it is deemed usable we should use it to html and merge it into the official documentation.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/603\n\n",
    "created_at": "2007-09-06T19:35:54Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "add documentation/tutorial on how to valgrind Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/603",
    "user": "mabshoff"
}
```
Assignee: burcin

CC:  mvngu

See http://www.sagemath.org:9001/ValgrindingSage for a working copy of the document. Once it is deemed usable we should use it to html and merge it into the official documentation.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/603





---

archive/issue_comments_003108.json:
```json
{
    "body": "It's probably better to have this in the documentation in some form than not at all - even a brief intro in the Developer Guide might encourage someone to learn to use it properly.   I'm cc:ing a likely suspect for doing so nicely :)",
    "created_at": "2009-12-30T04:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/603#issuecomment-3108",
    "user": "kcrisman"
}
```

It's probably better to have this in the documentation in some form than not at all - even a brief intro in the Developer Guide might encourage someone to learn to use it properly.   I'm cc:ing a likely suspect for doing so nicely :)



---

archive/issue_comments_003109.json:
```json
{
    "body": "Just a note to add a note that `sage -t --valgrind` runs the tests with the `--serial` option in order to have them all in one process (and therefore it's not necessary to add it explicitly---which may not work).",
    "created_at": "2015-10-12T06:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/603#issuecomment-3109",
    "user": "rws"
}
```

Just a note to add a note that `sage -t --valgrind` runs the tests with the `--serial` option in order to have them all in one process (and therefore it's not necessary to add it explicitly---which may not work).
