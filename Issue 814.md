# Issue 814: bug in number field printing

archive/issues_000814.json:
```json
{
    "body": "Assignee: was\n\nNotice the following printing bug with `NumberField`:\n\n\n```\n\nsage: K .<a,b>= NumberField([x^3-2,x^2+1])\nsage: K\nNumber Field in a with defining polynomial x^3 + -2 over its base field\n\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/814\n\n",
    "created_at": "2007-10-03T19:36:43Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "bug in number field printing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/814",
    "user": "craigcitro"
}
```
Assignee: was

Notice the following printing bug with `NumberField`:


```

sage: K .<a,b>= NumberField([x^3-2,x^2+1])
sage: K
Number Field in a with defining polynomial x^3 + -2 over its base field

```




Issue created by migration from https://trac.sagemath.org/ticket/814





---

archive/issue_comments_005061.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-10-04T18:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5061",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_005062.json:
```json
{
    "body": "NOt a bug.  Changing the + -2 to + 2 would be a nice enhancement.  The issue would be making\npoly's over number fields print even more nicely.",
    "created_at": "2007-10-04T18:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5062",
    "user": "was"
}
```

NOt a bug.  Changing the + -2 to + 2 would be a nice enhancement.  The issue would be making
poly's over number fields print even more nicely.



---

archive/issue_comments_005063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5063",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_005064.json:
```json
{
    "body": "Fixed by making the + - to - substitution more generally, since there are parenthesis.",
    "created_at": "2007-10-19T01:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5064",
    "user": "was"
}
```

Fixed by making the + - to - substitution more generally, since there are parenthesis.
