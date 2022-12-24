# Issue 2368: Compiling Atlas on Powerbook G4, Tuning Information

archive/issues_002368.json:
```json
{
    "body": "Assignee: mabshoff\n\nCompiling Atlas takes forever on Powerbook G4 running debian lenny. Please make the tuning information a part of sage distribution.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2368\n\n",
    "created_at": "2008-03-02T15:49:12Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "Compiling Atlas on Powerbook G4, Tuning Information",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2368",
    "user": "rishi"
}
```
Assignee: mabshoff

Compiling Atlas takes forever on Powerbook G4 running debian lenny. Please make the tuning information a part of sage distribution.

Issue created by migration from https://trac.sagemath.org/ticket/2368





---

archive/issue_comments_015975.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-02T15:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2368#issuecomment-15975",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015976.json:
```json
{
    "body": "I did fix the detection on the last G4 iBook build by Apple. I also created tuning info that will be integrated into the upcoming ATLAS 3.8.1.spkg (see #2269).\n\nThe G4 tuning info can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/ATLAS-tune/PPCG432.tgz\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T23:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2368#issuecomment-15976",
    "user": "mabshoff"
}
```

I did fix the detection on the last G4 iBook build by Apple. I also created tuning info that will be integrated into the upcoming ATLAS 3.8.1.spkg (see #2269).

The G4 tuning info can be found at

http://sage.math.washington.edu/home/mabshoff/ATLAS-tune/PPCG432.tgz

Cheers,

Michael



---

archive/issue_comments_015977.json:
```json
{
    "body": "Attachment [atlas-3.8.1-ppc-g4-7447-detect-fix.patch](tarball://root/attachments/some-uuid/ticket2368/atlas-3.8.1-ppc-g4-7447-detect-fix.patch) by mabshoff created at 2008-03-15 23:28:28\n\nI will also post this patch to the ATLAS tracker to get it merged upstream",
    "created_at": "2008-03-15T23:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2368#issuecomment-15977",
    "user": "mabshoff"
}
```

Attachment [atlas-3.8.1-ppc-g4-7447-detect-fix.patch](tarball://root/attachments/some-uuid/ticket2368/atlas-3.8.1-ppc-g4-7447-detect-fix.patch) by mabshoff created at 2008-03-15 23:28:28

I will also post this patch to the ATLAS tracker to get it merged upstream



---

archive/issue_comments_015978.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T10:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2368#issuecomment-15978",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015979.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0 via #2260.",
    "created_at": "2008-03-20T10:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2368#issuecomment-15979",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0 via #2260.
