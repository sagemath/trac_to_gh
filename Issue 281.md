# Issue 281: Errors in matrix for extensions of NumberFields

archive/issues_000281.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: extension numberfield matrix polynomial\n\nThe following is incorrect:\n\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^3 - 5)\n\nsage: L.<b> = K.extension(K['x'].0^2 - 3)\n\nsage: b.matrix()\n \n[0 1]\n[0 0]\n\nsage: M.<c> = NumberField(ZZ['x'].0^2 - 3)\n\nsage: c.matrix()\n \n[0 1]\n[3 0]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/281\n\n",
    "created_at": "2007-02-23T20:01:46Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "Errors in matrix for extensions of NumberFields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/281",
    "user": "https://github.com/ncalexan"
}
```
Assignee: somebody

Keywords: extension numberfield matrix polynomial

The following is incorrect:


```
sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)

sage: L.<b> = K.extension(K['x'].0^2 - 3)

sage: b.matrix()
 
[0 1]
[0 0]

sage: M.<c> = NumberField(ZZ['x'].0^2 - 3)

sage: c.matrix()
 
[0 1]
[3 0]
```


Issue created by migration from https://trac.sagemath.org/ticket/281





---

archive/issue_comments_001330.json:
```json
{
    "body": "This is simply not implemented, and will be hard to do without rewriting number fields completely :-)\nDavid Roe?\n\nAnyway, in sAge-2.8 it raises a notimplementederror, so I've changed this from bug to enhancement.\n\nWilliam\n\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^3 - 5)\nsage: L.<b> = K.extension(K['x'].0^2 - 3)\nsage: b.matrix()\n...    \nTraceback (most recent call last):\n...\nNotImplementedError\n```\n",
    "created_at": "2007-08-18T20:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/281#issuecomment-1330",
    "user": "https://github.com/williamstein"
}
```

This is simply not implemented, and will be hard to do without rewriting number fields completely :-)
David Roe?

Anyway, in sAge-2.8 it raises a notimplementederror, so I've changed this from bug to enhancement.

William


```
sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)
sage: L.<b> = K.extension(K['x'].0^2 - 3)
sage: b.matrix()
...    
Traceback (most recent call last):
...
NotImplementedError
```




---

archive/issue_comments_001331.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-18T20:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/281#issuecomment-1331",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_000630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T05:27:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/281#event-630"
}
```



---

archive/issue_events_000631.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-21T13:55:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/281#event-631"
}
```



---

archive/issue_events_000632.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-21T13:55:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/281#event-632"
}
```



---

archive/issue_comments_001332.json:
```json
{
    "body": "It works with Sage 2.8.8:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.8, Release Date: 2007-10-20                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)\nsage: sage: L.<b> = K.extension(K['x'].0^2 - 3)\nsage: sage: b.matrix()\n\n[0 1]\n[3 0]\nsage: \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T13:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/281#issuecomment-1332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It works with Sage 2.8.8:

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.8, Release Date: 2007-10-20                       |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)
sage: sage: L.<b> = K.extension(K['x'].0^2 - 3)
sage: sage: b.matrix()

[0 1]
[3 0]
sage: 
```


Cheers,

Michael



---

archive/issue_comments_001333.json:
```json
{
    "body": "I would actually say that this was fixed by roed's rewrite. So it would be \"fixed\" in my book.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-24T03:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/281#issuecomment-1333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I would actually say that this was fixed by roed's rewrite. So it would be "fixed" in my book.

Cheers,

Michael



---

archive/issue_comments_001334.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T03:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/281#issuecomment-1334",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000633.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-24T03:38:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/281#event-633"
}
```



---

archive/issue_comments_001335.json:
```json
{
    "body": "yep, fixed by my rewrite (not david's).",
    "created_at": "2007-10-24T03:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/281#issuecomment-1335",
    "user": "https://github.com/williamstein"
}
```

yep, fixed by my rewrite (not david's).
