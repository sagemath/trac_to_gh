# Issue 5723: sage new symbolics/pynac misbehave when evaluating with CDF elements

Issue created by migration from https://trac.sagemath.org/ticket/5723

Original creator: ncalexan

Original creation time: 2009-04-09 03:10:51

Keywords: sage symbolics pynac evaluating n CDF


```
sage: u0 = var('u0', ns=1)
sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/33117/_Users_ncalexan_sage_3_4_rc0_devel_sage_sage_symbolic_test_sage_23.py in <module>()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:6498)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_float (sage/symbolic/pynac.cpp:3959)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:5799)()

TypeError: can't convert complex to float; use abs(z)
```



---

Comment by burcin created at 2009-04-13 16:12:55

add doctest


---

Attachment

This is fixed with the changes in #5777, attached patch adds the doctest to sage/symbolic/function.pyx.


---

Comment by burcin created at 2009-04-13 16:14:55

Changing status from new to assigned.


---

Comment by burcin created at 2009-04-13 16:14:55

Set assignee to burcin.


---

Comment by jason created at 2009-05-30 07:11:34

I get a failure for this doctest in 4.0.  Burcin, could you look at this again?


```
sage -t  "devel/sage-main/sage/symbolic/function.pyx"       
**********************************************************************
File "/home/jason/sage/devel/sage-main/sage/symbolic/function.pyx", line 19:
    sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
Exception raised:
    Traceback (most recent call last):
      File "/home/jason/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jason/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jason/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        sage.symbolic.function.function('f')(u0).subs(u0=CDF.gen(0)).n()###line 19:
    sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
      File "expression.pyx", line 3211, in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15832)
        x = new_Expression_from_GEx(self._parent, self._gobj.evalf(0, prec)).pyobject()
      File "expression.pyx", line 199, in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2637)
        raise TypeError, "self must be a numeric expression"
    TypeError: self must be a numeric expression
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jason/sage/tmp/.doctest_function.py
	 [2.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/symbolic/function.pyx"
Total time for all tests: 2.0 seconds
```



---

Comment by was created at 2009-05-30 13:45:49

Wait.  

```
sage: u0 = var('u0', ns=1)
sage: sage.symbolic.function.function('f')(u0).subs(u0=CDF.0).n()
```

Why should the last line ever work?  You're taking f(I) for formal f and asking to give back a specific number.  That *should* always result in an error.  This ticket looks invalid to me.


---

Comment by mhansen created at 2009-06-05 02:33:58

This now gives


```
sage: function('f')(u0).subs(u0=CDF.0).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mhansen/.sage/temp/sage.math.washington.edu/3525/_home_mhansen__sage_init_sage_0.py in <module>()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:15832)()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.pyobject (sage/symbolic/expression.cpp:2637)()

TypeError: self must be a numeric expression
```


Nick, do you think we can close this?


---

Comment by ncalexan created at 2009-06-05 02:43:55

Fine by me.


---

Comment by mhansen created at 2009-06-05 02:49:36

Resolution: invalid
