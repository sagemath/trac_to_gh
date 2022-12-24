# Issue 9339: Notebook fails to print result of last expression if there is a line break

archive/issues_009339.json:
```json
{
    "body": "Assignee: jason, was\n\nConsider the following two notebook cells. Semantically, the input is the same in both examples. The only difference is that the second one has a line break inside a bracket.\n\nFirst one prints the result of the last expression (line) in the cell:\n\n```\n(x+1)\n///\nx + 1\n```\n\n\nBut the second one doesn't:\n\n```\n(x+\n1)\n///\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9339\n\n",
    "created_at": "2010-06-25T20:04:50Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook fails to print result of last expression if there is a line break",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9339",
    "user": "nbruin"
}
```
Assignee: jason, was

Consider the following two notebook cells. Semantically, the input is the same in both examples. The only difference is that the second one has a line break inside a bracket.

First one prints the result of the last expression (line) in the cell:

```
(x+1)
///
x + 1
```


But the second one doesn't:

```
(x+
1)
///
```



Issue created by migration from https://trac.sagemath.org/ticket/9339





---

archive/issue_comments_088237.json:
```json
{
    "body": "Should be fixed by #7997",
    "created_at": "2010-06-25T20:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9339#issuecomment-88237",
    "user": "acleone"
}
```

Should be fixed by #7997



---

archive/issue_comments_088238.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-19T04:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9339#issuecomment-88238",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088239.json:
```json
{
    "body": "This is really the same as http://trac.sagemath.org/ticket/8503 and https://github.com/sagemath/sagenb/issues/301 - note that some examples *do* work.",
    "created_at": "2014-12-19T04:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9339#issuecomment-88239",
    "user": "kcrisman"
}
```

This is really the same as http://trac.sagemath.org/ticket/8503 and https://github.com/sagemath/sagenb/issues/301 - note that some examples *do* work.



---

archive/issue_comments_088240.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-19T04:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9339#issuecomment-88240",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088241.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-01-13T01:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9339",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9339#issuecomment-88241",
    "user": "vbraun"
}
```

Resolution: duplicate
