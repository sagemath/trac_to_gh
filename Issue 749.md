# Issue 749: graphs: enum() functionality duplicated in relabel()

archive/issues_000749.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\nThe enum() code is duplicated in relabel() for the quick option.  It sure would be nice to factor that out so that the enum() code was all in one place.\n\nIssue created by migration from https://trac.sagemath.org/ticket/749\n\n",
    "created_at": "2007-09-24T22:02:34Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "graphs: enum() functionality duplicated in relabel()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/749",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graphs

The enum() code is duplicated in relabel() for the quick option.  It sure would be nice to factor that out so that the enum() code was all in one place.

Issue created by migration from https://trac.sagemath.org/ticket/749





---

archive/issue_comments_004410.json:
```json
{
    "body": "See ticket #729 for some relevant comments...",
    "created_at": "2007-10-22T16:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4410",
    "user": "https://github.com/rlmill"
}
```

See ticket #729 for some relevant comments...



---

archive/issue_comments_004411.json:
```json
{
    "body": "Or instead, just read them here:\n\n__cmp__ ultimateley ends up using enum() twice, and this is kind of too much, since we could just look at the two graphs from lexicographically most significant, and return the answer as soon as they differ. Also, as Jason points out we should be using __eq__, __neq__, __lt__, __le__, __gt__, __ge__ instead.",
    "created_at": "2007-10-23T17:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4411",
    "user": "https://github.com/rlmill"
}
```

Or instead, just read them here:

__cmp__ ultimateley ends up using enum() twice, and this is kind of too much, since we could just look at the two graphs from lexicographically most significant, and return the answer as soon as they differ. Also, as Jason points out we should be using __eq__, __neq__, __lt__, __le__, __gt__, __ge__ instead.



---

archive/issue_comments_004412.json:
```json
{
    "body": "Note - the quick option in the relabel function was originally an optimization for the graph_isom code, and no longer applies, since it is never used. Other than that purpose, it doesn't make sense to have it as an option, so I'll just remove it.\n\nHere is another aspect:\n\n```\nsage: G._nxg.adj\n{0: {1: [None]}, 1: {0: [None]}}\nsage: H._nxg.adj\n{0: {1: [None, None]}, 1: {0: [None, None]}}\nsage: G == H\nTrue\n```\n",
    "created_at": "2007-10-26T21:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4412",
    "user": "https://github.com/rlmill"
}
```

Note - the quick option in the relabel function was originally an optimization for the graph_isom code, and no longer applies, since it is never used. Other than that purpose, it doesn't make sense to have it as an option, so I'll just remove it.

Here is another aspect:

```
sage: G._nxg.adj
{0: {1: [None]}, 1: {0: [None]}}
sage: H._nxg.adj
{0: {1: [None, None]}, 1: {0: [None, None]}}
sage: G == H
True
```




---

archive/issue_comments_004413.json:
```json
{
    "body": "There is an attached patch that cleans up the whole situation.",
    "created_at": "2007-10-26T23:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4413",
    "user": "https://github.com/rlmill"
}
```

There is an attached patch that cleans up the whole situation.



---

archive/issue_comments_004414.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-26T23:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4414",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004415.json:
```json
{
    "body": "Changing assignee from @williamstein to @rlmill.",
    "created_at": "2007-10-26T23:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4415",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @williamstein to @rlmill.



---

archive/issue_comments_004416.json:
```json
{
    "body": "Attachment [trac749_1.patch](tarball://root/attachments/some-uuid/ticket749/trac749_1.patch) by @rlmill created at 2007-10-27 00:02:02\n\nThis one first, removed quick option from relabel().",
    "created_at": "2007-10-27T00:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4416",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac749_1.patch](tarball://root/attachments/some-uuid/ticket749/trac749_1.patch) by @rlmill created at 2007-10-27 00:02:02

This one first, removed quick option from relabel().



---

archive/issue_comments_004417.json:
```json
{
    "body": "This is the main overhaul.",
    "created_at": "2007-10-27T00:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4417",
    "user": "https://github.com/rlmill"
}
```

This is the main overhaul.



---

archive/issue_comments_004418.json:
```json
{
    "body": "Attachment [trac749_2.patch](tarball://root/attachments/some-uuid/ticket749/trac749_2.patch) by @rlmill created at 2007-10-27 00:14:07",
    "created_at": "2007-10-27T00:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4418",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac749_2.patch](tarball://root/attachments/some-uuid/ticket749/trac749_2.patch) by @rlmill created at 2007-10-27 00:14:07



---

archive/issue_comments_004419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T04:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/749#issuecomment-4419",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_events_000842.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-27T04:52:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/749",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/749#event-842"
}
```
