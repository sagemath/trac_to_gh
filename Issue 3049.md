# Issue 3049: combinatorics -- lame overflow with Compositions(n).count() (very easy to fix)

archive/issues_003049.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nThe following calculation is trivial, so shouldn't overflow:\n\n```\nsage: len(Compositions(30))\n536870912\nsage: len(Compositions(40))\nTraceback (most recent call last):\n...\nOverflowError: long int too large to convert to int\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3049\n\n",
    "created_at": "2008-04-28T15:24:02Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "combinatorics -- lame overflow with Compositions(n).count() (very easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3049",
    "user": "was"
}
```
Assignee: mhansen

CC:  sage-combinat

The following calculation is trivial, so shouldn't overflow:

```
sage: len(Compositions(30))
536870912
sage: len(Compositions(40))
Traceback (most recent call last):
...
OverflowError: long int too large to convert to int
```


Issue created by migration from https://trac.sagemath.org/ticket/3049





---

archive/issue_comments_021002.json:
```json
{
    "body": "This is also",
    "created_at": "2008-04-28T15:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3049#issuecomment-21002",
    "user": "was"
}
```

This is also



---

archive/issue_comments_021003.json:
```json
{
    "body": "This is caused by a stupid limitation in Python's len.  Use .count, etc. instead.",
    "created_at": "2008-04-28T19:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3049#issuecomment-21003",
    "user": "was"
}
```

This is caused by a stupid limitation in Python's len.  Use .count, etc. instead.



---

archive/issue_comments_021004.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-04-28T19:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3049#issuecomment-21004",
    "user": "was"
}
```

Resolution: invalid
