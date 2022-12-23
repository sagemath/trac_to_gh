# Issue 9227: units.length.millimeter missing

archive/issues_009227.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  asjarman@xtra.co.nz\n\na millimeter [mm] is 1/1000 of a meter and very often used by engineers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9227\n\n",
    "created_at": "2010-06-12T12:55:42Z",
    "labels": [
        "algebra",
        "trivial",
        "enhancement"
    ],
    "title": "units.length.millimeter missing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9227",
    "user": "schilly"
}
```
Assignee: AlexGhitza

CC:  asjarman@xtra.co.nz

a millimeter [mm] is 1/1000 of a meter and very often used by engineers.

Issue created by migration from https://trac.sagemath.org/ticket/9227





---

archive/issue_comments_086585.json:
```json
{
    "body": "Attachment\n\npatch to add mm and km",
    "created_at": "2010-08-27T23:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86585",
    "user": "allmar"
}
```

Attachment

patch to add mm and km



---

archive/issue_comments_086586.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T06:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86586",
    "user": "allmar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086587.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2010-09-02T11:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86587",
    "user": "AlexGhitza"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_086588.json:
```json
{
    "body": "You mentioned\n\n```\nEqual to 1000 meters.\n```\n\ntwice. You should replace one by a comparison to yards, feet or something else.",
    "created_at": "2011-01-07T09:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86588",
    "user": "aapitzsch"
}
```

You mentioned

```
Equal to 1000 meters.
```

twice. You should replace one by a comparison to yards, feet or something else.



---

archive/issue_comments_086589.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-07T22:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86589",
    "user": "spice"
}
```

Attachment



---

archive/issue_comments_086590.json:
```json
{
    "body": "Doctests fail due to there being TAB characters in this patch.\n\nI've added an updated patch, which replaces the TAB characters in the patch with spaces, as well as changing line 650:\n`'kilometer':'Equal to 1000 meters.\\nEqual to 1000 meters.',`\nto\n`'kilometer':'Equal to 1000 meters.\\nEqual to 3280.8399 feet.',`",
    "created_at": "2011-01-07T23:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86590",
    "user": "spice"
}
```

Doctests fail due to there being TAB characters in this patch.

I've added an updated patch, which replaces the TAB characters in the patch with spaces, as well as changing line 650:
`'kilometer':'Equal to 1000 meters.\nEqual to 1000 meters.',`
to
`'kilometer':'Equal to 1000 meters.\nEqual to 3280.8399 feet.',`



---

archive/issue_comments_086591.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2011-01-10T01:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86591",
    "user": "aly.deines"
}
```

Looks good to me.



---

archive/issue_comments_086592.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T01:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86592",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086593.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86593",
    "user": "jdemeyer"
}
```

Resolution: fixed
