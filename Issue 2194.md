# Issue 2194: Elliptic curves over QQbar: point creation fails

archive/issues_002194.json:
```json
{
    "body": "Assignee: was\n\nOn discovering QQbar I tried to define an elliptic curve over it and ran into difficulties creating a point:\n\n\n```\nsage: E=EllipticCurve(QQbar,[0,1])\nsage: E(0)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/jec/sage/<ipython console> in <module>()\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __call__(self, *args, **kwds)\n    435         if len(args) == 1 and args[0] == 0:\n    436             R = self.base_ring()\n--> 437             return self.point([R(0),R(1),R(0)], check=False)\n    438         if isinstance(args[0],\n    439               (ell_point.EllipticCurvePoint_field, ell_point.EllipticCurvePoint)):\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py in point(self, v, check)\n    152\n    153     def point(self, v, check=True):\n--> 154         return self._point_class(self, v, check=check)\n    155\n    156     def _point_class(self):\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in __init__(self, curve, v, check)\n    134     \"\"\"\n    135     def __init__(self, curve, v, check=True):\n--> 136         point_homset = curve.point_homset()\n    137         AdditiveGroupElement.__init__(self, point_homset)\n    138         if check:\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py in point_homset(self, R)\n    139                 return self.__ring_point_homset\n    140             except AttributeError:\n--> 141                 self.__ring_point_homset = self._homset_class(self,self.base_ring())\n    142                 return self.__ring_point_homset\n    143         try:\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in _homset_class(self, *args, **kwds)\n    543\n    544     def _homset_class(self, *args, **kwds):\n--> 545         return homset.SchemeHomsetModule_abelian_variety_coordinates_field(*args, **kwds)\n    546\n    547     def __getitem__(self, n):\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/homset.py in __init__(self, X, S, cat, check)\n    316     def __init__(self, X, S, cat=None, check=True):\n    317         R = X.base_ring()\n--> 318         Y = spec.Spec(S, R)\n    319         HomsetWithBase.__init__(self, Y, X, cat=cat,\n    320                                 check = check,\n\n/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/spec.py in __init__(self, R, S, check)\n     81                 S.hom(R)\n     82             except TypeError:\n---> 83                 raise ValueError, \"There must be a natural map S --> R, but S = %s and R = %s\"%(S,R)\n     84             self._base_ring = S\n     85\n\n<type 'exceptions.ValueError'>: There must be a natural map S --> R, but S = Algebraic Field and R = Algebraic Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2194\n\n",
    "created_at": "2008-02-17T18:21:47Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Elliptic curves over QQbar: point creation fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2194",
    "user": "cremona"
}
```
Assignee: was

On discovering QQbar I tried to define an elliptic curve over it and ran into difficulties creating a point:


```
sage: E=EllipticCurve(QQbar,[0,1])
sage: E(0)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/jec/sage/<ipython console> in <module>()

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __call__(self, *args, **kwds)
    435         if len(args) == 1 and args[0] == 0:
    436             R = self.base_ring()
--> 437             return self.point([R(0),R(1),R(0)], check=False)
    438         if isinstance(args[0],
    439               (ell_point.EllipticCurvePoint_field, ell_point.EllipticCurvePoint)):

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py in point(self, v, check)
    152
    153     def point(self, v, check=True):
--> 154         return self._point_class(self, v, check=check)
    155
    156     def _point_class(self):

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in __init__(self, curve, v, check)
    134     """
    135     def __init__(self, curve, v, check=True):
--> 136         point_homset = curve.point_homset()
    137         AdditiveGroupElement.__init__(self, point_homset)
    138         if check:

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py in point_homset(self, R)
    139                 return self.__ring_point_homset
    140             except AttributeError:
--> 141                 self.__ring_point_homset = self._homset_class(self,self.base_ring())
    142                 return self.__ring_point_homset
    143         try:

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in _homset_class(self, *args, **kwds)
    543
    544     def _homset_class(self, *args, **kwds):
--> 545         return homset.SchemeHomsetModule_abelian_variety_coordinates_field(*args, **kwds)
    546
    547     def __getitem__(self, n):

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/homset.py in __init__(self, X, S, cat, check)
    316     def __init__(self, X, S, cat=None, check=True):
    317         R = X.base_ring()
--> 318         Y = spec.Spec(S, R)
    319         HomsetWithBase.__init__(self, Y, X, cat=cat,
    320                                 check = check,

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/generic/spec.py in __init__(self, R, S, check)
     81                 S.hom(R)
     82             except TypeError:
---> 83                 raise ValueError, "There must be a natural map S --> R, but S = %s and R = %s"%(S,R)
     84             self._base_ring = S
     85

<type 'exceptions.ValueError'>: There must be a natural map S --> R, but S = Algebraic Field and R = Algebraic Field
```


Issue created by migration from https://trac.sagemath.org/ticket/2194





---

archive/issue_comments_014403.json:
```json
{
    "body": "Attachment [trac-2194.patch](tarball://root/attachments/some-uuid/ticket2194/trac-2194.patch) by mabshoff created at 2008-02-17 19:10:54",
    "created_at": "2008-02-17T19:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14403",
    "user": "mabshoff"
}
```

Attachment [trac-2194.patch](tarball://root/attachments/some-uuid/ticket2194/trac-2194.patch) by mabshoff created at 2008-02-17 19:10:54



---

archive/issue_comments_014404.json:
```json
{
    "body": "For some reason I assumed that the coercion model would automatically infer the existence of coercions AA->AA and QQbar->QQbar; it doesn't.\n\nAfter applying the attached patch, John's example becomes:\n\n```\nsage: E=EllipticCurve(QQbar,[0,1])\nsage: E(0)\n(0 : 1 : 0)\n```\n",
    "created_at": "2008-02-17T19:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14404",
    "user": "cwitty"
}
```

For some reason I assumed that the coercion model would automatically infer the existence of coercions AA->AA and QQbar->QQbar; it doesn't.

After applying the attached patch, John's example becomes:

```
sage: E=EllipticCurve(QQbar,[0,1])
sage: E(0)
(0 : 1 : 0)
```




---

archive/issue_comments_014405.json:
```json
{
    "body": "I am happy with this!",
    "created_at": "2008-02-17T20:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14405",
    "user": "cremona"
}
```

I am happy with this!



---

archive/issue_comments_014406.json:
```json
{
    "body": "Shouldn't we also add a doctest, too? I applied the patch and will close if we add a doctest :)",
    "created_at": "2008-02-17T20:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14406",
    "user": "mabshoff"
}
```

Shouldn't we also add a doctest, too? I applied the patch and will close if we add a doctest :)



---

archive/issue_comments_014407.json:
```json
{
    "body": "Attachment [trac-2194-doctest.patch](tarball://root/attachments/some-uuid/ticket2194/trac-2194-doctest.patch) by was created at 2008-02-17 22:33:32",
    "created_at": "2008-02-17T22:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14407",
    "user": "was"
}
```

Attachment [trac-2194-doctest.patch](tarball://root/attachments/some-uuid/ticket2194/trac-2194-doctest.patch) by was created at 2008-02-17 22:33:32



---

archive/issue_comments_014408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T22:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14408",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014409.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T22:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2194#issuecomment-14409",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
