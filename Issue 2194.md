# Issue 2194: Elliptic curves over QQbar: point creation fails

Issue created by migration from https://trac.sagemath.org/ticket/2194

Original creator: cremona

Original creation time: 2008-02-17 18:21:47

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



---

Attachment


---

Comment by cwitty created at 2008-02-17 19:14:50

For some reason I assumed that the coercion model would automatically infer the existence of coercions AA->AA and QQbar->QQbar; it doesn't.

After applying the attached patch, John's example becomes:

```
sage: E=EllipticCurve(QQbar,[0,1])
sage: E(0)
(0 : 1 : 0)
```



---

Comment by cremona created at 2008-02-17 20:13:19

I am happy with this!


---

Comment by mabshoff created at 2008-02-17 20:19:13

Shouldn't we also add a doctest, too? I applied the patch and will close if we add a doctest :)


---

Attachment


---

Comment by mabshoff created at 2008-02-17 22:37:50

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 22:37:50

Merged in Sage 2.10.2.alpha1
