# Issue 1249: [with patch] fixes bug in graph plotting with partitions

archive/issues_001249.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: graphs\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1249\n\n",
    "created_at": "2007-11-23T18:56:47Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] fixes bug in graph plotting with partitions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1249",
    "user": "@rlmill"
}
```
Assignee: @mwhansen

Keywords: graphs



Issue created by migration from https://trac.sagemath.org/ticket/1249





---

archive/issue_comments_007824.json:
```json
{
    "body": "Attachment [graph_plotting_partitions.patch](tarball://root/attachments/some-uuid/ticket1249/graph_plotting_partitions.patch) by cwitty created at 2007-11-28 02:28:38\n\nLooks good to me: the example in the doctests fails before the patch and succeeds after the patch.  There is one caveat: I think the call to D.show() in the first doctest chunk was supposed to be D.plot().\n\nBut IMHO good enough to apply, anyway.",
    "created_at": "2007-11-28T02:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1249#issuecomment-7824",
    "user": "cwitty"
}
```

Attachment [graph_plotting_partitions.patch](tarball://root/attachments/some-uuid/ticket1249/graph_plotting_partitions.patch) by cwitty created at 2007-11-28 02:28:38

Looks good to me: the example in the doctests fails before the patch and succeeds after the patch.  There is one caveat: I think the call to D.show() in the first doctest chunk was supposed to be D.plot().

But IMHO good enough to apply, anyway.



---

archive/issue_comments_007825.json:
```json
{
    "body": "`<mhansen-962> mabshoff: I think http://trac.sagemath.org/sage_trac/ticket/1249 is okay.`",
    "created_at": "2007-12-01T19:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1249#issuecomment-7825",
    "user": "mabshoff"
}
```

`<mhansen-962> mabshoff: I think http://trac.sagemath.org/sage_trac/ticket/1249 is okay.`



---

archive/issue_comments_007826.json:
```json
{
    "body": "Merged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T19:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1249#issuecomment-7826",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha1.



---

archive/issue_comments_007827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T19:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1249#issuecomment-7827",
    "user": "mabshoff"
}
```

Resolution: fixed
