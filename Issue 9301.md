# Issue 9301: Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents

archive/issues_009301.json:
```json
{
    "body": "Assignee: jason, mvngu, ncohen, rlm\n\nCC:  nathann.cohen@gmail.com\n\nKeywords: graph,label\n\nModified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents. Discussion and example here: http://groups.google.com/group/sage-devel/browse_thread/thread/310fba4f1c119e63#\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9301\n\n",
    "created_at": "2010-06-21T23:11:15Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9301",
    "user": "https://trac.sagemath.org/admin/accounts/users/comick"
}
```
Assignee: jason, mvngu, ncohen, rlm

CC:  nathann.cohen@gmail.com

Keywords: graph,label

Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents. Discussion and example here: http://groups.google.com/group/sage-devel/browse_thread/thread/310fba4f1c119e63#


Issue created by migration from https://trac.sagemath.org/ticket/9301





---

archive/issue_comments_087471.json:
```json
{
    "body": "Attachment [14371.patch](tarball://root/attachments/some-uuid/ticket9301/14371.patch) by comick created at 2010-06-21 23:11:51\n\nPatch",
    "created_at": "2010-06-21T23:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87471",
    "user": "https://trac.sagemath.org/admin/accounts/users/comick"
}
```

Attachment [14371.patch](tarball://root/attachments/some-uuid/ticket9301/14371.patch) by comick created at 2010-06-21 23:11:51

Patch



---

archive/issue_comments_087472.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-21T23:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87472",
    "user": "https://trac.sagemath.org/admin/accounts/users/comick"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087473.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-17T14:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87473",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087474.json:
```json
{
    "body": "Since this is a bug fix, you need to include a doctest which illustrates the bug you are fixing.",
    "created_at": "2010-07-17T14:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87474",
    "user": "https://github.com/rlmill"
}
```

Since this is a bug fix, you need to include a doctest which illustrates the bug you are fixing.



---

archive/issue_comments_087475.json:
```json
{
    "body": "Doctest for bad behavior.",
    "created_at": "2010-08-21T22:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87475",
    "user": "https://trac.sagemath.org/admin/accounts/users/comick"
}
```

Doctest for bad behavior.



---

archive/issue_comments_087476.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-21T23:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87476",
    "user": "https://trac.sagemath.org/admin/accounts/users/comick"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087477.json:
```json
{
    "body": "Attachment [doctest.py](tarball://root/attachments/some-uuid/ticket9301/doctest.py) by comick created at 2010-08-21 23:00:51",
    "created_at": "2010-08-21T23:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87477",
    "user": "https://trac.sagemath.org/admin/accounts/users/comick"
}
```

Attachment [doctest.py](tarball://root/attachments/some-uuid/ticket9301/doctest.py) by comick created at 2010-08-21 23:00:51



---

archive/issue_comments_087478.json:
```json
{
    "body": "Attachment [trac_9301-part1.patch](tarball://root/attachments/some-uuid/ticket9301/trac_9301-part1.patch) by @rlmill created at 2010-08-31 17:16:46\n\nReplaces previous patch - added trac # to commit message.",
    "created_at": "2010-08-31T17:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87478",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9301-part1.patch](tarball://root/attachments/some-uuid/ticket9301/trac_9301-part1.patch) by @rlmill created at 2010-08-31 17:16:46

Replaces previous patch - added trac # to commit message.



---

archive/issue_comments_087479.json:
```json
{
    "body": "There is a fly in the ointment:\n\nDuring one of the last NetworkX upgrades, many common Sage graph constructors were modified to give empty dictionaries as labels instead of None. I have been intending to fix many of Sage's graph generators not to depend on NetworkX (since simply constructing a CGraph would be much quicker), and revert the edge situation back to having labels equal to `None`. But until that happens, this patch causes several failures:\n\n```\nsage -t -long \"devel/sage-main/sage/graphs/generic_graph.py\"\nsage -t -long \"devel/sage-main/sage/graphs/base/sparse_graph.pyx\"\nsage -t -long \"devel/sage-main/sage/graphs/graph.py\"\n```\n\nAlso, I've changed the \"Report Upstream\" since here we *are* the upstream.",
    "created_at": "2010-08-31T17:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87479",
    "user": "https://github.com/rlmill"
}
```

There is a fly in the ointment:

During one of the last NetworkX upgrades, many common Sage graph constructors were modified to give empty dictionaries as labels instead of None. I have been intending to fix many of Sage's graph generators not to depend on NetworkX (since simply constructing a CGraph would be much quicker), and revert the edge situation back to having labels equal to `None`. But until that happens, this patch causes several failures:

```
sage -t -long "devel/sage-main/sage/graphs/generic_graph.py"
sage -t -long "devel/sage-main/sage/graphs/base/sparse_graph.pyx"
sage -t -long "devel/sage-main/sage/graphs/graph.py"
```

Also, I've changed the "Report Upstream" since here we *are* the upstream.



---

archive/issue_comments_087480.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-31T17:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87480",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_022923.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22923"
}
```



---

archive/issue_events_022924.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22924"
}
```



---

archive/issue_events_022925.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22925"
}
```



---

archive/issue_events_022926.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22926"
}
```



---

archive/issue_events_022927.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22927"
}
```



---

archive/issue_events_022928.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22928"
}
```



---

archive/issue_events_022929.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22929"
}
```



---

archive/issue_comments_087481.json:
```json
{
    "body": "It seems that this issue has been fixed long time ago. So I propose to close this ticket.",
    "created_at": "2021-10-19T12:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87481",
    "user": "https://github.com/dcoudert"
}
```

It seems that this issue has been fixed long time ago. So I propose to close this ticket.



---

archive/issue_comments_087482.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2021-10-19T12:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87482",
    "user": "https://github.com/dcoudert"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_022930.json:
```json
{
    "actor": "https://github.com/dcoudert",
    "created_at": "2021-10-19T12:55:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22930"
}
```



---

archive/issue_events_022931.json:
```json
{
    "actor": "https://github.com/dcoudert",
    "created_at": "2021-10-19T12:55:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22931"
}
```



---

archive/issue_comments_087483.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-25T15:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87483",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_022932.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-25T15:39:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9301#event-22932"
}
```
