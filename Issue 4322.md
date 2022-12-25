# Issue 4322: modular polynomials database is broken

archive/issues_004322.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @robertwb\n\nKeywords: modular polynomial database\n\nIn 3.1.4, install this optional spkg with\n\n\n```\nsage -i database_kohel-20060803\n```\n\n\nthen \n\n\n```\nsage: DBMP = ClassicalModularPolynomialDatabase()\nsage: DBMP[29]\n<string>:1: Warning: 'with' will become a reserved keyword in Python 2.6\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1683, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-3.1.4/devel/sage-main/sage/structure/<ipython console> in <module>()\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/databases/db_modular_polynomials.pyc in __getitem__(self, level)\n     93             for cff in coeff_list:\n     94                 poly[(cff[0],cff[1])] = Integer(cff[2])\n---> 95         return P(polydict.PolyDict(poly))\n     96 \n     97 class ModularCorrespondenceDatabase(ModularPolynomialDatabase):\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:6996)()\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3732)()\n    303                         del self._convert_from_list[i]\n    304                         break\n--> 305                 raise\n    306             \n    307         raise TypeError, \"No conversion defined from %s to %s\"%(R, self)\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.__call__ (sage/structure/parent.c:3619)()\n    294             try:\n    295                 if no_extra_args:\n--> 296                     return mor._call_(x)\n    297                 else:\n    298                     return mor._call_with_args(x, args, kwds)\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2622)()\n     74                 print type(self._codomain), self._codomain\n     75                 print type(self._codomain._element_constructor), self._codomain._element_constructor\n---> 76             raise\n     77 \n     78     cpdef Element _call_with_args(self, x, args=(), kwds={}):\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2537)()\n     69     cpdef Element _call_(self, x):\n     70         try:\n---> 71             return self._codomain._element_constructor(x)\n     72         except:\n     73             if print_warnings:\n\n/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5688)()\n\nTypeError: unable to coerce <type 'sage.rings.polynomial.polydict.PolyDict'> to an integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4322\n\n",
    "created_at": "2008-10-18T21:43:44Z",
    "labels": [
        "component: optional packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "modular polynomials database is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4322",
    "user": "https://github.com/aghitza"
}
```
Assignee: mabshoff

CC:  @robertwb

Keywords: modular polynomial database

In 3.1.4, install this optional spkg with


```
sage -i database_kohel-20060803
```


then 


```
sage: DBMP = ClassicalModularPolynomialDatabase()
sage: DBMP[29]
<string>:1: Warning: 'with' will become a reserved keyword in Python 2.6
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1683, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-3.1.4/devel/sage-main/sage/structure/<ipython console> in <module>()

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/databases/db_modular_polynomials.pyc in __getitem__(self, level)
     93             for cff in coeff_list:
     94                 poly[(cff[0],cff[1])] = Integer(cff[2])
---> 95         return P(polydict.PolyDict(poly))
     96 
     97 class ModularCorrespondenceDatabase(ModularPolynomialDatabase):

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:6996)()

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3732)()
    303                         del self._convert_from_list[i]
    304                         break
--> 305                 raise
    306             
    307         raise TypeError, "No conversion defined from %s to %s"%(R, self)

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.__call__ (sage/structure/parent.c:3619)()
    294             try:
    295                 if no_extra_args:
--> 296                     return mor._call_(x)
    297                 else:
    298                     return mor._call_with_args(x, args, kwds)

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2622)()
     74                 print type(self._codomain), self._codomain
     75                 print type(self._codomain._element_constructor), self._codomain._element_constructor
---> 76             raise
     77 
     78     cpdef Element _call_with_args(self, x, args=(), kwds={}):

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2537)()
     69     cpdef Element _call_(self, x):
     70         try:
---> 71             return self._codomain._element_constructor(x)
     72         except:
     73             if print_warnings:

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5688)()

TypeError: unable to coerce <type 'sage.rings.polynomial.polydict.PolyDict'> to an integer
```


Issue created by migration from https://trac.sagemath.org/ticket/4322





---

archive/issue_comments_031601.json:
```json
{
    "body": "Somewhere between sage-3.0.2 and sage-3.1.4 this broke:\n\nsage: P.<X,Y> = PolynomialRing(ZZ,2)\nsage: P(sage.rings.polynomial.polydict.PolyDict({(1,0):1,(0,1):-1}))\nX - Y\n\nThis looks like a problem with a change to the new coercion model; \nI will temporarily reassign to mabshoff.  Perhaps I am using access \nto the internal datastructure which has changed and/or not meant \nto be accessible. In that case he can send it back to me.",
    "created_at": "2008-10-20T22:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31601",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```

Somewhere between sage-3.0.2 and sage-3.1.4 this broke:

sage: P.<X,Y> = PolynomialRing(ZZ,2)
sage: P(sage.rings.polynomial.polydict.PolyDict({(1,0):1,(0,1):-1}))
X - Y

This looks like a problem with a change to the new coercion model; 
I will temporarily reassign to mabshoff.  Perhaps I am using access 
to the internal datastructure which has changed and/or not meant 
to be accessible. In that case he can send it back to me.



---

archive/issue_comments_031602.json:
```json
{
    "body": "Changing assignee from mabshoff to @robertwb.",
    "created_at": "2008-10-20T22:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @robertwb.



---

archive/issue_comments_031603.json:
```json
{
    "body": "Changing component from optional packages to coercion.",
    "created_at": "2008-10-20T22:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from optional packages to coercion.



---

archive/issue_comments_031604.json:
```json
{
    "body": "RobertWB is the man here :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-20T22:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

RobertWB is the man here :)

Cheers,

Michael



---

archive/issue_comments_031605.json:
```json
{
    "body": "Changing component from coercion to optional packages.",
    "created_at": "2008-10-21T19:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31605",
    "user": "https://github.com/robertwb"
}
```

Changing component from coercion to optional packages.



---

archive/issue_comments_031606.json:
```json
{
    "body": "Changing assignee from @robertwb to mabshoff.",
    "created_at": "2008-10-21T19:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31606",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @robertwb to mabshoff.



---

archive/issue_comments_031607.json:
```json
{
    "body": "Actually, it looks like it's due to #4021, MPolynomial_libsingular over ZZ. It still works in the generic case: \n\n\n```\nsage: P.<x,y> = ZZ['t']['x,y']\nsage: a = sage.rings.polynomial.polydict.PolyDict({(1,0):1,(0,1):-1})\nsage: P(a)\nx - y\n```\n\n\nDespite the fact that polydicts are no longer used, I can't think of any reason why one would need this construction. More efficient (and less prone to breakage in the future is) direct construction from a dict. \n\n\n```\nsage: P.<x,y> = ZZ[]\nsage: P({(1,0):1,(0,1):-1})\nx - y\n```\n",
    "created_at": "2008-10-21T19:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31607",
    "user": "https://github.com/robertwb"
}
```

Actually, it looks like it's due to #4021, MPolynomial_libsingular over ZZ. It still works in the generic case: 


```
sage: P.<x,y> = ZZ['t']['x,y']
sage: a = sage.rings.polynomial.polydict.PolyDict({(1,0):1,(0,1):-1})
sage: P(a)
x - y
```


Despite the fact that polydicts are no longer used, I can't think of any reason why one would need this construction. More efficient (and less prone to breakage in the future is) direct construction from a dict. 


```
sage: P.<x,y> = ZZ[]
sage: P({(1,0):1,(0,1):-1})
x - y
```




---

archive/issue_comments_031608.json:
```json
{
    "body": "Attachment [trac_4322.patch](tarball://root/attachments/some-uuid/ticket4322/trac_4322.patch) by @aghitza created at 2009-01-23 18:40:41\n\nThe attached patch removes the uses of polydict.",
    "created_at": "2009-01-23T18:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31608",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4322.patch](tarball://root/attachments/some-uuid/ticket4322/trac_4322.patch) by @aghitza created at 2009-01-23 18:40:41

The attached patch removes the uses of polydict.



---

archive/issue_events_004567.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-25T02:20:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4322#event-4567"
}
```



---

archive/issue_comments_031609.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T02:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_031610.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T02:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4322#issuecomment-31610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
