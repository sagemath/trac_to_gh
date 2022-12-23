# Issue 1135: Error in preparsing generators, QuadraticField

archive/issues_001135.json:
```json
{
    "body": "Assignee: ncalexan\n\nKeywords: preparse generators QuadraticField\n\n\n```\nsage: K.<a> = QuadraticField(-55, 'a')\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/emacs/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: QuadraticField() got multiple values for keyword argument 'names'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1135\n\n",
    "created_at": "2007-11-09T21:03:33Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Error in preparsing generators, QuadraticField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1135",
    "user": "ncalexan"
}
```
Assignee: ncalexan

Keywords: preparse generators QuadraticField


```
sage: K.<a> = QuadraticField(-55, 'a')
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/emacs/<ipython console> in <module>()

<type 'exceptions.TypeError'>: QuadraticField() got multiple values for keyword argument 'names'
```


Issue created by migration from https://trac.sagemath.org/ticket/1135





---

archive/issue_comments_006885.json:
```json
{
    "body": "This clearly belongs in \"number fields\" (\"interfaces\" is for Sage interfaces to other software, not for user-interface issues).",
    "created_at": "2010-04-16T16:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6885",
    "user": "davidloeffler"
}
```

This clearly belongs in "number fields" ("interfaces" is for Sage interfaces to other software, not for user-interface issues).



---

archive/issue_comments_006886.json:
```json
{
    "body": "Changing component from interfaces to number fields.",
    "created_at": "2010-04-16T16:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6886",
    "user": "davidloeffler"
}
```

Changing component from interfaces to number fields.



---

archive/issue_comments_006887.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-17T14:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6887",
    "user": "lftabera"
}
```

Attachment



---

archive/issue_comments_006888.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T14:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6888",
    "user": "lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006889.json:
```json
{
    "body": "This is a small error that is embarrasingly old. This patch solves the problem. You can use a generator name and the preparser in all combinations.\n\n- I have added a default name for the generator 'a' to be consistent with NumberField.\n\n- I have documented the behaviour of Sage when QuadraticField and NumberField are given two generators but there is a conflict in their names. The generator name given by the preparser has precedence in this case.",
    "created_at": "2010-09-17T14:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6889",
    "user": "lftabera"
}
```

This is a small error that is embarrasingly old. This patch solves the problem. You can use a generator name and the preparser in all combinations.

- I have added a default name for the generator 'a' to be consistent with NumberField.

- I have documented the behaviour of Sage when QuadraticField and NumberField are given two generators but there is a conflict in their names. The generator name given by the preparser has precedence in this case.



---

archive/issue_comments_006890.json:
```json
{
    "body": "Looks fine to me and passes tests on sage.math.  Positive review!",
    "created_at": "2010-09-17T15:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6890",
    "user": "ncalexan"
}
```

Looks fine to me and passes tests on sage.math.  Positive review!



---

archive/issue_comments_006891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T15:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6891",
    "user": "ncalexan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_006892.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1135#issuecomment-6892",
    "user": "mpatel"
}
```

Resolution: fixed
