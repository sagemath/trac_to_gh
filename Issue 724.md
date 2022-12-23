# Issue 724: graph6 parsing does not throw an error when the string is the wrong size.

archive/issues_000724.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graph6, graph\n\nMaking a graph from a graph6 string should check to make sure the string is the right size and throw an error if the string is too long or too short.  I believe now it just silently hands back a graph that is not correct.\n\nThis is bad, especially when your string has an escaped character and you didn't realize it :).\n\nIssue created by migration from https://trac.sagemath.org/ticket/724\n\n",
    "created_at": "2007-09-21T00:40:12Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "graph6 parsing does not throw an error when the string is the wrong size.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/724",
    "user": "jason"
}
```
Assignee: was

Keywords: graph6, graph

Making a graph from a graph6 string should check to make sure the string is the right size and throw an error if the string is too long or too short.  I believe now it just silently hands back a graph that is not correct.

This is bad, especially when your string has an escaped character and you didn't realize it :).

Issue created by migration from https://trac.sagemath.org/ticket/724





---

archive/issue_comments_004220.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4220",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004221.json:
```json
{
    "body": "Changing assignee from was to rlm.",
    "created_at": "2007-10-24T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4221",
    "user": "rlm"
}
```

Changing assignee from was to rlm.



---

archive/issue_comments_004222.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-24T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4222",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_004223.json:
```json
{
    "body": "This patches cleanly onto 2.8.9.",
    "created_at": "2007-10-25T18:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4223",
    "user": "rlm"
}
```

This patches cleanly onto 2.8.9.



---

archive/issue_comments_004224.json:
```json
{
    "body": "Please add doctests to show the new exceptions.  (Every bug fix should have a doctest.)\n\nThanks!",
    "created_at": "2007-10-26T06:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4224",
    "user": "cwitty"
}
```

Please add doctests to show the new exceptions.  (Every bug fix should have a doctest.)

Thanks!



---

archive/issue_comments_004225.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-27T04:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4225",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_004226.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T04:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4226",
    "user": "cwitty"
}
```

Resolution: fixed
