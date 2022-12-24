# Issue 845: Can't pass boolean as parameter to Magma

archive/issues_000845.json:
```json
{
    "body": "Assignee: was\n\nsage: magma('false')\nfalse\nsage: f = magma('Polynomial([-2,0,1])')\nsage: f.NumberField(Check = false)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/jvoight/totallyreal/<ipython console> in <module>()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, *args, **kwds)\n    552                                [self._obj.name()] + list(args),\n    553                                params = kwds,\n--> 554                                nvals = nvals)\n    555\n    556     def _sage_doc_(self):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in function_call(self, function, args, params, nvals)\n    405             ans = None\n    406         elif nvals == 1:\n--> 407             return self(fun)\n    408         else:\n    409             v = [self._next_var_name() for _ in range(nvals)]\n\n/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)\n    315         \"\"\"\n    316         if gens is None:\n--> 317             return Expect.__call__(self, x)\n    318         return self.objgens(x, gens)\n    319\n\n/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)\n    679             return x\n    680         if isinstance(x, basestring):\n--> 681             return cls(self, x)\n    682         try:\n    683             return self._coerce_from_special_method(x)\n\n/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)\n    920             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n    921                 self._session_number = -1\n--> 922                 raise TypeError, x\n    923         self._session_number = parent._session_number\n    924\n\n<type 'exceptions.TypeError'>: Error evaluation Magma code.\nIN:_sage_[5] := NumberField(_sage_[4] : Check:=False);\nOUT:\n>> _sage_[5] := NumberField(_sage_[4] : Check:=False);\n                                               ^\nUser error: Identifier 'False' has not been declared or assigned\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/845\n\n",
    "created_at": "2007-10-10T06:56:01Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "Can't pass boolean as parameter to Magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/845",
    "user": "jvoight"
}
```
Assignee: was

sage: magma('false')
false
sage: f = magma('Polynomial([-2,0,1])')
sage: f.NumberField(Check = false)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/jvoight/totallyreal/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, *args, **kwds)
    552                                [self._obj.name()] + list(args),
    553                                params = kwds,
--> 554                                nvals = nvals)
    555
    556     def _sage_doc_(self):

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in function_call(self, function, args, params, nvals)
    405             ans = None
    406         elif nvals == 1:
--> 407             return self(fun)
    408         else:
    409             v = [self._next_var_name() for _ in range(nvals)]

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)
    315         """
    316         if gens is None:
--> 317             return Expect.__call__(self, x)
    318         return self.objgens(x, gens)
    319

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    679             return x
    680         if isinstance(x, basestring):
--> 681             return cls(self, x)
    682         try:
    683             return self._coerce_from_special_method(x)

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    920             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    921                 self._session_number = -1
--> 922                 raise TypeError, x
    923         self._session_number = parent._session_number
    924

<type 'exceptions.TypeError'>: Error evaluation Magma code.
IN:_sage_[5] := NumberField(_sage_[4] : Check:=False);
OUT:
>> _sage_[5] := NumberField(_sage_[4] : Check:=False);
                                               ^
User error: Identifier 'False' has not been declared or assigned


Issue created by migration from https://trac.sagemath.org/ticket/845





---

archive/issue_comments_005223.json:
```json
{
    "body": "Attachment [magma_bool.patch](tarball://root/attachments/some-uuid/ticket845/magma_bool.patch) by malb created at 2007-10-30 16:37:55",
    "created_at": "2007-10-30T16:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/845#issuecomment-5223",
    "user": "malb"
}
```

Attachment [magma_bool.patch](tarball://root/attachments/some-uuid/ticket845/magma_bool.patch) by malb created at 2007-10-30 16:37:55



---

archive/issue_comments_005224.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-30T16:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/845#issuecomment-5224",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005225.json:
```json
{
    "body": "fixed in attached patch. A Magma guru should look at this patch, though.",
    "created_at": "2007-10-30T16:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/845#issuecomment-5225",
    "user": "malb"
}
```

fixed in attached patch. A Magma guru should look at this patch, though.



---

archive/issue_comments_005226.json:
```json
{
    "body": "Changing assignee from was to malb.",
    "created_at": "2007-10-30T16:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/845#issuecomment-5226",
    "user": "malb"
}
```

Changing assignee from was to malb.



---

archive/issue_comments_005227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T23:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/845#issuecomment-5227",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005228.json:
```json
{
    "body": "applied to 2.8.11.rc1",
    "created_at": "2007-11-01T23:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/845#issuecomment-5228",
    "user": "mabshoff"
}
```

applied to 2.8.11.rc1
