# Issue 5247: cuspform_lseries() computing sign of functional equation incorrectly

archive/issues_005247.json:
```json
{
    "body": "Assignee: @craigcitro\n\nSal reports: The following computation should produce identical values in the last line:\n\n```\nE=EllipticCurve('37b2')\nh=E.modular_form()\nLh = h.cuspform_lseries()\nLE=E.lseries()\nh.elliptic_curve()==E, Lh(1), LE(1)\n```\n\nThe output is:\n\n```\n(True, 0, 0.725681061936153)\n```\n\nI'm running Sage 3.3.alpha3 of sage.math.\n\nThe problem seems to be the sign of the functional equation -- it looks like the cuspform_lseries() incorrectly computes it to be -1, forcing the value at s=1 to be 0. In sage/modular/modform/element.py the sign of the functional equation fed into the Dokchister is computed by\n\n```\ne = (-1)**(l/2)*n.atkin_lehner_operator().matrix()[0,0]\n```\n\nwhich Gonzalo and Mark tell me is not correct.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5247\n\n",
    "created_at": "2009-02-12T16:43:56Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cuspform_lseries() computing sign of functional equation incorrectly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

Sal reports: The following computation should produce identical values in the last line:

```
E=EllipticCurve('37b2')
h=E.modular_form()
Lh = h.cuspform_lseries()
LE=E.lseries()
h.elliptic_curve()==E, Lh(1), LE(1)
```

The output is:

```
(True, 0, 0.725681061936153)
```

I'm running Sage 3.3.alpha3 of sage.math.

The problem seems to be the sign of the functional equation -- it looks like the cuspform_lseries() incorrectly computes it to be -1, forcing the value at s=1 to be 0. In sage/modular/modform/element.py the sign of the functional equation fed into the Dokchister is computed by

```
e = (-1)**(l/2)*n.atkin_lehner_operator().matrix()[0,0]
```

which Gonzalo and Mark tell me is not correct.

Issue created by migration from https://trac.sagemath.org/ticket/5247





---

archive/issue_comments_040143.json:
```json
{
    "body": "This is a dupe of #5262. William did open the other ticket later, but since #5262 has the better description I am closing this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5247#issuecomment-40143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe of #5262. William did open the other ticket later, but since #5262 has the better description I am closing this ticket.

Cheers,

Michael



---

archive/issue_comments_040144.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-02-14T02:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5247#issuecomment-40144",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate
