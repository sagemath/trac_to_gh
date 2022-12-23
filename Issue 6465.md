# Issue 6465: Derivative D acts wrongly on symbolic integration

Issue created by migration from https://trac.sagemath.org/ticket/6465

Original creator: gmhossain

Original creation time: 2009-07-05 02:31:55

In new symbolics, derivative operator does not know 
how to act on symbolic integration.


```
sage: f(x) = function('f',x)
sage: g = integrate(f(x),x)
sage: g.diff(x)
D[0](integrate)(f(x), x)*D[0](f)(x) + D[1](integrate)(f(x), x)
```



---

Comment by burcin created at 2009-08-01 02:36:54

support disabling chain rule for symbolic functions


---

Attachment

attachment:trac_6465-chain_rule.patch adds support for disabling chain rule for symbolic functions. It depends on the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p2.spkg


---

Attachment

Should be applied after the chain-rule patch


---

Comment by kcrisman created at 2009-09-10 15:23:34

There need to be deprecation warnings for things like 

```
sage: integral(sin(x), pi, 2*pi)
sage: integral(sin(x)^3
```



---

Comment by timdumol created at 2009-09-22 10:47:35

The sudden API change probably merits a deprecation warning, as kcrisman said. Also:

Doctest failure:


```

sage -t -long devel/sage/sage/libs/ginac/decl.pxi         
         [0.1 s]                                          
sage -t -long devel/sage/sage/misc/functional.py          
**********************************************************************
File "/opt/sage-bin/devel/sage-deriv/sage/misc/functional.py", line 412:
    sage: integral(exp(-x), (x, 1, oo))                                 
Expected:                                                               
    e^(-1)                                                              
Got:                                                                    
    gamma_incomplete(1, 1)                                              
**********************************************************************  
1 items had failures:                                                   
   1 of  15 in __main__.example_25                                      
***Test Failed*** 1 failures.                                           
For whitespace errors, see the file /opt/sage-bin/tmp/.doctest_functional.py
         [9.3 s]

```



---

Comment by kcrisman created at 2009-09-22 12:05:29

That may be due to the Maxima upgrade - has it been patched elsewhere?  Just FYI, I'm not certain on this.


---

Comment by timdumol created at 2009-11-30 08:37:51

This patch needs to be rebased on #6816. The doctest failure persists, but gamma_incomplete(1, 1) is equivalent to e^(-1) anyways.


---

Comment by burcin created at 2009-12-22 22:46:02

Both patches need major rebase after #7490. I'll take a look at this when I find some time.

The problem with `gamma_incomplete` might be related to/fixed by #7748.


---

Comment by kcrisman created at 2009-12-23 04:39:05

> The problem with `gamma_incomplete` might be related to/fixed by #7748.

Yes, I think so, as Maxima 5.20.1 now returns this for both integrate(exp(-x),x,1,inf) and integrate(1/%e^x,x,1,inf).  Note that 

```
sage: gamma_inc(1,1)
0.367...
```

rather than 1/e at this point, so it really is the symbolic piece, not just having translation from Maxima, that would be important.


---

Comment by burcin created at 2010-01-19 10:21:01

rebased to 4.3.rc0


---

Attachment

rebased to 4.3.1.rc0


---

Attachment

referee patch


---

Attachment

I uploaded new versions of the two old patches, rebased to 4.3.1.rc0, and a referee patch. I consider this ready now, though someone needs to review my changes.

Unfortunately attachment:trac_6465-chain_rule.take2.patch depends on the next version of pynac. I will release that real soon now. :)

The patches should be applied in this order:
 * attachment:trac_6465-chain_rule.take2.patch
 * attachment:trac_6465-moves-integration-into-sfunction-subclass.take2.patch
 * attachment:trac_6465-integral.patch

They probably depend on other tickets. ATM, my queue contains: #7822, #6961, #7876, #7363, #7955, #7957, #7916 related to symbolics.


---

Comment by burcin created at 2010-01-19 14:15:23

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-01-19 14:15:23

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The patches here depend on #7822, #7876, #7363, #7955, #7957 and #7916 (in this order).

The patches should be applied in this order:

    * attachment:trac_6465-chain_rule.take2.patch Download
    * attachment:trac_6465-moves-integration-into-sfunction-subclass.take2.patch Download
    * attachment:trac_6465-integral.patch


---

Comment by jason created at 2010-01-21 00:34:27

There is a reject on sage/symbolic/random_tests.py with the last patch.


---

Comment by jason created at 2010-01-21 01:45:50

See #6559 for the correct order of patches to avoid the reject.


---

Comment by kcrisman created at 2010-01-21 02:36:44

I've applied every one of Burcin's patches I could find, and get only one type of doctest failure with all of them (when applied in the right order).  So so far so good!  Unfortunately, I can't review any of them for two reasons - my understanding of C++/Pynac is not reliable enough to do a good job, and there are so many failures until one applies _all_ the patches that it's hard to separate out what's what.

The reason I say that here is that I do get a significant failure, in a few different files, for the _tderivative_ method, though the actual failure occurs as a RuntimeError in line 216 of sage/misc/derivative.pyx (with no error message, more's the pity).  For instance, in line 99 of sage/symbolic/integration/integral.py, 

```
sage: f = function('f'); a,b = var('a,b')
sage: h = indefinite_integral(f(x), x)
sage: h.diff(x)
RuntimeError
```

I hope this helps track it down.


---

Comment by burcin created at 2010-01-21 07:36:45

Can you download the package file again and install it?

I forgot to include a patch when I first put the release together. I fixed the spkg file once I realized the problem, assuming no one looked at it yet. You must have downloaded in that period.

Sorry for the inconvenience and many thanks for trying these patches out.


---

Comment by kcrisman created at 2010-01-28 21:00:38

Replying to [comment:14 burcin]:
> Can you download the package file again and install it?
> 
> I forgot to include a patch when I first put the release together. I fixed the spkg file once I realized the problem, assuming no one looked at it yet. You must have downloaded in that period.

I now get

```
sage: h.diff(x)
f(x)
```


However, I now get some errors after applying all patches up to and including this set.  Some should also be marked # optional - requires Internet (the mathematica_free ones).  They all seem to be related to some extra keyword being passed to the DeprecatedSFunction constructor.

```
sage -t  "devel/sage/sage/symbolic/integration/integration.py"
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 29:
    sage: from sage.symbolic.integration.integration import _maxima_integrator
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        from sage.symbolic.integration.integration import _maxima_integrator###line 29:
    sage: from sage.symbolic.integration.integration import _maxima_integrator
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 316, in <module>
        integral = SymbolicIntegration()
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 152, in __init__
        SFunction.__init__(self, "integrate", *args, **kwds)
      File "function.pyx", line 1059, in sage.symbolic.function.DeprecatedSFunction.__init__ (sage/symbolic/function.cpp:8588)
    TypeError: __init__() got an unexpected keyword argument 'built_in_function'
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 30:
    sage: _maxima_integrator(sin(x), x)
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[3]>", line 1, in <module>
        _maxima_integrator(sin(x), x)###line 30:
    sage: _maxima_integrator(sin(x), x)
    NameError: name '_maxima_integrator' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 33:
    sage: _maxima_integrator(f(x), x)
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError: Maxima failed to integrate
Got:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        _maxima_integrator(f(x), x)###line 33:
    sage: _maxima_integrator(f(x), x)
    NameError: name '_maxima_integrator' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 293:
    sage: from sage.symbolic.integration.integration import integral
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        from sage.symbolic.integration.integration import integral###line 293:
    sage: from sage.symbolic.integration.integration import integral
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 316, in <module>
        integral = SymbolicIntegration()
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 152, in __init__
        SFunction.__init__(self, "integrate", *args, **kwds)
      File "function.pyx", line 1059, in sage.symbolic.function.DeprecatedSFunction.__init__ (sage/symbolic/function.cpp:8588)
    TypeError: __init__() got an unexpected keyword argument 'built_in_function'
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 294:
    sage: _ilatex = integral._print_latex_
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        _ilatex = integral._print_latex_###line 294:
    sage: _ilatex = integral._print_latex_
    AttributeError: 'function' object has no attribute '_print_latex_'
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 298:
    sage: _ilatex(f(x),x)
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[6]>", line 1, in <module>
        _ilatex(f(x),x)###line 298:
    sage: _ilatex(f(x),x)
    NameError: name '_ilatex' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 300:
    sage: _ilatex(f(x),x,a,b)
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[7]>", line 1, in <module>
        _ilatex(f(x),x,a,b)###line 300:
    sage: _ilatex(f(x),x,a,b)
    NameError: name '_ilatex' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 51:
    sage: from sage.symbolic.integration.integration import _sympy_integrator
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        from sage.symbolic.integration.integration import _sympy_integrator###line 51:
    sage: from sage.symbolic.integration.integration import _sympy_integrator
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 316, in <module>
        integral = SymbolicIntegration()
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 152, in __init__
        SFunction.__init__(self, "integrate", *args, **kwds)
      File "function.pyx", line 1059, in sage.symbolic.function.DeprecatedSFunction.__init__ (sage/symbolic/function.cpp:8588)
    TypeError: __init__() got an unexpected keyword argument 'built_in_function'
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 52:
    sage: _sympy_integrator(sin(x), x)
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        _sympy_integrator(sin(x), x)###line 52:
    sage: _sympy_integrator(sin(x), x)
    NameError: name '_sympy_integrator' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 55:
    sage: _sympy_integrator(f(x), x)
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError: Sympy failed to integrate
Got:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[5]>", line 1, in <module>
        _sympy_integrator(f(x), x)###line 55:
    sage: _sympy_integrator(f(x), x)
    NameError: name '_sympy_integrator' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 76:
    sage: from sage.symbolic.integration.integration import _mathematica_free_integrator
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        from sage.symbolic.integration.integration import _mathematica_free_integrator###line 76:
    sage: from sage.symbolic.integration.integration import _mathematica_free_integrator
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 316, in <module>
        integral = SymbolicIntegration()
      File "/Users/.../sage-4.3.1/local/lib/python/site-packages/sage/symbolic/integration/integration.py", line 152, in __init__
        SFunction.__init__(self, "integrate", *args, **kwds)
      File "function.pyx", line 1059, in sage.symbolic.function.DeprecatedSFunction.__init__ (sage/symbolic/function.cpp:8588)
    TypeError: __init__() got an unexpected keyword argument 'built_in_function'
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 77:
    sage: _mathematica_free_integrator(sin(x), x)
Exception raised:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        _mathematica_free_integrator(sin(x), x)###line 77:
    sage: _mathematica_free_integrator(sin(x), x)
    NameError: name '_mathematica_free_integrator' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 80:
    sage: _mathematica_free_integrator(f(x), x)
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError: mathematica_free failed to integrate
Got:
    Traceback (most recent call last):
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/.../sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[5]>", line 1, in <module>
        _mathematica_free_integrator(f(x), x)###line 80:
    sage: _mathematica_free_integrator(f(x), x)
    NameError: name '_mathematica_free_integrator' is not defined
**********************************************************************
File "/Users/.../sage-4.3.1/devel/sage/sage/symbolic/integration/integration.py", line 241:
    sage: h.n()
Expected:
    0.472399177268953
Got:
    0.47239917726895253
**********************************************************************
5 items had failures:
   3 of   6 in __main__.example_1
   4 of   9 in __main__.example_10
   3 of   6 in __main__.example_2
   3 of   6 in __main__.example_3
   1 of   4 in __main__.example_8
***Test Failed*** 14 failures.
	 [6.5 s]
```


> Sorry for the inconvenience and many thanks for trying these patches out.

No problem.  Although I _strongly_ disagree with the removal of indefinite integration longterm without explicit variable, overall this set of changes will be a big improvement.  I am sorry again I cannot review much of the C++ related stuff, or the Pynac changes, though I am glad they are now up on [|pynac.sagemath.org] !


---

Comment by kcrisman created at 2010-01-28 21:00:38

Changing status from needs_review to needs_work.


---

Attachment

new version


---

Comment by burcin created at 2010-01-31 21:23:50

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-01-31 21:23:50

attachment:trac_6465-integral.patch renames the file `sage/symbolic/integration/integration.py` to `sage/symbolic/integration/integral.py`. Are you sure you applied the patches correctly? Since these are git style diffs using `hg import` or `hg qimport` is recommended.

I applied the whole batch of symbolics patches associated to pynac-0.11 to 4.3.2.alpha0, and tested the sage/{symbolic,calculus,functions} directories. The only doctest failure I got was in  `sage/symbolic/integration/external.py`. attachment:trac_6465-integral.take2.patch removes this dubious test.

The patches that need to be applied from this ticket are now:
 * attachment:trac_6465-chain_rule.take2.patch
 * attachment:trac_6465-moves-integration-into-sfunction-subclass.take2.patch
 * attachment:trac_6465-integral.take2.patch


---

Comment by burcin created at 2010-02-03 10:52:44

fix numerical problems in doctests


---

Attachment

After testing on a 32-bit Debian box, I uploaded attachment:trac_6465-integral.take3.patch to replace attachment:trac_6465-integral.take2.patch. The only difference is the `...` used for the trailing digits of the numerical integral on line 188 of `sage/symbolic/integration/integral.py`.

The patches that need to be applied are: 
    * attachment:trac_6465-chain_rule.take2.patch
    * attachment:trac_6465-moves-integration-into-sfunction-subclass.take2.patch
    * attachment:trac_6465-integral.take2.patch


---

Comment by burcin created at 2010-02-04 09:13:19

Oops, the last patch to be applied is attachment:trac_6465-integral.take3.patch! That was a typo in the list above.


---

Attachment

rebased to 4.3.2


---

Comment by burcin created at 2010-02-09 10:57:46

rebased to 4.3.2


---

Attachment

I rebased the patches to 4.3.2. Patches to be applied are now:

 * attachment:trac_6465-chain_rule.take2.patch
 * attachment:trac_6465-moves-integration-into-sfunction-subclass.take3.patch
 * attachment:trac_6465-integral.take4.patch


---

Comment by rossk created at 2010-02-18 14:03:18

The patch solves the stated problem without loss of functionality (at
least in the tests below). +1 for positive review.

```
sage: f(x) = function('f',x)
sage: g = integrate(f(x),x)
sage: g.diff(x)
f(x)
sage: integrate(f(x),x).diff(x)
f(x)

sage: h(x,y) = function('h',x,y)
sage: kx = integrate(h(x,y),x)
sage: kx
integrate(h(x, y), x)
sage: kx.diff(x)
h(x, y)

sage: kxy = integrate( integrate(h(x,y),x), y)
sage: kxy
integrate(integrate(h(x, y), x), y)
sage: kxy.diff(y).diff(x)
h(x, y)
sage: kxy.diff(x).diff(y)
h(x, y)
sage: kxy.diff(x)
integrate(h(x, y), y)

sage: integrate(1/(2*x+1)^2, x, 0, 1)
1/3

sage: loads(dumps(integrate(1/(2*x+1)^2, x, 0, 1))) == 1/3
True

sage: integrate(1/(2*x+1)^2, x, 0.0, 1.0)
0.333333333333

sage: integrate(1/(2*x+1)^2, x, 0, 1.0)
0.333333333333

sage: integrate(1/(2*x+1)^2, x, CC(0), 1.0)
0.333333333333

sage: integrate(x/(1+x^2),x)
1/2*log(x^2 + 1)

sage: integrate(tan(x),x)
log(sec(x))
```


There is one issue (that is not necessarily a part of this ticket). 
I may be wrong but I'm reasonably sure that in general that 
integrate( integrate(h(x,y),x), y).diff(y).diff(x) <>
integrate( integrate(h(x,y),x), y).diff(x).diff(y)
But the following seems to imply it is (both are equal to h(x, y) )

```
sage: kxy = integrate( integrate(h(x,y),x), y)
sage: kxy
integrate(integrate(h(x, y), x), y)
sage: kxy.diff(y).diff(x)
h(x, y)
sage: kxy.diff(x).diff(y)
h(x, y)
```



---

Comment by mvngu created at 2010-02-18 21:29:25

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 21:29:25

The rebase looks good. See #6961 for the order in which to apply patches.


---

Comment by mvngu created at 2010-02-18 21:51:14

Merged in this order:

 1. [trac_6465-chain_rule.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-chain_rule.take2.patch)
 1. [trac_6465-moves-integration-into-sfunction-subclass.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch)
 1. [trac_6465-integral.take4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-integral.take4.patch)


---

Comment by mvngu created at 2010-02-18 21:51:14

Resolution: fixed
