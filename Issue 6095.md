# Issue 6095: implement sloane sequence: A060302 (digits of (pi^4+pi^5))^(1/6)

archive/issues_006095.json:
```json
{
    "body": "Assignee: mhansen\n\ninteresting because almost digits of e.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6095\n\n",
    "created_at": "2009-05-20T21:20:44Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "implement sloane sequence: A060302 (digits of (pi^4+pi^5))^(1/6)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6095",
    "user": "was"
}
```
Assignee: mhansen

interesting because almost digits of e.

Issue created by migration from https://trac.sagemath.org/ticket/6095





---

archive/issue_comments_048599.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-20T21:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6095#issuecomment-48599",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_048600.json:
```json
{
    "body": "The code looks good, but is this useful enough to have in Sage?",
    "created_at": "2009-05-20T21:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6095#issuecomment-48600",
    "user": "robertwb"
}
```

The code looks good, but is this useful enough to have in Sage?



---

archive/issue_comments_048601.json:
```json
{
    "body": "cwitty and robertwb pointed out a BUG.  If there is a sequence of more than ten 9's in a row, then this code can give a wrong answer.   One has to specifically deal with the case of 9's and use that the number is transcendental.",
    "created_at": "2009-05-21T06:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6095#issuecomment-48601",
    "user": "was"
}
```

cwitty and robertwb pointed out a BUG.  If there is a sequence of more than ten 9's in a row, then this code can give a wrong answer.   One has to specifically deal with the case of 9's and use that the number is transcendental.
