# Issue 6183: Quaternion algebra latexification

archive/issues_006183.json:
```json
{
    "body": "Assignee: tbd\n\nQuaternion algebra elements don't have a nice latexification. This should be easy for someone to add. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6183\n\n",
    "created_at": "2009-06-02T07:28:18Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Quaternion algebra latexification",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6183",
    "user": "robertwb"
}
```
Assignee: tbd

Quaternion algebra elements don't have a nice latexification. This should be easy for someone to add. 

Issue created by migration from https://trac.sagemath.org/ticket/6183





---

archive/issue_comments_049362.json:
```json
{
    "body": "Changing assignee from tbd to AlexGhitza.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49362",
    "user": "AlexGhitza"
}
```

Changing assignee from tbd to AlexGhitza.



---

archive/issue_comments_049363.json:
```json
{
    "body": "Changing keywords from \"\" to \"quaternion latex\".",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49363",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "quaternion latex".



---

archive/issue_comments_049364.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49364",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_049365.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49365",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049366.json:
```json
{
    "body": "See attached patch.",
    "created_at": "2009-07-11T13:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49366",
    "user": "AlexGhitza"
}
```

See attached patch.



---

archive/issue_comments_049367.json:
```json
{
    "body": "Attachment [trac_6183.patch](tarball://root/attachments/some-uuid/ticket6183/trac_6183.patch) by AlexGhitza created at 2009-07-11 13:12:23",
    "created_at": "2009-07-11T13:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49367",
    "user": "AlexGhitza"
}
```

Attachment [trac_6183.patch](tarball://root/attachments/some-uuid/ticket6183/trac_6183.patch) by AlexGhitza created at 2009-07-11 13:12:23



---

archive/issue_comments_049368.json:
```json
{
    "body": "\n```\nsage: B.<i, j, k> = QuaternionAlgebra(RR, -1, -1) \nsage: latex(i + 1 - k) \n1.00000000000000 + i - k\n```\n\n\nWith all due respect, this is hideous :-) I know you only did it for consistency with the `repr` method, of course; but what would you say to the suggestion that we change `repr`, and `latex`, so they return something like `1.00000000000000 + 1.00000000000000*i - 1.00000000000000*k`? This is consistent with our conventions for other algebras over inexact rings (e.g. polynomials and power series).",
    "created_at": "2009-07-13T19:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49368",
    "user": "davidloeffler"
}
```


```
sage: B.<i, j, k> = QuaternionAlgebra(RR, -1, -1) 
sage: latex(i + 1 - k) 
1.00000000000000 + i - k
```


With all due respect, this is hideous :-) I know you only did it for consistency with the `repr` method, of course; but what would you say to the suggestion that we change `repr`, and `latex`, so they return something like `1.00000000000000 + 1.00000000000000*i - 1.00000000000000*k`? This is consistent with our conventions for other algebras over inexact rings (e.g. polynomials and power series).



---

archive/issue_comments_049369.json:
```json
{
    "body": "Point taken.\n\nI'm changing this to \"needs work\".  I'll try to find an elegant way of using the printing code for polynomials so that things are consistent (and stay that way).",
    "created_at": "2009-07-14T07:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49369",
    "user": "AlexGhitza"
}
```

Point taken.

I'm changing this to "needs work".  I'll try to find an elegant way of using the printing code for polynomials so that things are consistent (and stay that way).



---

archive/issue_comments_049370.json:
```json
{
    "body": "Actually, note that printing of polynomials is *not* consistent, in that multivariable polynomials have \"hideous\" printing, whereas univariate ones have \"pretty\" printing:\n\n\n```\nsage: R.<i, j, k> = RR[]\nsage: i + 1 - k\ni - k + 1.00000000000000\nsage: R.<i> = RR[[]]\nsage: i+1\n1.00000000000000 + 1.00000000000000*i\n```\n\n\nSo this needs fixing.",
    "created_at": "2009-07-14T07:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6183#issuecomment-49370",
    "user": "AlexGhitza"
}
```

Actually, note that printing of polynomials is *not* consistent, in that multivariable polynomials have "hideous" printing, whereas univariate ones have "pretty" printing:


```
sage: R.<i, j, k> = RR[]
sage: i + 1 - k
i - k + 1.00000000000000
sage: R.<i> = RR[[]]
sage: i+1
1.00000000000000 + 1.00000000000000*i
```


So this needs fixing.
