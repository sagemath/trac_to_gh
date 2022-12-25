# Issue 504: make lie interface more robust

archive/issues_000504.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe Lie interface doesn't gracefully handle errors, which totally corrupt the io stream. \n\n\n```\nsage: A4 = lie('A4')\nsage: A4.i_Cartan()\n\n     [[4,3,2,1]\n     ,[3,6,4,2]\n     ,[2,4,6,3]\n     ,[1,2,3,4]\n     ]\n\nsage: A4.multiplicative_order()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/home/was/<ipython console> in <module>()\n\n/home/was/element.pyx in element.RingElement.multiplicative_order()\n\n/home/was/element.pyx in element.RingElement.is_unit()\n\n<type 'exceptions.NotImplementedError'>:\nsage: A4.i_Cartan()\n\nsage: A4.i_Cartan()\nsage0\nsage: A4.i_Cartan()\n\nArgument types do not match in call. Types are: ==(grp, bin).\nValid argument types are for instance: ==(bin, bin).\nsage: A4.i_Cartan()\n\n     [[4,3,2,1]\n     ,[3,6,4,2]\n     ,[2,4,6,3]\n     ,[1,2,3,4]\n     ]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/504\n\n",
    "created_at": "2007-08-28T23:38:44Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "make lie interface more robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/504",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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

archive/issue_comments_002515.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-08-28T23:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/504#issuecomment-2515",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_002516.json:
```json
{
    "body": "Attachment [lie.py](tarball://root/attachments/some-uuid/ticket504/lie.py) by @mwhansen created at 2007-08-28 23:58:42",
    "created_at": "2007-08-28T23:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/504#issuecomment-2516",
    "user": "https://github.com/mwhansen"
}
```

Attachment [lie.py](tarball://root/attachments/some-uuid/ticket504/lie.py) by @mwhansen created at 2007-08-28 23:58:42



---

archive/issue_comments_002517.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T00:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/504#issuecomment-2517",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_000539.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2007-08-29T00:02:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/504",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/504#event-539"
}
```
