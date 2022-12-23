# Issue 4517: magma <--> sage (3.2) conversion failure case -- nested multivariate polynomials

Issue created by migration from https://trac.sagemath.org/ticket/4517

Original creator: was

Original creation time: 2008-11-13 23:13:05

Assignee: was

Converted a nested multivariate polynomial to Magma fails miserably:


```
was@sage:~/build/sage-3.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<x,y> = QQ[]; S.<z,w> = R[]; magma(x+z)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1510, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/was/build/sage-3.2.rc0/<ipython console> in <module>()

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)
    507             if isinstance(x, bool):
    508                 return Expect.__call__(self, str(x).lower())
--> 509             return Expect.__call__(self, x)
    510         return self.objgens(x, gens)
    511         

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
    965             return cls(self, x, name=name)
    966         try:
--> 967             return self._coerce_from_special_method(x)
    968         except TypeError:
    969             raise

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)
    989             s = '_gp_'
    990         try:
--> 991             return (x.__getattribute__(s))(self)
    992         except AttributeError:
    993             return self(x._interface_init_())

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._magma_ (sage/structure/sage_object.c:3696)()

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._magma_convert_ (sage/structure/sage_object.c:3826)()

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2383)()

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)
    507             if isinstance(x, bool):
    508                 return Expect.__call__(self, str(x).lower())
--> 509             return Expect.__call__(self, x)
    510         return self.objgens(x, gens)
    511         

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
    963             return x
    964         if isinstance(x, basestring):
--> 965             return cls(self, x, name=name)
    966         try:
    967             return self._coerce_from_special_method(x)

/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1291             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1292                 self._session_number = -1
-> 1293                 raise TypeError, x
   1294         self._session_number = parent._session_number
   1295 

TypeError: Error evaluating Magma code.
IN:_sage_[10] := _sage_[7] + x;
OUT:
>> _sage_[10] := _sage_[7] + x;
                             ^
User error: Identifier 'x' has not been declared or assigned
```



---

Comment by was created at 2008-12-11 05:00:09

This is actually now fixed in sage-3.2.2.alpha1...


---

Comment by was created at 2008-12-11 05:00:09

Resolution: fixed
