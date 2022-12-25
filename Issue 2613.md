# Issue 2613: Moving "all_paths()" to "GenericGraph"

archive/issues_002613.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe class Graph has a method \"all_paths\", but DiGraph don't.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2613\n\n",
    "created_at": "2008-03-20T14:29:48Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Moving \"all_paths()\" to \"GenericGraph\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2613",
    "user": "https://github.com/m-r-k"
}
```
Assignee: @rlmill

The class Graph has a method "all_paths", but DiGraph don't.

Issue created by migration from https://trac.sagemath.org/ticket/2613





---

archive/issue_comments_017892.json:
```json
{
    "body": "Attachment [all_paths.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths.patch) by @m-r-k created at 2008-03-20 15:06:27",
    "created_at": "2008-03-20T15:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17892",
    "user": "https://github.com/m-r-k"
}
```

Attachment [all_paths.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths.patch) by @m-r-k created at 2008-03-20 15:06:27



---

archive/issue_comments_017893.json:
```json
{
    "body": "I moved all_paths() and interior_paths() (with modifications) to class GenericGraph",
    "created_at": "2008-03-20T15:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17893",
    "user": "https://github.com/m-r-k"
}
```

I moved all_paths() and interior_paths() (with modifications) to class GenericGraph



---

archive/issue_comments_017894.json:
```json
{
    "body": "The code looks sensible, but you haven't created any new doctests to demonstrate the case of a DiGraph in either function!",
    "created_at": "2008-03-20T20:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17894",
    "user": "https://github.com/rlmill"
}
```

The code looks sensible, but you haven't created any new doctests to demonstrate the case of a DiGraph in either function!



---

archive/issue_comments_017895.json:
```json
{
    "body": "Attachment [all_paths_doctests.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths_doctests.patch) by @m-r-k created at 2008-03-21 12:54:10",
    "created_at": "2008-03-21T12:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17895",
    "user": "https://github.com/m-r-k"
}
```

Attachment [all_paths_doctests.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths_doctests.patch) by @m-r-k created at 2008-03-21 12:54:10



---

archive/issue_comments_017896.json:
```json
{
    "body": "The second patch adds doctests for all_paths() and interior_paths() of DiGraphs.",
    "created_at": "2008-03-21T12:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17896",
    "user": "https://github.com/m-r-k"
}
```

The second patch adds doctests for all_paths() and interior_paths() of DiGraphs.



---

archive/issue_comments_017897.json:
```json
{
    "body": "Looks good, all tests in `graph.py` pass.",
    "created_at": "2008-03-21T20:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17897",
    "user": "https://github.com/rlmill"
}
```

Looks good, all tests in `graph.py` pass.



---

archive/issue_comments_017898.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0 - all doctests pass [except know issues]",
    "created_at": "2008-03-22T04:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0 - all doctests pass [except know issues]



---

archive/issue_events_002803.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-22T04:02:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2613#event-2803"
}
```



---

archive/issue_comments_017899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T04:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17899",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
