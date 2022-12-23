# Issue 2954: [with spkg. needs review] ATLAS 3.8.1: Fix Itanium 2 detection on Itanium/gcc compiler flags on RHEL5/Itanium

archive/issues_002954.json:
```json
{
    "body": "Assignee: mabshoff\n\nItanium 2 on RHEL 5 and pretty much any other modern kernel is not properly detected. ATLAS also uses the -m64 flags which is not available on RHEL 5 on Itanium. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/atlas-3.8.1.p0.spkg\n\nfixes both issues.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2954\n\n",
    "created_at": "2008-04-19T04:00:01Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "[with spkg. needs review] ATLAS 3.8.1: Fix Itanium 2 detection on Itanium/gcc compiler flags on RHEL5/Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2954",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Itanium 2 on RHEL 5 and pretty much any other modern kernel is not properly detected. ATLAS also uses the -m64 flags which is not available on RHEL 5 on Itanium. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/atlas-3.8.1.p0.spkg

fixes both issues.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2954





---

archive/issue_comments_020370.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T04:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20370",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020371.json:
```json
{
    "body": "REPORT:\n\n Well I give #2954 a positive review if it builds and works for you.\nI've read the patches.",
    "created_at": "2008-04-19T05:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20371",
    "user": "was"
}
```

REPORT:

 Well I give #2954 a positive review if it builds and works for you.
I've read the patches.



---

archive/issue_comments_020372.json:
```json
{
    "body": "Build time on Itanium is quite bad, especially compared to x86-64, but I guess that it is partially the fault of gcc 4.1.1 I used.\n\nOh well,\n\nMichael",
    "created_at": "2008-04-19T06:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20372",
    "user": "mabshoff"
}
```

Build time on Itanium is quite bad, especially compared to x86-64, but I guess that it is partially the fault of gcc 4.1.1 I used.

Oh well,

Michael



---

archive/issue_comments_020373.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-19T06:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20373",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_020374.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-19T06:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2954#issuecomment-20374",
    "user": "mabshoff"
}
```

Resolution: fixed
