# Issue 1364: 2.8.15.alpha2: sage/modules/quotient_module.py doctest failure

archive/issues_001364.json:
```json
{
    "body": "Assignee: roed\n\n\n```\nsage -t  devel/sage-main/sage/modules/quotient_module.py \n**********************************************************************\nFile \"quotient_module.py\", line 130:\n    sage: hash(Q)\nExpected:\n    -1880683406\nGot:\n    2870563926094318706\n**********************************************************************\nFile \"quotient_module.py\", line 134:\n    sage: hash((V, W))\nExpected:\n    -1880683406\nGot:\n    2870563926094318706\n**********************************************************************\nFile \"quotient_module.py\", line 159:\n    sage: cmp(Q1, 5)\nExpected:\n    1\nGot:\n    -1\n**********************************************************************\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1364\n\n",
    "created_at": "2007-12-02T05:27:03Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "2.8.15.alpha2: sage/modules/quotient_module.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1364",
    "user": "mabshoff"
}
```
Assignee: roed


```
sage -t  devel/sage-main/sage/modules/quotient_module.py 
**********************************************************************
File "quotient_module.py", line 130:
    sage: hash(Q)
Expected:
    -1880683406
Got:
    2870563926094318706
**********************************************************************
File "quotient_module.py", line 134:
    sage: hash((V, W))
Expected:
    -1880683406
Got:
    2870563926094318706
**********************************************************************
File "quotient_module.py", line 159:
    sage: cmp(Q1, 5)
Expected:
    1
Got:
    -1
**********************************************************************


Issue created by migration from https://trac.sagemath.org/ticket/1364





---

archive/issue_comments_008733.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-02T05:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1364#issuecomment-8733",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_008734.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T05:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1364#issuecomment-8734",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.



---

archive/issue_comments_008735.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T05:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1364#issuecomment-8735",
    "user": "mabshoff"
}
```

Resolution: fixed
