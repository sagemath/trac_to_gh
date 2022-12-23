# Issue 1158: mathematical functions should remain symbolic

Issue created by migration from https://trac.sagemath.org/ticket/1158

Original creator: zimmerma

Original creation time: 2007-11-12 22:07:27

Assignee: was

Some mathematical functions automatically evaluate to floating-point, even for a symbolic input
(integer or variable):


```
sage: Ei(10)
2492.22897624
sage: bessel_J(0,10)
-0.245935764451348
sage: bessel_J(0,x)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/gmp-4.2.2/tune/<ipython console> in <module>()

/usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/functions/special.py in bessel_J(nu, z, alg, prec)
    492         else:
    493             K,a = _setup(prec)
--> 494         b = K(nu.besselj(z))
    495         pari.set_real_precision(a)
    496         return b

/tmp/gmp-4.2.2/tune/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()

/tmp/gmp-4.2.2/tune/real_mpfr.pyx in sage.rings.real_mpfr.RealNumber._set()

<type 'exceptions.TypeError'>: Unable to convert x (='1-1/4*x^2+1/64*x^4-1/2304*x^6+1/147456*x^8-1/14745600*x^10+1/2123366400*x^12-1/416179814400*x^14+1/106542032486400*x^16+O(x^17)') to real number.
```


In my opinion, foo(10) should evaluate to foo(10), and similarly foo(x).


---

Comment by mhansen created at 2008-01-27 02:09:26

This requires going through and look at all the numerical (special) functions we have an making a SymbolicFunction wrapper class around them.  Some thoughts need to be given how to handle the case where we have a function that Maxima does not.


---

Comment by gfurnish created at 2008-03-23 18:37:56

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-23 18:38:01

Changing status from new to assigned.


---

Comment by burcin created at 2009-04-24 12:57:28

This is fixed in the new symbolics with #5777.


---

Comment by mvngu created at 2009-07-26 05:15:52

What is the status of this ticket? Can it be closed as fixed? In Sage 4.1, I get this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Ei(10)
2492.22897624
sage: bessel_J(0,10)
-0.245935764451348
sage: bessel_J(0,x)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1171, 0))
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/12800/_home_mvngu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)
    753             C = ComplexField(prec)
    754             nu = C(nu)
--> 755             z = C(z)
    756             K = C
    757         if nu == 0:

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_field.pyc in __call__(self, x, im)
    265         if im is not None:
    266             x = x, im
--> 267         return Parent.__call__(self, x)
    268 
    269     def _element_constructor_(self, x):

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_field.pyc in _element_constructor_(self, x)
    289 
    290             try:
--> 291                 return x._complex_mpfr_field_( self )
    292             except AttributeError:
    293                 pass

/usr/local/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._complex_mpfr_field_ (sage/symbolic/expression.cpp:5371)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._eval_self (sage/symbolic/expression.cpp:4825)()

TypeError: Cannot evaluate symbolic expression to a numeric value.
```



---

Comment by zimmerma created at 2009-07-27 06:08:38

> What is the status of this ticket? Can it be closed as fixed?

no, the status is still the same (here with 3.4 since I cannot compile 4.1 from source on my laptop, but I guess the behaviour
in 4.1 is still the same):

```
sage: sin(10)
sin(10)
sage: Ei(10)
2492.22897624
sage: sin(x)
sin(x)
sage: Ei(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/zimmerma/.sage/temp/toto.loria.fr/6274/_home_zimmerma__sage_init_sage_0.py in <module>()

/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/functions/transcendental.pyc in Ei(z)

TypeError: complex() argument must be a string or a number
```

To be coherent, Ei(10) should return Ei(10) as sin(10) returns sin(10), and Ei(x) should return Ei(x) as sin(x) does return sin(x).


---

Comment by mvngu created at 2009-07-27 06:13:47

OK, I get the same inconsistent behaviour:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sin(10)
sin(10)
sage: Ei(10)
2492.22897624
sage: sin(x)
sin(x)
sage: Ei(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/.sage/temp/sage.math.washington.edu/32665/_home_mvngu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/functions/transcendental.pyc in Ei(z)
    261     """
    262     import scipy.special, math
--> 263     return CDF(-scipy.special.exp1(-complex(z)) + complex(0,math.pi))
    264 
    265 def Li(x, eps_rel=None, err_bound=False):

/usr/local/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__complex__ (sage/symbolic/expression.cpp:5609)()

TypeError: unable to simplify to complex approximation
```



---

Comment by kcrisman created at 2009-12-10 05:26:11

Changing component from calculus to symbolics.


---

Comment by kcrisman created at 2009-12-10 05:26:11

Note that Pynac does have a lot of our as-yet-un-symbolic functions available, though not all, so this is a feasible goal.


---

Comment by zimmerma created at 2010-02-05 20:47:22

any progress on that issue?


---

Comment by mhansen created at 2010-02-05 22:13:23

Hi Paul,

I could work on this if you need/want things for your talk.  It really is just a matter of going through the functions one by one and switching them over / adding more features.


---

Comment by zimmerma created at 2010-02-07 20:56:06

Hi Mike,

my talk is over, see http://www.loria.fr/~zimmerma/talks/sage-20100204.pdf (in french).
However it would be useful to fix that issue. If you can describe what is needed to
fix a particular function, then we could share the work.

Paul


---

Comment by burcin created at 2010-02-07 21:31:40

Hi Paul,

#7748 has patches that make `Ei()` and `gamma_inc()` symbolic. The conversion process is not very smooth yet, but we're getting there slowly. My deadline for the conversion of all the functions to new symbolics and addition of other special functions is the [Sage Days 24](http://wiki.sagemath.org/days24) workshop at RISC. Hopefully then we can get Sage included in [the software list of the DLMF](http://dlmf.nist.gov/software/).

Any help is greatly appreciated of course.


---

Comment by kcrisman created at 2012-01-26 02:59:01

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-01-26 03:02:29

We now have

```
sage: Ei(10)
Ei(10)
```

but the rest aren't there yet...

But the problem is that this ticket is WAY too broad, at least in the current framework of how we deal with tickets.  We now have an entire [metapage on the wiki](symbolics-functions) devoted to this topic!   Bessel J is #4102, log gamma is #10075, etc.  

So I recommend that this ticket be closed as far too broad (in retrospect - somehow it seemed easier two years ago!) and adequately replaced by a slew of tickets already opened.


---

Comment by kcrisman created at 2012-01-26 03:02:29

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-31 09:37:13

Resolution: invalid
