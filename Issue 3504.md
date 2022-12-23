# Issue 3504: sage sometimes leaves matlab processes that eat 100% cpu time

archive/issues_003504.json:
```json
{
    "body": "Assignee: was\n\nI've found a way to somewhat reproducibly leave a matlab process eating 100% cpu time.\n\nI log on to sage.math, start Sage, and run the following commands:\n\n```\nsage: m = matlab(matrix(RR, [[1]]))\nsage: m.det()\n```\n\nThen I kill my local ssh client with \"kill -9\" (to make a non-clean ssh shutdown).\n\nOften (not always, but I think more than half the time) this leaves a matlab process eating 100% of the cpu time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3504\n\n",
    "created_at": "2008-06-24T20:47:54Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "sage sometimes leaves matlab processes that eat 100% cpu time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3504",
    "user": "cwitty"
}
```
Assignee: was

I've found a way to somewhat reproducibly leave a matlab process eating 100% cpu time.

I log on to sage.math, start Sage, and run the following commands:

```
sage: m = matlab(matrix(RR, [[1]]))
sage: m.det()
```

Then I kill my local ssh client with "kill -9" (to make a non-clean ssh shutdown).

Often (not always, but I think more than half the time) this leaves a matlab process eating 100% of the cpu time.

Issue created by migration from https://trac.sagemath.org/ticket/3504





---

archive/issue_comments_024714.json:
```json
{
    "body": "Changing component from interfaces to interfaces: optional.",
    "created_at": "2015-06-23T13:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3504#issuecomment-24714",
    "user": "jdemeyer"
}
```

Changing component from interfaces to interfaces: optional.
