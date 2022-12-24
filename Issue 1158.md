# Issue 1158: mathematical functions should remain symbolic

archive/issues_001158.json:
```json
{
    "body": "Assignee: was\n\nSome mathematical functions automatically evaluate to floating-point, even for a symbolic input\n(integer or variable):\n\n\n```\nsage: Ei(10)\n2492.22897624\nsage: bessel_J(0,10)\n-0.245935764451348\nsage: bessel_J(0,x)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/tmp/gmp-4.2.2/tune/<ipython console> in <module>()\n\n/usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/functions/special.py in bessel_J(nu, z, alg, prec)\n    492         else:\n    493             K,a = _setup(prec)\n--> 494         b = K(nu.besselj(z))\n    495         pari.set_real_precision(a)\n    496         return b\n\n/tmp/gmp-4.2.2/tune/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__()\n\n/tmp/gmp-4.2.2/tune/real_mpfr.pyx in sage.rings.real_mpfr.RealNumber._set()\n\n<type 'exceptions.TypeError'>: Unable to convert x (='1-1/4*x^2+1/64*x^4-1/2304*x^6+1/147456*x^8-1/14745600*x^10+1/2123366400*x^12-1/416179814400*x^14+1/106542032486400*x^16+O(x^17)') to real number.\n```\n\n\nIn my opinion, foo(10) should evaluate to foo(10), and similarly foo(x).\n\nIssue created by migration from https://trac.sagemath.org/ticket/1158\n\n",
    "created_at": "2007-11-12T22:07:27Z",
    "labels": [
        "calculus",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "mathematical functions should remain symbolic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1158",
    "user": "zimmerma"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/1158





---

archive/issue_comments_007066.json:
```json
{
    "body": "This requires going through and look at all the numerical (special) functions we have an making a SymbolicFunction wrapper class around them.  Some thoughts need to be given how to handle the case where we have a function that Maxima does not.",
    "created_at": "2008-01-27T02:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7066",
    "user": "mhansen"
}
```

This requires going through and look at all the numerical (special) functions we have an making a SymbolicFunction wrapper class around them.  Some thoughts need to be given how to handle the case where we have a function that Maxima does not.



---

archive/issue_comments_007067.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-23T18:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7067",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_007068.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-23T18:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7068",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007069.json:
```json
{
    "body": "This is fixed in the new symbolics with #5777.",
    "created_at": "2009-04-24T12:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7069",
    "user": "burcin"
}
```

This is fixed in the new symbolics with #5777.



---

archive/issue_comments_007070.json:
```json
{
    "body": "What is the status of this ticket? Can it be closed as fixed? In Sage 4.1, I get this:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: Ei(10)\n2492.22897624\nsage: bessel_J(0,10)\n-0.245935764451348\nsage: bessel_J(0,x)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1171, 0))\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/mvngu/.sage/temp/sage.math.washington.edu/12800/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)\n    753             C = ComplexField(prec)\n    754             nu = C(nu)\n--> 755             z = C(z)\n    756             K = C\n    757         if nu == 0:\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_field.pyc in __call__(self, x, im)\n    265         if im is not None:\n    266             x = x, im\n--> 267         return Parent.__call__(self, x)\n    268 \n    269     def _element_constructor_(self, x):\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_field.pyc in _element_constructor_(self, x)\n    289 \n    290             try:\n--> 291                 return x._complex_mpfr_field_( self )\n    292             except AttributeError:\n    293                 pass\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._complex_mpfr_field_ (sage/symbolic/expression.cpp:5371)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._eval_self (sage/symbolic/expression.cpp:4825)()\n\nTypeError: Cannot evaluate symbolic expression to a numeric value.\n```\n",
    "created_at": "2009-07-26T05:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7070",
    "user": "mvngu"
}
```

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

archive/issue_comments_007071.json:
```json
{
    "body": "> What is the status of this ticket? Can it be closed as fixed?\n\nno, the status is still the same (here with 3.4 since I cannot compile 4.1 from source on my laptop, but I guess the behaviour\nin 4.1 is still the same):\n\n```\nsage: sin(10)\nsin(10)\nsage: Ei(10)\n2492.22897624\nsage: sin(x)\nsin(x)\nsage: Ei(x)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/zimmerma/.sage/temp/toto.loria.fr/6274/_home_zimmerma__sage_init_sage_0.py in <module>()\n\n/usr/local/sage-3.4/sage/local/lib/python2.5/site-packages/sage/functions/transcendental.pyc in Ei(z)\n\nTypeError: complex() argument must be a string or a number\n```\n\nTo be coherent, Ei(10) should return Ei(10) as sin(10) returns sin(10), and Ei(x) should return Ei(x) as sin(x) does return sin(x).",
    "created_at": "2009-07-27T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7071",
    "user": "zimmerma"
}
```

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

archive/issue_comments_007072.json:
```json
{
    "body": "OK, I get the same inconsistent behaviour:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sin(10)\nsin(10)\nsage: Ei(10)\n2492.22897624\nsage: sin(x)\nsin(x)\nsage: Ei(x)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mvngu/.sage/temp/sage.math.washington.edu/32665/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/functions/transcendental.pyc in Ei(z)\n    261     \"\"\"\n    262     import scipy.special, math\n--> 263     return CDF(-scipy.special.exp1(-complex(z)) + complex(0,math.pi))\n    264 \n    265 def Li(x, eps_rel=None, err_bound=False):\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__complex__ (sage/symbolic/expression.cpp:5609)()\n\nTypeError: unable to simplify to complex approximation\n```\n",
    "created_at": "2009-07-27T06:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7072",
    "user": "mvngu"
}
```

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

archive/issue_comments_007073.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2009-12-10T05:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7073",
    "user": "kcrisman"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_007074.json:
```json
{
    "body": "Note that Pynac does have a lot of our as-yet-un-symbolic functions available, though not all, so this is a feasible goal.",
    "created_at": "2009-12-10T05:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7074",
    "user": "kcrisman"
}
```

Note that Pynac does have a lot of our as-yet-un-symbolic functions available, though not all, so this is a feasible goal.



---

archive/issue_comments_007075.json:
```json
{
    "body": "any progress on that issue?",
    "created_at": "2010-02-05T20:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7075",
    "user": "zimmerma"
}
```

any progress on that issue?



---

archive/issue_comments_007076.json:
```json
{
    "body": "Hi Paul,\n\nI could work on this if you need/want things for your talk.  It really is just a matter of going through the functions one by one and switching them over / adding more features.",
    "created_at": "2010-02-05T22:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7076",
    "user": "mhansen"
}
```

Hi Paul,

I could work on this if you need/want things for your talk.  It really is just a matter of going through the functions one by one and switching them over / adding more features.



---

archive/issue_comments_007077.json:
```json
{
    "body": "Hi Mike,\n\nmy talk is over, see http://www.loria.fr/~zimmerma/talks/sage-20100204.pdf (in french).\nHowever it would be useful to fix that issue. If you can describe what is needed to\nfix a particular function, then we could share the work.\n\nPaul",
    "created_at": "2010-02-07T20:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7077",
    "user": "zimmerma"
}
```

Hi Mike,

my talk is over, see http://www.loria.fr/~zimmerma/talks/sage-20100204.pdf (in french).
However it would be useful to fix that issue. If you can describe what is needed to
fix a particular function, then we could share the work.

Paul



---

archive/issue_comments_007078.json:
```json
{
    "body": "Hi Paul,\n\n#7748 has patches that make `Ei()` and `gamma_inc()` symbolic. The conversion process is not very smooth yet, but we're getting there slowly. My deadline for the conversion of all the functions to new symbolics and addition of other special functions is the [Sage Days 24](http://wiki.sagemath.org/days24) workshop at RISC. Hopefully then we can get Sage included in [the software list of the DLMF](http://dlmf.nist.gov/software/).\n\nAny help is greatly appreciated of course.",
    "created_at": "2010-02-07T21:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7078",
    "user": "burcin"
}
```

Hi Paul,

#7748 has patches that make `Ei()` and `gamma_inc()` symbolic. The conversion process is not very smooth yet, but we're getting there slowly. My deadline for the conversion of all the functions to new symbolics and addition of other special functions is the [Sage Days 24](http://wiki.sagemath.org/days24) workshop at RISC. Hopefully then we can get Sage included in [the software list of the DLMF](http://dlmf.nist.gov/software/).

Any help is greatly appreciated of course.



---

archive/issue_comments_007079.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-26T02:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7079",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_007080.json:
```json
{
    "body": "We now have\n\n```\nsage: Ei(10)\nEi(10)\n```\n\nbut the rest aren't there yet...\n\nBut the problem is that this ticket is WAY too broad, at least in the current framework of how we deal with tickets.  We now have an entire [metapage on the wiki](symbolics-functions) devoted to this topic!   Bessel J is #4102, log gamma is #10075, etc.  \n\nSo I recommend that this ticket be closed as far too broad (in retrospect - somehow it seemed easier two years ago!) and adequately replaced by a slew of tickets already opened.",
    "created_at": "2012-01-26T03:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7080",
    "user": "kcrisman"
}
```

We now have

```
sage: Ei(10)
Ei(10)
```

but the rest aren't there yet...

But the problem is that this ticket is WAY too broad, at least in the current framework of how we deal with tickets.  We now have an entire [metapage on the wiki](symbolics-functions) devoted to this topic!   Bessel J is #4102, log gamma is #10075, etc.  

So I recommend that this ticket be closed as far too broad (in retrospect - somehow it seemed easier two years ago!) and adequately replaced by a slew of tickets already opened.



---

archive/issue_comments_007081.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-26T03:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7081",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007082.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-01-31T09:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1158#issuecomment-7082",
    "user": "jdemeyer"
}
```

Resolution: invalid
