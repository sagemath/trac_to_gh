# Issue 4116: 3.1.2.rc2 doctest failure: sage/interfaces/sage0.py (part II)

Issue created by migration from https://trac.sagemath.org/ticket/4116

Original creator: AlexGhitza

Original creation time: 2008-09-14 09:36:38

Assignee: was

Even with the patches at #4112, the following ends up happening on a 32-bit machine running ubuntu:


```
ghitza@artin:/opt/sage/devel/sage/sage/interfaces$ sage -t sage0.py
sage -t  3.1.2.rc2/devel/sage-main/sage/interfaces/sage0.py **********************************************************************
File "/opt/sage/tmp/sage0.py", line 47:
    sage: a^3
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 52:
    sage: V.gens()
Expected:
    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 62:
    sage: g = V.0;  g
Expected:
    (1, 0, 0, 0)
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 69:
    sage: s('%s.parent()'%g.name())
Expected:
    Vector space of dimension 4 over Rational Field
Got:
    (1, 0, 0, 0)
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 74:
    sage: s('x = 5')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 78:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 85:
    sage: a
Expected:
    10
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 91:
    sage: s3('"x"')
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 93:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 276:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 289:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '4'
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 317:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    '2'
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 326:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 348:
    sage: sage0.version()
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[2]>", line 1, in <module>
        sage0.version()###line 348:
    sage: sage0.version()
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 353, in version
        return sage0_version()
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 490, in sage0_version
        return str(sage0('version()'))
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 225, in __call__
        return SageElement(self, x)
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1281, in __init__
        raise TypeError, x
    TypeError: Error executing code in SAGE
    CODE:
    	sage0=version()
    SAGE ERROR:
    	---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    /opt/sage-3.1.2.rc2/data/extcode/sage/<ipython console> in <module>()

    NameError: name 'x' is not defined
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 350:
    sage: sage0.version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 366:
    sage: sage0.new(2)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 393:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 393:
    sage: F == sage0(F)._sage_()
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 403, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 448, in sage.structure.sage_object.load (sage/structure/sage_object.c:4541)
    IOError: [Errno 2] No such file or directory: '/home/ghitza/.sage//temp/artin/22488//interface//tmp22488.sobj'
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 410:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 432:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 457:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 487:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 148:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 148:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 159, in cputime
        return float(s)
    ValueError: invalid literal for float(): SAGE Version 3.1.2.rc2, Release Date: 2008-09-12
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 150:
    sage: sage0('factor(2^157-1)')
Expected:
    852133201 * 60726444167 * 1654058017289 * 2134387368610417
Got:
    1.1760729999999999
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 152:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 152:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 159, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 165:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 165:
    sage: len(t) > 100
    TypeError: object of type 'long' has no len()
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 167:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 167:
    sage: 'gcd' in t
    TypeError: argument of type 'long' is not iterable
**********************************************************************
File "/opt/sage/tmp/sage0.py", line 177:
    sage: s.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
15 items had failures:
   9 of  23 in __main__.example_1
   1 of   3 in __main__.example_10
   1 of   4 in __main__.example_11
   1 of   6 in __main__.example_13
   1 of   3 in __main__.example_14
   2 of   4 in __main__.example_16
   1 of   4 in __main__.example_18
   1 of   5 in __main__.example_20
   1 of   4 in __main__.example_21
   1 of   3 in __main__.example_22
   1 of   6 in __main__.example_24
   1 of   4 in __main__.example_26
   3 of   5 in __main__.example_3
   2 of   5 in __main__.example_4
   1 of   5 in __main__.example_5
***Test Failed*** 27 failures.
For whitespace errors, see the file /opt/sage/tmp/.doctest_sage0.py
	 [5.1 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  3.1.2.rc2/devel/sage-main/sage/interfaces/sage0.py
Total time for all tests: 5.1 seconds
```



---

Comment by AlexGhitza created at 2008-09-15 02:05:12

Same outcome with rc3.  I just noticed that there are related failures in misc/randstate.pyx:


```
sage -t  devel/sage/sage/misc/randstate.pyx                 **********************************************************************
File "/opt/sage-3.1.2.rc3/tmp/randstate.py", line 124:
    : s = ZZ(subsage('initial_seed()'))
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage-3.1.2.rc3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[32]>", line 1, in <module>
        s = ZZ(subsage('initial_seed()'))###line 124:
    : s = ZZ(subsage('initial_seed()'))
      File "integer_ring.pyx", line 278, in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:5028)
      File "/opt/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 425, in __call__
        z = SageElement(P, callstr)
      File "/opt/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1281, in __init__
        raise TypeError, x
    TypeError: Error executing code in SAGE
    CODE:
    	sage2=sage1.get_as_sage_int()
    SAGE ERROR:
    	---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)

    /opt/sage-3.1.2.rc3/data/extcode/sage/<ipython console> in <module>()

    AttributeError: 'long' object has no attribute 'lift'
**********************************************************************
File "/opt/sage-3.1.2.rc3/tmp/randstate.py", line 125:
    : r = ZZ(subsage('ZZ.random_element(2^200)'))
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage-3.1.2.rc3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[33]>", line 1, in <module>
        r = ZZ(subsage('ZZ.random_element(2^200)'))###line 125:
    : r = ZZ(subsage('ZZ.random_element(2^200)'))
      File "/opt/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 225, in __call__
        return SageElement(self, x)
      File "/opt/sage-3.1.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1281, in __init__
        raise TypeError, x
    TypeError: Error executing code in SAGE
    CODE:
    	sage3=ZZ.random_element(2^200)
    SAGE ERROR:
    	---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    /opt/sage-3.1.2.rc3/data/extcode/sage/<ipython console> in <module>()

    NameError: name 'sage1' is not defined
**********************************************************************
File "/opt/sage-3.1.2.rc3/tmp/randstate.py", line 131:
    : r == ZZ.random_element(2^200)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   3 of  62 in __main__.example_0
***Test Failed*** 3 failures.
For whitespace errors, see the file /opt/sage-3.1.2.rc3/tmp/.doctest_randstate.py
	 [14.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/misc/randstate.pyx
Total time for all tests: 14.0 seconds
```



---

Comment by AlexGhitza created at 2008-09-16 03:40:45

Actually, I just noticed that I get the same failures with 3.1.1.


---

Comment by mabshoff created at 2008-09-16 06:21:46

Resolution: invalid


---

Comment by mabshoff created at 2008-09-16 06:21:46

This turned out to be a problem with a stale .sage directory. So make this invalied.

Cheers,

Michael
