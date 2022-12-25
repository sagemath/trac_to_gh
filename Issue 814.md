# Issue 814: bug in number field printing

archive/issues_000814.json:
```json
{
    "body": "Assignee: @williamstein\n\nNotice the following printing bug with `NumberField`:\n\n\n```\n\nsage: K .<a,b>= NumberField([x^3-2,x^2+1])\nsage: K\nNumber Field in a with defining polynomial x^3 + -2 over its base field\n\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/814\n\n",
    "created_at": "2007-10-03T19:36:43Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "bug in number field printing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/814",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @williamstein

Notice the following printing bug with `NumberField`:


```

sage: K .<a,b>= NumberField([x^3-2,x^2+1])
sage: K
Number Field in a with defining polynomial x^3 + -2 over its base field

```




Issue created by migration from https://trac.sagemath.org/ticket/814





---

archive/issue_comments_005045.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-10-04T18:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5045",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_005046.json:
```json
{
    "body": "NOt a bug.  Changing the + -2 to + 2 would be a nice enhancement.  The issue would be making\npoly's over number fields print even more nicely.",
    "created_at": "2007-10-04T18:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5046",
    "user": "https://github.com/williamstein"
}
```

NOt a bug.  Changing the + -2 to + 2 would be a nice enhancement.  The issue would be making
poly's over number fields print even more nicely.



---

archive/issue_comments_005047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5047",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_005048.json:
```json
{
    "body": "Fixed by making the + - to - substitution more generally, since there are parenthesis.",
    "created_at": "2007-10-19T01:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/814#issuecomment-5048",
    "user": "https://github.com/williamstein"
}
```

Fixed by making the + - to - substitution more generally, since there are parenthesis.
