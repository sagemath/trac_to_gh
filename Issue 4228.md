# Issue 4228: eclib-20080310.p6.spkg is broken with 'export MAKE="make -j4"'

archive/issues_004228.json:
```json
{
    "body": "Assignee: mabshoff\n\nJust as the title says. spkg coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4228\n\n",
    "created_at": "2008-10-01T08:54:28Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "eclib-20080310.p6.spkg is broken with 'export MAKE=\"make -j4\"'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4228",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Just as the title says. spkg coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4228





---

archive/issue_comments_030729.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-12T23:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4228#issuecomment-30729",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030730.json:
```json
{
    "body": "The spkg fixes that issue by disabling parallel make for know. In case gmake is used it passes it to the main makefile, so the OpenBSD build still works. The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/rc0/eclib-20080310.p7.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-10-12T23:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4228#issuecomment-30730",
    "user": "mabshoff"
}
```

The spkg fixes that issue by disabling parallel make for know. In case gmake is used it passes it to the main makefile, so the OpenBSD build still works. The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/rc0/eclib-20080310.p7.spkg

Cheers,

Michael



---

archive/issue_comments_030731.json:
```json
{
    "body": "Looks good to me and builds on my box.",
    "created_at": "2008-10-13T00:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4228#issuecomment-30731",
    "user": "mhansen"
}
```

Looks good to me and builds on my box.



---

archive/issue_comments_030732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-13T00:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4228#issuecomment-30732",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030733.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-13T00:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4228#issuecomment-30733",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.rc0
