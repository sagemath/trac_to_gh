# Issue 504: make lie interface more robust

archive/issues_000504.json:
```json
{
    "body": "Assignee: was\n\nThe Lie interface doesn't gracefully handle errors, which totally corrupt the io stream. \n\n\n```\nsage: A4 = lie('A4')\nsage: A4.i_Cartan()\n\n     [[4,3,2,1]\n     ,[3,6,4,2]\n     ,[2,4,6,3]\n     ,[1,2,3,4]\n     ]\n\nsage: A4.multiplicative_order()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/home/was/<ipython console> in <module>()\n\n/home/was/element.pyx in element.RingElement.multiplicative_order()\n\n/home/was/element.pyx in element.RingElement.is_unit()\n\n<type 'exceptions.NotImplementedError'>:\nsage: A4.i_Cartan()\n\nsage: A4.i_Cartan()\nsage0\nsage: A4.i_Cartan()\n\nArgument types do not match in call. Types are: ==(grp, bin).\nValid argument types are for instance: ==(bin, bin).\nsage: A4.i_Cartan()\n\n     [[4,3,2,1]\n     ,[3,6,4,2]\n     ,[2,4,6,3]\n     ,[1,2,3,4]\n     ]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/504\n\n",
    "created_at": "2007-08-28T23:38:44Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "make lie interface more robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/504",
    "user": "was"
}
```
Assignee: was

The Lie interface doesn't gracefully handle errors, which totally corrupt the io stream. 


```
sage: A4 = lie('A4')
sage: A4.i_Cartan()

     [[4,3,2,1]
     ,[3,6,4,2]
     ,[2,4,6,3]
     ,[1,2,3,4]
     ]

sage: A4.multiplicative_order()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/was/<ipython console> in <module>()

/home/was/element.pyx in element.RingElement.multiplicative_order()

/home/was/element.pyx in element.RingElement.is_unit()

<type 'exceptions.NotImplementedError'>:
sage: A4.i_Cartan()

sage: A4.i_Cartan()
sage0
sage: A4.i_Cartan()

Argument types do not match in call. Types are: ==(grp, bin).
Valid argument types are for instance: ==(bin, bin).
sage: A4.i_Cartan()

     [[4,3,2,1]
     ,[3,6,4,2]
     ,[2,4,6,3]
     ,[1,2,3,4]
     ]
```


Issue created by migration from https://trac.sagemath.org/ticket/504





---

archive/issue_comments_002525.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-08-28T23:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/504#issuecomment-2525",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_002526.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-08-28T23:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/504#issuecomment-2526",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_002527.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T00:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/504#issuecomment-2527",
    "user": "mhansen"
}
```

Resolution: fixed
