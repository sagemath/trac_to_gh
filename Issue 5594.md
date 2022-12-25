# Issue 5594: better error message for list_plot

archive/issues_005594.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri\n\nWe might consider testing whether the second argument to list_plot (which is \"plotjoined\", should be boolean) is a list or tuple, and then print a warning, because perhaps someone ran \"list_plot([list1], [list2])\" without meaning to.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5594\n\n",
    "created_at": "2009-03-23T21:22:32Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "better error message for list_plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5594",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @jhpalmieri

We might consider testing whether the second argument to list_plot (which is "plotjoined", should be boolean) is a list or tuple, and then print a warning, because perhaps someone ran "list_plot([list1], [list2])" without meaning to.

Issue created by migration from https://trac.sagemath.org/ticket/5594





---

archive/issue_comments_043486.json:
```json
{
    "body": "This patch raises a `TypeError` if plotjoined is a list or a tuple.",
    "created_at": "2009-06-10T22:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5594#issuecomment-43486",
    "user": "https://github.com/jhpalmieri"
}
```

This patch raises a `TypeError` if plotjoined is a list or a tuple.



---

archive/issue_comments_043487.json:
```json
{
    "body": "Attachment [trac_5594.patch](tarball://root/attachments/some-uuid/ticket5594/trac_5594.patch) by @jhpalmieri created at 2009-06-10 22:34:40",
    "created_at": "2009-06-10T22:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5594#issuecomment-43487",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_5594.patch](tarball://root/attachments/some-uuid/ticket5594/trac_5594.patch) by @jhpalmieri created at 2009-06-10 22:34:40



---

archive/issue_comments_043488.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-06-15T19:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5594#issuecomment-43488",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_events_013181.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T10:06:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5594",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5594#event-13181"
}
```



---

archive/issue_comments_043489.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5594#issuecomment-43489",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
