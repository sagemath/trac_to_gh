# Issue 9329: Make it easy to access expression tree of a symbolic expression

archive/issues_009329.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  rossk @mforets @slel\n\n\n```\nsage: var('n')\nn\nsage: g=e^((n*pi-pi*2))\n```\n\nBut there doesn't seem to be an easy (i.e. not via `fast_callable`) way to access the underlying expression tree.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9329\n\n",
    "created_at": "2010-06-24T13:03:40Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Make it easy to access expression tree of a symbolic expression",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9329",
    "user": "@kcrisman"
}
```
Assignee: @burcin

CC:  rossk @mforets @slel


```
sage: var('n')
n
sage: g=e^((n*pi-pi*2))
```

But there doesn't seem to be an easy (i.e. not via `fast_callable`) way to access the underlying expression tree.

Issue created by migration from https://trac.sagemath.org/ticket/9329





---

archive/issue_comments_087992.json:
```json
{
    "body": "Did you have something specific in mind?  You can always get at the underlying tree with operand() and operands()\n\n\n```\nsage: var('n')\nn\nsage: g = e^((n*pi-pi*2))\nsage: g.operator(), g.operands()\n(exp, [-2*pi + pi*n])\n```\n\n\nThis is what is done in expression_conversions.py",
    "created_at": "2010-06-25T00:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87992",
    "user": "@mwhansen"
}
```

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

archive/issue_comments_087993.json:
```json
{
    "body": "I think the original request from a user was in order to access the whole tree at once as a \"parsed tree\", since here of course `g.operands()` is itself something with an operator and operands.   Maybe there isn't such an object per se?",
    "created_at": "2010-06-25T13:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87993",
    "user": "@kcrisman"
}
```

I think the original request from a user was in order to access the whole tree at once as a "parsed tree", since here of course `g.operands()` is itself something with an operator and operands.   Maybe there isn't such an object per se?



---

archive/issue_comments_087994.json:
```json
{
    "body": "See http://sagenb.org/home/pub/1760/ for a simple implementation.\n\n\n```\n\ndef tree(expr): \n    if expr.operator() is None: \n        return expr \n    else: \n        return [expr.operator()]+map(tree, expr.operands()) \n```\n",
    "created_at": "2010-06-27T03:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87994",
    "user": "@jasongrout"
}
```

See http://sagenb.org/home/pub/1760/ for a simple implementation.


```

def tree(expr): 
    if expr.operator() is None: 
        return expr 
    else: 
        return [expr.operator()]+map(tree, expr.operands()) 
```




---

archive/issue_comments_087995.json:
```json
{
    "body": "Here is the thread:\n\nhttp://groups.google.com/group/sage-support/t/e4b769a26269b6ed\n\n\nI think this is more of a documentation problem. We don't have any explanation of how to work with symbolic expressions, either traversing the tree using `operator()` and `operands()` or pattern matching with `find()` and `match()`.\n\nI don't think adding a function like Jason suggests in comment:3 would provide anything more than that is already there. Note that in the example worksheet Jason also doesn't use this function.\n\nI suggest to close this ticket unless there is a more concrete suggestion.",
    "created_at": "2010-06-30T12:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87995",
    "user": "@burcin"
}
```

Here is the thread:

http://groups.google.com/group/sage-support/t/e4b769a26269b6ed


I think this is more of a documentation problem. We don't have any explanation of how to work with symbolic expressions, either traversing the tree using `operator()` and `operands()` or pattern matching with `find()` and `match()`.

I don't think adding a function like Jason suggests in comment:3 would provide anything more than that is already there. Note that in the example worksheet Jason also doesn't use this function.

I suggest to close this ticket unless there is a more concrete suggestion.



---

archive/issue_comments_087996.json:
```json
{
    "body": "Well, this seems very reasonable; I certainly wouldn't have ever figured out the way you do it in that thread.  This probably belongs either at the top of one of expression.pyx or in the documentation for SymbolicExpression, huh?  It would be nice to do an example with simplification as well as substitution.  \n\nChanging ticket summary",
    "created_at": "2010-06-30T13:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87996",
    "user": "@kcrisman"
}
```

Well, this seems very reasonable; I certainly wouldn't have ever figured out the way you do it in that thread.  This probably belongs either at the top of one of expression.pyx or in the documentation for SymbolicExpression, huh?  It would be nice to do an example with simplification as well as substitution.  

Changing ticket summary



---

archive/issue_comments_087997.json:
```json
{
    "body": "Resurrecting the original idea because I want this for my discrete math class in a couple days and realize that even having a very basic example of how to use `Converter` to make an expression tree - say one I could plot! - would be really useful.  Right now I'm stuck with Jason's idea, which works but perhaps isn't as \"Sage-ic\".\n\n```\nsage: from sage.symbolic.random_tests import random_expr\nsage: S = random_expr(20,nvars=2)\nsage: S\nsinh_integral(-sec(-4*abs(e))/((kronecker_delta(e, v1) - 52)*arctan(elliptic_kc(-2) - 2)))\nsage: def tree(expr):\n....:     if expr.operator() is None:\n....:         return expr\n....:     else:\n....:         return [expr.operator()]+map(tree,expr.operands())\n....:     \nsage: tree(S)\n[sinh_integral, [<built-in function mul>, [<built-in function pow>, [<built-in function add>, [kronecker_delta, [exp, 1], v1], -52], -1], [<built-in function pow>, [arctan, [<built-in function add>, [elliptic_kc, -2], -2]], -1], [sec, [<built-in function mul>, [abs, [exp, 1]], -4]], -1]]\n```\n\nI'm realizing it might even be useful to have a (binary) tree returned from a list of lists... but that wouldn't be here.",
    "created_at": "2012-12-06T03:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87997",
    "user": "@kcrisman"
}
```

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

archive/issue_comments_087998.json:
```json
{
    "body": "By the way, http://interact.sagemath.org/node/76 might be a nice example too (that's an extremely simple expression->Java translator...)",
    "created_at": "2012-12-06T12:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87998",
    "user": "@jasongrout"
}
```

By the way, http://interact.sagemath.org/node/76 might be a nice example too (that's an extremely simple expression->Java translator...)



---

archive/issue_comments_087999.json:
```json
{
    "body": "Does\n\n```\nsage: S._maxima_lib_().ecl().python()\n```\n\ncount?",
    "created_at": "2012-12-08T00:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-87999",
    "user": "@nbruin"
}
```

Does

```
sage: S._maxima_lib_().ecl().python()
```

count?



---

archive/issue_comments_088000.json:
```json
{
    "body": "> Does\n> {{{\n> sage: S._maxima_lib_().ecl().python()\n> }}}\n> count?\nThat certainly counts as one example.   I don't know that people will know what to do with `'MTIMES'` :-)\n\nBasically, an introduction to how to write something like this for people who don't know jack about expression trees (like me, though teaching it certainly helped) is what would be helpful here.",
    "created_at": "2012-12-08T04:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-88000",
    "user": "@kcrisman"
}
```

> Does
> {{{
> sage: S._maxima_lib_().ecl().python()
> }}}
> count?
That certainly counts as one example.   I don't know that people will know what to do with `'MTIMES'` :-)

Basically, an introduction to how to write something like this for people who don't know jack about expression trees (like me, though teaching it certainly helped) is what would be helpful here.



---

archive/issue_comments_088001.json:
```json
{
    "body": "See also #9424.",
    "created_at": "2015-02-10T16:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-88001",
    "user": "@kcrisman"
}
```

See also #9424.



---

archive/issue_comments_088002.json:
```json
{
    "body": "Changing keywords from \"\" to \"expression tree, symbolic expression\".",
    "created_at": "2018-05-21T17:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-88002",
    "user": "@slel"
}
```

Changing keywords from "" to "expression tree, symbolic expression".



---

archive/issue_comments_088003.json:
```json
{
    "body": "Note: the worksheet mentioned by jason in comment:3, originally at\n\n- http://sagenb.org/home/pub/1760/\n\nis now available, translated into a .sagews worksheet, at:\n\n- https://share.cocalc.com/share/19575ea0-317e-402b-be57-368d04c113db/pub/1701-1801/1760.sagews?viewer=share",
    "created_at": "2019-01-18T19:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9329#issuecomment-88003",
    "user": "@slel"
}
```

Note: the worksheet mentioned by jason in comment:3, originally at

- http://sagenb.org/home/pub/1760/

is now available, translated into a .sagews worksheet, at:

- https://share.cocalc.com/share/19575ea0-317e-402b-be57-368d04c113db/pub/1701-1801/1760.sagews?viewer=share
