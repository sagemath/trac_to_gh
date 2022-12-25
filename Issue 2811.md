# Issue 2811: make check is broken due to #2746

archive/issues_002811.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nSAGE build/upgrade complete!\n. local/bin/sage-env && sage-maketest\n/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 3: [: argument expected\nmkdir: `': No such file or directory\n/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 11: /test.log: Permission denied\n/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 12: /test.log: Permission denied\ntee: /test.log: Permission denied\nTesting of examples currently not implemented.\nTesting SAGE documentation\nTesting SAGE tutorial\ntee: /test.log: Permission denied\nsage -t  devel/doc/tut/tut.tex                              Testing SAGE programming guide\ntee: /test.log: Permission denied\nsage -t  devel/doc/prog/prog.tex\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2811\n\n",
    "created_at": "2008-04-05T18:10:14Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "make check is broken due to #2746",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
SAGE build/upgrade complete!
. local/bin/sage-env && sage-maketest
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 3: [: argument expected
mkdir: `': No such file or directory
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 11: /test.log: Permission denied
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 12: /test.log: Permission denied
tee: /test.log: Permission denied
Testing of examples currently not implemented.
Testing SAGE documentation
Testing SAGE tutorial
tee: /test.log: Permission denied
sage -t  devel/doc/tut/tut.tex                              Testing SAGE programming guide
tee: /test.log: Permission denied
sage -t  devel/doc/prog/prog.tex
```


Issue created by migration from https://trac.sagemath.org/ticket/2811





---

archive/issue_comments_019253.json:
```json
{
    "body": "Attachment [trac_2811.patch](tarball://root/attachments/some-uuid/ticket2811/trac_2811.patch) by mabshoff created at 2008-04-07 01:27:03",
    "created_at": "2008-04-07T01:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2811.patch](tarball://root/attachments/some-uuid/ticket2811/trac_2811.patch) by mabshoff created at 2008-04-07 01:27:03



---

archive/issue_comments_019254.json:
```json
{
    "body": "This patch needs some additional fixes to the main makefile which are not up here since the file isn't under revision control.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T01:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch needs some additional fixes to the main makefile which are not up here since the file isn't under revision control.

Cheers,

Michael



---

archive/issue_comments_019255.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-07T01:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019256.json:
```json
{
    "body": "Good",
    "created_at": "2008-04-07T01:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19256",
    "user": "https://github.com/garyfurnish"
}
```

Good



---

archive/issue_comments_019257.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019258.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19258",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006470.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T01:33:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2811#event-6470"
}
```
