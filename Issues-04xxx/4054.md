# Issue 4054: [with patch, positive review] shorten doctesting in graph_generators.py

archive/issues_004054.json:
```json
{
    "body": "Assignee: @rlmill\n\nOn my MacBook Pro, before this patch:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph_generators.py    \n [117.4 s]\nsage -t -long devel/sage-main/sage/graphs/graph_generators.py\n [242.7 s]\n```\n\nAnd after this patch:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph_generators.py    \n [20.7 s]\nsage -t -long devel/sage-main/sage/graphs/graph_generators.py\n [109.6 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4054\n\n",
    "closed_at": "2008-09-04T23:22:43Z",
    "created_at": "2008-09-03T22:53:32Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, positive review] shorten doctesting in graph_generators.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4054",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

On my MacBook Pro, before this patch:

```
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
 [117.4 s]
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
 [242.7 s]
```

And after this patch:

```
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
 [20.7 s]
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
 [109.6 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/4054





---

archive/issue_comments_029163.json:
```json
{
    "body": "Changing assignee from tbd to @rlmill.",
    "created_at": "2008-09-03T23:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29163",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from tbd to @rlmill.



---

archive/issue_events_009257.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T00:12:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4054#event-9257"
}
```



---

archive/issue_comments_029164.json:
```json
{
    "body": "Hi,\n\nI would make the \"not tested\" \"long\" since one day we will have a framework that compares expected with actual plotting output. Other than that positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T00:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi,

I would make the "not tested" "long" since one day we will have a framework that compares expected with actual plotting output. Other than that positive review.

Cheers,

Michael



---

archive/issue_comments_029165.json:
```json
{
    "body": "Attachment [trac_4054-long_docs.patch](tarball://root/attachments/some-uuid/ticket4054/trac_4054-long_docs.patch) by @rlmill created at 2008-09-04 22:54:41",
    "created_at": "2008-09-04T22:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29165",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_4054-long_docs.patch](tarball://root/attachments/some-uuid/ticket4054/trac_4054-long_docs.patch) by @rlmill created at 2008-09-04 22:54:41



---

archive/issue_comments_029166.json:
```json
{
    "body": "Positive review now that the \"not tested\" have been converted.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T23:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review now that the "not tested" have been converted.

Cheers,

Michael



---

archive/issue_comments_029167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T23:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029168.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T23:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_events_009258.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T23:22:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4054#event-9258"
}
```
