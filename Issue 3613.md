# Issue 3613: symbolic equations are not passed to Maple correctly

archive/issues_003613.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: maple(x==2)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x, name)\n    945             return cls(self, x, name=name)\n    946         try:\n--> 947             return self._coerce_from_special_method(x)\n    948         except TypeError:\n    949             raise\n\n/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)\n    969             s = '_gp_'\n    970         try:\n--> 971             return (x.__getattribute__(s))(self)\n    972         except AttributeError:\n    973             return self(x._interface_init_())\n\n/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/sage_object.pyx in sage.structure.sage_object.SageObject._maple_ (sage/structure/sage_object.c:3342)()\n\n/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2009)()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x, name)\n    943             return x\n    944         if isinstance(x, basestring):\n--> 945             return cls(self, x, name=name)\n    946         try:\n    947             return self._coerce_from_special_method(x)\n\n/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name, name)\n   1208             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1209                 self._session_number = -1\n-> 1210                 raise TypeError, x\n   1211         self._session_number = parent._session_number\n   1212 \n\nTypeError: An error occured running a Maple command:\nINPUT:\nread \"/home/mike/.sage//temp/mike_laptop/21257//interface//tmp\";\nOUTPUT:\non line 1, syntax error, `=` unexpected:\nsage1:=x == 2:;\n          ^\nError, while reading `/home/mike/.sage//temp/mike_laptop/21257//interface//tmp`\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3613\n\n",
    "created_at": "2008-07-08T17:58:37Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "symbolic equations are not passed to Maple correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3613",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein


```
sage: maple(x==2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x, name)
    945             return cls(self, x, name=name)
    946         try:
--> 947             return self._coerce_from_special_method(x)
    948         except TypeError:
    949             raise

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)
    969             s = '_gp_'
    970         try:
--> 971             return (x.__getattribute__(s))(self)
    972         except AttributeError:
    973             return self(x._interface_init_())

/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/sage_object.pyx in sage.structure.sage_object.SageObject._maple_ (sage/structure/sage_object.c:3342)()

/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2009)()

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x, name)
    943             return x
    944         if isinstance(x, basestring):
--> 945             return cls(self, x, name=name)
    946         try:
    947             return self._coerce_from_special_method(x)

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name, name)
   1208             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1209                 self._session_number = -1
-> 1210                 raise TypeError, x
   1211         self._session_number = parent._session_number
   1212 

TypeError: An error occured running a Maple command:
INPUT:
read "/home/mike/.sage//temp/mike_laptop/21257//interface//tmp";
OUTPUT:
on line 1, syntax error, `=` unexpected:
sage1:=x == 2:;
          ^
Error, while reading `/home/mike/.sage//temp/mike_laptop/21257//interface//tmp`
```


Issue created by migration from https://trac.sagemath.org/ticket/3613





---

archive/issue_comments_025456.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-09T00:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3613#issuecomment-25456",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025457.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-07-09T00:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3613#issuecomment-25457",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_025458.json:
```json
{
    "body": "Attachment [trac_3613.patch](tarball://root/attachments/some-uuid/ticket3613/trac_3613.patch) by @ncalexan created at 2008-08-10 20:22:13\n\nFine by me, apply!",
    "created_at": "2008-08-10T20:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3613#issuecomment-25458",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_3613.patch](tarball://root/attachments/some-uuid/ticket3613/trac_3613.patch) by @ncalexan created at 2008-08-10 20:22:13

Fine by me, apply!



---

archive/issue_comments_025459.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T05:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3613#issuecomment-25459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003831.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T05:15:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3613",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3613#event-3831"
}
```



---

archive/issue_comments_025460.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T05:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3613#issuecomment-25460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha1
