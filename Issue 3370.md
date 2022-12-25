# Issue 3370: [with patch, positive review] converting strings to ZZ[x,y] fails

archive/issues_003370.json:
```json
{
    "body": "Assignee: @malb\n\nWith 3.0.2:\n\n```\nsage: P.<x,y> = ZZ[]\nsage: P('x+y')\nTypeError                                 Traceback (most recent call last)\n\n/home/burcin/work/sage/sage-3.0.2/<ipython console> in <module>()\n\n/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py in __call__(self, x, check)\n    386 \n    387         elif isinstance(x , str) and self._has_singular:\n--> 388             self._singular_().set_ring()\n    389             try:\n    390                 return self._singular_().parent(x).sage_poly(self)\n\n/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_(self, singular, force)\n    172             return R\n    173         except (AttributeError, ValueError):\n--> 174             return self._singular_init_(singular, force)\n    175 \n    176     def _singular_init_(self, singular=singular_default, force=False):\n\n/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_init_(self, singular, force)\n    243 \n    244         else:\n--> 245             raise TypeError, \"no conversion to a Singular ring defined\"\n    246 \n    247         return self.__singular\n\nTypeError: no conversion to a Singular ring defined\n\n```\n\nAttached patch fixes this problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3370\n\n",
    "closed_at": "2008-06-15T19:00:34Z",
    "created_at": "2008-06-05T01:57:38Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, positive review] converting strings to ZZ[x,y] fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3370",
    "user": "https://github.com/burcin"
}
```
Assignee: @malb

With 3.0.2:

```
sage: P.<x,y> = ZZ[]
sage: P('x+y')
TypeError                                 Traceback (most recent call last)

/home/burcin/work/sage/sage-3.0.2/<ipython console> in <module>()

/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py in __call__(self, x, check)
    386 
    387         elif isinstance(x , str) and self._has_singular:
--> 388             self._singular_().set_ring()
    389             try:
    390                 return self._singular_().parent(x).sage_poly(self)

/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_(self, singular, force)
    172             return R
    173         except (AttributeError, ValueError):
--> 174             return self._singular_init_(singular, force)
    175 
    176     def _singular_init_(self, singular=singular_default, force=False):

/home/burcin/work/sage/sage-3.0.2/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in _singular_init_(self, singular, force)
    243 
    244         else:
--> 245             raise TypeError, "no conversion to a Singular ring defined"
    246 
    247         return self.__singular

TypeError: no conversion to a Singular ring defined

```

Attached patch fixes this problem.

Issue created by migration from https://trac.sagemath.org/ticket/3370





---

archive/issue_comments_023532.json:
```json
{
    "body": "convert strings to mpolynomials using sage_eval",
    "created_at": "2008-06-05T02:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3370#issuecomment-23532",
    "user": "https://github.com/burcin"
}
```

convert strings to mpolynomials using sage_eval



---

archive/issue_comments_023533.json:
```json
{
    "body": "Attachment [string_to_ZZxy_conversion.patch](tarball://root/attachments/some-uuid/ticket3370/string_to_ZZxy_conversion.patch) by @malb created at 2008-06-12 23:02:02\n\npatch looks good.",
    "created_at": "2008-06-12T23:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3370#issuecomment-23533",
    "user": "https://github.com/malb"
}
```

Attachment [string_to_ZZxy_conversion.patch](tarball://root/attachments/some-uuid/ticket3370/string_to_ZZxy_conversion.patch) by @malb created at 2008-06-12 23:02:02

patch looks good.



---

archive/issue_comments_023534.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T19:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3370#issuecomment-23534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007597.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T19:00:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3370",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3370#event-7597"
}
```



---

archive/issue_comments_023535.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T19:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3370#issuecomment-23535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_events_007598.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T19:08:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3370",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3370#event-7598"
}
```
