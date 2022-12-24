# Issue 2797: [with spkg, needs review] fix memleaks in zn_poly

archive/issues_002797.json:
```json
{
    "body": "Assignee: mabshoff\n\nA minor update to the `zn_poly` spkg I posted a few days ago. This fixes some memory leaks in the test suite and a read from uninitialised memory picked up by valgrind, and retrospectively renames the previous release to `zn_poly-0.8.alpha0` :-)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2797\n\n",
    "created_at": "2008-04-04T14:22:29Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with spkg, needs review] fix memleaks in zn_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2797",
    "user": "dmharvey"
}
```
Assignee: mabshoff

A minor update to the `zn_poly` spkg I posted a few days ago. This fixes some memory leaks in the test suite and a read from uninitialised memory picked up by valgrind, and retrospectively renames the previous release to `zn_poly-0.8.alpha0` :-)


Issue created by migration from https://trac.sagemath.org/ticket/2797





---

archive/issue_comments_019209.json:
```json
{
    "body": "Attachment [zn_poly-0.8.p0.spkg](tarball://root/attachments/some-uuid/ticket2797/zn_poly-0.8.p0.spkg) by dmharvey created at 2008-04-04 14:22:58",
    "created_at": "2008-04-04T14:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2797#issuecomment-19209",
    "user": "dmharvey"
}
```

Attachment [zn_poly-0.8.p0.spkg](tarball://root/attachments/some-uuid/ticket2797/zn_poly-0.8.p0.spkg) by dmharvey created at 2008-04-04 14:22:58



---

archive/issue_comments_019210.json:
```json
{
    "body": "There are two issues with this SPKG which I have fixed:\n\n* the changes to SPKG.txt haven't been checked in\n* the spkg named zn_poly-0.8.p0.spkg must unpack to zn_poly-0.8.p0\n\nI have fixed both issues [and some in accuracies in SPKG.txt, i.e. the renaming, in the SPKG I merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T16:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2797#issuecomment-19210",
    "user": "mabshoff"
}
```

There are two issues with this SPKG which I have fixed:

* the changes to SPKG.txt haven't been checked in
* the spkg named zn_poly-0.8.p0.spkg must unpack to zn_poly-0.8.p0

I have fixed both issues [and some in accuracies in SPKG.txt, i.e. the renaming, in the SPKG I merged.

Cheers,

Michael



---

archive/issue_comments_019211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T16:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2797#issuecomment-19211",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019212.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T16:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2797#issuecomment-19212",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1
