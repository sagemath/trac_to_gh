# Issue 9329: Make it easy to access expression tree of a symbolic expression

Issue created by migration from https://trac.sagemath.org/ticket/9329

Original creator: kcrisman

Original creation time: 2010-06-24 13:03:40

Assignee: burcin

CC:  rossk mforets slelievre


```
sage: var('n')
n
sage: g=e^((n*pi-pi*2))
```

But there doesn't seem to be an easy (i.e. not via `fast_callable`) way to access the underlying expression tree.


---

Comment by mhansen created at 2010-06-25 00:41:40

Did you have something specific in mind?  You can always get at the underlying tree with operand() and operands()


```
sage: var('n')
n
sage: g = e^((n*pi-pi*2))
sage: g.operator(), g.operands()
(exp, [-2*pi + pi*n])
```


This is what is done in expression_conversions.py


---

Comment by kcrisman created at 2010-06-25 13:07:33

I think the original request from a user was in order to access the whole tree at once as a "parsed tree", since here of course `g.operands()` is itself something with an operator and operands.   Maybe there isn't such an object per se?


---

Comment by jason created at 2010-06-27 03:47:15

See http://sagenb.org/home/pub/1760/ for a simple implementation.


```

def tree(expr): 
    if expr.operator() is None: 
        return expr 
    else: 
        return [expr.operator()]+map(tree, expr.operands()) 
```



---

Comment by burcin created at 2010-06-30 12:24:12

Here is the thread:

http://groups.google.com/group/sage-support/t/e4b769a26269b6ed


I think this is more of a documentation problem. We don't have any explanation of how to work with symbolic expressions, either traversing the tree using `operator()` and `operands()` or pattern matching with `find()` and `match()`.

I don't think adding a function like Jason suggests in comment:3 would provide anything more than that is already there. Note that in the example worksheet Jason also doesn't use this function.

I suggest to close this ticket unless there is a more concrete suggestion.


---

Comment by kcrisman created at 2010-06-30 13:12:33

Well, this seems very reasonable; I certainly wouldn't have ever figured out the way you do it in that thread.  This probably belongs either at the top of one of expression.pyx or in the documentation for SymbolicExpression, huh?  It would be nice to do an example with simplification as well as substitution.  

Changing ticket summary


---

Comment by kcrisman created at 2012-12-06 03:52:13

Resurrecting the original idea because I want this for my discrete math class in a couple days and realize that even having a very basic example of how to use `Converter` to make an expression tree - say one I could plot! - would be really useful.  Right now I'm stuck with Jason's idea, which works but perhaps isn't as "Sage-ic".

```
sage: from sage.symbolic.random_tests import random_expr
sage: S = random_expr(20,nvars=2)
sage: S
sinh_integral(-sec(-4*abs(e))/((kronecker_delta(e, v1) - 52)*arctan(elliptic_kc(-2) - 2)))
sage: def tree(expr):
....:     if expr.operator() is None:
....:         return expr
....:     else:
....:         return [expr.operator()]+map(tree,expr.operands())
....:     
sage: tree(S)
[sinh_integral, [<built-in function mul>, [<built-in function pow>, [<built-in function add>, [kronecker_delta, [exp, 1], v1], -52], -1], [<built-in function pow>, [arctan, [<built-in function add>, [elliptic_kc, -2], -2]], -1], [sec, [<built-in function mul>, [abs, [exp, 1]], -4]], -1]]
```

I'm realizing it might even be useful to have a (binary) tree returned from a list of lists... but that wouldn't be here.


---

Comment by jason created at 2012-12-06 12:43:10

By the way, http://interact.sagemath.org/node/76 might be a nice example too (that's an extremely simple expression->Java translator...)


---

Comment by nbruin created at 2012-12-08 00:39:47

Does

```
sage: S._maxima_lib_().ecl().python()
```

count?


---

Comment by kcrisman created at 2012-12-08 04:16:55

> Does
> {{{
> sage: S._maxima_lib_().ecl().python()
> }}}
> count?
That certainly counts as one example.   I don't know that people will know what to do with `'MTIMES'` :-)

Basically, an introduction to how to write something like this for people who don't know jack about expression trees (like me, though teaching it certainly helped) is what would be helpful here.


---

Comment by kcrisman created at 2015-02-10 16:06:35

See also #9424.


---

Comment by slelievre created at 2018-05-21 17:10:21

Changing keywords from "" to "expression tree, symbolic expression".


---

Comment by slelievre created at 2019-01-18 19:32:45

Note: the worksheet mentioned by jason in comment:3, originally at

- http://sagenb.org/home/pub/1760/

is now available, translated into a .sagews worksheet, at:

- https://share.cocalc.com/share/19575ea0-317e-402b-be57-368d04c113db/pub/1701-1801/1760.sagews?viewer=share
