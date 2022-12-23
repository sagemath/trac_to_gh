# Issue 791: ugly absprec parameter in Polynomial constructor

archive/issues_000791.json:
```json
{
    "body": "Assignee: was\n\nI'm not happy with the profusion of code to deal with the absprec parameter in Polynomial-related code (for example, search for the string \"absprec\" in sage/rings/polynomial/polynomial_element.pyx). Something feels wrong with this design; the code keeps splitting into branches to deal with \"absprec\" or \"no absprec\" cases. I believe the \"absprec\" parameter has something to do with polynomials over p-adics. There has to be a cleaner way to deal with this issue. Please add comments below.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/791\n\n",
    "created_at": "2007-10-02T18:38:47Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "ugly absprec parameter in Polynomial constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/791",
    "user": "dmharvey"
}
```
Assignee: was

I'm not happy with the profusion of code to deal with the absprec parameter in Polynomial-related code (for example, search for the string "absprec" in sage/rings/polynomial/polynomial_element.pyx). Something feels wrong with this design; the code keeps splitting into branches to deal with "absprec" or "no absprec" cases. I believe the "absprec" parameter has something to do with polynomials over p-adics. There has to be a cleaner way to deal with this issue. Please add comments below.


Issue created by migration from https://trac.sagemath.org/ticket/791





---

archive/issue_comments_004756.json:
```json
{
    "body": "Changing assignee from was to somebody.",
    "created_at": "2007-10-04T19:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4756",
    "user": "mabshoff"
}
```

Changing assignee from was to somebody.



---

archive/issue_comments_004757.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-10-04T19:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4757",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_004758.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-24T08:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4758",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_004759.json:
```json
{
    "body": "rebase of previous patch against 3.3.alpha2",
    "created_at": "2009-01-27T06:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4759",
    "user": "AlexGhitza"
}
```

rebase of previous patch against 3.3.alpha2



---

archive/issue_comments_004760.json:
```json
{
    "body": "Attachment\n\nLooks good.  I have rebased the patch against 3.3.alpha2, since it got entangled in the whole Sage Days 12 flurry of activity.",
    "created_at": "2009-01-27T06:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4760",
    "user": "AlexGhitza"
}
```

Attachment

Looks good.  I have rebased the patch against 3.3.alpha2, since it got entangled in the whole Sage Days 12 flurry of activity.



---

archive/issue_comments_004761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T12:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4761",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004762.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-28T12:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/791#issuecomment-4762",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3
