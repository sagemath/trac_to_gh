# Issue 6405: Typesetting of imaginary 'I' in new Symbolics is not proper

archive/issues_006405.json:
```json
{
    "body": "CC:  robertwb\n\nIn new symbolics, imaginary 'I' is typeset as 'I' which is not \"textbook style\". This is a regression compared to Sage 3.4\n\n\n```\nsage: latex( exp(i*x))\ne^{I \\, x}\n```\n\n\nLower case letter 'i' should be used in the typeset version.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6405\n\n",
    "created_at": "2009-06-25T14:30:01Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Typesetting of imaginary 'I' in new Symbolics is not proper",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6405",
    "user": "gmhossain"
}
```
CC:  robertwb

In new symbolics, imaginary 'I' is typeset as 'I' which is not "textbook style". This is a regression compared to Sage 3.4


```
sage: latex( exp(i*x))
e^{I \, x}
```


Lower case letter 'i' should be used in the typeset version.


Issue created by migration from https://trac.sagemath.org/ticket/6405





---

archive/issue_comments_051439.json:
```json
{
    "body": "Complex I in new symbolics is nothing but a quadratic number field element.\n\nRobert, any thoughts on how to handle this?",
    "created_at": "2009-08-01T02:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6405#issuecomment-51439",
    "user": "burcin"
}
```

Complex I in new symbolics is nothing but a quadratic number field element.

Robert, any thoughts on how to handle this?



---

archive/issue_comments_051440.json:
```json
{
    "body": "See #9017",
    "created_at": "2010-05-22T15:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6405#issuecomment-51440",
    "user": "robertwb"
}
```

See #9017



---

archive/issue_comments_051441.json:
```json
{
    "body": "This was fixed by #9017. attachment:9017-latex-sqrt-neg1.patch:ticket:9017 changes a doctest in `sage.symbolic.pynac.pyx` to test this change.\n\nI'm closing this as a duplicate.",
    "created_at": "2010-07-11T16:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6405#issuecomment-51441",
    "user": "burcin"
}
```

This was fixed by #9017. attachment:9017-latex-sqrt-neg1.patch:ticket:9017 changes a doctest in `sage.symbolic.pynac.pyx` to test this change.

I'm closing this as a duplicate.



---

archive/issue_comments_051442.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-11T16:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6405#issuecomment-51442",
    "user": "burcin"
}
```

Resolution: duplicate
