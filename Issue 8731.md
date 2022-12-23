# Issue 8731: update maxima to 5.21.0

Issue created by migration from https://trac.sagemath.org/ticket/8731

Original creator: jason

Original creation time: 2010-04-20 19:32:25

Assignee: tbd

CC:  kcrisman robert.marik mhansen

This update fixes #8729.  It also includes the fixes noted in #8645 (so this spkg supersedes the maxima spkg at #8645).

The spkg is up at http://sage.math.washington.edu/home/jason/maxima-5.21.0.spkg

A patch needs to be applied to fix some doctests.  In particular, apparently maxima has gotten better at integration.


---

Comment by kcrisman created at 2010-04-20 19:41:15

Just a comment:

```
### maxima-5.21.0 (Jason Grout, 20 APR 2009)
```

is not in the style of the other items in the changelog, where it would be April 20th, 2009.  Actually, it would be April 20th, 2010, but who's counting?


---

Comment by jason created at 2010-04-20 19:54:03

Replying to [comment:1 kcrisman]:
> Just a comment:
> {{{
> === maxima-5.21.0 (Jason Grout, 20 APR 2009) ===
> }}}
> is not in the style of the other items in the changelog, where it would be April 20th, 2009.  Actually, it would be April 20th, 2010, but who's counting?

There are no less than three different styles in the other dates in the changelog, so apparently it's okay to have inconsistent date styles, so I did the dates in a much more standard notation.  However, I'll change it to spell out April since the date is wrong anyway.


---

Comment by jason created at 2010-04-20 20:01:29

Here are the doctests that are broken for me with this spkg:


```

        sage -t  -long 4.3.5/devel/sage/sage/misc/functional.py # 2 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/symbolic/relation.py # 7 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/symbolic/integration/integral.py # 6 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/symbolic/expression.pyx # 3 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/interfaces/maxima.py # 8 doctests failed
```



---

Comment by jason created at 2010-04-20 20:03:31

I've uploaded a new spkg with the changelog date now the correct date (and formatted as 20 April 2010)


---

Comment by jason created at 2010-04-20 20:07:41

For the doctests that return binomial(n,n) instead of 1, we just have to put an assumption in: assume(n>0)


---

Comment by jason created at 2010-04-20 20:07:47

Changing status from new to needs_work.


---

Comment by kcrisman created at 2010-04-27 19:59:45

I had the following problem while trying to install this on Sage 4.4:

```
; registering #<SYSTEM :MAXIMA 4321148288> as MAXIMA
An error occurred during initialization:
Unknown keyword :MOVE-HERE.

installing Maxima library as /Users/karl-dietercrisman/Desktop/sage-4.4/local/lib/ecl//maxima.fas
cp: maxima.fasb: No such file or directory
***********************************************************
Failed to install maxima.fasb as a library
***********************************************************
```

Nonetheless, I get Maxima 5.21.0 in the console, and the various binomial(n,n) errors you mention, so maybe something went right?


---

Comment by was created at 2010-04-28 18:53:34

(1) Now the latest maxima is 5.21.1

(2) This should be done in conjunction with upgrading ECL. See #8808.  The maxima in sage-4.4 doesn't build with ecl-10.4.1, but Maxima 5.21.1 *does* build fine on top of ECL-10.4.1.

A new spkg is here (but, again, first install the ECL spkg from #8808 when testing this):

    http://wstein.org/home/wstein/patches/maxima-5.21.1.spkg


---

Comment by was created at 2010-04-28 18:54:06

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-04-28 19:01:14

Question: Does this still incorporate the fixes mentioned in the Description? I assume it still needs doctest fixes due to improvements.


---

Comment by kcrisman created at 2010-04-28 19:12:21

I still get 

```
installing Maxima library as /Users/karl-dietercrisman/Desktop/sage-4.4/local/lib/ecl//maxima.fas
cp: maxima.fasb: No such file or directory
```

though I no longer get the unknown keyword error.  maxima_console() does give me 5.21.1.  Testing now.


---

Comment by was created at 2010-04-28 19:23:15

With 5.21.1 Maxima and 10.4.1 ECL, the new failure list is:

```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/symbolic/expression.pyx # 3 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py # 0 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed
        sage -t  devel/sage/sage/calculus/calculus.py # 2 doctests failed
        sage -t  devel/sage/sage/interfaces/maxima.py # 8 doctests failed
        sage -t  devel/sage/sage/misc/functional.py # 2 doctests failed
        sage -t  devel/sage/sage/symbolic/relation.py # 7 doctests failed
        sage -t  devel/sage/sage/symbolic/integration/integral.py # 6 doctests failed
        sage -t  devel/sage/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 358.3 seconds
                                             
```


See http://sage.math.washington.edu/home/wstein/build/san_diego/sage-4.4/8731.out for the complete doctest run.


---

Comment by robert.marik created at 2010-04-28 22:49:38

Replying to [comment:12 was]:
> 
> See http://sage.math.washington.edu/home/wstein/build/san_diego/sage-4.4/8731.out for the complete doctest run. 

Oops, seems that solving inequalities is completely broken with this new version of Maxima.


---

Comment by kcrisman created at 2010-04-29 00:38:58

Yes, though I wouldn't say completely broken, since not every doctest fails, correct?  

Other issues:

In symbolic/integration/integral.py, there is one integral which has been improved, and one which seems to affected by the rational approximation thing, but wasn't before.   There is also an integral (in that file, I think) which Maxima can now do, and we need to replace it with one Maxima can't do.  There is also a slight change in the numeric value because of this, but that wasn't the  point of that doctest.

The binomial issue seems easy to fix, but apparently now binomial(n,n)=1 for all n in Sage, but not in Maxima.  Should we change Sage, or do what Jason recommends (assume n>0 or something)?

And in interfaces/maxima.py there are a lot of erros where Maxima loads like

```
    ;;; Loading #P".../local/lib/ecl/cmp.fas"
    ;;; Loading #P".../local/lib/ecl/sysfun.lsp"
```

as well as of course the Maxima version being wrong and, oddly, the following:

```
sage: maxima.eval('sage0: x == x;')
Expected <Error>
Got:
    'x'
```

which is not good at all if real, but maybe just means Maxima changed something minor?

The plot3d one is not too significant, I think.  I haven't looked at the other ones.

Anyway, obviously 'needs work' until someone posts a fairly comprehensive patch.


---

Comment by kcrisman created at 2010-04-29 00:38:58

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-04-29 00:44:12

Also, the spkg-install for the most recent spkg does not include the fix from #8645, as opposed to the one Jason posted.  That is crucial to close this ticket.


---

Comment by robert.marik created at 2010-04-29 19:11:51

Reported the problem with [solve_rat_ineq](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/30696) in Maxima forum, (problem probably in algsys and realonly)


---

Comment by robert.marik created at 2010-04-30 04:34:55

Replying to [comment:17 robert.marik]:
> Reported the problem with [solve_rat_ineq](http://thread.gmane.org/gmane.comp.mathematics.maxima.general/30696) in Maxima forum, (problem probably in algsys and realonly)
.... and it is already fixed in the CVS version (one-line fix)


---

Comment by jason created at 2010-05-13 04:24:49

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-05-13 04:24:49

A new spkg is up at: http://sage.math.washington.edu/home/jason/maxima-5.21.1.spkg

This spkg includes the upstream bugfix for the solve_rat_ineq issue noted above.


---

Comment by jason created at 2010-05-13 04:25:17

My 5.21.1 spkg also includes the fixes noted in the description.


---

Comment by jason created at 2010-05-13 04:33:59

This upgrade fixes #8729


---

Attachment

The doctests that still fail after the patch is applied (under ptestlong) are listed below:



I couldn't find a way to double-check that the new answer is correct in the following output mismatch


```

sage -t -long "4.4.1/devel/sage/sage/symbolic/integration/integral.py"
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 464:
    sage: integrate(sin(x)*cos(10*x)*log(x), x)
Expected:
    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
Got:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
**********************************************************************
```



The next doctest is testing that #780 is fixed.  Here, it appears that #780 is *not* fixed again.  However, the actual maxima bug that was fixed for #780 is still fixed.  The problem seems to be that we use keepfloat: true, and when we have keepfloat: true, the erroneous question pops up.


```
File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 486:
    sage: res = integral(f,x,0.0001414, 1.); res
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[56]>", line 1, in <module>
        res = integral(f,x,RealNumber('0.0001414'), RealNumber('1.')); res###line 486:
    sage: res = integral(f,x,0.0001414, 1.); res
      File "/home/grout/sage/local/lib/python/site-packages/sage/misc/functional.py", line 720, in integral
        return x.integral(*args, **kwds)
      File "expression.pyx", line 7330, in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:29048)
      File "/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 589, in integrate
        return definite_integral(expression, v, a, b)
      File "function.pyx", line 425, in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4359)
      File "/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/integral.py", line 174, in _eval_
        return integrator(*args)
      File "/home/grout/sage/local/lib/python/site-packages/sage/symbolic/integration/external.py", line 21, in maxima_integrator
        result = expression._maxima_().integrate(v, a, b)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/maxima.py", line 2112, in integral
        return I(var, min, max)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1408, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1316, in function_call
        return self.new(s)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1097, in new
        return self(code)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1032, in __call__
        return cls(self, x, name=name)
      File "/home/grout/sage/local/lib/python/site-packages/sage/interfaces/expect.py", line 1451, in __init__
        raise TypeError, x
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume((y-1)*(y+1)>0)' before integral or limit evaluation, for example):
    Is  (y-1)*(y+1)  positive, negative, or zero?
```


Here is a maxima session (5.21.1) showing the problem.  When keepfloat is false, an integral comes right back


```
% sage -maxima
;;; Loading #P"/home/grout/sage/local/lib/ecl/sb-bsd-sockets.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/sockets.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/defsystem.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
Maxima 5.21.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) assume(y^2>1);
                                     2
(%o1)                              [y  > 1]
(%i2) keepfloat: true;              
(%o2)                                true
(%i3) integrate(log(x^2+y^2),x,0,1);
                               2               1
                        2 log(y  + 1) + 4 atan(-) y - 4
                                               y
(%o3)                   -------------------------------
                                       2
(%i4) integrate(log(x^2+y^2),x,0.0001414,1);
Is  (y - 1) (y + 1)  positive, negative, or zero?
```



There is some output mismatch in transform.pyx.  This occurs in an explanatory section of the docs, and just consists of simplifying a horrendous matrix.  The matrix just simplifies differently now (we get explicit imaginary values now, for some reason).  Does anyone want to check that the simplifications are actually correct now?


```
sage -t -long "4.4.1/devel/sage/sage/plot/plot3d/transform.pyx"
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/plot/plot3d/transform.pyx", line 217:
    sage: m
Expected:
    [                                             -(cos(theta) - 1)*x^2 + cos(theta)                 -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x - sqrt(z^2)*sin(theta)         -((cos(theta) - 1)*x*z^2 - sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z]
    [                -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x + sqrt(z^2)*sin(theta)                                 (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1 -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z + x*z*sin(theta))/sqrt(z^2)]
    [        -((cos(theta) - 1)*x*z^2 + sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z - x*z*sin(theta))/sqrt(z^2)                                              -(cos(theta) - 1)*z^2 + cos(theta)]
Got:
    [                                                                                                          -(cos(theta) - 1)*x^2 + cos(theta)                 -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)         -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z^2*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z^2)/(sqrt(-x^2 + 1)*z)]
    [                -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)                                                                                              (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1  (sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) - sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)]
    [        -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z^2*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z^2)/(sqrt(-x^2 + 1)*z) -(sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) + sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)                                                                                                           -(cos(theta) - 1)*z^2 + cos(theta)]
**********************************************************************
```




There are a few errors in the interfaces/maxima.py file.  These seem to all stem from more output, rather than actual errors.


```
sage -t -long "4.4.1/devel/sage/sage/interfaces/maxima.py"  
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 871:
    sage: maxima._command_runner('describe', 'gcd')
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 896:
    sage: maxima.help('gcd')
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 906:
    sage: maxima.example('arrays')
Expected:
    a[n]:=n*a[n-1]
                                    a  := n a
                                     n       n - 1
    a[0]:1
    a[5]
                                          120
    a[n]:=n
    a[6]
                                           6
    a[4]
                                          24
                                         done
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    a[n]:=n*a[n-1]
                                    a  := n a
                                     n       n - 1
    a[0]:1
    a[5]
                                          120
    a[n]:=n
    a[6]
                                           6
    a[4]
                                          24
                                         done
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 2384:
    sage: m.gcd._sage_doc_()
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 2395:
    sage: maxima.gcd._sage_doc_()
Expected:
    -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
    ...
Got:
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
    ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
    <BLANKLINE>
     -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
         Returns the greatest common divisor of <p_1> and <p_2>.  The flag
         `gcd' determines which algorithm is employed.  Setting `gcd' to
         `ez', `subres', `red', or `spmod' selects the `ezgcd',
         subresultant `prs', reduced, or modular algorithm, respectively.
         If `gcd' `false' then `gcd (<p_1>, <p_2>, <x>)' always returns 1
         for all <x>.  Many functions (e.g.  `ratsimp', `factor', etc.)
         cause gcd's to be taken implicitly.  For homogeneous polynomials
         it is recommended that `gcd' equal to `subres' be used.  To take
         the gcd when an algebraic is present, e.g., `gcd (<x>^2 -
         2*sqrt(2)*<x> + 2, <x> - sqrt(2))', `algebraic' must be `true' and
         `gcd' must not be `ez'.
    <BLANKLINE>
         The `gcd' flag, default: `spmod', if `false' will also prevent the
         greatest common divisor from being taken when expressions are
         converted to canonical rational expression (CRE) form.  This will
         sometimes speed the calculation if gcds are not required.
    <BLANKLINE>
    <BLANKLINE>
      There are also some inexact matches for `gcd'.
      Try `?? gcd' to see them.
    <BLANKLINE>
                                         true
    <BLANKLINE>
```


Finally, I'm not sure what is happening in this error:


```
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/interfaces/maxima.py", line 729:
    sage: maxima.eval('sage0: x == x;')
Expected:
    Traceback (most recent call last):
    ...
    TypeError: error evaluating "sage0: x == x;":...
Got:
    'x'
**********************************************************************
```



---

Comment by jason created at 2010-05-13 06:07:32

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-05-13 12:49:23

Thanks for the comprehensive report; I had my own private list of these from a few weeks ago, but had not had time to look into all of them yet.

I think with the last two things there must have been internal changes in Maxima which lead to different handling - in particular, that gcd must now load some modules?  I'm going to check what maxima_console() does with these things.


---

Comment by jason created at 2010-05-13 12:56:06

Replying to [comment:23 kcrisman]:


> I think with the last two things there must have been internal changes in Maxima which lead to different handling - in particular, that gcd must now load some modules?  I'm going to check what maxima_console() does with these things.

Well, I wouldn't be surprised if those extra lines actually came from the updated ECL package, given what the messages are.


---

Comment by kcrisman created at 2010-05-13 12:58:27

Hmm, maybe ECL does something not silently it did silently before?  I forgot I had to install that spkg, by the way - to all others, remember to use #8808 first!


---

Comment by kcrisman created at 2010-05-13 13:19:14

With the new ECL and the new Maxima, I no longer get the error messages about installing a .fas or .fasb file.  That is good.

Anyway, doctest should just be changed for the loading thing, regardless of where it does it.  All documentation requests do that, as does running maxima_console().  Unless... before, maxima_console() gave three loading statements, the last two of which are the ones which show up in your examples.  Now there are five, but the top two are new... are we stripping away three load statements in the output, but not more?  Just a wild idea.

As for the last error, here it is in the maxima_console() - something's not going right.

```
Maxima 5.21.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) sage0: x==x;

stdin:1289935:incorrect syntax: = is not a prefix operator
(%i1) (%o1)                                  x
```

Yet in the previous one we get

```
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) sage0: x==x;

stdin:1373:Incorrect syntax: = is not a prefix operator
(%i1) (%o1)                                  x
```

which sure looks the same to me, yet Sage catches it correctly before and not now!  What the heck?


---

Comment by jason created at 2010-05-14 00:51:29

Before, there was a lowercase "i", now it is upper-case in "Incorrect".  Maybe that's the problem.


---

Comment by kcrisman created at 2010-05-14 00:59:59

Oh yes, I should have seen that.  A quick search_src doesn't reveal anything useful, though.


---

Comment by kcrisman created at 2010-05-25 15:42:25

Regarding the other errors:

Replying to [comment:22 jason]:
> The doctests that still fail after the patch is applied (under ptestlong) are listed below:
> 
> 
> 
> I couldn't find a way to double-check that the new answer is correct in the following output mismatch
> 

```

sage -t -long "4.4.1/devel/sage/sage/symbolic/integration/integral.py"
**********************************************************************
File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 464:
    sage: integrate(sin(x)*cos(10*x)*log(x), x)
Expected:
    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
Got:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
**********************************************************************
```

This is true if the cosine integral ci(x) (Ci in Mma) is 1/2*(Ei(I*x)+Ei(-I*x).  Several online references imply it, and also noting that cos(x) is 1/2*(exp(i*x)+exp(-i*x)) (by Taylor series or whatever you like) suffices.


> Here is a maxima session (5.21.1) showing the problem.  When keepfloat is false, an integral comes right back
> 
> {{{
> % sage -maxima
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/sb-bsd-sockets.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/sockets.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/defsystem.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/cmp.fas"
> ;;; Loading #P"/home/grout/sage/local/lib/ecl/sysfun.lsp"
> Maxima 5.21.1 http://maxima.sourceforge.net
> using Lisp ECL 10.4.1
> Distributed under the GNU Public License. See the file COPYING.
> Dedicated to the memory of William Schelter.
> The function bug_report() provides bug reporting information.
> (%i1) assume(y^2>1);
>                                      2
> (%o1)                              [y  > 1]
> (%i2) keepfloat: true;              
> (%o2)                                true
> (%i3) integrate(log(x<sup>2+y</sup>2),x,0,1);
>                                2               1
>                         2 log(y  + 1) + 4 atan(-) y - 4
>                                                y
> (%o3)                   -------------------------------
>                                        2
> (%i4) integrate(log(x<sup>2+y</sup>2),x,0.0001414,1);
> Is  (y - 1) (y + 1)  positive, negative, or zero?
> }}}
> 

I'm not sure what to do with this.  keepfloat is so annoying.

> 
> There is some output mismatch in transform.pyx.  This occurs in an explanatory section of the docs, and just consists of simplifying a horrendous matrix.  The matrix just simplifies differently now (we get explicit imaginary values now, for some reason).  Does anyone want to check that the simplifications are actually correct now?
> 
> {{{
> sage -t -long "4.4.1/devel/sage/sage/plot/plot3d/transform.pyx"
> **********************************************************************
> File "/home/grout/sage-4.4.1/devel/sage/sage/plot/plot3d/transform.pyx", line 217:
>     sage: m
> Expected:
>     [                                             -(cos(theta) - 1)*x^2 + cos(theta)                 -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x - sqrt(z^2)*sin(theta)         -((cos(theta) - 1)*x*z^2 - sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z]
>     [                -(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x + sqrt(z^2)*sin(theta)                                 (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1 -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z + x*z*sin(theta))/sqrt(z^2)]
>     [        -((cos(theta) - 1)*x*z^2 + sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*sin(theta))/z -((cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*sqrt(z^2)*z - x*z*sin(theta))/sqrt(z^2)                                              -(cos(theta) - 1)*z^2 + cos(theta)]
> Got:
>     [                                                                                                          -(cos(theta) - 1)*x^2 + cos(theta)                 -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) - I*sqrt(x^2 - 1)*sin(theta))*sqrt(z<sup>2)/sqrt(-x</sup>2 + 1)         -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z<sup>2*sqrt(z</sup>(-2)) + I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z<sup>2)/(sqrt(-x</sup>2 + 1)*z)]
>     [                -((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) + I*sqrt(x^2 - 1)*sin(theta))*sqrt(z<sup>2)/sqrt(-x</sup>2 + 1)                                                                                              (cos(theta) - 1)*x^2 + (cos(theta) - 1)*z^2 + 1  (sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) - sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)]
>     [        -((cos(theta) - 1)*sqrt(-x^2 + 1)*x*z<sup>2*sqrt(z</sup>(-2)) - I*sqrt(x^2 - 1)*sqrt(-x^2 - z^2 + 1)*sin(theta))*sqrt(z<sup>2)/(sqrt(-x</sup>2 + 1)*z) -(sqrt(-x^2 + 1)*sqrt(x^2 - 1)*x*z*sqrt(z^(-2))*sin(theta) + sqrt(-x^2 - z^2 + 1)*((I*cos(theta) - I)*x^2 - I*cos(theta) + I)*z)/(I*x^2 - I)                                                                                                           -(cos(theta) - 1)*z^2 + cos(theta)]
> **********************************************************************
> }}}
> 

I believe this is all related to a change made in how sqrt behaves with respect to factors (sqrt(ab) and sqrt(a), sqrt(b)) and whether an I gets factored out or not. They all come down to the same essential things:

```
-(cos(theta) - 1)*sqrt(-x^2 - z^2 + 1)*x
-((cos(theta) - 1)*sqrt(-x^2 + 1)*sqrt(-x^2 - z^2 + 1)*x*sqrt(z^(-2)) 
```


```
- sqrt(z^2)*sin(theta)
- I*sqrt(x^2 - 1)*sin(theta))*sqrt(z^2)/sqrt(-x^2 + 1)
```

The latter seems ok immediately (or at least no worse than other decision made for us about which root of -1 to choose), but even given that $x<sup>2+y</sup>2+z^2=1$, which is asserted earlier in the file, I can't quite make out the former. I'll look into this a little more.


---

Comment by kcrisman created at 2010-05-25 15:43:30

Replying to [comment:25 kcrisman]:
> Hmm, maybe ECL does something not silently it did silently before?  I forgot I had to install that spkg, by the way - to all others, remember to use #8808 first!
Now remember to use #8951 first.


---

Comment by kcrisman created at 2010-05-25 16:06:03

> sage -t -long "4.4.1/devel/sage/sage/symbolic/integration/integral.py"
> **********************************************************************
> File "/home/grout/sage-4.4.1/devel/sage/sage/symbolic/integration/integral.py", line 464:
>     sage: integrate(sin(x)*cos(10*x)*log(x), x)
> Expected:
>     1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
> Got:
>     1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
> **********************************************************************
> }}}
> This is true if the cosine integral ci(x) (Ci in Mma) is 1/2*(Ei(I*x)+Ei(-I*x).  Several online references imply it, and also noting that cos(x) is 1/2*(exp(i*x)+exp(-i*x)) (by Taylor series or whatever you like) suffices.
 
Burcin has also already pointed this out at #8624.


---

Comment by kcrisman created at 2010-05-25 17:18:16

I get the following on Mac OSX 10.6 on Intel (see the patch for the which test):

```
    sage: h.n()
Expected:
    0.075715991017028972
Got:
    0.075715991017028958
```



---

Comment by jason created at 2010-05-28 03:40:21

That h.n() doctest is interesting.  (From what I recall when I investigated it) the old maxima agreed with both mathematica and mpmath, but the new maxima is off in the last few digits---it might be worth checking into, though it may just be numerical error.


---

Comment by jason created at 2010-05-28 03:42:06

(but those h.n() errors I talked about were for the old sin function, not the new tan function, IIRC)


---

Comment by nbruin created at 2010-06-21 05:14:46

Replying to [comment:12 was]:

It may be useful to note that all the doctests that fail with maxima.5.21.1 and ecl.10.4.1, pass with maxima.5.20.1.p1 from #8645. So, ecl.10.4.1 is not of influence. All changes in doctest responses are due to changes in maxima.


---

Comment by nbruin created at 2010-06-21 18:25:13

> And in interfaces/maxima.py there are a lot of erros where Maxima loads like
> {{{
>     ;;; Loading #P".../local/lib/ecl/cmp.fas"
>     ;;; Loading #P".../local/lib/ecl/sysfun.lsp"
> }}}

It's actually possible to turn messages like this off. If you're driving maxima via a pexpect interface, that might be the proper thing to do. The key is the "Common Lisp HyperSpec", the de facto official CL documentation. Looking at `load` leads to the global variable `*load-verbose*`:

http://www.lispworks.com/documentation/HyperSpec/Body/v_ld_prs.htm#STload-verboseST

It's on by default in ECL, but can be turned off:


```
ECL (Embeddable Common-Lisp) 10.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  
Top level.
> (require 'maxima)

;;; Loading #P"/mnt/usb1/scratch/nbruin/sage-4.4.3/local/lib/ecl/maxima.fas"
("MAXIMA")
```



```
ECL (Embeddable Common-Lisp) 10.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  
Top level.
> *load-verbose*

T
> (setf *load-verbose* NIL)

NIL
> (require 'maxima)

("MAXIMA")
```



---

Comment by kcrisman created at 2010-06-25 13:10:18

Note to eventual author of patch - please confirm here that #8729 is fixed when writing doctests.


---

Comment by mpatel created at 2010-07-11 08:56:30

With 4.5.alpha4 + http://sage.math.washington.edu/home/jason/maxima-5.21.1.spkg + [attachment:trac-8731-maxima-upgrade.patch], the long tests on sage.math give reproducible failures in

```
        sage -t -long  devel/sage/sage/calculus/calculus.py # 1 doctests failed
        sage -t -long  devel/sage/sage/plot/plot3d/transform.pyx # 1 doctests failed
        sage -t -long  devel/sage/sage/interfaces/maxima.py # 6 doctests failed
        sage -t -long  devel/sage/sage/symbolic/integration/integral.py # 4 doctests failed
```

The full raw test log is [here](http://sage.math.washington.edu/home/mpatel/trac/8731/ptestlong_4.5.alpha4.log).


---

Comment by kcrisman created at 2010-08-02 14:45:23

Just FYI:

```

Message: 4
Date: Sun, 1 Aug 2010 15:39:28 -0600
From: Robert Dodier <robert.dodier@gmail.com>
To: Maxima Mailing List <maxima@math.utexas.edu>
Subject: [Maxima] Maxima 5.22.0
Message-ID:
       <AANLkTimGPxt1uLWDmFEVUgDU8nxByJ=V00Fxk4o2_3yc@mail.gmail.com>
Content-Type: text/plain; charset=ISO-8859-1

Hi, I;ve tagged version-5_22_0 in CVS and built rpms
and tar.gz and upload them all to SF.
Should be available real soon now at:
http://sourceforge.net/projects/maxima/files/
(looks like the list hasn't been refreshed yet, I don't
know what the refresh schedule is)

If someone can build & upload a Windows installer that
would be great.

As ever please give the new version a try and if/when
there aren't too many complaints I'll make a general announcement.

best

Robert Dodier
```

So maybe we should change this ticket to 5.22.0 if they don't get too many problems with it?


---

Comment by kcrisman created at 2010-08-12 16:39:02

And now the latest is 5.22.1.


---

Comment by kcrisman created at 2010-09-22 14:44:41

This will probably also fix #8582.


---

Comment by kcrisman created at 2010-10-15 17:11:44

Just FYI on this ticket - from an email on the Maxima list by Robert Dodier:

```
The next release is planned for December, with the release branch
(5.23) on Dec 1 or soon thereafter, with a stable release to follow
around Christmas.
```



---

Comment by aginiewicz created at 2010-10-29 16:22:07

As sooner or later maxima would have to be updated to 5.22 or newer I decided to share my experiences of first approach to update to it. I wanted to try 5.22 because it's first version that supports inversion of error function, and first to support integrals of form abs(x) from 0 to a without assumptions. I based on patch by Jason for 5.21 and wanted to reach at least same level of failures as with 5.21. Unfortunately, I got stuck at one place - maxima hangs in some situations. I tracked that to this difference:

before it was

```
sage -maxima -p /home/giniu/dev/sage/local/bin/sage-maxima.lisp
;;; Loading #P"/opt/sage/local/lib/ecl/defsystem.fas"
;;; Loading #P"/opt/sage/local/lib/ecl/cmp.fas"
;;; Loading #P"/opt/sage/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 0;
<sage-display>(%o1)                                  0
(%i2) sage0: x==x;
Incorrect syntax: = is not a prefix operator
(%i2) <sage-display>(%o2)                                  x
```

and now it is

```
./sage -maxima -p /home/giniu/dev/sage/local/bin/sage-maxima.lisp
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/sb-bsd-sockets.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/sockets.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/defsystem.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/cmp.fas"
;;; Loading #P"/home/giniu/dev/sage/local/lib/ecl/sysfun.lsp"
Maxima 5.22.1 http://maxima.sourceforge.net
using Lisp ECL 10.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 0;
<sage-display>(%o1)                                  0
(%i2) sage0: x==x;
incorrect syntax: = is not a prefix operator
sage0: x==
        ^
```


which makes Sage wait for "<sage-display>" forever.

I made spkg: http://lab15.im.pwr.wroc.pl/~giniew/maxima-5.22.1.spkg and patch - http://lab15.im.pwr.wroc.pl/~giniew/trac-8731-maxima-upgrade-to-5.22.1.patch - those are not working but I'm attaching them in case someone wants to pick up from here - as I said I gave up for now.

(btw, the doctest that was failing in devel/sage/sage/calculus/calculus.py is just different grouping, checked it and added new version to doctest, and there is one new doctest failure in devel/sage/sage/calculus/calculus.py that fails because maxima can integrate abs(x) in x from 0 to any a and returns correct 1/2*a*abs(a). There was also change to how logcontract works, they don't make full rational simplification now. I added one more step of rational simplification to simplify_full to simplify it more, though it might change some results.)


---

Comment by vbraun created at 2010-10-29 23:56:55

See #10187 for up-to-date ecl/maxima spkgs and a workaround to the `sage-display` issue.


---

Comment by mvngu created at 2010-12-06 11:46:54

Close as a duplicate of #10187. The latter ticket upgrades Maxima to version 5.22.1.


---

Comment by mvngu created at 2010-12-06 11:46:54

Resolution: duplicate
