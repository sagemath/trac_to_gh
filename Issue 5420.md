# Issue 5420: imag(complex(0,1)) gives TypeError (easy)

archive/issues_005420.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage: imag(complex(0,1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/.sage/temp/good/9936/_home_grout__sage_init_sage_0.py in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/functional.pyc in imag(x)\n    376     Return the imaginary part of x.\n    377     \"\"\"\n--> 378     try: return x.imag()\n    379     except AttributeError: return CDF(x).imag()\n    380 \n\nTypeError: 'float' object is not callable\n```\n\n\nThis is because complex(0,1).imag is a number, not a function, so trying to call that number gives the error.  As Robert Bradshaw said on the mailing list, Sage's imag() should really know about python complex numbers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5420\n\n",
    "created_at": "2009-03-02T17:38:06Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "imag(complex(0,1)) gives TypeError (easy)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5420",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd


```
sage: imag(complex(0,1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/good/9936/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/functional.pyc in imag(x)
    376     Return the imaginary part of x.
    377     """
--> 378     try: return x.imag()
    379     except AttributeError: return CDF(x).imag()
    380 

TypeError: 'float' object is not callable
```


This is because complex(0,1).imag is a number, not a function, so trying to call that number gives the error.  As Robert Bradshaw said on the mailing list, Sage's imag() should really know about python complex numbers.

Issue created by migration from https://trac.sagemath.org/ticket/5420





---

archive/issue_comments_041850.json:
```json
{
    "body": "Changing assignee from tbd to @jasongrout.",
    "created_at": "2009-03-13T17:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5420#issuecomment-41850",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from tbd to @jasongrout.



---

archive/issue_comments_041851.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-13T17:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5420#issuecomment-41851",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041852.json:
```json
{
    "body": "This looks fine in sage-4.0:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: imag(complex(0,1))\n1.00000000000000\n```\n",
    "created_at": "2009-06-02T07:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5420#issuecomment-41852",
    "user": "https://github.com/aghitza"
}
```

This looks fine in sage-4.0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: imag(complex(0,1))
1.00000000000000
```




---

archive/issue_comments_041853.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-26T02:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5420#issuecomment-41853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_041854.json:
```json
{
    "body": "This also looks OK with Sage 4.1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: imag(complex(0,1))\n1.00000000000000\n```\n\nSo I'm closing this ticket as fixed.",
    "created_at": "2009-07-26T02:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5420",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5420#issuecomment-41854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This also looks OK with Sage 4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: imag(complex(0,1))
1.00000000000000
```

So I'm closing this ticket as fixed.
