# Issue 5802: use tuples rather than copying lists for immutable data

archive/issues_005802.json:
```json
{
    "body": "Assignee: cwitty\n\nAn example came up at #5756 where one returns the list `__im_gens` but for fear that it be mutated, a copy is created. I've seen this same thing elsewhere in the library. It would be better to just return a tuple. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5802\n\n",
    "created_at": "2009-04-16T07:21:10Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "use tuples rather than copying lists for immutable data",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5802",
    "user": "@robertwb"
}
```
Assignee: cwitty

An example came up at #5756 where one returns the list `__im_gens` but for fear that it be mutated, a copy is created. I've seen this same thing elsewhere in the library. It would be better to just return a tuple. 

Issue created by migration from https://trac.sagemath.org/ticket/5802





---

archive/issue_comments_045548.json:
```json
{
    "body": "A similar issue arose at #20743.",
    "created_at": "2016-08-17T00:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5802",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5802#issuecomment-45548",
    "user": "@kedlaya"
}
```

A similar issue arose at #20743.
