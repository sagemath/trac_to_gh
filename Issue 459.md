# Issue 459: TypeError: unsupported operand parent(s) for '*': 'Polynomial Ring in u, v over Integer Ring'

archive/issues_000459.json:
```json
{
    "body": "Assignee: somebody\n\n\nHere we go:\n\n**********************************************************************\nFile \"constructor.py\", line 82:\n   sage: EllipticCurve(R, [1,1])\nException raised:\n   Traceback (most recent call last):\n     File \"/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/\ndoctest.py\", line 1212, in __run\n       compileflags, 1) in test.globs\n     File \"<doctest __main__.example_1[10]>\", line 1, in <module>\n       EllipticCurve(R, [Integer(1),Integer(1)])###line 82:\n   sage: EllipticCurve(R, [1,1])\n     File \"/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-\npackages/sage/schemes/elliptic_curves/constructor.py\", line 112, in\nEllipticCurve\n       return ell_generic.EllipticCurve_generic(x, y)\n     File \"/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-\npackages/sage/schemes/elliptic_curves/ell_generic.py\", line 98, in\n__init__\n- (x**3 + a2*x**2*z + a4*x*z**2 + a6*z**3)\n     File \"element.pyx\", line 1365, in element.RingElement.__mul__\n     File \"coerce.pyx\", line 219, in\ncoerce.CoercionModel_cache_maps.bin_op_c\n   TypeError: unsupported operand parent(s) for '*': 'Polynomial Ring\nin u, v over Integer Ring' and 'Polynomial Ring in x, y, z over\nPolynomial Ring in u, v over Integer Ring'\n**********************************************************************\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/459\n\n",
    "created_at": "2007-08-19T14:26:12Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "TypeError: unsupported operand parent(s) for '*': 'Polynomial Ring in u, v over Integer Ring'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/459",
    "user": "mhansen"
}
```
Assignee: somebody


Here we go:

**********************************************************************
File "constructor.py", line 82:
   sage: EllipticCurve(R, [1,1])
Exception raised:
   Traceback (most recent call last):
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/
doctest.py", line 1212, in __run
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[10]>", line 1, in <module>
       EllipticCurve(R, [Integer(1),Integer(1)])###line 82:
   sage: EllipticCurve(R, [1,1])
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/schemes/elliptic_curves/constructor.py", line 112, in
EllipticCurve
       return ell_generic.EllipticCurve_generic(x, y)
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/schemes/elliptic_curves/ell_generic.py", line 98, in
__init__
- (x**3 + a2*x**2*z + a4*x*z**2 + a6*z**3)
     File "element.pyx", line 1365, in element.RingElement.__mul__
     File "coerce.pyx", line 219, in
coerce.CoercionModel_cache_maps.bin_op_c
   TypeError: unsupported operand parent(s) for '*': 'Polynomial Ring
in u, v over Integer Ring' and 'Polynomial Ring in x, y, z over
Polynomial Ring in u, v over Integer Ring'
**********************************************************************

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/459





---

archive/issue_comments_002288.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T18:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/459#issuecomment-2288",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002289.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-08-19T18:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/459#issuecomment-2289",
    "user": "was"
}
```

Attachment
