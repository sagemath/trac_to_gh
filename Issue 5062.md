# Issue 5062: Make sure that "sage -b" checks build compatibility on shared filesystems

archive/issues_005062.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a followup to #22:\n\nHaving thought about this and played around a little with uname it seems that it will not work and is not fine grained enough anyway. I would suggest to do write a small C program that identifies the following:\n\n* mode: i.e. 32, 64 bit\n* os: linux, osx, solaris, freebsd, cygwin\n* release: this would be the distribution on Linux, OSX 10.4/10.5, Solaris 10/Solaris 11/Opensolaris and so on \n\nThe way we can properly identify the build platform and decide more intelligently if we issue a warning, i.e running the Fedora 10 build on a Fedora 9 box should abort since it doesn't work. The test should be wrapped in a shell script since the binary will obviously only run on a subset of arches, i.e. if the binary fails to run we just about and print a canned warning together with a config info saved as text that is created when building the binary.\n\nThis is enough a task to split it off to a new ticket. I have some basic code that does some of the above already for OSX since I need this kind of code while cleaning up the build system.\n\nThoughts?\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5062\n\n",
    "created_at": "2009-01-23T00:33:30Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make sure that \"sage -b\" checks build compatibility on shared filesystems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5062",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is a followup to #22:

Having thought about this and played around a little with uname it seems that it will not work and is not fine grained enough anyway. I would suggest to do write a small C program that identifies the following:

* mode: i.e. 32, 64 bit
* os: linux, osx, solaris, freebsd, cygwin
* release: this would be the distribution on Linux, OSX 10.4/10.5, Solaris 10/Solaris 11/Opensolaris and so on 

The way we can properly identify the build platform and decide more intelligently if we issue a warning, i.e running the Fedora 10 build on a Fedora 9 box should abort since it doesn't work. The test should be wrapped in a shell script since the binary will obviously only run on a subset of arches, i.e. if the binary fails to run we just about and print a canned warning together with a config info saved as text that is created when building the binary.

This is enough a task to split it off to a new ticket. I have some basic code that does some of the above already for OSX since I need this kind of code while cleaning up the build system.

Thoughts?

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/5062





---

archive/issue_comments_038565.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T00:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5062#issuecomment-38565",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038566.json:
```json
{
    "body": "No idea really what this is about...",
    "created_at": "2013-12-19T12:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5062#issuecomment-38566",
    "user": "@jdemeyer"
}
```

No idea really what this is about...



---

archive/issue_comments_038567.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-19T12:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5062#issuecomment-38567",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038568.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-19T12:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5062#issuecomment-38568",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038569.json:
```json
{
    "body": "E.g. on skynet one could print an error when trying to run a sparc binary on x86. Though I can assure you there will be an error even without the theck ;-)  In any case, implementation would just have to compare some uname entries, no need for a C program.",
    "created_at": "2013-12-20T15:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5062#issuecomment-38569",
    "user": "@vbraun"
}
```

E.g. on skynet one could print an error when trying to run a sparc binary on x86. Though I can assure you there will be an error even without the theck ;-)  In any case, implementation would just have to compare some uname entries, no need for a C program.



---

archive/issue_comments_038570.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-12-20T15:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5062#issuecomment-38570",
    "user": "@vbraun"
}
```

Resolution: wontfix
