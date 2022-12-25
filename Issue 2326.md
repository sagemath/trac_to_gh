# Issue 2326: compiled sparse and dense graph datastructures

archive/issues_002326.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout\n\nImplement compiled base classes for graphs, which will be faster than Python based NetworkX classes (especially when accessed from Cython).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2326\n\n",
    "created_at": "2008-02-27T00:00:40Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "compiled sparse and dense graph datastructures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2326",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  @jasongrout

Implement compiled base classes for graphs, which will be faster than Python based NetworkX classes (especially when accessed from Cython).

Issue created by migration from https://trac.sagemath.org/ticket/2326





---

archive/issue_comments_015447.json:
```json
{
    "body": "The patches on this ticket will depend on those in #2307.",
    "created_at": "2008-02-27T00:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15447",
    "user": "https://github.com/rlmill"
}
```

The patches on this ticket will depend on those in #2307.



---

archive/issue_comments_015448.json:
```json
{
    "body": "Don't know what's up with the HTML preview on the second patch, but...",
    "created_at": "2008-02-27T01:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15448",
    "user": "https://github.com/rlmill"
}
```

Don't know what's up with the HTML preview on the second patch, but...



---

archive/issue_comments_015449.json:
```json
{
    "body": "For the results of `sage -t -valgrind` on the new code, see\n\nsparse_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.12219\n\ndense_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.18970\n\nThey certainly look clean to me :)",
    "created_at": "2008-02-28T19:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15449",
    "user": "https://github.com/rlmill"
}
```

For the results of `sage -t -valgrind` on the new code, see

sparse_graph:

http://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.12219

dense_graph:

http://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.18970

They certainly look clean to me :)



---

archive/issue_comments_015450.json:
```json
{
    "body": "Alternatively,\n\nsparse_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/sage-memcheck.12219\n\ndense_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/sage-memcheck.18970",
    "created_at": "2008-02-28T20:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15450",
    "user": "https://github.com/rlmill"
}
```

Alternatively,

sparse_graph:

http://sage.math.washington.edu/home/rlmill/sage-memcheck.12219

dense_graph:

http://sage.math.washington.edu/home/rlmill/sage-memcheck.18970



---

archive/issue_comments_015451.json:
```json
{
    "body": "Attachment [2326-final.patch](tarball://root/attachments/some-uuid/ticket2326/2326-final.patch) by @jasongrout created at 2008-03-01 10:24:41\n\nSorry for the caps, but I just wanted to make sure mabshoff saw it :)  It looks good to me.",
    "created_at": "2008-03-01T10:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15451",
    "user": "https://github.com/jasongrout"
}
```

Attachment [2326-final.patch](tarball://root/attachments/some-uuid/ticket2326/2326-final.patch) by @jasongrout created at 2008-03-01 10:24:41

Sorry for the caps, but I just wanted to make sure mabshoff saw it :)  It looks good to me.



---

archive/issue_comments_015452.json:
```json
{
    "body": "Merged 2326-final.patch in Sage 2.10.3.rc1",
    "created_at": "2008-03-01T23:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15452",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2326-final.patch in Sage 2.10.3.rc1



---

archive/issue_events_002504.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-01T23:55:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2326#event-2504"
}
```



---

archive/issue_comments_015453.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-01T23:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
