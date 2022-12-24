# Issue 4086: [with spkg, needs review] Fix polybori-0.5rc.p3.spkg build issue from vanilla tarball

archive/issues_004086.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn spkg-install we touch pbori.pyx to force a rebuild. But when building from a vanilla tarball that file does not exist and spkg-install exists with a non-zero status and fails. The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/polybori-0.5rc.p4.spkg\n\nfixes the issue.\n\nBuild tested on x86, x86-64 and Itanium Linux as well as OSX.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4086\n\n",
    "created_at": "2008-09-09T10:18:04Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] Fix polybori-0.5rc.p3.spkg build issue from vanilla tarball",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4086",
    "user": "mabshoff"
}
```
Assignee: mabshoff

In spkg-install we touch pbori.pyx to force a rebuild. But when building from a vanilla tarball that file does not exist and spkg-install exists with a non-zero status and fails. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/polybori-0.5rc.p4.spkg

fixes the issue.

Build tested on x86, x86-64 and Itanium Linux as well as OSX.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4086





---

archive/issue_comments_029480.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-09T10:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4086#issuecomment-29480",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029481.json:
```json
{
    "body": "New spkg at:\n\n  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.5rc.p4.spkg\n\nwhich replaces the `test -a` with `test -f` since that seems to be the safe choice. I only checked the SPKG by reading the changes, I didn't test it on a bunch of platforms yet.",
    "created_at": "2008-09-09T10:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4086#issuecomment-29481",
    "user": "malb"
}
```

New spkg at:

  http://sage.math.washington.edu/home/malb/spkgs/polybori-0.5rc.p4.spkg

which replaces the `test -a` with `test -f` since that seems to be the safe choice. I only checked the SPKG by reading the changes, I didn't test it on a bunch of platforms yet.



---

archive/issue_comments_029482.json:
```json
{
    "body": "Spkg looks good to me. I will post a followup polybori-0.5rc.p5.spkg with the OSX 10.4 fix at #4090.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-10T02:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4086#issuecomment-29482",
    "user": "mabshoff"
}
```

Spkg looks good to me. I will post a followup polybori-0.5rc.p5.spkg with the OSX 10.4 fix at #4090.

Cheers,

Michael



---

archive/issue_comments_029483.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-10T02:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4086#issuecomment-29483",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc2



---

archive/issue_comments_029484.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-10T02:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4086#issuecomment-29484",
    "user": "mabshoff"
}
```

Resolution: fixed
