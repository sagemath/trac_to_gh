# Issue 4687: Points on  Elliptic Curve over GF(2)

archive/issues_004687.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  cremona\n\n\n```\n\nsage: E=EllipticCurve(GF(2),[0, 0, 1, 1, 1])\nsage: E\nElliptic Curve defined by y^2 + y = x^3 + x +1 over Finite Field of size 2\nsage: E.points()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/Volumes/Panther/sage/<ipython console> in <module>()\n\n/Volumes/Panther/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.pyc in points(self)\n    214         from sage.structure.sequence import Sequence\n    215         if self.base_ring().is_prime_field():\n--> 216             v = self._points_via_group_structure()\n    217         else:\n    218             v =self._points_fast_sqrt()\n\n/Volumes/Panther/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.pyc in _points_via_group_structure(self)\n    165 \n    166         H0=[self(0)]\n--> 167         for m in range(1,ni[0]): H0.append(H0[-1]+pts[0])\n    168         if len(ni)==1:   # cyclic case\n    169             return H0\n\nIndexError: list index out of range\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4687\n\n",
    "created_at": "2008-12-03T18:00:27Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Points on  Elliptic Curve over GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4687",
    "user": "rishi"
}
```
Assignee: tbd

CC:  cremona


```

sage: E=EllipticCurve(GF(2),[0, 0, 1, 1, 1])
sage: E
Elliptic Curve defined by y^2 + y = x^3 + x +1 over Finite Field of size 2
sage: E.points()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Volumes/Panther/sage/<ipython console> in <module>()

/Volumes/Panther/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.pyc in points(self)
    214         from sage.structure.sequence import Sequence
    215         if self.base_ring().is_prime_field():
--> 216             v = self._points_via_group_structure()
    217         else:
    218             v =self._points_fast_sqrt()

/Volumes/Panther/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.pyc in _points_via_group_structure(self)
    165 
    166         H0=[self(0)]
--> 167         for m in range(1,ni[0]): H0.append(H0[-1]+pts[0])
    168         if len(ni)==1:   # cyclic case
    169             return H0

IndexError: list index out of range

```


Issue created by migration from https://trac.sagemath.org/ticket/4687





---

archive/issue_comments_035328.json:
```json
{
    "body": "I guess the category number theory might be more appropriate. Also CCing John just in case he might be interested in this ticket and not aware of its existence.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T14:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35328",
    "user": "mabshoff"
}
```

I guess the category number theory might be more appropriate. Also CCing John just in case he might be interested in this ticket and not aware of its existence.

Cheers,

Michael



---

archive/issue_comments_035329.json:
```json
{
    "body": "Changing component from algebra to number theory.",
    "created_at": "2008-12-04T14:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35329",
    "user": "mabshoff"
}
```

Changing component from algebra to number theory.



---

archive/issue_comments_035330.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2008-12-04T14:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35330",
    "user": "mabshoff"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_035331.json:
```json
{
    "body": "Attachment [sage-trac-4687.patch](tarball://root/attachments/some-uuid/ticket4687/sage-trac-4687.patch) by cremona created at 2008-12-04 14:32:04",
    "created_at": "2008-12-04T14:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35331",
    "user": "cremona"
}
```

Attachment [sage-trac-4687.patch](tarball://root/attachments/some-uuid/ticket4687/sage-trac-4687.patch) by cremona created at 2008-12-04 14:32:04



---

archive/issue_comments_035332.json:
```json
{
    "body": "Thanks for the bug report:  the code did not handle the case of a trivial group properly!  Your curve is essentially the only example of that (and did appear in a doctest elsewhere).\n\nThe attached patch fixes this, adding doctests to show that all three cases (#gens=0,1,2) can be handled.  It is based on 3.2.1.",
    "created_at": "2008-12-04T14:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35332",
    "user": "cremona"
}
```

Thanks for the bug report:  the code did not handle the case of a trivial group properly!  Your curve is essentially the only example of that (and did appear in a doctest elsewhere).

The attached patch fixes this, adding doctests to show that all three cases (#gens=0,1,2) can be handled.  It is based on 3.2.1.



---

archive/issue_comments_035333.json:
```json
{
    "body": "Works good.",
    "created_at": "2008-12-04T17:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35333",
    "user": "rishi"
}
```

Works good.



---

archive/issue_comments_035334.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T18:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35334",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_035335.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T18:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4687#issuecomment-35335",
    "user": "mabshoff"
}
```

Resolution: fixed
