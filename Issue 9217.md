# Issue 9217: Taylor expansion of gamma functions is broken

Issue created by migration from https://trac.sagemath.org/ticket/9217

Original creator: tomc

Original creation time: 2010-06-11 18:01:35

Assignee: tomc

Keywords: symbolic calculus, gamma function, taylor expansion

Taylor expansion of the gamma function often causes an error.  
This example works:


```
sage: taylor(gamma(1/2+x),x,0,2)
1/4*(pi^2 + 2*euler_gamma^2 + 8*euler_gamma*log(2) + 8*log(2)^2)*sqrt(pi)*x^2 - (euler_gamma + 2*log(2))*sqrt(pi)*x + sqrt(pi)
```


but this doesn't:


```
sage: taylor(gamma(1/3+x),x,0,2)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1254, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/tomc/sage-4.4.1/<ipython console> in <module>()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/calculus/functional.pyc in taylor(f, *args)
    369     if not isinstance(f, Expression):
    370         f = SR(f)
--> 371     return f.taylor(*args)
    372 
    373 def expand(x, *args, **kwds):

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.taylor (sage/symbolic/expression.cpp:13236)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4053)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/interfaces/maxima.pyc in _symbolic_(self, R)
   1810             sqrt(2)
   1811         """
-> 1812         return R(self._sage_())
   1813 
   1814     def __complex__(self):

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/interfaces/maxima.pyc in _sage_(self)
   1791         import sage.calculus.calculus as calculus
   1792         return calculus.symbolic_expression_from_maxima_string(self.name(),
-> 1793                 maxima=self.parent())
   1794 
   1795     def _symbolic_(self, R):

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_expression_from_maxima_string(x, equals_sub, maxima)
   1526         return symbolic_expression_from_string(s, syms, accept_sequence=True)
   1527     except SyntaxError:
-> 1528         raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s
   1529     finally:
   1530         is_simplified = False

TypeError: unable to make sense of Maxima expression 'gamma(1/3)-(6*euler_gamma+pi*sqrt(3)+9*log(3))*gamma(1/3)*x/6+(12*gamma(1/3)*psi[1](1/3)+(12*euler_gamma^2+(4*pi*sqrt(3)+36*log(3))*euler_gamma+6*log(3)*pi*sqrt(3)+pi^2+27*log(3)^2)*gamma(1/3))*x^2/24' in Sage
```


This occurs because when parsing the output from Maxima we should replace all occurrences of the polygamma function psi[n](foo) by 
psi(n,foo).

I am running Sage 4.4.1 on Mac OS X version 10.6 (Snow Leopard), built from source.  But the second example also fails on Sage 4.3.5 on 64-bit Linux, built from source.  Looking at the source code suggests that the second example will fail on all platforms.  




---

Comment by tomc created at 2010-06-11 18:17:36

Changing status from new to needs_review.


---

Comment by tomc created at 2010-06-11 18:17:36

I uploaded a patch to fix this.


---

Comment by tomc created at 2010-06-11 18:35:20

revised patch also changes the AUTHORS block to match the format suggested in the Developer's Guide


---

Attachment

It looks like the patch just changes the AUTHORS block and doesn't have the actual fix for the problem in it.


---

Comment by tomc created at 2010-06-11 19:39:06

Replying to [comment:2 mhansen]:
> It looks like the patch just changes the AUTHORS block and doesn't have the actual fix for the problem in it.

Argh!  Will upload new patch.


---

Attachment


---

Attachment


---

Comment by tomc created at 2010-06-11 19:58:07

OK, sorry about that.  I uploaded 2 patches.  The first one:

trac_9217-fix-1.patch

fixes the problem with Taylor expanding gamma functions.  The second one:

trac_9217-fix-2.patch

should be applied after the first one, and fixes the AUTHOR block.


---

Comment by mhansen created at 2010-06-11 20:46:01

Resolution: fixed


---

Comment by mhansen created at 2010-06-11 20:46:01

Looks good to me.
