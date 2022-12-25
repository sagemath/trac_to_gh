# Issue 4106: error coercing symbolic variable into polynomial ring modulo 4 (but not mod 3)

archive/issues_004106.json:
```json
{
    "body": "Assignee: tbd\n\nPaul Zimmerman reports that one coercion works, and another natural similar coercion doesn't, as illustrated below:\n\n\n\n```\nx = var('x')\nR = IntegerModRing(3)\nS = PolynomialRing(R, x)\nS(x)\n///\n\nx\n```\n\n\n\n```\nx = var('x')\nR = IntegerModRing(4)\nS = PolynomialRing(R, x)\nS(x)\n///\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/wstein/.sage/sage_notebook/worksheets/admin/1/code/22.py\", line 9, in <module>\n    exec compile(ur'S(x)' + '\\n', '', 'single')\n  File \"/home/wstein/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/home/wstein/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 1097, in __call__\n    return polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz(self, x, check, is_gen, construct=construct)\n  File \"polynomial_modn_dense_ntl.pyx\", line 574, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz.__init__ (sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:7017)\n  File \"polynomial_modn_dense_ntl.pyx\", line 130, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.__init__ (sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:3188)\n  File \"/home/wstein/sage/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py\", line 617, in __call__\n    return integer_mod.IntegerMod(self, x)\n  File \"integer_mod.pyx\", line 132, in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2187)\n  File \"integer_mod.pyx\", line 1430, in sage.rings.integer_mod.IntegerMod_int.__init__ (sage/rings/integer_mod.c:10773)\n  File \"integer_ring.pyx\", line 282, in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:4998)\nTypeError: unable to convert x (=x) to an integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4106\n\n",
    "created_at": "2008-09-12T15:52:42Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "error coercing symbolic variable into polynomial ring modulo 4 (but not mod 3)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4106",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Paul Zimmerman reports that one coercion works, and another natural similar coercion doesn't, as illustrated below:



```
x = var('x')
R = IntegerModRing(3)
S = PolynomialRing(R, x)
S(x)
///

x
```



```
x = var('x')
R = IntegerModRing(4)
S = PolynomialRing(R, x)
S(x)
///

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/wstein/.sage/sage_notebook/worksheets/admin/1/code/22.py", line 9, in <module>
    exec compile(ur'S(x)' + '\n', '', 'single')
  File "/home/wstein/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/home/wstein/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 1097, in __call__
    return polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz(self, x, check, is_gen, construct=construct)
  File "polynomial_modn_dense_ntl.pyx", line 574, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz.__init__ (sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:7017)
  File "polynomial_modn_dense_ntl.pyx", line 130, in sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_n.__init__ (sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:3188)
  File "/home/wstein/sage/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py", line 617, in __call__
    return integer_mod.IntegerMod(self, x)
  File "integer_mod.pyx", line 132, in sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:2187)
  File "integer_mod.pyx", line 1430, in sage.rings.integer_mod.IntegerMod_int.__init__ (sage/rings/integer_mod.c:10773)
  File "integer_ring.pyx", line 282, in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:4998)
TypeError: unable to convert x (=x) to an integer
```


Issue created by migration from https://trac.sagemath.org/ticket/4106





---

archive/issue_comments_029677.json:
```json
{
    "body": "Attachment [trac4106-coerce_symbolic_x_into_poly.patch](tarball://root/attachments/some-uuid/ticket4106/trac4106-coerce_symbolic_x_into_poly.patch) by @aghitza created at 2008-10-04 09:48:35\n\nSee the fairly trivial patch attached.",
    "created_at": "2008-10-04T09:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4106#issuecomment-29677",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac4106-coerce_symbolic_x_into_poly.patch](tarball://root/attachments/some-uuid/ticket4106/trac4106-coerce_symbolic_x_into_poly.patch) by @aghitza created at 2008-10-04 09:48:35

See the fairly trivial patch attached.



---

archive/issue_comments_029678.json:
```json
{
    "body": "Positive review.\n\nI did notice this unfortunate property of the _polynomial_ function that is used\nto implement this patch, namely it does something dumb when given x+y as input:\n\n\n```\nsage: var('x')\nx\nsage: var('y')\ny\nsage: S = PolynomialRing(Integers(4),1,'x')\nsage: S(x+y)\n2*x\nsage: (x+y)._polynomial_(S)\n2*x\n```\n\n\nI think in this case it should raise a TypeError. \n\nThis is my fault, since I implemented _polynomial_... of course.",
    "created_at": "2008-10-05T16:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4106#issuecomment-29678",
    "user": "https://github.com/williamstein"
}
```

Positive review.

I did notice this unfortunate property of the _polynomial_ function that is used
to implement this patch, namely it does something dumb when given x+y as input:


```
sage: var('x')
x
sage: var('y')
y
sage: S = PolynomialRing(Integers(4),1,'x')
sage: S(x+y)
2*x
sage: (x+y)._polynomial_(S)
2*x
```


I think in this case it should raise a TypeError. 

This is my fault, since I implemented _polynomial_... of course.



---

archive/issue_comments_029679.json:
```json
{
    "body": "I've opened a new ticket #4246 addressing the issue reported by William (and put a patch there -- it is independent of this ticket).",
    "created_at": "2008-10-05T21:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4106#issuecomment-29679",
    "user": "https://github.com/aghitza"
}
```

I've opened a new ticket #4246 addressing the issue reported by William (and put a patch there -- it is independent of this ticket).



---

archive/issue_comments_029680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-07T22:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4106#issuecomment-29680",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029681.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-07T22:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4106#issuecomment-29681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_events_004343.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-07T22:12:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4106",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4106#event-4343"
}
```
