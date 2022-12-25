# Issue 5639: minpoly of symbolic matrices is broken

archive/issues_005639.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\n\n```\nsage: m = matrix(2,[1,sqrt(2), 3, -5/2])\nsage: m.minpoly()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5639\n\n",
    "created_at": "2009-03-30T03:03:04Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "minpoly of symbolic matrices is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5639",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin

CC:  @kcrisman


```
sage: m = matrix(2,[1,sqrt(2), 3, -5/2])
sage: m.minpoly()
```


Issue created by migration from https://trac.sagemath.org/ticket/5639





---

archive/issue_comments_043944.json:
```json
{
    "body": "This is because the charpoly method needs to return a univariate polynomial rather than an Expression.",
    "created_at": "2009-06-05T02:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43944",
    "user": "https://github.com/mwhansen"
}
```

This is because the charpoly method needs to return a univariate polynomial rather than an Expression.



---

archive/issue_comments_043945.json:
```json
{
    "body": "Changing keywords from \"\" to \"\".",
    "created_at": "2009-06-05T02:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43945",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "" to "".



---

archive/issue_comments_043946.json:
```json
{
    "body": "Changing assignee from @burcin to @mwhansen.",
    "created_at": "2009-09-30T07:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43946",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @burcin to @mwhansen.



---

archive/issue_comments_043947.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-30T07:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43947",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043948.json:
```json
{
    "body": "in the docstring, \"polynomial\" is misspelled \"polynomail\"",
    "created_at": "2009-10-06T21:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43948",
    "user": "https://github.com/jasongrout"
}
```

in the docstring, "polynomial" is misspelled "polynomail"



---

archive/issue_comments_043949.json:
```json
{
    "body": "Consider applying #6936, which also implements a generic way to test this fix!",
    "created_at": "2009-10-06T21:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43949",
    "user": "https://github.com/jasongrout"
}
```

Consider applying #6936, which also implements a generic way to test this fix!



---

archive/issue_comments_043950.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-06T21:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43950",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_043951.json:
```json
{
    "body": "I think this patch broke charpoly.  See the doctest around line 280 of matrix_symbolic_dense.pyx:\n\n\n```\nsage: M = matrix(SR, 2, 2, var('a,b,c,d'))\nsage: M.charpoly('t')\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (288, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/.sage/temp/sage.math.washington.edu/17572/_home_jason__sage_init_sage_0.py in <module>()\n\n/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix_symbolic_dense.so in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.charpoly (sage/matrix/matrix_symbolic_dense.c:2620)()\n    289         # correct for the discrepancy.\n    290         cp = self._maxima_(maxima).charpoly(var)._sage_()\n--> 291         cp = cp.expand().polynomial(None, ring=SR[var])\n    292         if self.nrows() % 2 == 1:\n    293             cp = -cp\n\n/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17292)()\n\n/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in polynomial(ex, base_ring, ring)\n    985          1.87813065119873*x^2 + 20.0855369231877\n    986     \"\"\"\n--> 987     converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)\n    988     res = converter()\n    989     return converter.ring(res)\n\n/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __init__(self, ex, base_ring, ring)\n    843             G = ring.variable_names_recursive()\n    844             if any([repr(v) not in G for v in ex.variables()]):\n--> 845                 raise TypeError, \"%s is not a variable of %s\" %(v, ring)\n    846             self.ring = ring\n    847             self.base_ring = ring.base_ring()\n\nTypeError: t is not a variable of Univariate Polynomial Ring in t over Symbolic Ring\n```\n",
    "created_at": "2009-10-06T21:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43951",
    "user": "https://github.com/jasongrout"
}
```

I think this patch broke charpoly.  See the doctest around line 280 of matrix_symbolic_dense.pyx:


```
sage: M = matrix(SR, 2, 2, var('a,b,c,d'))
sage: M.charpoly('t')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (288, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/.sage/temp/sage.math.washington.edu/17572/_home_jason__sage_init_sage_0.py in <module>()

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/matrix/matrix_symbolic_dense.so in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.charpoly (sage/matrix/matrix_symbolic_dense.c:2620)()
    289         # correct for the discrepancy.
    290         cp = self._maxima_(maxima).charpoly(var)._sage_()
--> 291         cp = cp.expand().polynomial(None, ring=SR[var])
    292         if self.nrows() % 2 == 1:
    293             cp = -cp

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17292)()

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in polynomial(ex, base_ring, ring)
    985          1.87813065119873*x^2 + 20.0855369231877
    986     """
--> 987     converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)
    988     res = converter()
    989     return converter.ring(res)

/home/jason/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __init__(self, ex, base_ring, ring)
    843             G = ring.variable_names_recursive()
    844             if any([repr(v) not in G for v in ex.variables()]):
--> 845                 raise TypeError, "%s is not a variable of %s" %(v, ring)
    846             self.ring = ring
    847             self.base_ring = ring.base_ring()

TypeError: t is not a variable of Univariate Polynomial Ring in t over Symbolic Ring
```




---

archive/issue_comments_043952.json:
```json
{
    "body": "Hey, might that last error be related to the ticket which implements getting variables out of polynomial rings (e.g. 1.00*t was a variable but t wasn't)?",
    "created_at": "2009-10-07T01:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43952",
    "user": "https://github.com/kcrisman"
}
```

Hey, might that last error be related to the ticket which implements getting variables out of polynomial rings (e.g. 1.00*t was a variable but t wasn't)?



---

archive/issue_comments_043953.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> Hey, might that last error be related to the ticket which implements getting variables out of polynomial rings (e.g. 1.00*t was a variable but t wasn't)?\n\nThat doesn't seem likely to me.  I'm wondering if the error has to do with the variable in the symbolic expression coming from maxima being a different variable than what is requested in SR[var] (i.e., the \"t\"s in the TypeError are not the same object).  This is just a guess, though.",
    "created_at": "2009-10-07T02:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43953",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 kcrisman]:
> Hey, might that last error be related to the ticket which implements getting variables out of polynomial rings (e.g. 1.00*t was a variable but t wasn't)?

That doesn't seem likely to me.  I'm wondering if the error has to do with the variable in the symbolic expression coming from maxima being a different variable than what is requested in SR[var] (i.e., the "t"s in the TypeError are not the same object).  This is just a guess, though.



---

archive/issue_comments_043954.json:
```json
{
    "body": "I believe this shows the error more clearly, maybe:\n\n\n```\nsage: var('s,t')\n(s, t)\nsage: expr=t^2-2*s*t+1\nsage: expr.expand()\n-2*s*t + t^2 + 1\nsage: expr.polynomial(None,ring=SR['t'])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/.sage/temp/littleone/25931/_home_jason__sage_init_sage_0.py in <module>()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17284)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in polynomial(ex, base_ring, ring)\n    985          1.87813065119873*x^2 + 20.0855369231877\n    986     \"\"\"\n--> 987     converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)\n    988     res = converter()\n    989     return converter.ring(res)\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __init__(self, ex, base_ring, ring)\n    843             G = map(repr, ring.gens())\n    844             if any([repr(v) not in G for v in ex.variables()]):\n--> 845                 raise TypeError, \"%s is not a variable of %s\" %(v, ring)\n    846             self.ring = ring\n    847             self.base_ring = ring.base_ring()\n\nTypeError: t is not a variable of Univariate Polynomial Ring in t over Symbolic Ring\n\n```\n",
    "created_at": "2009-10-07T03:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43954",
    "user": "https://github.com/jasongrout"
}
```

I believe this shows the error more clearly, maybe:


```
sage: var('s,t')
(s, t)
sage: expr=t^2-2*s*t+1
sage: expr.expand()
-2*s*t + t^2 + 1
sage: expr.polynomial(None,ring=SR['t'])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/.sage/temp/littleone/25931/_home_jason__sage_init_sage_0.py in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.polynomial (sage/symbolic/expression.cpp:17284)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in polynomial(ex, base_ring, ring)
    985          1.87813065119873*x^2 + 20.0855369231877
    986     """
--> 987     converter = PolynomialConverter(ex, base_ring=base_ring, ring=ring)
    988     res = converter()
    989     return converter.ring(res)

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __init__(self, ex, base_ring, ring)
    843             G = map(repr, ring.gens())
    844             if any([repr(v) not in G for v in ex.variables()]):
--> 845                 raise TypeError, "%s is not a variable of %s" %(v, ring)
    846             self.ring = ring
    847             self.base_ring = ring.base_ring()

TypeError: t is not a variable of Univariate Polynomial Ring in t over Symbolic Ring

```




---

archive/issue_comments_043955.json:
```json
{
    "body": "Yep, the problem is in this code in `PolynomialConverter` in `sage/symbolic/expression_conversions.py`:\n\n\n```\n        if ring is not None:\n            G = map(repr, ring.gens())\n            if any([repr(v) not in G for v in ex.variables()]):\n                raise TypeError, \"%s is not a variable of %s\" %(v, ring)\n            self.ring = ring\n            self.base_ring = ring.base_ring()\n```\n\n\nNote that this does not allow for coefficients to have variables, but coefficients may have variables if the base ring is the symbolic ring!\n\nNote that the error message in the last comment is misleading: it should say that \"s is not a variable of ...\", but since the test uses \"any\", it doesn't know which variable is bad.",
    "created_at": "2009-10-07T03:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43955",
    "user": "https://github.com/jasongrout"
}
```

Yep, the problem is in this code in `PolynomialConverter` in `sage/symbolic/expression_conversions.py`:


```
        if ring is not None:
            G = map(repr, ring.gens())
            if any([repr(v) not in G for v in ex.variables()]):
                raise TypeError, "%s is not a variable of %s" %(v, ring)
            self.ring = ring
            self.base_ring = ring.base_ring()
```


Note that this does not allow for coefficients to have variables, but coefficients may have variables if the base ring is the symbolic ring!

Note that the error message in the last comment is misleading: it should say that "s is not a variable of ...", but since the test uses "any", it doesn't know which variable is bad.



---

archive/issue_comments_043956.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-19T18:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43956",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043957.json:
```json
{
    "body": "I've posted a patch which address the issues above.",
    "created_at": "2009-10-19T18:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43957",
    "user": "https://github.com/mwhansen"
}
```

I've posted a patch which address the issues above.



---

archive/issue_comments_043958.json:
```json
{
    "body": "Looks great!  Doctests pass in matrix/*.py[x]",
    "created_at": "2009-10-28T21:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43958",
    "user": "https://github.com/jasongrout"
}
```

Looks great!  Doctests pass in matrix/*.py[x]



---

archive/issue_comments_043959.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-28T21:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43959",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005880.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T05:30:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5639#event-5880"
}
```



---

archive/issue_comments_043960.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T05:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43960",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_043961.json:
```json
{
    "body": "There were a few failures cauesed by this in wester and coerce_maps for example.  I've backed out the patch.\n\nI'll post a new patch addressing these issues.",
    "created_at": "2009-10-31T09:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43961",
    "user": "https://github.com/mwhansen"
}
```

There were a few failures cauesed by this in wester and coerce_maps for example.  I've backed out the patch.

I'll post a new patch addressing these issues.



---

archive/issue_comments_043962.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2009-10-31T09:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43962",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_005881.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T09:10:55Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5639#event-5881"
}
```



---

archive/issue_comments_043963.json:
```json
{
    "body": "Attachment [trac_5639.patch](tarball://root/attachments/some-uuid/ticket5639/trac_5639.patch) by @mwhansen created at 2009-11-03 10:14:48\n\nI've posted a new patch which takes care of these issues.",
    "created_at": "2009-11-03T10:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43963",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5639.patch](tarball://root/attachments/some-uuid/ticket5639/trac_5639.patch) by @mwhansen created at 2009-11-03 10:14:48

I've posted a new patch which takes care of these issues.



---

archive/issue_comments_043964.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-03T10:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43964",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_043965.json:
```json
{
    "body": "Hmmm, generating a new variable based on a name that is not likely to be used is questionable.  Does symbolics not have a gensym-like function that generates a new variable that is not currently being used?",
    "created_at": "2009-11-03T10:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43965",
    "user": "https://github.com/jasongrout"
}
```

Hmmm, generating a new variable based on a name that is not likely to be used is questionable.  Does symbolics not have a gensym-like function that generates a new variable that is not currently being used?



---

archive/issue_comments_043966.json:
```json
{
    "body": "Not right now, but there's a patch on trac which adds that functionality.\n\nI'm just left the current behavior in this patch.",
    "created_at": "2009-11-03T12:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43966",
    "user": "https://github.com/mwhansen"
}
```

Not right now, but there's a patch on trac which adds that functionality.

I'm just left the current behavior in this patch.



---

archive/issue_comments_043967.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-11-10T04:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43967",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_043968.json:
```json
{
    "body": "Attachment [trac-5639-doctest.patch](tarball://root/attachments/some-uuid/ticket5639/trac-5639-doctest.patch) by @jasongrout created at 2009-11-10 04:37:32\n\nLooks okay, doctests pass on affected files.  I posted a patch with a doctest as well, as a reviewer patch.  Positive review.",
    "created_at": "2009-11-10T04:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43968",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5639-doctest.patch](tarball://root/attachments/some-uuid/ticket5639/trac-5639-doctest.patch) by @jasongrout created at 2009-11-10 04:37:32

Looks okay, doctests pass on affected files.  I posted a patch with a doctest as well, as a reviewer patch.  Positive review.



---

archive/issue_comments_043969.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T04:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5639#issuecomment-43969",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005882.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-12T07:15:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5639",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5639#event-5882"
}
```
