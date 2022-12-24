# Issue 2811: make check is broken due to #2746

archive/issues_002811.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nSAGE build/upgrade complete!\n. local/bin/sage-env && sage-maketest\n/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 3: [: argument expected\nmkdir: `': No such file or directory\n/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 11: /test.log: Permission denied\n/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 12: /test.log: Permission denied\ntee: /test.log: Permission denied\nTesting of examples currently not implemented.\nTesting SAGE documentation\nTesting SAGE tutorial\ntee: /test.log: Permission denied\nsage -t  devel/doc/tut/tut.tex                              Testing SAGE programming guide\ntee: /test.log: Permission denied\nsage -t  devel/doc/prog/prog.tex\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2811\n\n",
    "created_at": "2008-04-05T18:10:14Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "make check is broken due to #2746",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2811",
    "user": "mabshoff"
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

archive/issue_comments_019294.json:
```json
{
    "body": "Attachment [trac_2811.patch](tarball://root/attachments/some-uuid/ticket2811/trac_2811.patch) by mabshoff created at 2008-04-07 01:27:03",
    "created_at": "2008-04-07T01:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19294",
    "user": "mabshoff"
}
```

Attachment [trac_2811.patch](tarball://root/attachments/some-uuid/ticket2811/trac_2811.patch) by mabshoff created at 2008-04-07 01:27:03



---

archive/issue_comments_019295.json:
```json
{
    "body": "This patch needs some additional fixes to the main makefile which are not up here since the file isn't under revision control.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T01:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19295",
    "user": "mabshoff"
}
```

This patch needs some additional fixes to the main makefile which are not up here since the file isn't under revision control.

Cheers,

Michael



---

archive/issue_comments_019296.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-07T01:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19296",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019297.json:
```json
{
    "body": "Good",
    "created_at": "2008-04-07T01:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19297",
    "user": "@garyfurnish"
}
```

Good



---

archive/issue_comments_019298.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19298",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019299.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2811#issuecomment-19299",
    "user": "mabshoff"
}
```

Resolution: fixed
