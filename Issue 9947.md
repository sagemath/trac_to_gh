# Issue 9947: Conversion of p-adic to gp is buggy because of "+Infinity" exponent

archive/issues_009947.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mstreng\n\n\n```\nsage: gp(pAdicField(5)(0))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jdemeyer/<ipython console> in <module>()\n\n/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1032             return cls(self, x, name=name)\n   1033         try:\n-> 1034             return self._coerce_from_special_method(x)\n   1035         except TypeError:\n   1036             raise\n\n/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)\n   1056             s = '_gp_'\n   1057         try:\n-> 1058             return (x.__getattribute__(s))(self)\n   1059         except AttributeError:\n   1060             return self(x._interface_init_())\n\n/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._gp_ (sage/structure/sage_object.c:4092)()\n\n/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)()\n\n/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1030\n   1031         if isinstance(x, basestring):\n-> 1032             return cls(self, x, name=name)\n   1033         try:\n   1034             return self._coerce_from_special_method(x)\n\n/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1450                 self._session_number = -1\n-> 1451                 raise TypeError, x\n   1452         self._session_number = parent._session_number\n   1453\n\nTypeError: Error executing code in GP/PARI:\nCODE:\n        sage[2]=0 + O(5^+Infinity);\nGP/PARI ERROR:\n  ***   at top-level: sage[2]=0+O(5^+Infinity)\n  ***                                ^---------\n  ***   gtos expected an integer, got 'Infinity'.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9948\n\n",
    "created_at": "2010-09-19T11:02:53Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Conversion of p-adic to gp is buggy because of \"+Infinity\" exponent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9947",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

CC:  @mstreng


```
sage: gp(pAdicField(5)(0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jdemeyer/<ipython console> in <module>()

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1032             return cls(self, x, name=name)
   1033         try:
-> 1034             return self._coerce_from_special_method(x)
   1035         except TypeError:
   1036             raise

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)
   1056             s = '_gp_'
   1057         try:
-> 1058             return (x.__getattribute__(s))(self)
   1059         except AttributeError:
   1060             return self(x._interface_init_())

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._gp_ (sage/structure/sage_object.c:4092)()

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)()

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453

TypeError: Error executing code in GP/PARI:
CODE:
        sage[2]=0 + O(5^+Infinity);
GP/PARI ERROR:
  ***   at top-level: sage[2]=0+O(5^+Infinity)
  ***                                ^---------
  ***   gtos expected an integer, got 'Infinity'.
```


Issue created by migration from https://trac.sagemath.org/ticket/9948





---

archive/issue_comments_099022.json:
```json
{
    "body": "Attachment [9948_padic_pari_gp.patch](tarball://root/attachments/some-uuid/ticket9948/9948_padic_pari_gp.patch) by @jdemeyer created at 2011-11-11 21:20:50",
    "created_at": "2011-11-11T21:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99022",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9948_padic_pari_gp.patch](tarball://root/attachments/some-uuid/ticket9948/9948_padic_pari_gp.patch) by @jdemeyer created at 2011-11-11 21:20:50



---

archive/issue_comments_099023.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd35\".",
    "created_at": "2012-01-06T12:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99023",
    "user": "https://github.com/mstreng"
}
```

Changing keywords from "" to "sd35".



---

archive/issue_comments_099024.json:
```json
{
    "body": "This seems to have been fixed in the meantime.  In Sage 6.2.beta6:\n\n```\nsage: gp(pAdicField(5)(0))\n0\nsage: pari(pAdicField(5)(0))\n0\n```\n\nI propose to close this as invalid/worksforme/whatever...",
    "created_at": "2014-04-10T23:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99024",
    "user": "https://github.com/pjbruin"
}
```

This seems to have been fixed in the meantime.  In Sage 6.2.beta6:

```
sage: gp(pAdicField(5)(0))
0
sage: pari(pAdicField(5)(0))
0
```

I propose to close this as invalid/worksforme/whatever...



---

archive/issue_comments_099025.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-10T23:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99025",
    "user": "https://github.com/pjbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099026.json:
```json
{
    "body": "Yes, seems fixed.",
    "created_at": "2014-04-11T08:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99026",
    "user": "https://github.com/jdemeyer"
}
```

Yes, seems fixed.



---

archive/issue_comments_099027.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-11T08:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99027",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-04-12T07:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9947#issuecomment-99028",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
