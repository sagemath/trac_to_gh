# Issue 2613: Moving "all_paths()" to "GenericGraph"

archive/issues_002613.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe class Graph has a method \"all_paths\", but DiGraph don't.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2613\n\n",
    "created_at": "2008-03-20T14:29:48Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Moving \"all_paths()\" to \"GenericGraph\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2613",
    "user": "@m-r-k"
}
```
Assignee: @rlmill

The class Graph has a method "all_paths", but DiGraph don't.

Issue created by migration from https://trac.sagemath.org/ticket/2613





---

archive/issue_comments_017930.json:
```json
{
    "body": "Attachment [all_paths.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths.patch) by @m-r-k created at 2008-03-20 15:06:27",
    "created_at": "2008-03-20T15:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17930",
    "user": "@m-r-k"
}
```

Attachment [all_paths.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths.patch) by @m-r-k created at 2008-03-20 15:06:27



---

archive/issue_comments_017931.json:
```json
{
    "body": "I moved all_paths() and interior_paths() (with modifications) to class GenericGraph",
    "created_at": "2008-03-20T15:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17931",
    "user": "@m-r-k"
}
```

I moved all_paths() and interior_paths() (with modifications) to class GenericGraph



---

archive/issue_comments_017932.json:
```json
{
    "body": "The code looks sensible, but you haven't created any new doctests to demonstrate the case of a DiGraph in either function!",
    "created_at": "2008-03-20T20:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17932",
    "user": "@rlmill"
}
```

The code looks sensible, but you haven't created any new doctests to demonstrate the case of a DiGraph in either function!



---

archive/issue_comments_017933.json:
```json
{
    "body": "Attachment [all_paths_doctests.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths_doctests.patch) by @m-r-k created at 2008-03-21 12:54:10",
    "created_at": "2008-03-21T12:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17933",
    "user": "@m-r-k"
}
```

Attachment [all_paths_doctests.patch](tarball://root/attachments/some-uuid/ticket2613/all_paths_doctests.patch) by @m-r-k created at 2008-03-21 12:54:10



---

archive/issue_comments_017934.json:
```json
{
    "body": "The second patch adds doctests for all_paths() and interior_paths() of DiGraphs.",
    "created_at": "2008-03-21T12:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17934",
    "user": "@m-r-k"
}
```

The second patch adds doctests for all_paths() and interior_paths() of DiGraphs.



---

archive/issue_comments_017935.json:
```json
{
    "body": "Looks good, all tests in `graph.py` pass.",
    "created_at": "2008-03-21T20:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17935",
    "user": "@rlmill"
}
```

Looks good, all tests in `graph.py` pass.



---

archive/issue_comments_017936.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0 - all doctests pass [except know issues]",
    "created_at": "2008-03-22T04:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17936",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0 - all doctests pass [except know issues]



---

archive/issue_comments_017937.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T04:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2613#issuecomment-17937",
    "user": "mabshoff"
}
```

Resolution: fixed
