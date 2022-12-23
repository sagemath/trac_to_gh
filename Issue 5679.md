# Issue 5679: fix a bug in solve and polynomial generators

Issue created by migration from https://trac.sagemath.org/ticket/5679

Original creator: was

Original creation time: 2009-04-04 04:49:15

Assignee: burcin


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



---

Comment by kcrisman created at 2011-03-16 15:52:58

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

which _does_ raise the error in question.

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

Comment by kcrisman created at 2011-09-13 17:01:13

> Incidentally, we never get to the `args[0]` because you are solving a single expression, so it goes to `ex.solve(*args)`.  So maybe we should check for that...  But in any case the syntax is now
> Weirdly, 
> {{{
> sage: solve([symbolic_expression(x0) == 0], SR(x0), SR(x1), SR(x2))
> ([x0 == 0], [1])
> }}}

These (tangential) things are both addressed at #10750, as it turns out.
