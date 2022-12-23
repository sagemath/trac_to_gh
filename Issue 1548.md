# Issue 1548: Sage 2.9: calculus/calculus.py numerical noise doctest

archive/issues_001548.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage-main/sage/calculus/calculus.py\n**********************************************************************\nFile \"calculus.py\", line 2460:\n    sage: v.find_root(0, 0.002)\nExpected:\n    0.0015403270679114178\nGot:\n    0.0015403270679114176\n**********************************************************************\nFile \"calculus.py\", line 2473:\n    sage: a.find_root(0,0.002)\nExpected:\n    0.00041105140493493411\nGot:\n    0.00041105140493493417\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1548\n\n",
    "created_at": "2007-12-17T13:32:31Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 2.9: calculus/calculus.py numerical noise doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1548",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage-main/sage/calculus/calculus.py
**********************************************************************
File "calculus.py", line 2460:
    sage: v.find_root(0, 0.002)
Expected:
    0.0015403270679114178
Got:
    0.0015403270679114176
**********************************************************************
File "calculus.py", line 2473:
    sage: a.find_root(0,0.002)
Expected:
    0.00041105140493493411
Got:
    0.00041105140493493417
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/1548





---

archive/issue_comments_009873.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-18T21:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1548#issuecomment-9873",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_009874.json:
```json
{
    "body": "Merged in 2.9.1.alpha1",
    "created_at": "2007-12-18T21:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1548#issuecomment-9874",
    "user": "rlm"
}
```

Merged in 2.9.1.alpha1



---

archive/issue_comments_009875.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-18T21:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1548#issuecomment-9875",
    "user": "rlm"
}
```

Resolution: fixed
