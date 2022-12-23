# Issue 2734: SAGE Debian doctest errors whose cause I don't understand

Issue created by migration from https://trac.sagemath.org/ticket/2734

Original creator: tabbott

Original creation time: 2008-03-30 05:37:22

Assignee: tabbott

Below are the SAGE doctest errors so far that I don't see an obvious cause of:

- CRT gives the wrong answer
- modular symbols in ambient.py get wrong answers
- Many constants are rounded in constants.py
- Various problems with sympy; perhaps a version mismatch?  Debian has 0.5.12-1
- the doctests on calculus.py have been hanging for an hour.

Help debugging these would be appreciated.

sage -t  tut.tex                                            **********************************************************************
File "tut.py", line 1150:
    : x = crt(2, 1, 3, 5); x
Expected:
    11
Got:
    -4
**********************************************************************

sage -t  devel/sage-main/sage/modular/modsym/ambient.py
**********************************************************************
File "ambient.py", line 427:
    sage: M.modular_symbol([2/11, oo])
Expected:
    -{8/9,1}
Got:
    -{-1/9,0}
**********************************************************************
File "ambient.py", line 429:
    sage: M.1
Expected:
    {7/8,1}
Got:
    {-1/8,0}
**********************************************************************
File "ambient.py", line 431:
    sage: M.modular_symbol([-1/8, 0])
Expected:
    {7/8,1}
Got:
    {-1/8,0}
**********************************************************************
File "ambient.py", line 433:
    sage: M.modular_symbol([0, -1/8, 0])
Expected:
    {7/8,1}
Got:
    {-1/8,0}
**********************************************************************

sage -t  devel/sage-main/sage/functions/constants.py        **********************************************************************
File "constants.py", line 148:
    sage: RQDF(e)
Expected:
    2.718281828459045235360287471352662497757247093699959574966967630
Got:
    3.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
File "constants.py", line 150:
    sage: RQDF(pi)
Expected:
    3.141592653589793238462643383279502884197169399375105820974944590
Got:
    3.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
File "constants.py", line 152:
    sage: RQDF(e)
Expected:
    2.718281828459045235360287471352662497757247093699959574966967630
Got:
    3.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
File "constants.py", line 160:
    sage: RQDF(log2)
Expected:
    0.693147180559945309417232121458176568075500134360255254120680009
Got:
    0.700000000000000000000000000000000000000000000000000000000000000
**********************************************************************
File "constants.py", line 184:
    sage: RQDF(a)
Expected:
    13.27134794019724931009881919957581394087110682000307481783297119
Got:
    13.41832627758846552685865622348547199084119019256775416777037896
**********************************************************************
File "constants.py", line 733:
    sage: pi._real_rqdf_(RQDF)
Expected:
    3.141592653589793238462643383279502884197169399375105820974944590
Got:
    3.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
File "constants.py", line 1032:
    sage: RQDF.e()
Expected:
    2.718281828459045235360287471352662497757247093699959574966967630
Got:
    3.000000000000000000000000000000000000000000000000000000000000000
**********************************************************************
File "constants.py", line 1226:
    sage: maxima(log2).float()
Expected:
    .6931471805599453
Got:
    0.69314718055995
**********************************************************************
File "constants.py", line 1283:
    sage: RQDF(log2)
Expected:
    0.693147180559945309417232121458176568075500134360255254120680009
Got:
    0.700000000000000000000000000000000000000000000000000000000000000
**********************************************************************

sage -t  devel/sage-main/sage/calculus/test_sympy.py        **********************************************************************
File "test_sympy.py", line 102:
    : f = e.series(x, 10); f
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[41]>", line 1, in <module>
        f = e.series(x, Integer(10)); f###line 102:
    : f = e.series(x, 10); f
      File "/var/lib/python-support/python2.5/sympy/core/basic.py", line 950, in series
        raise NotImplementedError("series expansion around arbitrary point")
    NotImplementedError: series expansion around arbitrary point
**********************************************************************
File "test_sympy.py", line 106:
    : pprint(e)
Expected:
           -3
        cos  (x)
Got:
       1
    -------
       3
    cos (x)
**********************************************************************
File "test_sympy.py", line 109:
    : pprint(f)
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[43]>", line 1, in <module>
        pprint(f)###line 109:
    : pprint(f)
    NameError: name 'f' is not defined
**********************************************************************
File "test_sympy.py", line 116:
    : e._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[44]>", line 1, in <module>
        e._sage_()###line 116:
    : e._sage_()
      File "/var/lib/python-support/python2.5/sympy/core/power.py", line 479, in _sage_
        return self[0]._sage_() ** self[1]._sage_()
    TypeError: 'Pow' object is unindexable
**********************************************************************
File "test_sympy.py", line 118:
    : print e._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[45]>", line 1, in <module>
        print e._sage_()###line 118:
    : print e._sage_()
      File "/var/lib/python-support/python2.5/sympy/core/power.py", line 479, in _sage_
        return self[0]._sage_() ** self[1]._sage_()
    TypeError: 'Pow' object is unindexable
**********************************************************************
File "test_sympy.py", line 123:
    : e._sage_().taylor(x._sage_(), 0, 8)
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[46]>", line 1, in <module>
        e._sage_().taylor(x._sage_(), Integer(0), Integer(8))###line 123:
    : e._sage_().taylor(x._sage_(), 0, 8)
      File "/var/lib/python-support/python2.5/sympy/core/power.py", line 479, in _sage_
        return self[0]._sage_() ** self[1]._sage_()
    TypeError: 'Pow' object is unindexable
**********************************************************************
File "test_sympy.py", line 125:
    : f._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[47]>", line 1, in <module>
        f._sage_()###line 125:
    : f._sage_()
    NameError: name 'f' is not defined
**********************************************************************
File "test_sympy.py", line 149:
    : e=e._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[60]>", line 1, in <module>
        e=e._sage_()###line 149:
    : e=e._sage_()
      File "/var/lib/python-support/python2.5/sympy/core/add.py", line 324, in _sage_
        for x in self:
    TypeError: 'Add' object is not iterable
**********************************************************************
File "test_sympy.py", line 150:
    : print type(e)
Expected:
    <class 'sage.calculus.calculus.SymbolicArithmetic'>
Got:
    <class 'sympy.core.add.Add'>
**********************************************************************
File "test_sympy.py", line 152:
    : print e
Expected:
                                    sin(y) + cos(x)
Got:
    cos(x) + sin(y)
**********************************************************************
1 items had failures:
  10 of  66 in __main__.example_0
***Test Failed*** 10 failures.
For whitespace errors, see the file .doctest_test_sympy.py
         [7.2 s]
sage -t  devel/sage-main/sage/calculus/tests.py             **********************************************************************
File "tests.py", line 198:
    sage: f.nintegral(x, 0, 999)
Expected:
    (-0.87005772672831549, 7.5584116743243612e-10, 567, 0)
Got:
    (-0.87005772672832005, 7.5584127845473859e-10, 567, 0)
**********************************************************************



---

Comment by mabshoff created at 2008-03-30 09:52:17

Sorry Tim, this should go to debian-sage or sage-devel. *One Issue Per Ticket* hasn't been met.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-30 09:52:17

Resolution: invalid
