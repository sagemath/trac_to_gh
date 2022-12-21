# Issue 8056: symbolic expressions involving rational functions with numerator 1 cannot be converted to fast callable

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-01-25 17:17:02

Assignee: burcin

CC:  schilly kcrisman

From the sage-devel list:

http://groups.google.com/group/sage-devel/t/575627f654d21dd9


```
sage: t = 1/pi/x
sage: from sage.ext.fast_callable import ExpressionTreeBuilder
sage: etb = ExpressionTreeBuilder(vars=[x])
sage: t._fast_callable_(etb)
<boom>
```





---

Attachment


---

Comment by burcin created at 2010-01-25 19:10:48

Changing status from new to needs_review.


---

Comment by schilly created at 2010-01-27 23:13:27

I asked the reporter of the bug, and he found yet another problem. I think it's still related:

For me the patch fixes the problem only partially.

things like

`var('X'); f(x)=1/pi/x; fast_callable(f)(x)`

do now work as expected, but

`var('X');  f(x)=1/pi/x; plot(f,2,3)`

still fails -- now with a different error:


```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/<ipython console> in <module>()

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args,
**kwds)
   241                     kwds[new_name] = kwds[old_name]
   242                     del kwds[old_name]
--> 243             return func(*args, **kwds)
   244
   245         from sage.misc.sageinspect import sage_getsource

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args,
**kwds)
   136                 options['__original_opts'] = kwds
   137             options.update(kwds)
--> 138             return func(*args, **options)
   139
   140

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-packages/sage/plot/plot.pyc in plot(funcs,
*args, **kwds)
  2463
  2464     if hasattr(funcs, 'plot'):
-> 2465         G = funcs.plot(*args, **original_opts)
  2466     # if we are using the generic plotting method
  2467     else:

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in
sage.symbolic.expression.Expression.plot (sage/symbolic/expression.cpp:25582)
()

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in
sage.symbolic.expression.Expression._plot_fast_callable
(sage/symbolic/expression.cpp:26014)()

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in
sage.symbolic.expression.Expression._fast_float_
(sage/symbolic/expression.cpp:25025)()

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-
packages/sage/symbolic/expression_conversions.py in fast_float(ex, *vars)
  1199         1.4142135623730951
  1200     """
-> 1201     return FastFloatConverter(ex, *vars)()
  1202
  1203 #################

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-
packages/sage/symbolic/expression_conversions.py in __call__(self, ex)
   211             if getattr(self, 'use_fake_div', False) and operator is
_operator.mul:
   212                 div = self.get_fake_div(ex)
--> 213                 return self.arithmetic(div, div.operator())
   214             return self.arithmetic(ex, operator)
   215         elif operator in relation_operators:

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-
packages/sage/symbolic/expression_conversions.py in arithmetic(self, ex,
operator)
  1150             from sage.functions.all import sqrt
  1151             return sqrt(self(operands[0]))
-> 1152         fops = map(self, operands)
  1153         return reduce(operator, fops)
  1154

/usr/local/sage-mathe/sage-4.3.1-linux-openSUSE_11.1_x86_64-x86_64-
Linux/local/lib/python2.6/site-
packages/sage/symbolic/expression_conversions.py in __call__(self, ex)
   198
   199         try:
--> 200             obj = ex.pyobject()
   201             return self.pyobject(ex, obj)
   202         except TypeError, err:

AttributeError: 'sage.rings.integer.Integer' object has no attribute
'pyobject'
```



---

Attachment

second try


---

Comment by burcin created at 2010-01-31 21:51:22

Thank you for the review.

attachment:trac_8056-fast_callable.take2.patch uses `SR.one_element()` instead of `ZZ(1)`. This fixes the problems reported in comment:2.

Apply only attachment:trac_8056-fast_callable.take2.patch.

Can you take another look?


---

Comment by schilly created at 2010-02-01 10:52:33

thomas hupfer:

>  looks good, plotting now works for me as expected.


---

Comment by schilly created at 2010-02-01 10:52:33

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:03:18

Resolution: fixed
