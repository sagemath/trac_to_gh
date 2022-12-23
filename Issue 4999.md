# Issue 4999: Solaris 10/Sparc: numerical noise doctest failure in sage/gsl/integration.pyx

archive/issues_004999.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  \"devel/sage/sage/gsl/integration.pyx\"              \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.3/sage-3.2.3-mark/devel/sage/sage/gsl/integration.pyx\", line 163:\n    sage: numerical_integral(exp(-1/x), 1, 2)\nExpected:\n    (0.50479221787318407, 5.6043194293440744e-15)\nGot:\n    (0.50479221787318396, 5.6043194293440728e-15)\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4999\n\n",
    "created_at": "2009-01-17T16:02:24Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "Solaris 10/Sparc: numerical noise doctest failure in sage/gsl/integration.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4999",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t  "devel/sage/sage/gsl/integration.pyx"              
**********************************************************************
File "/home/mabshoff/build-3.2.3/sage-3.2.3-mark/devel/sage/sage/gsl/integration.pyx", line 163:
    sage: numerical_integral(exp(-1/x), 1, 2)
Expected:
    (0.50479221787318407, 5.6043194293440744e-15)
Got:
    (0.50479221787318396, 5.6043194293440728e-15)
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4999





---

archive/issue_comments_038131.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-17T16:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38131",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038132.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-18T06:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38132",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_038133.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T14:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38133",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_038134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T14:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4999#issuecomment-38134",
    "user": "mabshoff"
}
```

Resolution: fixed
