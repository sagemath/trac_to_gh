# Issue 4826: change return type of G.cusps() for G a congruence subgroup

archive/issues_004826.json:
```json
{
    "body": "Assignee: craigcitro\n\nAs pointed out on [this](http://groups.google.com/group/sage-nt/browse_thread/thread/f0a95b54181ba6c5) thread on sage-nt, it might be more reasonable to have `G.cusps()` return a list instead of a set (for `G` a congruence subgroup). In particular, seeing an ordered list as output makes it easier to look through.\n\nThe attached patch changes this return type, as well as making a few small fixes so that this is just as fast as before (or faster, in some cases). \n\nThis patch depends on #4747.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4826\n\n",
    "created_at": "2008-12-18T10:42:22Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "change return type of G.cusps() for G a congruence subgroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4826",
    "user": "craigcitro"
}
```
Assignee: craigcitro

As pointed out on [this](http://groups.google.com/group/sage-nt/browse_thread/thread/f0a95b54181ba6c5) thread on sage-nt, it might be more reasonable to have `G.cusps()` return a list instead of a set (for `G` a congruence subgroup). In particular, seeing an ordered list as output makes it easier to look through.

The attached patch changes this return type, as well as making a few small fixes so that this is just as fast as before (or faster, in some cases). 

This patch depends on #4747.

Issue created by migration from https://trac.sagemath.org/ticket/4826





---

archive/issue_comments_036591.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-18T10:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4826#issuecomment-36591",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036592.json:
```json
{
    "body": "Attachment [trac-4826.patch](tarball://root/attachments/some-uuid/ticket4826/trac-4826.patch) by craigcitro created at 2008-12-18 10:55:54",
    "created_at": "2008-12-18T10:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4826#issuecomment-36592",
    "user": "craigcitro"
}
```

Attachment [trac-4826.patch](tarball://root/attachments/some-uuid/ticket4826/trac-4826.patch) by craigcitro created at 2008-12-18 10:55:54



---

archive/issue_comments_036593.json:
```json
{
    "body": "Patch applied cleanly to 3.2.2.rc1 (after removing the e-acute in Thiery's name in sage/combinat/ranker.py).\n\nAll tests in sage/modular pass, as well as some other testing that I did.\n\nPositive review!",
    "created_at": "2008-12-18T17:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4826#issuecomment-36593",
    "user": "cremona"
}
```

Patch applied cleanly to 3.2.2.rc1 (after removing the e-acute in Thiery's name in sage/combinat/ranker.py).

All tests in sage/modular pass, as well as some other testing that I did.

Positive review!



---

archive/issue_comments_036594.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T11:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4826#issuecomment-36594",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036595.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T11:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4826#issuecomment-36595",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0
