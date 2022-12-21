# Issue 1773: piecewise functions and integration / arithmetic do not play well together

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-14 06:02:44

Assignee: was

CC:  kcrisman jondo vbraun slelievre mkoeppe eviatarbach rws


```
On 1/13/08, Hector Villafuerte <> wrote:
> 
> I defined a piecewise function (specifically, a triangular wave) like this:
> 
> sage: f1(x) = -abs(x) + 1
> sage: f2(x) = abs(x - 2) - 1
> sage: tri_wave = piecewise([ [(-1,1), f1], [(1,3), f2]])
> 
> One can plot it and it looks very nice:
> 
> sage: tri_wave.plot()
> 
> But while calculating this integral I get "ValueError: Value not
> defined outside of domain."
> 
> sage: integrate(tri_wave(x)^2, x, -1, 3)
> 
> Is there a way to integrate piecewise-defined functions?
> As always, thanks for your help,

This is clearly broken.  As a band-aide, you can at least
numerically integrate as follows:

sage: integral_numerical(lambda x: tri_wave(x)^2, -1, 3)
(1.3333333333333333, 1.4765966227514582e-14)

The first output (1.3333...) is the answer, and the second is an error bound.

 -- William
```



---

Comment by gfurnish created at 2008-03-16 20:11:06

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:11:06

Changing status from new to assigned.


---

Comment by rlm created at 2009-01-22 07:04:27

This isn't specific to integrate. The problem is that piecewise functions don't play well with *symbolics*


```
sage: f1(x) = -abs(x) + 1
sage: f2(x) = abs(x - 2) - 1
sage: tri_wave = piecewise([ [(-1,1), f1], [(1,3), f2]])
sage: tri_wave(x)
SAME ERROR
```



---

Comment by rlm created at 2009-01-22 07:51:41

What should maybe happen is in piecewise.py, in the `__call__` method, if a SymbolicVariable is passed in as `x0`, it should return a CallableSymbolicExpression which just in turn calls back to the `__call__` method again. Does this sound reasonable? If so, how would one implement this?


---

Comment by kcrisman created at 2011-08-15 14:36:48

See also #11225, which is about plotting - but sometimes this stuff causes plots to not work, of course.


---

Comment by kcrisman created at 2011-08-15 14:38:41

Replying to [comment:2 rlm]:
> This isn't specific to integrate. The problem is that piecewise functions don't play well with *symbolics*
> 
> {{{
> sage: f1(x) = -abs(x) + 1
> sage: f2(x) = abs(x - 2) - 1
> sage: tri_wave = piecewise([ [(-1,1), f1], [(1,3), f2]])
> sage: tri_wave(x)
> SAME ERROR
> }}}

Or see what happens when we try to multiply piecewise and symbolic.

```
sage: f = Piecewise([[(0,pi/2),-1],[(pi/2,pi),2]]) 
sage: f*sin(x)
---------------------------------------------------------------------------
AttributeError              
```



---

Comment by mkoeppe created at 2016-06-25 17:32:14

While all the examples appearing in the comments are fixed with the new `piecewise` of #14801, the original bug example still fails (but with a different error message). 

Cc'ing #14801's cc list.


```
sage: f1(x) = -abs(x) + 1
sage: f2(x) = abs(x - 2) - 1
sage: tri_wave = piecewise([ [(-1,1), f1], [(1,3), f2]])
sage: tri_wave.plot()
Launched png viewer for Graphics object consisting of 1 graphics primitive
sage: integrate(tri_wave(x)^2, x, -1, 3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-9387c34a513c> in <module>()
----> 1 integrate(tri_wave(x)**Integer(2), x, -Integer(1), Integer(3))

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/misc/functional.py in integral(x, *args, **kwds)
    663     """
    664     if hasattr(x, 'integral'):
--> 665         return x.integral(*args, **kwds)
    666     else:
    667         from sage.symbolic.ring import SR

/Users/mkoeppe/cvs/sage/src/sage/symbolic/expression.pyx in sage.symbolic.expression.Expression.integral (/Users/mkoeppe/cvs/sage/src/build/cythonized/sage/symbolic/expression.cpp:60225)()
  11484                     R = ring.SR
  11485             return R(integral(f, v, a, b, **kwds))
> 11486         return integral(self, *args, **kwds)
  11487 
  11488     integrate = integral

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/symbolic/integration/integral.py in integrate(expression, v, a, b, algorithm, hold)
    763         return indefinite_integral(expression, v, hold=hold)
    764     else:
--> 765         return definite_integral(expression, v, a, b, hold=hold)
    766 
    767 integral = integrate

/Users/mkoeppe/cvs/sage/src/sage/symbolic/function.pyx in sage.symbolic.function.BuiltinFunction.__call__ (/Users/mkoeppe/cvs/sage/src/build/cythonized/sage/symbolic/function.cpp:11170)()
    970             res = self._evalf_try_(*args)
    971             if res is None:
--> 972                 res = super(BuiltinFunction, self).__call__(
    973                         *args, coerce=coerce, hold=hold)
    974 

/Users/mkoeppe/cvs/sage/src/sage/symbolic/function.pyx in sage.symbolic.function.Function.__call__ (/Users/mkoeppe/cvs/sage/src/build/cythonized/sage/symbolic/function.cpp:6921)()
    481             for i from 0 <= i < len(args):
    482                 vec.push_back((<Expression>args[i])._gobj)
--> 483             res = g_function_evalv(self._serial, vec, hold)
    484         elif self._nargs == 1:
    485             res = g_function_eval1(self._serial,

/Users/mkoeppe/cvs/sage/src/sage/symbolic/function.pyx in sage.symbolic.function.BuiltinFunction._evalf_or_eval_ (/Users/mkoeppe/cvs/sage/src/build/cythonized/sage/symbolic/function.cpp:12417)()
   1059         res = self._evalf_try_(*args)
   1060         if res is None:
-> 1061             return self._eval0_(*args)
   1062         else:
   1063             return res

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/symbolic/integration/integral.py in _eval_(self, f, x, a, b)
    176         for integrator in self.integrators:
    177             try:
--> 178                 return integrator(*args)
    179             except NotImplementedError:
    180                 pass

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/symbolic/integration/external.py in maxima_integrator(expression, v, a, b)
     22         result = maxima.sr_integral(expression,v)
     23     else:
---> 24         result = maxima.sr_integral(expression, v, a, b)
     25     return result._sage_()
     26 

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/interfaces/maxima_lib.py in sr_integral(self, *args)
    796         """
    797         try:
--> 798             return max_to_sr(maxima_eval(([max_integrate],[sr_to_max(SR(a)) for a in args])))
    799         except RuntimeError as error:
    800             s = str(error)

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/interfaces/maxima_lib.py in max_to_sr(expr)
   1634         op_max=caar(expr)
   1635         if op_max in special_max_to_sage:
-> 1636             return special_max_to_sage[op_max](expr)
   1637         if not(op_max in max_op_dict):
   1638             op_max_str=maxprint(op_max).python()[1:-1]

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/interfaces/maxima_lib.py in dummy_integrate(expr)
   1428         integrate(f(x), x, 0, 10)
   1429     """
-> 1430     args=[max_to_sr(a) for a in cdr(expr)]
   1431     if len(args) == 4 :
   1432         return sage.symbolic.integration.integral.definite_integral(*args,

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/interfaces/maxima_lib.py in max_to_sr(expr)
   1651             op=max_op_dict[op_max]
   1652         max_args=cdr(expr)
-> 1653         args=[max_to_sr(a) for a in max_args]
   1654         return op(*args)
   1655     elif expr.symbolp():

/Users/mkoeppe/cvs/sage/local/lib/python2.7/site-packages/sage/interfaces/maxima_lib.py in max_to_sr(expr)
   1652         max_args=cdr(expr)
   1653         args=[max_to_sr(a) for a in max_args]
-> 1654         return op(*args)
   1655     elif expr.symbolp():
   1656         if not(expr in max_sym_dict):

TypeError: __call__() takes exactly 2 arguments (3 given)
```



---

Comment by rws created at 2016-06-26 15:23:23

The problem on first sight here is that operations on `piecewise` do not get translated to what is expected, i.e., squaring the pieces. Also it seems that Maxima does not convert them, nor is it considering loading `pw.mac` without which it simply knows nothing about piecewise functions. So we must either load this package when encountering `piecewise` in the Maxima interface then convert, or the expression must be simplified, i.e., the operations applied piecewise, probably by Pynac. Or both.

Of course, the `integral` member function is accessible with pure `piecewise` objects:

```
sage: tri_wave1 = piecewise([ [(-1,1), f1^2], [(1,3), f2^2]])
sage: tri_wave1.integral(definite=True)
4/3
```



---

Comment by mforets created at 2017-05-07 19:25:32

`@`rws: does adding a new `__pow__` method in piecewise fix the issue or not? (cf. code+test added in this branch)


----


... well it doesn't work for the OP problem, but that's another thing (misuse?) i guess, since:


```
sage: integrate(piecewise([ [(-1,1), x], [(1,3), x^2]]), x, -1, 3)
...
ValueError: point 3 is not in the domain
```


although


```
sage: integrate(piecewise([ [(-1,1), x], [(1,3), x^2]]), x)
piecewise(x|-->1/2*x^2 - 1/2 on (-1, 1), x|-->1/3*x^3 - 1/3 on (1, 3); x)
```


and with the current patch one has:


```
sage: integrate(piecewise([ [(-1,1), x], [(1,3), x^2]])**2, x)
piecewise(x|-->1/3*x^3 + 1/3 on (-1, 1), x|-->1/5*x^5 + 7/15 on (1, 3); x)
```

----
New commits:


---

Comment by mforets created at 2017-05-07 19:25:32

Changing status from new to needs_review.


---

Comment by mforets created at 2017-05-07 19:31:34

Hmmm, what i've uploaded doesn't work well with symbolic expressions as exponents!


```
sage: f = piecewise([ [(-1,1), x], [(1,3), x^2]])
sage: k = var('k')
sage: f**k
piecewise(k|-->x^k on (-1, 1), k|-->(x^2)^k on (1, 3); k)
```


the independent variable is misunderstood.


---

Comment by rws created at 2017-05-08 06:16:30

This seems to depend on if the expression contains a lexicographically earlier symbol:

```
sage: f^y
piecewise(x|-->x^y on (-1, 1), x|-->(x^2)^y on (1, 3); x)
sage: f^k
piecewise(k|-->x^k on (-1, 1), k|-->(x^2)^k on (1, 3); k)
sage: f^z
piecewise(x|-->x^z on (-1, 1), x|-->(x^2)^z on (1, 3); x)
sage: f^t
piecewise(t|-->x^t on (-1, 1), t|-->(x^2)^t on (1, 3); t)
```



---

Comment by git created at 2017-05-08 13:58:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mforets created at 2017-05-08 14:01:13

Replying to [comment:17 rws]:
> This seems to depend on if the expression contains a lexicographically earlier symbol:
> {{{
> sage: f^y
> piecewise(x|-->x^y on (-1, 1), x|-->(x<sup>2)</sup>y on (1, 3); x)
> sage: f^k
> piecewise(k|-->x^k on (-1, 1), k|-->(x<sup>2)</sup>k on (1, 3); k)
> sage: f^z
> piecewise(x|-->x^z on (-1, 1), x|-->(x<sup>2)</sup>z on (1, 3); x)
> sage: f^t
> piecewise(t|-->x^t on (-1, 1), t|-->(x<sup>2)</sup>t on (1, 3); t)
> }}}

Ok, i see. as a workaround i've specified the `var` argument to the constructor, which gives the same result as `self.variables()[0]`.


---

Comment by chapoton created at 2018-05-05 07:25:20

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2018-05-05 07:25:20

does not apply


---

Comment by git created at 2018-05-31 11:37:27

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by vdelecroix created at 2018-08-03 19:20:18

update milestone 8.3 -> 8.4


---

Comment by chapoton created at 2018-12-17 19:38:15

New commits:


---

Comment by chapoton created at 2018-12-17 19:38:15

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2018-12-17 20:28:18

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2018-12-23 23:41:12

Resolution: fixed
