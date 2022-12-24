# Issue 3124: bug in solve_mod

archive/issues_003124.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  alexghitza\n\n\n```\nHi,\n\nI think this is a bug. Solving x == y mod 3 works fine:\n\nsage: var('x,y')\n(x, y)\nsage: solve_mod([x == y], 3)\n[(0, 0), (1, 1), (2, 2)]\n\nBut solving mod 2 blows up:\n\n\nsage: solve_mod([x == y], 2)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/carlo/work/sagestuff/<ipython console> in <module>()\n\n/home/carlo/sage/local/lib/python2.5/site-packages/sage/calculus/equations.py\nin solve_mod(eqns, modulus)\n  1339     S = MPolynomialRing(R, len(vars), vars)\n  1340     eqns_mod = [S(eq) if is_SymbolicExpression(eq) else \\\n-> 1341                   S(eq.lhs() - eq.rhs()) for eq in eqns]\n  1342\n  1343     ans = []\n\n/home/carlo/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py\nin __call__(self, x, check)\n   380\n   381         elif hasattr(x, '_polynomial_'):\n--> 382             return x._polynomial_(self)\n   383\n   384         elif isinstance(x, str) and x in self.variable_names():\n\n/home/carlo/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\nin _polynomial_(self, R)\n  1809         if len(sub) == 0:\n  1810             try:\n-> 1811                 return R(B(self))\n  1812             except TypeError:\n  1813                 if len(vars) == 1:\n\n/home/carlo/sage/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py\nin __call__(self, x)\n   574     def __call__(self, x):\n   575         try:\n--> 576             return integer_mod.IntegerMod(self, x)\n   577         except (NotImplementedError, PariError):\n   578             return TypeError, \"error coercing to finite field\"\n\n/home/carlo/work/sagestuff/integer_mod.pyx in\nsage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:1731)()\n\n/home/carlo/work/sagestuff/integer_mod.pyx in\nsage.rings.integer_mod.IntegerMod_int.__init__\n(sage/rings/integer_mod.c:10153)()\n\n/home/carlo/work/sagestuff/integer_ring.pyx in\nsage.rings.integer_ring.IntegerRing_class.__call__\n(sage/rings/integer_ring.c:4473)()\n\n<type 'exceptions.TypeError'>: unable to convert x (=x - y) to an integer\n\n\n\nAny ideas?\n\n--\nCarlo Hamalainen\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3124\n\n",
    "created_at": "2008-05-07T15:43:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in solve_mod",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3124",
    "user": "was"
}
```
Assignee: somebody

CC:  alexghitza


```
Hi,

I think this is a bug. Solving x == y mod 3 works fine:

sage: var('x,y')
(x, y)
sage: solve_mod([x == y], 3)
[(0, 0), (1, 1), (2, 2)]

But solving mod 2 blows up:


sage: solve_mod([x == y], 2)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/carlo/work/sagestuff/<ipython console> in <module>()

/home/carlo/sage/local/lib/python2.5/site-packages/sage/calculus/equations.py
in solve_mod(eqns, modulus)
  1339     S = MPolynomialRing(R, len(vars), vars)
  1340     eqns_mod = [S(eq) if is_SymbolicExpression(eq) else \
-> 1341                   S(eq.lhs() - eq.rhs()) for eq in eqns]
  1342
  1343     ans = []

/home/carlo/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py
in __call__(self, x, check)
   380
   381         elif hasattr(x, '_polynomial_'):
--> 382             return x._polynomial_(self)
   383
   384         elif isinstance(x, str) and x in self.variable_names():

/home/carlo/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py
in _polynomial_(self, R)
  1809         if len(sub) == 0:
  1810             try:
-> 1811                 return R(B(self))
  1812             except TypeError:
  1813                 if len(vars) == 1:

/home/carlo/sage/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py
in __call__(self, x)
   574     def __call__(self, x):
   575         try:
--> 576             return integer_mod.IntegerMod(self, x)
   577         except (NotImplementedError, PariError):
   578             return TypeError, "error coercing to finite field"

/home/carlo/work/sagestuff/integer_mod.pyx in
sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:1731)()

/home/carlo/work/sagestuff/integer_mod.pyx in
sage.rings.integer_mod.IntegerMod_int.__init__
(sage/rings/integer_mod.c:10153)()

/home/carlo/work/sagestuff/integer_ring.pyx in
sage.rings.integer_ring.IntegerRing_class.__call__
(sage/rings/integer_ring.c:4473)()

<type 'exceptions.TypeError'>: unable to convert x (=x - y) to an integer



Any ideas?

--
Carlo Hamalainen
```


Issue created by migration from https://trac.sagemath.org/ticket/3124





---

archive/issue_comments_021647.json:
```json
{
    "body": "The underlying issue is that the reprs of the generators of polynomial rings over Z/2Z have minus signs and SymbolicArithmetic._polynomial_ expects them to not have the signs.  I think the appropriate fix would be to fix the printing for the generators of polynomial rings over Z/2Z\n\n\n```\nsage: Integers(3)['x,y'].gens()\n(x, y)\nsage: Integers(2)['x,y'].gens()\n(-x, -y)\n```\n\n\n\n\n```\n        for v in vars:\n            r = repr(v)\n            for g in G:\n                if repr(g) == r:\n                    sub.append((v,g))\n```\n",
    "created_at": "2008-05-08T04:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21647",
    "user": "mhansen"
}
```

The underlying issue is that the reprs of the generators of polynomial rings over Z/2Z have minus signs and SymbolicArithmetic._polynomial_ expects them to not have the signs.  I think the appropriate fix would be to fix the printing for the generators of polynomial rings over Z/2Z


```
sage: Integers(3)['x,y'].gens()
(x, y)
sage: Integers(2)['x,y'].gens()
(-x, -y)
```




```
        for v in vars:
            r = repr(v)
            for g in G:
                if repr(g) == r:
                    sub.append((v,g))
```




---

archive/issue_comments_021648.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-21T21:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21648",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021649.json:
```json
{
    "body": "This patch also fixes #3125.",
    "created_at": "2009-01-21T21:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21649",
    "user": "mhansen"
}
```

This patch also fixes #3125.



---

archive/issue_comments_021650.json:
```json
{
    "body": "Changing assignee from somebody to mhansen.",
    "created_at": "2009-01-21T21:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21650",
    "user": "mhansen"
}
```

Changing assignee from somebody to mhansen.



---

archive/issue_comments_021651.json:
```json
{
    "body": "Attachment [trac_3124.patch](tarball://root/attachments/some-uuid/ticket3124/trac_3124.patch) by mhansen created at 2009-01-21 21:04:01\n\nAnd by #3125, I mean #3135.",
    "created_at": "2009-01-21T21:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21651",
    "user": "mhansen"
}
```

Attachment [trac_3124.patch](tarball://root/attachments/some-uuid/ticket3124/trac_3124.patch) by mhansen created at 2009-01-21 21:04:01

And by #3125, I mean #3135.



---

archive/issue_comments_021652.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-21T23:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21652",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_021653.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21653",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021654.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3124#issuecomment-21654",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
