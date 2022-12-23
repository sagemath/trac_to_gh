# Issue 7810: bug in fast_callable (reducing empty sequence)

Issue created by migration from https://trac.sagemath.org/ticket/7810

Original creator: jason

Original creation time: 2010-01-01 18:53:48

Assignee: AlexGhitza

CC:  cwitty burcin


```
sage: var('x,y')
sage: fast_float(-1/x-1/y+1/(x*y),x,y)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/tiny/2056/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.fast_float (sage/ext/fast_eval.c:8434)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.fast_callable (sage/ext/fast_callable.c:3134)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._fast_callable_ (sage/symbolic/expression.cpp:24715)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1353 
   1354     """
-> 1355     return FastCallableConverter(ex, etb)()
   1356 
   1357 class RingConverter(Converter):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    212                 div = self.get_fake_div(ex)
    213                 return self.arithmetic(div, div.operator())
--> 214             return self.arithmetic(ex, operator)
    215         elif operator in relation_operators:
    216             return self.relation(ex, operator)

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in arithmetic(self, ex, operator)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in <lambda>(x, y)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.call (sage/ext/fast_callable.c:4986)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.__call__ (sage/ext/fast_callable.c:4313)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._fast_callable_ (sage/symbolic/expression.cpp:24715)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1353 
   1354     """
-> 1355     return FastCallableConverter(ex, etb)()
   1356 
   1357 class RingConverter(Converter):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    211             if getattr(self, 'use_fake_div', False) and operator is _operator.mul:
    212                 div = self.get_fake_div(ex)
--> 213                 return self.arithmetic(div, div.operator())
    214             return self.arithmetic(ex, operator)
    215         elif operator in relation_operators:

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in arithmetic(self, ex, operator)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in <lambda>(x, y)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.call (sage/ext/fast_callable.c:4986)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.__call__ (sage/ext/fast_callable.c:4313)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in _fast_callable_(self, etb)
    119             [('load_arg', 0), ('load_arg', 1), 'div', 'return']
    120         """
--> 121         return fast_callable(self, etb)
    122 
    123     def _fast_float_(self, *vars):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1353 
   1354     """
-> 1355     return FastCallableConverter(ex, etb)()
   1356 
   1357 class RingConverter(Converter):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    211             if getattr(self, 'use_fake_div', False) and operator is _operator.mul:
    212                 div = self.get_fake_div(ex)
--> 213                 return self.arithmetic(div, div.operator())
    214             return self.arithmetic(ex, operator)
    215         elif operator in relation_operators:

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in arithmetic(self, ex, operator)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

TypeError: reduce() of empty sequence with no initial value
sage: fast_callable(-1/x-1/y+1/(x*y),vars=[x,y])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/tiny/2056/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.fast_callable (sage/ext/fast_callable.c:3134)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._fast_callable_ (sage/symbolic/expression.cpp:24715)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1353 
   1354     """
-> 1355     return FastCallableConverter(ex, etb)()
   1356 
   1357 class RingConverter(Converter):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    212                 div = self.get_fake_div(ex)
    213                 return self.arithmetic(div, div.operator())
--> 214             return self.arithmetic(ex, operator)
    215         elif operator in relation_operators:
    216             return self.relation(ex, operator)

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in arithmetic(self, ex, operator)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in <lambda>(x, y)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.call (sage/ext/fast_callable.c:4986)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.__call__ (sage/ext/fast_callable.c:4313)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._fast_callable_ (sage/symbolic/expression.cpp:24715)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1353 
   1354     """
-> 1355     return FastCallableConverter(ex, etb)()
   1356 
   1357 class RingConverter(Converter):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    211             if getattr(self, 'use_fake_div', False) and operator is _operator.mul:
    212                 div = self.get_fake_div(ex)
--> 213                 return self.arithmetic(div, div.operator())
    214             return self.arithmetic(ex, operator)
    215         elif operator in relation_operators:

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in arithmetic(self, ex, operator)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in <lambda>(x, y)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.call (sage/ext/fast_callable.c:4986)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/ext/fast_callable.so in sage.ext.fast_callable.ExpressionTreeBuilder.__call__ (sage/ext/fast_callable.c:4313)()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in _fast_callable_(self, etb)
    119             [('load_arg', 0), ('load_arg', 1), 'div', 'return']
    120         """
--> 121         return fast_callable(self, etb)
    122 
    123     def _fast_float_(self, *vars):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1353 
   1354     """
-> 1355     return FastCallableConverter(ex, etb)()
   1356 
   1357 class RingConverter(Converter):

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    211             if getattr(self, 'use_fake_div', False) and operator is _operator.mul:
    212                 div = self.get_fake_div(ex)
--> 213                 return self.arithmetic(div, div.operator())
    214             return self.arithmetic(ex, operator)
    215         elif operator in relation_operators:

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in arithmetic(self, ex, operator)
   1293         elif operator is _operator.neg:
   1294             return self.etb.call(operator, operands[0])
-> 1295         return reduce(lambda x,y: self.etb.call(operator, x,y), operands)
   1296 
   1297     def symbol(self, ex):

TypeError: reduce() of empty sequence with no initial value
```



---

Comment by burcin created at 2010-01-26 15:15:40

This works for me after applying the patch at #8056. Since the patch is attached there, I suggest we close this as a duplicate.


```
sage: var('x,y')
(x, y)
sage: fast_float(-1/x-1/y+1/(x*y),x,y)
<sage.ext.interpreters.wrapper_rdf.Wrapper_rdf object at 0x7fc3b89ba248>
```



---

Comment by jason created at 2010-03-17 05:05:26

This works for me in 4.3.3 too.  This ticket should be closed.


---

Comment by mvngu created at 2010-03-17 05:07:09

Close as a duplicate of #8056.


---

Comment by mvngu created at 2010-03-17 05:07:09

Resolution: duplicate
