# Issue 6243: add support for arbitrary parents in pynac's evalf

Issue created by migration from https://trac.sagemath.org/ticket/6243

Original creator: burcin

Original creation time: 2009-06-07 19:07:43

CC:  mhansen

From Alex Raichev on sage-support:


```
Hi all:

Upon upgrading to Sage 4.0, i can no longer make a dictionary with
derivatives as keys (see below).  Can someone please fix this?

Alex

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: X= var('x,y')
sage: f= function('f',*X); f
f(x, y)
sage: for x in X:
....:     diff(f,x)
....:
D[0](f)(x, y)
D[1](f)(x, y)
sage: d= {}
sage: for x in X:
....:     d[diff(f,x)] = 1
....:
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call
last)
| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
/Users/raichev/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression.so in sage.symbolic.expression.Expression.__nonzero__ (sage/
symbolic/expression.cpp:7814)()

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression.so in sage.symbolic.expression.Expression.test_relation
(sage/symbolic/expression.cpp:9187)()

/Applications/sage/local/lib/python2.5/site-packages/sage/rings/
complex_interval_field.pyc in __call__(self, x, im)
    286
    287             try:
--> 288                 return x._complex_mpfi_( self )  
    289             except AttributeError:
    290                 pass

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression.so in sage.symbolic.expression.Expression._complex_mpfi_
(sage/symbolic/expression.cpp:5484)()

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in __call__(self, ex)
    212                 div = self.get_fake_div(ex)
    213                 return self.arithmetic(div, div.operator())
--> 214             return self.arithmetic(ex, operator)  
    215         elif operator in relation_operators:
    216             return self.relation(ex, operator)

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in arithmetic(self, ex, operator)
   1424             return base ** expt
   1425         else:
-> 1426             return reduce(operator, map(self, operands))  
   1427
   1428     def composition(self, ex, operator):

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in __call__(self, ex)
    216             return self.relation(ex, operator)
    217         elif isinstance(operator, FDerivativeOperator):
--> 218             return self.derivative(ex, operator)  
    219         else:
    220             return self.composition(ex, operator)

/Applications/sage/local/lib/python2.5/site-packages/sage/symbolic/
expression_conversions.pyc in derivative(self, ex, operator)
    344             NotImplementedError: derivative
    345         """
--> 346         raise NotImplementedError, "derivative"  
    347
    348     def arithmetic(self, ex, operator):

NotImplementedError: derivative
```


I suppose an immediate fix is to implement the derivative method in `sage.symbolic.expression_conversions.Converter`. I believe the right fix is to change pynac to pass on the parent for numerical approximation instead of just the precision. I'll work on making the necessary changes in pynac.



---

Comment by burcin created at 2009-07-31 21:20:34

doctests for the fix


---

Attachment

I have a fix for this in my local pynac tree. I took a shortcut and changed the fderivative hashes to include the parameters.

I'll make a new pynac package with fixes for some other bugs available soon.


---

Comment by burcin created at 2009-08-01 02:31:33

Changing status from new to assigned.


---

Comment by burcin created at 2009-08-01 02:31:33

This now depends on the package linked from #6404.

Please follow the instructions on that ticket to apply & test.


---

Comment by burcin created at 2009-08-01 02:31:33

Set assignee to burcin.


---

Comment by gmhossain created at 2009-08-02 17:12:11

I tested this out. Pynac changes seem fine to me. I encountered one issue though:

```
sage: d = {}
sage: d[x] = 1
sage: d
{x: 1}
sage: f(x) = function('f',x)
sage: d[diff(f(x),x)] = 2
sage: d.keys()
[D[0](f)(x), x]
sage: d.values()
[2, 1]
sage: d
!boom!
```


The origin of this !boom! lies in expression_conversions.py for fderivative
which is clearly NOT in purview of this patch. So I am going to give it a positive review 
shortly.


---

Comment by gmhossain created at 2009-08-02 19:13:24

Note: I am giving partial positive review because I tested this patch against my stable 
sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.


---

Comment by mvngu created at 2009-08-03 00:32:38

I applied patches in the following order:
 1. the spkg `pynac-0.1.8.p2.spkg` at #6404
 1. `trac_6404-conjugate_typesetting.patch`
 1. `trac_6401-real_imag_typesetting.patch`
 1. `trac_6377-exp_infinity.patch`
 1. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.


---

Comment by mvngu created at 2009-08-03 00:32:38

Resolution: fixed
