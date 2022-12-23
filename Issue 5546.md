# Issue 5546: jacobian fails for pynac expressions

Issue created by migration from https://trac.sagemath.org/ticket/5546

Original creator: burcin

Original creation time: 2009-03-17 09:36:03

Assignee: burcin

CC:  wstein mhansen robertwb

Reported by Alex Raichev on sage-support:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('x,y', ns=1)
(x, y)
sage: f= x+y
sage: type(f)
<type 'sage.symbolic.expression.Expression'>
sage: jacobian(f,[x,y])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
/Users/arai021/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/calculus/
functions.pyc in jacobian(functions, variables)
    136
    137     if not isinstance(variables, (tuple, list)) and not
is_Vector(variables):
    138         variables = [variables]
    139
--> 140     return matrix([[diff(f, v) for v in variables] for f in  
functions])

/Applications/sage/local/lib/python2.5/site-packages/sage/calculus/
functional.pyc in derivative(f, *args, **kwds)
    145         pass
    146     if not isinstance(f, SymbolicExpression):
--> 147         f = SR(f)  
    148     return f.derivative(*args, **kwds)
    149

/Applications/sage/local/lib/python2.5/site-packages/sage/calculus/
calculus.pyc in __call__(self, x)
    504                 msg, s, pos = err.args
    505                 raise TypeError, "%s: %s !!! %s" % (msg, s
[:pos], s[pos:])
--> 506         return self._coerce_impl(x)  
    507
    508     def _coerce_impl(self, x):

/Applications/sage/local/lib/python2.5/site-packages/sage/calculus/
calculus.pyc in _coerce_impl(self, x)
    566             return self(x._sage_())
    567         else:
--> 568             raise TypeError, "cannot coerce type '%s' into a  
SymbolicExpression."%type(x)
    569
    570     def _repr_(self):

TypeError: cannot coerce type '<type
'sage.symbolic.expression.Expression'>' into a SymbolicExpression.  
```


`sage.symbolic.expression.Expression` doesn't support .derivative(), and the interface to .diff() doesn't match the Sage conventions.


---

Comment by burcin created at 2009-03-24 15:49:29

Changing status from new to assigned.


---

Comment by burcin created at 2009-03-24 15:49:29

Attached patches allow forming matrices and vectors with pynac expressions, and make them use the multi_derivative framework. This makes the jacobian command in the example above work.


---

Comment by burcin created at 2009-03-24 16:33:33

allow forming matrices and vectors from pynac expressions


---

Attachment

make pynac expressions use the multi_derivative framework


---

Comment by ncalexan created at 2009-04-09 17:05:52

With these two patches applied, you can get some wild things:


```
sage: var('x,y,z',ns=1)
(x, y, z)
sage: M = matrix(2,2,[x,y,z,x])
sage: M.base_ring()
New Symbolic Ring
sage: v = vector([x,y])
sage: v.base_ring()
New Symbolic Ring
sage: M * v
Exception exceptions.TypeError: 'mutable matrices are unhashable' in 'sage.modules.free_module_element.FreeModuleElement._cmp_same_ambient_c' ignored
<ERROR: mutable matrices are unhashable>
(([x y]
[z x])*x, ([x y]
[z x])*y)
sage: v * M
(x^2 + y*z, 2*x*y)
sage: M * v
<ERROR: mutable matrices are unhashable>
(([x y]
[z x])*x, ([x y]
[z x])*y)
sage: v * M * v
2*x*y^2 + (x^2 + y*z)*x
sage: v * (M * v)
/Users/ncalexan/.sage/temp/dhcp_v007_000.mobile.uci.edu/36399/_Users_ncalexan__sage_init_sage_0.py:1: RuntimeWarning: tp_compare didn't return -1 or -2 for exception
  # -*- coding: utf-8 -*-
([x y] + ([x y]
```



---

Attachment

patch to pynac to handle exceptions during hashing


---

Comment by burcin created at 2009-04-24 15:34:43

doctests for the fix


---

Attachment

attachment:pynac-hash_exception.patch fixes exception handling during hashing in pynac and the problems reported by Nick in comment:2.

I will hold off on doing another pynac release to address this, since I don't know if mhansen made any changes which might be affected.

BTW, another pynac release, 0.1.6 in this case, would introduce circular dependencies in trac. :)

Comments on how to proceed?


---

Comment by was created at 2009-04-24 15:57:51

> Comments on how to proceed? 

I'd just like to remark that Mike Hansen is probably the best person I've ever met at using rebasing patches and using revision control systems.  With him, I would not be worried about doing something that conflicts with what he has done or with circular trac dependencies.


---

Comment by burcin created at 2009-05-05 23:30:13

The necessary changes for pynac, i.e., attachment:pynac-hash_exception.patch, is included in the new package for pynac-0.1.6 at #5777. The doctests in attachment:5546_doctests.patch are also posted in #5777.

This now introduces a circular dependency in trac. I hope this won't cause problems, since all these patches will go in together. Faster reviews in the future may prevent this from happening again.


Note that only:

 * attachment:trac_5546-1-pynac_matrix_vector.patch
 * attachment:trac_5546-2-pynac_derivative.patch

needs to be applied from this ticket.


---

Comment by burcin created at 2009-05-24 16:38:49

Some variants of these patches seem to be in 4.0.rc0. This bug should be closed. Trac doesn't allow me to close bugs any more though.


---

Comment by mhansen created at 2009-05-26 16:21:39

Resolution: fixed


---

Comment by mhansen created at 2009-05-26 16:21:39

This was fixed by #5777 and #5390
