# Issue 2202: [with spkg; needs review] Debianize rubiks spkg

archive/issues_002202.json:
```json
{
    "body": "Assignee: tabbott\n\nI created a new spkg for rubiks that has a global Makefile, and added Debian build support to it:\n\nhttp://sage.math.washington.edu/home/tabbott/rubiks-20070912.p2.spkg\n\nThe process involved adding distclean targets to the individual Makefiles for the various solvers; for now I made these changes in the spkg because I'm a bad person; but we should submit them upstream for those that we are not the official distribution point for.  I've attached patches for each to this ticket which we can submit to the upstream authors.\n\nThere are two things that bug me about this package.  One is that I'm not convinced Debian will want this motley assortment of rubiks cube solvers (so that we might end up leaving it as part of the \"sagemath\" package), and the other is that we don't install all the solvers that we build.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2202\n\n",
    "created_at": "2008-02-18T02:05:29Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "title": "[with spkg; needs review] Debianize rubiks spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2202",
    "user": "tabbott"
}
```
Assignee: tabbott

I created a new spkg for rubiks that has a global Makefile, and added Debian build support to it:

http://sage.math.washington.edu/home/tabbott/rubiks-20070912.p2.spkg

The process involved adding distclean targets to the individual Makefiles for the various solvers; for now I made these changes in the spkg because I'm a bad person; but we should submit them upstream for those that we are not the official distribution point for.  I've attached patches for each to this ticket which we can submit to the upstream authors.

There are two things that bug me about this package.  One is that I'm not convinced Debian will want this motley assortment of rubiks cube solvers (so that we might end up leaving it as part of the "sagemath" package), and the other is that we don't install all the solvers that we build.

Issue created by migration from https://trac.sagemath.org/ticket/2202





---

archive/issue_comments_014493.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-18T02:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14493",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_014494.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-18T02:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14494",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_014495.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-18T02:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14495",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_014496.json:
```json
{
    "body": "spkg looks good, nice fixes for the makefile.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T13:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14496",
    "user": "mabshoff"
}
```

spkg looks good, nice fixes for the makefile.

Cheers,

Michael



---

archive/issue_comments_014497.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T13:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14497",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014498.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T13:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14498",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_014499.json:
```json
{
    "body": "The look fine to me.\n\nThe main reason for the rubiks solvers is that David Joyner has a book out on Rubik's cubes, and solving them via the word problem is *extremely* slow.",
    "created_at": "2008-02-18T23:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2202#issuecomment-14499",
    "user": "robertwb"
}
```

The look fine to me.

The main reason for the rubiks solvers is that David Joyner has a book out on Rubik's cubes, and solving them via the word problem is *extremely* slow.
