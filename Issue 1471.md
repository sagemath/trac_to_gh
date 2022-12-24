# Issue 1471: moving a sage install breaks clisp

archive/issues_001471.json:
```json
{
    "body": "Assignee: mabshoff\n\nMoving a Sage install breaks clisp. I moved `sage-2.9.alpha5` to `sage-2.9.alpha5-vg` and it broke clisp:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5-vg$ clisp\nclisp: /tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/local/lib/clisp/base/lisp.run: No such file or directory\n```\n\nI have no clue how Maxima still manages to work, but there must be a fix somehow.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1471\n\n",
    "created_at": "2007-12-12T09:36:13Z",
    "labels": [
        "distribution",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "moving a sage install breaks clisp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1471",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Moving a Sage install breaks clisp. I moved `sage-2.9.alpha5` to `sage-2.9.alpha5-vg` and it broke clisp:

```
mabshoff@sage:/tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5-vg$ clisp
clisp: /tmp/Work-mabshoff/release-cycles-2.9/sage-2.9.alpha5/local/lib/clisp/base/lisp.run: No such file or directory
```

I have no clue how Maxima still manages to work, but there must be a fix somehow.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1471





---

archive/issue_comments_009468.json:
```json
{
    "body": "Since sage-2.9.1.alpha3 this issue seems to be gone, maybe earlier? My standard procedure now is to relocate my installed sage before I do a make check.\n\nclisp just worked\n\nJaap",
    "created_at": "2007-12-22T19:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1471#issuecomment-9468",
    "user": "@jaapspies"
}
```

Since sage-2.9.1.alpha3 this issue seems to be gone, maybe earlier? My standard procedure now is to relocate my installed sage before I do a make check.

clisp just worked

Jaap



---

archive/issue_comments_009469.json:
```json
{
    "body": "I still see the problem with Sage 2.9.1.1. I assume you might have some other sage install in the right location, so you don't see the problem. I needed to adapt maxima to use `clisp.bin` instead of clisp (the default) to build. The following two spkgs fix the problem:\n\n* http://sage.math.washington.edu/home/mabshoff/clisp-2.41.p12.spkg\n* http://sage.math.washington.edu/home/mabshoff/maxima-5.13.0.p2.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-02T21:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1471#issuecomment-9469",
    "user": "mabshoff"
}
```

I still see the problem with Sage 2.9.1.1. I assume you might have some other sage install in the right location, so you don't see the problem. I needed to adapt maxima to use `clisp.bin` instead of clisp (the default) to build. The following two spkgs fix the problem:

* http://sage.math.washington.edu/home/mabshoff/clisp-2.41.p12.spkg
* http://sage.math.washington.edu/home/mabshoff/maxima-5.13.0.p2.spkg

Cheers,

Michael



---

archive/issue_comments_009470.json:
```json
{
    "body": "Michael, your spkgs fixed the problem for me.",
    "created_at": "2008-01-03T07:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1471#issuecomment-9470",
    "user": "@mwhansen"
}
```

Michael, your spkgs fixed the problem for me.



---

archive/issue_comments_009471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T07:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1471#issuecomment-9471",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009472.json:
```json
{
    "body": "Merged in 2.9.2.alpha0",
    "created_at": "2008-01-03T07:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1471#issuecomment-9472",
    "user": "mabshoff"
}
```

Merged in 2.9.2.alpha0
