# Issue 5630: improve doctest coverage for schemes/generic/spec.py

archive/issues_005630.json:
```json
{
    "body": "Assignee: was\n\nKeywords: spec doctest latex\n\nThe attached patch adds a `_latex_()` method for Spec's of rings and improves the doctest coverage of `spec.py` from 42% (3 of 7) to 75% (6 of 8).\n\nThe two remaining methods are currently involved in other tickets that will also take care of adding doctests: see #5629 for `dimension()` and #5479 for `__call__()`\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5630\n\n",
    "created_at": "2009-03-29T04:55:42Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "title": "improve doctest coverage for schemes/generic/spec.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5630",
    "user": "AlexGhitza"
}
```
Assignee: was

Keywords: spec doctest latex

The attached patch adds a `_latex_()` method for Spec's of rings and improves the doctest coverage of `spec.py` from 42% (3 of 7) to 75% (6 of 8).

The two remaining methods are currently involved in other tickets that will also take care of adding doctests: see #5629 for `dimension()` and #5479 for `__call__()`


Issue created by migration from https://trac.sagemath.org/ticket/5630





---

archive/issue_comments_043966.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-03-29T08:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5630#issuecomment-43966",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_043967.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T08:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5630#issuecomment-43967",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043968.json:
```json
{
    "body": "This doctest fails for me on 32-bit OS X:\n\n```\nteragon:sage-3.4 wstein$ sage -t devel/sage/sage/schemes/generic/spec.py \nsage -t  \"devel/sage/sage/schemes/generic/spec.py\"          \n**********************************************************************\nFile \"/Users/wstein/build/sage-3.4/devel/sage/sage/schemes/generic/spec.py\", line 116:\n    sage: Spec(QQ) < 5\nExpected:\n    True\nGot:\n    False\n```\n\n\nSince the result is meaningless, you could flag it \n\n```\nsage:  spec(QQ) < 5   # random -- platform dependent\n```\n\n\nor instead have a test\n\n```\nsage: spec(QQ) == 5\nFalse\n```\n\n\nIf you fix this one issue, then this will get \"positive review\" from me.",
    "created_at": "2009-03-29T17:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5630#issuecomment-43968",
    "user": "was"
}
```

This doctest fails for me on 32-bit OS X:

```
teragon:sage-3.4 wstein$ sage -t devel/sage/sage/schemes/generic/spec.py 
sage -t  "devel/sage/sage/schemes/generic/spec.py"          
**********************************************************************
File "/Users/wstein/build/sage-3.4/devel/sage/sage/schemes/generic/spec.py", line 116:
    sage: Spec(QQ) < 5
Expected:
    True
Got:
    False
```


Since the result is meaningless, you could flag it 

```
sage:  spec(QQ) < 5   # random -- platform dependent
```


or instead have a test

```
sage: spec(QQ) == 5
False
```


If you fix this one issue, then this will get "positive review" from me.



---

archive/issue_comments_043969.json:
```json
{
    "body": "Attachment\n\nAh, I had misinterpreted the existing docstring for `_cmp_`.  I removed the offending doctest (the one with `Spec(QQ) == 5` is already there) and clarified the docstring a little bit.\n\nNew patch is up replacing the old one.",
    "created_at": "2009-03-29T21:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5630#issuecomment-43969",
    "user": "AlexGhitza"
}
```

Attachment

Ah, I had misinterpreted the existing docstring for `_cmp_`.  I removed the offending doctest (the one with `Spec(QQ) == 5` is already there) and clarified the docstring a little bit.

New patch is up replacing the old one.



---

archive/issue_comments_043970.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T06:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5630#issuecomment-43970",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_043971.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T06:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5630",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5630#issuecomment-43971",
    "user": "mabshoff"
}
```

Resolution: fixed
