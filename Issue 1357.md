# Issue 1357: the polynomial .roots() method should work with ring=QQbar

archive/issues_001357.json:
```json
{
    "body": "Assignee: cwitty\n\nSomething like this should work:\n\n```\nsage: x = polygen(ZZ)\nsage: (x^2 + x + 1).roots(ring=QQbar)\n```\n\nbut currently it doesn't.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1357\n\n",
    "created_at": "2007-12-02T01:28:37Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "the polynomial .roots() method should work with ring=QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1357",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

Something like this should work:

```
sage: x = polygen(ZZ)
sage: (x^2 + x + 1).roots(ring=QQbar)
```

but currently it doesn't.

Issue created by migration from https://trac.sagemath.org/ticket/1357





---

archive/issue_comments_008653.json:
```json
{
    "body": "Attachment [1357.patch](tarball://root/attachments/some-uuid/ticket1357/1357.patch) by cwitty created at 2007-12-02 05:21:13",
    "created_at": "2007-12-02T05:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1357#issuecomment-8653",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1357.patch](tarball://root/attachments/some-uuid/ticket1357/1357.patch) by cwitty created at 2007-12-02 05:21:13



---

archive/issue_comments_008654.json:
```json
{
    "body": "Before:\n\n```\nsage: from sage.rings.polynomial.complex_roots import complex_roots\nsage: E = EllipticCurve('389a')\nsage: f = E.division_polynomial(3)\nsage: interval_roots = f.roots(ring=CIF)\nsage: x_coords = [QQbar.polynomial_root(f, x_interval[0]) for x_interval in interval_roots]\nsage: f = E.defining_polynomial()\nsage: y = polygen(QQbar,'y')\nsage: points = []\nsage: for x in x_coords:\n...       g = f(x,y,1)\n...       rootsg = complex_roots(g, min_prec=53)\n...       for root in rootsg:\n...           y_coord = root[0]\n...           yy = QQbar.polynomial_root(g, y_coord)\n...           points.append([x, yy])\n```\n\nAfter:\n\n```\nsage: E = EllipticCurve('389a')\nsage: f = E.division_polynomial(3)\nsage: x_coords = f.roots(ring=QQbar)\nsage: g = E.defining_polynomial()\nsage: y = polygen(QQbar, 'y')\nsage: points = []\nsage: for x in x_coords:\n...    h = g(x[0],y,1)\n...    rootsh = h.roots(ring=QQbar)\n...    for root in rootsh:\n...        points.append([x[0], root[0]])\n```\n",
    "created_at": "2007-12-02T19:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1357#issuecomment-8654",
    "user": "https://github.com/rlmill"
}
```

Before:

```
sage: from sage.rings.polynomial.complex_roots import complex_roots
sage: E = EllipticCurve('389a')
sage: f = E.division_polynomial(3)
sage: interval_roots = f.roots(ring=CIF)
sage: x_coords = [QQbar.polynomial_root(f, x_interval[0]) for x_interval in interval_roots]
sage: f = E.defining_polynomial()
sage: y = polygen(QQbar,'y')
sage: points = []
sage: for x in x_coords:
...       g = f(x,y,1)
...       rootsg = complex_roots(g, min_prec=53)
...       for root in rootsg:
...           y_coord = root[0]
...           yy = QQbar.polynomial_root(g, y_coord)
...           points.append([x, yy])
```

After:

```
sage: E = EllipticCurve('389a')
sage: f = E.division_polynomial(3)
sage: x_coords = f.roots(ring=QQbar)
sage: g = E.defining_polynomial()
sage: y = polygen(QQbar, 'y')
sage: points = []
sage: for x in x_coords:
...    h = g(x[0],y,1)
...    rootsh = h.roots(ring=QQbar)
...    for root in rootsh:
...        points.append([x[0], root[0]])
```




---

archive/issue_events_003504.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T20:11:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1357",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1357#event-3504"
}
```



---

archive/issue_comments_008655.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T20:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1357#issuecomment-8655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T20:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1357#issuecomment-8656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
