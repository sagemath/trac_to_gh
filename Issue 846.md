# Issue 846: Split cdefs.pxi

archive/issues_000846.json:
```json
{
    "body": "Assignee: was\n\nCC:  craigcitro\n\nThis should probably go into several different files. At least the gmp stuff could be moved to a different file (perhaps the current gmp.pxi should be renamed?) \n\nIssue created by migration from https://trac.sagemath.org/ticket/846\n\n",
    "created_at": "2007-10-10T10:53:06Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "title": "Split cdefs.pxi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/846",
    "user": "robertwb"
}
```
Assignee: was

CC:  craigcitro

This should probably go into several different files. At least the gmp stuff could be moved to a different file (perhaps the current gmp.pxi should be renamed?) 

Issue created by migration from https://trac.sagemath.org/ticket/846





---

archive/issue_comments_005229.json:
```json
{
    "body": "This should be more relevant now that .pxd files are more flexible. cdefs.pxi is sometimes reparsed 5-10 times.",
    "created_at": "2008-10-15T21:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5229",
    "user": "robertwb"
}
```

This should be more relevant now that .pxd files are more flexible. cdefs.pxi is sometimes reparsed 5-10 times.



---

archive/issue_comments_005230.json:
```json
{
    "body": "Don't forget to put mpz_set_longlong in stdsage.",
    "created_at": "2008-11-20T23:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5230",
    "user": "robertwb"
}
```

Don't forget to put mpz_set_longlong in stdsage.



---

archive/issue_comments_005231.json:
```json
{
    "body": "Attachment [846-move-gmp.patch](tarball://root/attachments/some-uuid/ticket846/846-move-gmp.patch) by robertwb created at 2008-11-22 00:40:59\n\nAlso, this now has the complete list of gmp functions found in the manual.",
    "created_at": "2008-11-22T00:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5231",
    "user": "robertwb"
}
```

Attachment [846-move-gmp.patch](tarball://root/attachments/some-uuid/ticket846/846-move-gmp.patch) by robertwb created at 2008-11-22 00:40:59

Also, this now has the complete list of gmp functions found in the manual.



---

archive/issue_comments_005232.json:
```json
{
    "body": "See also #4579 about mpz_set_longlong",
    "created_at": "2008-11-22T00:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5232",
    "user": "robertwb"
}
```

See also #4579 about mpz_set_longlong



---

archive/issue_comments_005233.json:
```json
{
    "body": "See also #4580",
    "created_at": "2008-11-22T01:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5233",
    "user": "robertwb"
}
```

See also #4580



---

archive/issue_comments_005234.json:
```json
{
    "body": "Attachment [846-move-gmp-reviewer.patch](tarball://root/attachments/some-uuid/ticket846/846-move-gmp-reviewer.patch) by cwitty created at 2008-11-23 03:23:51\n\nVery nice!  My patch fixes a couple of compile errors; with my patch, all doctests pass.\n\nPositive review.  Apply both patches.",
    "created_at": "2008-11-23T03:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5234",
    "user": "cwitty"
}
```

Attachment [846-move-gmp-reviewer.patch](tarball://root/attachments/some-uuid/ticket846/846-move-gmp-reviewer.patch) by cwitty created at 2008-11-23 03:23:51

Very nice!  My patch fixes a couple of compile errors; with my patch, all doctests pass.

Positive review.  Apply both patches.



---

archive/issue_comments_005235.json:
```json
{
    "body": "\n```\n[7:40pm] cwitty: Argh... and #4564 conflicts with 846-more-gmp-reviewer.patch (I was wondering why the original patch didn't even compile...)\n[7:41pm] mabshoff: mmmh\n[7:41pm] mabshoff: So I don't need the reviewer patch I assume.\n[7:41pm] cwitty: You need the half of it that creates an __init__.py file; probably not the half that patches integer.pyx .\n[7:44pm] mabshoff: mk\n[7:45pm] mabshoff: I assume that is lost in RobertWB's patch since hg screws up the empty file creation as usual.\n[7:45pm] mabshoff: I will copy and paste the last couple lines to the ticket and then merge it.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T03:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5235",
    "user": "mabshoff"
}
```


```
[7:40pm] cwitty: Argh... and #4564 conflicts with 846-more-gmp-reviewer.patch (I was wondering why the original patch didn't even compile...)
[7:41pm] mabshoff: mmmh
[7:41pm] mabshoff: So I don't need the reviewer patch I assume.
[7:41pm] cwitty: You need the half of it that creates an __init__.py file; probably not the half that patches integer.pyx .
[7:44pm] mabshoff: mk
[7:45pm] mabshoff: I assume that is lost in RobertWB's patch since hg screws up the empty file creation as usual.
[7:45pm] mabshoff: I will copy and paste the last couple lines to the ticket and then merge it.
```


Cheers,

Michael



---

archive/issue_comments_005236.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T06:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5236",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005237.json:
```json
{
    "body": "Merged both patches (the reviewer patch was limited to the first hunk) in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T06:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/846#issuecomment-5237",
    "user": "mabshoff"
}
```

Merged both patches (the reviewer patch was limited to the first hunk) in Sage 3.2.1.alpha0
