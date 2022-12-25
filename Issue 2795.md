# Issue 2795: [with patch,needs review] QuotientRing -> Magma

archive/issues_002795.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: magma\n\n\n```\nsage: P.<x,y> = PolynomialRing(GF(2))\nsage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))\nsage: xbar, ybar = Q.gens()\nsage: xbar._magma_() # optional requires magma\nx\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2795\n\n",
    "created_at": "2008-04-04T11:21:03Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch,needs review] QuotientRing -> Magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2795",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Keywords: magma


```
sage: P.<x,y> = PolynomialRing(GF(2))
sage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))
sage: xbar, ybar = Q.gens()
sage: xbar._magma_() # optional requires magma
x
```


Issue created by migration from https://trac.sagemath.org/ticket/2795





---

archive/issue_comments_019148.json:
```json
{
    "body": "Attachment [qring_2_magma.patch](tarball://root/attachments/some-uuid/ticket2795/qring_2_magma.patch) by @mwhansen created at 2008-04-04 19:53:01\n\nLooks good to me.",
    "created_at": "2008-04-04T19:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19148",
    "user": "https://github.com/mwhansen"
}
```

Attachment [qring_2_magma.patch](tarball://root/attachments/some-uuid/ticket2795/qring_2_magma.patch) by @mwhansen created at 2008-04-04 19:53:01

Looks good to me.



---

archive/issue_events_006449.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T20:07:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2795#event-6449"
}
```



---

archive/issue_comments_019149.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T20:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019150.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T20:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_019151.json:
```json
{
    "body": "I'm changing this from closed -- positive review to \"opened, negative review\", since the given doctest doesn't even work if you *do* have Magma:\n\n\n```\nteragon:~ was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: referee\nsage: sage: P.<x,y> = PolynomialRing(GF(2))\nsage:  sage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))\nsage:  sage: xbar, ybar = Q.gens()\nsage:  sage: xbar._magma_() \n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n| SAGE Version sage-2.11, Release Date: 2008-03-30                   |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/was/<ipython console> in <module>()\n\n/Users/was/sage_object.pyx in sage.structure.sage_object.SageObject._magma_()\n\n/Users/was/sage_object.pyx in sage.structure.sage_object.SageObject._interface_()\n\n/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)\n    332             if isinstance(x, bool):\n    333                 return Expect.__call__(self, str(x).lower())\n--> 334             return Expect.__call__(self, x)\n    335         return self.objgens(x, gens)\n    336         \n\n/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)\n    736             return x\n    737         if isinstance(x, basestring):\n--> 738             return cls(self, x)\n    739         try:\n    740             return self._coerce_from_special_method(x)\n\n/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)\n   1005             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1006                 self._session_number = -1\n-> 1007                 raise TypeError, x\n   1008         self._session_number = parent._session_number\n   1009 \n\n<type 'exceptions.TypeError'>: Error evaluation Magma code.\nIN:_sage_[1] := xbar;\nOUT:\n>> _sage_[1] := xbar;\n                ^\nUser error: Identifier 'xbar' has not been declared or assigned\nsage: \n```\n",
    "created_at": "2008-04-05T20:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19151",
    "user": "https://github.com/williamstein"
}
```

I'm changing this from closed -- positive review to "opened, negative review", since the given doctest doesn't even work if you *do* have Magma:


```
teragon:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: referee
sage: sage: P.<x,y> = PolynomialRing(GF(2))
sage:  sage: Q = P.quotient(sage.rings.ideal.FieldIdeal(P))
sage:  sage: xbar, ybar = Q.gens()
sage:  sage: xbar._magma_() 
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
| SAGE Version sage-2.11, Release Date: 2008-03-30                   |
| Type notebook() for the GUI, and license() for information.        |
/Users/was/<ipython console> in <module>()

/Users/was/sage_object.pyx in sage.structure.sage_object.SageObject._magma_()

/Users/was/sage_object.pyx in sage.structure.sage_object.SageObject._interface_()

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)
    332             if isinstance(x, bool):
    333                 return Expect.__call__(self, str(x).lower())
--> 334             return Expect.__call__(self, x)
    335         return self.objgens(x, gens)
    336         

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    736             return x
    737         if isinstance(x, basestring):
--> 738             return cls(self, x)
    739         try:
    740             return self._coerce_from_special_method(x)

/Users/was/build/sage-2.10.4/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
   1005             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1006                 self._session_number = -1
-> 1007                 raise TypeError, x
   1008         self._session_number = parent._session_number
   1009 

<type 'exceptions.TypeError'>: Error evaluation Magma code.
IN:_sage_[1] := xbar;
OUT:
>> _sage_[1] := xbar;
                ^
User error: Identifier 'xbar' has not been declared or assigned
sage: 
```




---

archive/issue_comments_019152.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-05T20:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19152",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006450.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-04-05T20:26:10Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2795#event-6450"
}
```



---

archive/issue_comments_019153.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-05T20:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19153",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_019154.json:
```json
{
    "body": "Never mind:\n\n```\n13:27 < wstein> Ah, I think I mistunderstood what the ticket is about.\n13:27 < wstein> Oops.\n13:27 < wstein> I'll change it back.\n13:28 < wstein> The problem was that the ticket description was a little vague.\n13:28 < wstein> Sorry\n```\n",
    "created_at": "2008-04-05T20:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19154",
    "user": "https://github.com/williamstein"
}
```

Never mind:

```
13:27 < wstein> Ah, I think I mistunderstood what the ticket is about.
13:27 < wstein> Oops.
13:27 < wstein> I'll change it back.
13:28 < wstein> The problem was that the ticket description was a little vague.
13:28 < wstein> Sorry
```




---

archive/issue_events_006451.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-04-05T20:28:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2795#event-6451"
}
```



---

archive/issue_comments_019155.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T20:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2795#issuecomment-19155",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
