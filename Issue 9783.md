# Issue 9783: list_plot should accept dictionaries

archive/issues_009783.json:
```json
{
    "body": "Assignee: jason, was\n\nKeywords: list_plot, plotting, dictionaries\n\nIf I give the following dictionary to `list_plot`, it seems very obvious what I want it to do:\n\n```\n{67: 1770, 52: 2735, 37: 3135, 22: 3365, 72: 1560, 57: 2550, 42: 3020,\n27: 3295, 62: 1960, 47: 2880}\n```\n\n...especially since list_plot plots functions with a finite domain, and dictionaries in Python are called \"mapping types\"! We should make `list_plot` be able to deal with dictionaries with numeric keys and values.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9784\n\n",
    "created_at": "2010-08-23T01:53:27Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "list_plot should accept dictionaries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9783",
    "user": "ddrake"
}
```
Assignee: jason, was

Keywords: list_plot, plotting, dictionaries

If I give the following dictionary to `list_plot`, it seems very obvious what I want it to do:

```
{67: 1770, 52: 2735, 37: 3135, 22: 3365, 72: 1560, 57: 2550, 42: 3020,
27: 3295, 62: 1960, 47: 2880}
```

...especially since list_plot plots functions with a finite domain, and dictionaries in Python are called "mapping types"! We should make `list_plot` be able to deal with dictionaries with numeric keys and values.

Issue created by migration from https://trac.sagemath.org/ticket/9784





---

archive/issue_comments_096030.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-24T07:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9783#issuecomment-96030",
    "user": "ddrake"
}
```

Attachment



---

archive/issue_comments_096031.json:
```json
{
    "body": "Patch up, please review. One decision I'd like feedback on is sorting the resulting list -- I made it so that it only sorts the list when `plotjoined=True`, but maybe it would be fine to always sort the list?",
    "created_at": "2010-08-24T07:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9783#issuecomment-96031",
    "user": "ddrake"
}
```

Patch up, please review. One decision I'd like feedback on is sorting the resulting list -- I made it so that it only sorts the list when `plotjoined=True`, but maybe it would be fine to always sort the list?



---

archive/issue_comments_096032.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-24T07:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9783#issuecomment-96032",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096033.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-05T03:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9783#issuecomment-96033",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096034.json:
```json
{
    "body": "Looks good to me.  I agree with only sorting when plotjoined=True.",
    "created_at": "2010-09-05T03:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9783#issuecomment-96034",
    "user": "jason"
}
```

Looks good to me.  I agree with only sorting when plotjoined=True.



---

archive/issue_comments_096035.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9783#issuecomment-96035",
    "user": "mpatel"
}
```

Resolution: fixed
