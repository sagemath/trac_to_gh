# Issue 5679: fix a bug in solve and polynomial generators

archive/issues_005679.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\nSome code that used to work in sage-3.0.6 (or something close like\n3.0.3), now break with this error message:\n\n>>> R.<x0,x1,x2> = PolynomialRing(RR, 3)\n>>> solve([symbolic_expression(x0) == 0], x0, x1, x2)\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"/Users/anakha/.sage/sage_notebook/worksheets/admin/12/code/30.py\",\nline 8, in <module>\n   solve(x0 == _sage_const_0 , x0, x1, x2)\n File \"/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\",\nline 1, in <module>\n\n File \"/Volumes/Place/anakha/Applications/sage-3.4/local/lib/python2.5/site-packages/sage/calculus/equations.py\",\nline 1563, in solve\n   raise TypeError, \"%s is not a valid variable.\"%v\nTypeError: not all arguments converted during string formatting\n\nThe printing problem is due to the fact that Polynomials have an\nimplicit conversion to sequence types triggered by this code:\n\n       try:\n           variables = tuple(args[0])\n       except TypeError:\n           variables = args\n\nnear the start of solve(), (Hint: tuple(args[0]) works if the first\nvariable is a PolynomialElement and thus the rest of the vars are\nignored and you get the bogus ((1.0000000, x0),) tuple as variables)\n\nIf that is fixed, then you get this message which does not help much more:\n\n>>> R.<x0,x1,x2> = PolynomialRing(RR, 3)\n>>> solve([symbolic_expression(x0) == 0], x0, x1, x2)\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"/Users/anakha/.sage/sage_notebook/worksheets/admin/12/code/55.py\",\nline 8, in <module>\n   solve(x0 == _sage_const_0 , x0, x1, x2)\n File \"/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\",\nline 1, in <module>\n\n File \"/Users/anakha/.sage/sage_notebook/worksheets/admin/12/code/54.py\",\nline 22, in solve\n   raise TypeError, \"%s is not a valid variable.\"%v\nTypeError: x0 is not a valid variable.\n\nFurthermore, if you disable the type checking that is done on the\ninput variables, then it works as before:\n\n>>> R.<x0,x1,x2> = PolynomialRing(RR, 3)\n>>> solve([symbolic_expression(x0) == 0], x0, x1, x2)\n[[x0 == 0, x1 == r10, x2 == r9]]\n\nI don't think killing the typecheck is the way to go, but maybe\nextending it to cover the polynomial elements.\n\nOr maybe another better way to do this has come up.\n\nArnaud\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5679\n\n",
    "created_at": "2009-04-04T04:49:15Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "fix a bug in solve and polynomial generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5679",
    "user": "@williamstein"
}
```
Assignee: @burcin


```
Some code that used to work in sage-3.0.6 (or something close like
3.0.3), now break with this error message:

>>> R.<x0,x1,x2> = PolynomialRing(RR, 3)
>>> solve([symbolic_expression(x0) == 0], x0, x1, x2)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/Users/anakha/.sage/sage_notebook/worksheets/admin/12/code/30.py",
line 8, in <module>
   solve(x0 == _sage_const_0 , x0, x1, x2)
 File "/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/",
line 1, in <module>

 File "/Volumes/Place/anakha/Applications/sage-3.4/local/lib/python2.5/site-packages/sage/calculus/equations.py",
line 1563, in solve
   raise TypeError, "%s is not a valid variable."%v
TypeError: not all arguments converted during string formatting

The printing problem is due to the fact that Polynomials have an
implicit conversion to sequence types triggered by this code:

       try:
           variables = tuple(args[0])
       except TypeError:
           variables = args

near the start of solve(), (Hint: tuple(args[0]) works if the first
variable is a PolynomialElement and thus the rest of the vars are
ignored and you get the bogus ((1.0000000, x0),) tuple as variables)

If that is fixed, then you get this message which does not help much more:

>>> R.<x0,x1,x2> = PolynomialRing(RR, 3)
>>> solve([symbolic_expression(x0) == 0], x0, x1, x2)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/Users/anakha/.sage/sage_notebook/worksheets/admin/12/code/55.py",
line 8, in <module>
   solve(x0 == _sage_const_0 , x0, x1, x2)
 File "/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/",
line 1, in <module>

 File "/Users/anakha/.sage/sage_notebook/worksheets/admin/12/code/54.py",
line 22, in solve
   raise TypeError, "%s is not a valid variable."%v
TypeError: x0 is not a valid variable.

Furthermore, if you disable the type checking that is done on the
input variables, then it works as before:

>>> R.<x0,x1,x2> = PolynomialRing(RR, 3)
>>> solve([symbolic_expression(x0) == 0], x0, x1, x2)
[[x0 == 0, x1 == r10, x2 == r9]]

I don't think killing the typecheck is the way to go, but maybe
extending it to cover the polynomial elements.

Or maybe another better way to do this has come up.

Arnaud
```


Issue created by migration from https://trac.sagemath.org/ticket/5679





---

archive/issue_comments_044418.json:
```json
{
    "body": "In Sage 4.6.2:\n{{[\nsage: f = symbolic_expression(x0) == 0\nsage: f.solve(x0)\n---------------------------------------------------------------------------\nTypeError: x0 is not a valid variable.\nsage: f.solve(symbolic_expression(x0))\n[x0 == 0]\n}}}\n\nThis is because \n\n```\n        if not isinstance(x, Expression):\n            raise TypeError, \"%s is not a valid variable.\"%x\n```\n\nSo I guess one could check whether SR(x) is a symbol?\n\n```\nsage: symbolic_expression(x0)._is_symbol()\nTrue\n```\n\n\nIncidentally, we never get to the `args[0]` because you are solving a single expression, so it goes to `ex.solve(*args)`.  So maybe we should check for that...  But in any case the syntax is now\n\n```\nsage: solve([symbolic_expression(x0) == 0, 0==0], [x0, x1, x2])\n---------------------------------------------------------------------------\nTypeError: x0 is not a valid variable.\n```\n\nwhich *does* raise the error in question.\n\nBut \n\n```\nsage: solve([symbolic_expression(x0) == 0, 0==0], [SR(x0), SR(x1), SR(x2)])\n[[x0 == 0, x1 == r2, x2 == r1]]\n```\n\n\nWeirdly, \n\n```\nsage: solve([symbolic_expression(x0) == 0], SR(x0), SR(x1), SR(x2))\n([x0 == 0], [1])\n```\n",
    "created_at": "2011-03-16T15:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5679#issuecomment-44418",
    "user": "@kcrisman"
}
```

In Sage 4.6.2:
{{[
sage: f = symbolic_expression(x0) == 0
sage: f.solve(x0)
---------------------------------------------------------------------------
TypeError: x0 is not a valid variable.
sage: f.solve(symbolic_expression(x0))
[x0 == 0]
}}}

This is because 

```
        if not isinstance(x, Expression):
            raise TypeError, "%s is not a valid variable."%x
```

So I guess one could check whether SR(x) is a symbol?

```
sage: symbolic_expression(x0)._is_symbol()
True
```


Incidentally, we never get to the `args[0]` because you are solving a single expression, so it goes to `ex.solve(*args)`.  So maybe we should check for that...  But in any case the syntax is now

```
sage: solve([symbolic_expression(x0) == 0, 0==0], [x0, x1, x2])
---------------------------------------------------------------------------
TypeError: x0 is not a valid variable.
```

which *does* raise the error in question.

But 

```
sage: solve([symbolic_expression(x0) == 0, 0==0], [SR(x0), SR(x1), SR(x2)])
[[x0 == 0, x1 == r2, x2 == r1]]
```


Weirdly, 

```
sage: solve([symbolic_expression(x0) == 0], SR(x0), SR(x1), SR(x2))
([x0 == 0], [1])
```




---

archive/issue_comments_044419.json:
```json
{
    "body": "> Incidentally, we never get to the `args[0]` because you are solving a single expression, so it goes to `ex.solve(*args)`.  So maybe we should check for that...  But in any case the syntax is now\n> Weirdly, \n> {{{\n> sage: solve([symbolic_expression(x0) == 0], SR(x0), SR(x1), SR(x2))\n> ([x0 == 0], [1])\n> }}}\n\nThese (tangential) things are both addressed at #10750, as it turns out.",
    "created_at": "2011-09-13T17:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5679#issuecomment-44419",
    "user": "@kcrisman"
}
```

> Incidentally, we never get to the `args[0]` because you are solving a single expression, so it goes to `ex.solve(*args)`.  So maybe we should check for that...  But in any case the syntax is now
> Weirdly, 
> {{{
> sage: solve([symbolic_expression(x0) == 0], SR(x0), SR(x1), SR(x2))
> ([x0 == 0], [1])
> }}}

These (tangential) things are both addressed at #10750, as it turns out.
