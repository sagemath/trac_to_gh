# Issue 4765: Sage 3.2.2.alpha1: numerical noise in sage/rings/number_field/number_field_morphisms.pyx on OSX 10.4/G5

archive/issues_004765.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long \"devel/sage/sage/rings/number_field/number_field_morphisms.pyx\"\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/number_field_morphisms.pyx\", line 214, in __main__.example_10\nFailed example:\n    matching_root(x**Integer(3)-Integer(1), CDF.gen(0))###line 227:_sage_    >>> matching_root(x^3-1, CDF.0)\nExpected:\n    -0.500000000000000 + 0.86602540378443...*I\nGot:\n    -0.500000000000001 + 0.866025403784439*I\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4765\n\n",
    "created_at": "2008-12-12T03:42:00Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.2.2.alpha1: numerical noise in sage/rings/number_field/number_field_morphisms.pyx on OSX 10.4/G5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4765",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t -long "devel/sage/sage/rings/number_field/number_field_morphisms.pyx"
**********************************************************************
File "/Users/mabshoff/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/number_field_morphisms.pyx", line 214, in __main__.example_10
Failed example:
    matching_root(x**Integer(3)-Integer(1), CDF.gen(0))###line 227:_sage_    >>> matching_root(x^3-1, CDF.0)
Expected:
    -0.500000000000000 + 0.86602540378443...*I
Got:
    -0.500000000000001 + 0.866025403784439*I
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4765





---

archive/issue_comments_036110.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-12T03:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4765#issuecomment-36110",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036111.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-12T13:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4765#issuecomment-36111",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_036112.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-12-12T13:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4765#issuecomment-36112",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_036113.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T14:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4765#issuecomment-36113",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_comments_036114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T14:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4765#issuecomment-36114",
    "user": "mabshoff"
}
```

Resolution: fixed
