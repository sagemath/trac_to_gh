# Issue 468: quaddouble wrapper sets fpu precision to 53 bits for entire sage session

archive/issues_000468.json:
```json
{
    "body": "Assignee: bober\n\nKeywords: quaddouble, fpu, ReadQuadDouble\n\nsage/rings/real_rqdf.pyx contains the following code:\n\n\n```\ncdef class RealQuadDoubleField_class(Field):\n    \"\"\"\n    Real Quad Double Field\n    \"\"\"\n\n    def __init__(self):\n        fpu_fix_start(self.cwf)        \n\n    def __dealloc__(self):\n        fpu_fix_end(self.cwf)\n```\n\n\nOn systems where `fpu_fix_start()` does something, it sets the fpu precision to 53 bits. A poor side effect of this is that the type `long double` ought to have 64 bits of precision on some systems, but it doesn't when it is used in code run from SAGE.\n\nThe short term fix will be to rewrite the wrapper to have an fpu_fix_start() and fpu_fix_end() call before and after every arithmetic operation on a `RealQuadDouble` element, and nowhere else, to make sure that the quaddouble wrapper doesn't ever unexpected change the fpu precision.\n\nIt would also be nice to have a doctest that can check the fpu precision, so it can be checked that nothing ever changes it unexpectedly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/468\n\n",
    "created_at": "2007-08-20T20:58:22Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "quaddouble wrapper sets fpu precision to 53 bits for entire sage session",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/468",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: bober

Keywords: quaddouble, fpu, ReadQuadDouble

sage/rings/real_rqdf.pyx contains the following code:


```
cdef class RealQuadDoubleField_class(Field):
    """
    Real Quad Double Field
    """

    def __init__(self):
        fpu_fix_start(self.cwf)        

    def __dealloc__(self):
        fpu_fix_end(self.cwf)
```


On systems where `fpu_fix_start()` does something, it sets the fpu precision to 53 bits. A poor side effect of this is that the type `long double` ought to have 64 bits of precision on some systems, but it doesn't when it is used in code run from SAGE.

The short term fix will be to rewrite the wrapper to have an fpu_fix_start() and fpu_fix_end() call before and after every arithmetic operation on a `RealQuadDouble` element, and nowhere else, to make sure that the quaddouble wrapper doesn't ever unexpected change the fpu precision.

It would also be nice to have a doctest that can check the fpu precision, so it can be checked that nothing ever changes it unexpectedly.

Issue created by migration from https://trac.sagemath.org/ticket/468





---

archive/issue_comments_002317.json:
```json
{
    "body": "Attachment [5834.patch](tarball://root/attachments/some-uuid/ticket468/5834.patch) by bober created at 2007-08-23 18:09:05\n\nThis patch should fix this issue.",
    "created_at": "2007-08-23T18:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/468#issuecomment-2317",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Attachment [5834.patch](tarball://root/attachments/some-uuid/ticket468/5834.patch) by bober created at 2007-08-23 18:09:05

This patch should fix this issue.



---

archive/issue_comments_002318.json:
```json
{
    "body": "x86 specific fpu stuff -- see ticket discussion (this should NOT be included in sage)",
    "created_at": "2007-08-23T18:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/468#issuecomment-2318",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

x86 specific fpu stuff -- see ticket discussion (this should NOT be included in sage)



---

archive/issue_comments_002319.json:
```json
{
    "body": "Attachment [5835-fpu-status.patch](tarball://root/attachments/some-uuid/ticket468/5835-fpu-status.patch) by bober created at 2007-08-23 18:28:54\n\nThe attachment `5835-fpu-status.patch` provides a module for checking/setting the fpu precision on an x86 processor, which can be useful for debugging problems like this one. Some example usage of this patch:\n\n\n```\nsage: import sage.misc.fpu as fpu\nsage: fpu.get_precision()\n'extended'\nsage: fpu.set_double_precision()\nsage: fpu.get_precision()\n'double'\nsage: fpu.set_single_precision()\nsage: fpu.get_precision()\n'single'\nsage: fpu.set_extended_precision()\nsage: fpu.get_precision()\n'extended'\n```\n\n\nThis patch should NOT be included in sage currently, as it relies on an x86 processor to function, and also just isn't written very nicely in general.",
    "created_at": "2007-08-23T18:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/468#issuecomment-2319",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Attachment [5835-fpu-status.patch](tarball://root/attachments/some-uuid/ticket468/5835-fpu-status.patch) by bober created at 2007-08-23 18:28:54

The attachment `5835-fpu-status.patch` provides a module for checking/setting the fpu precision on an x86 processor, which can be useful for debugging problems like this one. Some example usage of this patch:


```
sage: import sage.misc.fpu as fpu
sage: fpu.get_precision()
'extended'
sage: fpu.set_double_precision()
sage: fpu.get_precision()
'double'
sage: fpu.set_single_precision()
sage: fpu.get_precision()
'single'
sage: fpu.set_extended_precision()
sage: fpu.get_precision()
'extended'
```


This patch should NOT be included in sage currently, as it relies on an x86 processor to function, and also just isn't written very nicely in general.



---

archive/issue_comments_002320.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-08-23T18:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/468#issuecomment-2320",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_events_000497.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-13T06:42:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/468",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/468#event-497"
}
```



---

archive/issue_comments_002321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T06:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/468#issuecomment-2321",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
