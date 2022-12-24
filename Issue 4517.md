# Issue 4517: magma <--> sage (3.2) conversion failure case -- nested multivariate polynomials

archive/issues_004517.json:
```json
{
    "body": "Assignee: @williamstein\n\nConverted a nested multivariate polynomial to Magma fails miserably:\n\n\n```\nwas@sage:~/build/sage-3.2.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2.rc0, Release Date: 2008-11-10                     |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R.<x,y> = QQ[]; S.<z,w> = R[]; magma(x+z)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1510, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/was/build/sage-3.2.rc0/<ipython console> in <module>()\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)\n    507             if isinstance(x, bool):\n    508                 return Expect.__call__(self, str(x).lower())\n--> 509             return Expect.__call__(self, x)\n    510         return self.objgens(x, gens)\n    511         \n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n    965             return cls(self, x, name=name)\n    966         try:\n--> 967             return self._coerce_from_special_method(x)\n    968         except TypeError:\n    969             raise\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)\n    989             s = '_gp_'\n    990         try:\n--> 991             return (x.__getattribute__(s))(self)\n    992         except AttributeError:\n    993             return self(x._interface_init_())\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._magma_ (sage/structure/sage_object.c:3696)()\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._magma_convert_ (sage/structure/sage_object.c:3826)()\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2383)()\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)\n    507             if isinstance(x, bool):\n    508                 return Expect.__call__(self, str(x).lower())\n--> 509             return Expect.__call__(self, x)\n    510         return self.objgens(x, gens)\n    511         \n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n    963             return x\n    964         if isinstance(x, basestring):\n--> 965             return cls(self, x, name=name)\n    966         try:\n    967             return self._coerce_from_special_method(x)\n\n/home/was/build/sage-3.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1291             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1292                 self._session_number = -1\n-> 1293                 raise TypeError, x\n   1294         self._session_number = parent._session_number\n   1295 \n\nTypeError: Error evaluating Magma code.\nIN:_sage_[10] := _sage_[7] + x;\nOUT:\n>> _sage_[10] := _sage_[7] + x;\n                             ^\nUser error: Identifier 'x' has not been declared or assigned\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4517\n\n",
    "created_at": "2008-11-13T23:13:05Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "magma <--> sage (3.2) conversion failure case -- nested multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4517",
    "user": "@williamstein"
}
```
Assignee: @williamstein

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


Issue created by migration from https://trac.sagemath.org/ticket/4517





---

archive/issue_comments_033527.json:
```json
{
    "body": "This is actually now fixed in sage-3.2.2.alpha1...",
    "created_at": "2008-12-11T05:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4517#issuecomment-33527",
    "user": "@williamstein"
}
```

This is actually now fixed in sage-3.2.2.alpha1...



---

archive/issue_comments_033528.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T05:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4517#issuecomment-33528",
    "user": "@williamstein"
}
```

Resolution: fixed
