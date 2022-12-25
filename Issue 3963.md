# Issue 3963: [with patch, needs review] bug in converting Sage's rationals to Sympy rationals

archive/issues_003963.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nfrom sympy import Symbol\nQQ(1)+Symbol('x')*QQ(2)\n\nproduces an error:\n\nTypeError                                 Traceback (most recent call\nlast)\n\n/Applications/sage/<ipython console> in <module>()\n\n/Applications/sage/element.pyx in\nsage.structure.element.ModuleElement.__add__ (sage/structure/element.c:\n5606)()\n\n/Applications/sage/coerce.pyx in\nsage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/\ncoerce.c:6288)()\n\nTypeError: unsupported operand parent(s) for '+': 'Rational Field' and\n'<class 'sympy.core.mul.Mul'>'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3963\n\n",
    "created_at": "2008-08-27T00:52:43Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] bug in converting Sage's rationals to Sympy rationals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3963",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein


```
from sympy import Symbol
QQ(1)+Symbol('x')*QQ(2)

produces an error:

TypeError                                 Traceback (most recent call
last)

/Applications/sage/<ipython console> in <module>()

/Applications/sage/element.pyx in
sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:
5606)()

/Applications/sage/coerce.pyx in
sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/
coerce.c:6288)()

TypeError: unsupported operand parent(s) for '+': 'Rational Field' and
'<class 'sympy.core.mul.Mul'>'
```


Issue created by migration from https://trac.sagemath.org/ticket/3963





---

archive/issue_comments_028412.json:
```json
{
    "body": "Attachment [trac_3963.patch](tarball://root/attachments/some-uuid/ticket3963/trac_3963.patch) by @mwhansen created at 2008-08-27 00:53:57",
    "created_at": "2008-08-27T00:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3963#issuecomment-28412",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3963.patch](tarball://root/attachments/some-uuid/ticket3963/trac_3963.patch) by @mwhansen created at 2008-08-27 00:53:57



---

archive/issue_comments_028413.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T00:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3963#issuecomment-28413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_028414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T00:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3963#issuecomment-28414",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004191.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-27T00:57:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3963",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3963#event-4191"
}
```



---

archive/issue_comments_028415.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T00:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3963#issuecomment-28415",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha1
