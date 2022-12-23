# Issue 6759: [with spkg; needs review] Update sqlite to latest release - needed for Sun's compiler

Issue created by migration from https://trac.sagemath.org/ticket/6759

Original creator: drkirkby

Original creation time: 2009-08-16 08:22:40

Assignee: tbd

CC:  ddrake

I tried to build Sage using Sun's compiler suite, based on Sun Studio 12 update 1. This is of course good for Solaris, but will also find other issues. Since the Sun compiler is a lot stricter than the GNU one, it will find bad code. (It has for example already found code in libgcrypt where the code attempts to return an integer from a function declared with a return type of void). 

The version of sqlite in Sage (3.5.3) is the first package I found which failed to build with Sun's compiler. I downloaded the latest (3.6.17) source, and with the addition of 
"-I $SAGE_LOCAL/include" to CPPFLAGS, sqlite 3.6.17 will build with Sun's compiler. (I made many other changes to the spkg-install to, to generally improve it, but I think that was the only mandatory change).

Here's the update spkg and associated files. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite-3.6.17/

Dave 


---

Comment by AlexGhitza created at 2009-08-16 08:31:53

Changing assignee from tbd to mabshoff.


---

Comment by AlexGhitza created at 2009-08-16 08:31:53

Changing component from solaris to packages.


---

Comment by mvngu created at 2009-09-18 02:56:13

Resolution: fixed


---

Comment by mvngu created at 2009-09-18 02:56:13

An updated spkg is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/sqlite-3.6.17.spkg

which has changes committed in David Kirkby's name. I tested the package on the following platforms:


 * sage.math: x86_64 Ubuntu 8.04.3 --- compiles OK; all doctests pass.


 * bsd.math 32-bit: Mac OS X 10.5.8 --- compiles OK; the following doctest failed:
 {{{
sage -t -long "1-6759-sqlite/devel/sage/sage/interfaces/sage0.py"
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 445:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 445:
    sage: F == sage0(F)._sage_()
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 455, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)
    IOError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/1215//interface//tmp1215.sobj'
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 463:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 486:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 512:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 544:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 176:
    sage: sage0('factor(2^157-1)')
Expected:
    852133201 * 60726444167 * 1654058017289 * 2134387368610417
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: invalid literal for float(): e(None)
    852133201 * 60726444167 * 1654058017289 * 213438736861041
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 192:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 192:
    sage: len(t) > 100
    TypeError: object of type 'float' has no len()
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 194:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 194:
    sage: 'gcd' in t
    TypeError: argument of type 'float' is not iterable
**********************************************************************
7 items had failures:
   1 of   5 in __main__.example_20
   1 of   4 in __main__.example_21
   1 of   3 in __main__.example_22
   1 of   6 in __main__.example_24
   1 of   4 in __main__.example_26
   3 of   5 in __main__.example_3
   2 of   5 in __main__.example_4
***Test Failed*** 10 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-32/sage-4.1.2.alpha1-6759-sqlite/tmp/.doctest_sage0.py
	 [16.7 s]

 }}}


 * bsd.math 64-bit mode: Mac OS X 10.5.8 --- compiles OK; the following doctest failed:
 {{{
sage -t -long "fort-cliq-ecl/devel/sage/sage/interfaces/maxima.py"
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-6759-sqlite-fort-cliq-ecl/devel/sage/sage/interfaces/maxima.py", line 2108:
    sage: list(v)
Expected:
    [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
Got:
    [0, x, , 3*x^3, 4*x^4, 5*x^5]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_64
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-6759-sqlite-fort-cliq-ecl/tmp/.doctest_maxima.py
	 [18.0 s]

 }}}
 This doctest failure can be fixed by the patch at #6883.


 * cicero on SkyNet (x86 Fedora 9 with GCC 4.4.1) --- compiles OK; the following doctests failed:
 {{{
sage -t -long "devel/sage/sage/misc/randstate.pyx"          
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/misc/randstate.pyx", line 124:
    : s = ZZ(subsage('initial_seed()'))
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[32]>", line 1, in <module>
        s = ZZ(subsage('initial_seed()'))###line 124:
    : s = ZZ(subsage('initial_seed()'))
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/expect.py", line 1726, in _integer_
        return sage.rings.all.Integer(repr(self))
      File "integer.pyx", line 564, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6399)
    TypeError: unable to convert x (=---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/17448/_home_mvngu__sage_init_sage_0.py in <module>()

    /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python2.6/site-packages/sage/misc/functional.pyc in gen(x)
        353     Return the generator of x.
        354     """
    --> 355     return x.gen()
        356 
        357 def gens(x):

    AttributeError: 'int' object has no attribute 'gen') to an integer
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/misc/randstate.pyx", line 131:
    : r == ZZ.random_element(2^200)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   2 of  62 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/tmp/.doctest_randstate.py
	 [21.5 s]

<SNIP>

sage -t -long "devel/sage/sage/interfaces/expect.py"        
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/expect.py", line 805:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    �[0m
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/tmp/.doctest_expect.py
	 [16.3 s]
sage -t -long "devel/sage/sage/interfaces/scilab.py"        
	 [4.4 s]
sage -t -long "devel/sage/sage/interfaces/tachyon.py"       
	 [4.4 s]
sage -t -long "devel/sage/sage/interfaces/povray.py"        
	 [4.4 s]
sage -t -long "devel/sage/sage/interfaces/all.py"           
	 [0.1 s]
sage -t -long "devel/sage/sage/interfaces/tests.py"         
	 [6.4 s]
sage -t -long "devel/sage/sage/interfaces/sage0.py"         
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 55:
    sage: a^3
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 62:
    sage: V.gens()
Expected:
    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 75:
    sage: g = V.0;  g
Expected:
    (1, 0, 0, 0)
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 85:
    sage: s('%s.parent()'%g.name())
Expected:
    Vector space of dimension 4 over Rational Field
Got:
    (1, 0, 0, 0)
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 93:
    sage: s('x = 5')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 97:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 105:
    sage: a
Expected:
    10
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 114:
    sage: s3('"x"')
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 116:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 320:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 334:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '4'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 364:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    '2'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 373:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 397:
    sage: sage0.version()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[2]>", line 1, in <module>
        sage0.version()###line 397:
    sage: sage0.version()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 402, in version
        return sage0_version()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 547, in sage0_version
        return str(sage0('version()'))
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 263, in __call__
        return SageElement(self, x)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/expect.py", line 1433, in __init__
        raise TypeError, x
    TypeError: Error executing code in Sage
    CODE:
    	sage0=version()
    Sage ERROR:
    	---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/11961/_home_mvngu__sage_init_sage_0.py in <module>()

    NameError: name 'x' is not defined
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 399:
    sage: sage0.version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 417:
    sage: sage0.new(2)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 445:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 445:
    sage: F == sage0(F)._sage_()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 455, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)
    IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//temp/cicero/11791//interface//tmp11791.sobj'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 463:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 486:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 512:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 544:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: invalid literal for float(): Sage Version 4.1.2.alpha1, Release Date: 2009-09-07
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 176:
    sage: sage0('factor(2^157-1)')
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        sage0('factor(2^157-1)')###line 176:
    sage: sage0('factor(2^157-1)')
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/expect.py", line 1592, in __repr__
        s =  s.replace(self._name, self.__dict__['__custom_name'])
    KeyError: '__custom_name'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 192:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 192:
    sage: len(t) > 100
    TypeError: object of type 'float' has no len()
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 194:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 194:
    sage: 'gcd' in t
    TypeError: argument of type 'float' is not iterable
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/interfaces/sage0.py", line 204:
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
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/tmp/.doctest_sage0.py
	 [26.6 s]

<SNIP>

sage -t -long "devel/sage/sage/server/simple/twist.py"      
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/devel/sage/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6759-sqlite/tmp/.doctest_twist.py
	 [17.9 s]
 }}}


 * eno on SkyNet (x86_64 Fedora 9 with GCC 4.4.1) --- compiles OK; the following doctest failed:
 {{{
sage -t -long "devel/sage/sage/combinat/designs/covering_design.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
	 [1.4 s]
 }}}
 This passes on a second try.


 * lena on SkyNet (x86_64 RHEL 5.3 with GCC 4.4.1) --- compiles OK; all doctests pass.


 * menas on SkyNet (x86_64 openSUSE 11.1 with GCC 4.4.1) --- compiles OK; all doctests pass.


 * t2.math --- compiles OK; I can't run any doctests since Sage doesn't completely build on t2.math yet.


As far as I'm concerned, it's positive review from me. Merged in standard packages repository.


---

Comment by was created at 2009-09-29 02:40:19

Changing status from closed to reopened.


---

Comment by was created at 2009-09-29 02:40:19

This breaks on Cygwin, whereas the version currently in Sage works fine:

```
/sage -i http://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite-3.6.17/sqlite-3.6.17.spkg

...
configure: creating ./config.status
config.status: creating Makefile
config.status: creating sqlite3.pc
config.status: executing depfiles commands
make: *** No rule to make target `src/sqlite.h.in', needed by `sqlite3.h'.  Stop.
Error making sqlite

real    4m0.010s
user    1m7.730s
sys     3m5.796s
sage: An error occurred while installing sqlite-3.6.17
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wstein/sage-4.1.2.alpha1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wstein/sage-4.1.2.alpha1/spkg/build/sqlite-3.6.17 and type 'make'.
Instead type "/home/wstein/sage-4.1.2.alpha1/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wstein/sage-4.1.2.alpha1/spkg/build/sqlite-3.6.17
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


In irc ddrake conjectures that:

```
ddrake: spkg-install copies over a Makefile.in that I think is from the older version, and it fails immediately because source files got moved
```


Thus we're changing this back to "needs work".


---

Comment by was created at 2009-09-29 02:40:19

Resolution changed from fixed to 


---

Comment by ddrake created at 2009-09-29 03:02:15

Here's the effect of the old Makefile.in "patch":

```
--- src/Makefile.in	2007-11-24 00:05:48.000000000 +0900
+++ patches/Makefile.in	2008-05-17 03:36:19.000000000 +0900
@@ -570,11 +570,12 @@
 		libtclsqlite3.la $(LIBTCL)
 
 
-install:	sqlite3 libsqlite3.la sqlite3.h ${HAVE_TCL:1=tcl_install}
+#install:	sqlite3 libsqlite3.la sqlite3.h ${HAVE_TCL:1=tcl_install}
+install: 	libsqlite3.la sqlite3.h ${HAVE_TCL:1=tcl_install}
 	$(INSTALL) -d $(DESTDIR)$(libdir)
 	$(LTINSTALL) libsqlite3.la $(DESTDIR)$(libdir)
 	$(INSTALL) -d $(DESTDIR)$(exec_prefix)/bin
-	$(LTINSTALL) sqlite3 $(DESTDIR)$(exec_prefix)/bin
+	#$(LTINSTALL) sqlite3 $(DESTDIR)$(exec_prefix)/bin
 	$(INSTALL) -d $(DESTDIR)$(prefix)/include
 	$(INSTALL) -m 0644 sqlite3.h $(DESTDIR)$(prefix)/include
 	$(INSTALL) -m 0644 $(TOP)/src/sqlite3ext.h $(DESTDIR)$(prefix)/include
```

It just comments out a bit of the install target. In 3.6.17, Makefile.in is all automake-generated, and it's not at all obvious (to me, at any rate) how to make the corresponding change. However, I'm wondering if we need to make the change at all. The idea is to not install the sqlite client; what will happen if we do that? In `spkg-install`, it says the client isn't needed for Sage, but if we install it anyway, will anything bad happen? 

If we can get by without any patches at all to the source, that seems ideal and very easy. Certainly better than manually patching an automake Makefile!


---

Comment by was created at 2009-09-29 04:01:26

David says: "
For reasons I do not understand, I am unable to edit the ticket. I was
going to suggest we remake the Makefile.in using the latest automake

Dave"


---

Comment by ddrake created at 2009-09-29 05:10:29

I have an updated spkg available at http://sage.math.washington.edu/home/drake/sqlite-3.6.17.p0.spkg

It is identical to the current one, except it doesn't copy over a new Makefile.in on Cygwin. It appears to build and install fine on Cygwin, and since the only change is in a block of code only executed on Cygwin, it should also work on all other platforms too.


---

Comment by was created at 2009-10-24 19:21:47

"The requested URL /home/drake/sqlite-3.6.17.p0.spkg was not found on this server."


---

Comment by ddrake created at 2009-10-25 00:31:39

Replying to [comment:8 was]:
> "The requested URL /home/drake/sqlite-3.6.17.p0.spkg was not found on this server."

Oops, I deleted that the other day, thinking it had been dealt with. I'll remake the spkg. Marking as "needs work"


---

Comment by ddrake created at 2009-10-25 00:31:39

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2009-10-25 01:31:05

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2009-10-25 01:31:05

Here's the recreated spkg: http://sage.math.washington.edu/home/drake/spkg/sqlite-3.6.17.p0.spkg

I haven't tested it on Cygwin, since I don't have access to my Cygwin VM right now, but It Should Work. (Famous last words...?)


---

Comment by mhansen created at 2009-10-26 09:15:39

Dan's changes worked for me in Cygwin.  So, +1 on Dan's package.

I have a SQLite 3.6.19 spkg at http://sage.math.washington.edu/home/mhansen/sqlite-3.6.19.p0.spkg which is based off of sqlite-3.6.17.p0.spkg and merely replaces the src/ directory.


---

Comment by mhansen created at 2009-10-26 09:15:49

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 05:24:48

Resolution: fixed


---

Comment by mhansen created at 2009-10-31 05:24:48

Merged sqlite-3.6.19.p0.spkg


---

Attachment


---

Comment by mhansen created at 2009-10-31 09:08:28

The above patch also had to be applied due to a change in the order the graphs appear.
