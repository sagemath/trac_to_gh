# Issue 6240: singular interface failure on itanium

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-07 13:32:18

Assignee: was

I see the following test failure every time on *iras* (SUSE Itanium on skynet).  I do not see it Redhat Itanium.

```

wstein`@`iras:~/build/iras/sage-4.0.1> ./sage -t  "devel/sage/doc/en/constructions/polynomials.rst"
sage -t  "devel/sage/doc/en/constructions/polynomials.rst"  
**********************************************************************
File "/home/wstein/build/iras/sage-4.0.1/devel/sage/doc/en/constructions/polynomials.rst", line 322:
    sage: print "ignore this";  J.minimal_associated_primes ()     # slightly random output
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[7]>", line 1, in <module>
        print "ignore this";  J.minimal_associated_primes ()     # slightly random output###line 322:
    sage: print "ignore this";  J.minimal_associated_primes ()     # slightly random output
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 365, in wrapper
        return func(*args, **kwds)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 341, in __exit__
        self.singular.option("set",self.o)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1074, in option
        self.eval("option(set,%s)"%val.name())
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 543, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? unknown option `set`
       ? unknown option `sage44`
       ? error occurred in STDIN line 3: `option(set,sage44);`
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_14
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/iras/sage-4.0.1/tmp/.doctest_polynomials.py
         [5.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/doc/en/constructions/polynomials.rst"
Total time for all tests: 5.3 seconds
wstein`@`iras:~/build/iras/sage-4.0.1> cat /etc/issue

Welcome to SUSE Linux Enterprise Server 10 SP1 (ia64) - Kernel \r (\l).

```



---

Comment by was created at 2009-06-07 13:33:39

There is also one other related failure on that box:

```
wstein`@`iras:~/build/iras/sage-4.0.1> ./sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/home/wstein/build/iras/sage-4.0.1/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 1262:
    sage: I.minimal_associated_primes ()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[5]>", line 1, in <module>
        I.minimal_associated_primes ()###line 1262:
    sage: I.minimal_associated_primes ()
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 365, in wrapper
        return func(*args, **kwds)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 341, in __exit__
        self.singular.option("set",self.o)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1074, in option
        self.eval("option(set,%s)"%val.name())
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 543, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? unknown option `set`
       ? unknown option `sage789`
       ? error occurred in STDIN line 3: `option(set,sage789);`
**********************************************************************
File "/home/wstein/build/iras/sage-4.0.1/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 1301:
    sage: I.radical()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[8]>", line 1, in <module>
        I.radical()###line 1301:
    sage: I.radical()
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 365, in wrapper
        return func(*args, **kwds)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 341, in __exit__
        self.singular.option("set",self.o)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1074, in option
        self.eval("option(set,%s)"%val.name())
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 543, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? unknown option `set`
       ? unknown option `sage816`
       ? error occurred in STDIN line 3: `option(set,sage816);`
**********************************************************************
File "/home/wstein/build/iras/sage-4.0.1/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 1315:
    sage: I.radical()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[12]>", line 1, in <module>
        I.radical()###line 1315:
    sage: I.radical()
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 365, in wrapper
        return func(*args, **kwds)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 341, in __exit__
        self.singular.option("set",self.o)
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1074, in option
        self.eval("option(set,%s)"%val.name())
      File "/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 543, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? unknown option `set`
       ? unknown option `sage823`
       ? error occurred in STDIN line 3: `option(set,sage823);`
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_24
   2 of  13 in __main__.example_25
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wstein/build/iras/sage-4.0.1/tmp/.doctest_multi_polynomial_ideal.py
         [25.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
```



---

Comment by craigcitro created at 2009-06-18 23:16:40

We still have these problems with the new singular, in `4.0.2.rc3`. One can trace this through to singular segfaulting when trying to run certain commands; here's a sample session on iras:


```
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-1-0
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   Mar 2009
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> ring r = 0,(x,y,z),dp;
> poly p = z2+1;
> poly q = z3+2;
> ideal i = p*q*q,y-z2;
> LIB "primdec.lib";
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/primdec.lib (1.147,2009/04/15)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/absfact.lib (1.7,2008/07/16)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/triang.lib (1.14,2009/04/14)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/matrix.lib (1.48,2009/04/10)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/nctools.lib (1.53,2009/04/15)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/ring.lib (1.34,2009/04/15)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/inout.lib (1.34,2009/04/15)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/random.lib (1.20,2009/04/15)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/poly.lib (1.53,2009/04/15)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/elim.lib (1.34,2009/05/05)
// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/general.lib (1.62,2009/04/15)
> radical(i);
Singular : signal 11 (v: 3102/2009061815):
current line:>>    pr = facstd(i);<<
Segment fault/Bus error occurred (r:1245365674)
please inform the authors
trying to restart...
Singular : signal 11 (v: 3102/2009061815):
current line:>>  rad=interred(phi(rad));<<
Segment fault/Bus error occurred (r:1245365674)
please inform the authors
trying to restart...
   ? error occurred in primdec.lib::radical line 5609: `  rad=interred(phi(rad));`
Singular : signal 11 (v: 3102/2009061815):
current line:>>  rad=interred(phi(rad));<<
Segment fault/Bus error occurred (r:1245365674)
please inform the authors
trying to restart...
   ? error occurred in primdec.lib::radical line 5609: `  rad=interred(phi(rad));`
Singular : signal 11 (v: 3102/2009061815):
current line:>>  rad=interred(phi(rad));<<
Segment fault/Bus error occurred (r:1245365674)
please inform the authors
```


We're going to try compiling with `-O0` to see if that helps; we'll see.


---

Comment by craigcitro created at 2009-06-19 04:48:27

Turning the optimization level down to `-O0` from `-O2` fixes this -- see #6360. We'll merge the new spkg there for now, and hopefully Martin (or someone) will get to the bottom of this before the next release.


---

Comment by was created at 2009-07-09 05:03:57

Note that this is still fixed by lowering the optimization level, so i'm lowering the priority from blocker so we can make this release.


---

Comment by was created at 2009-07-09 05:03:57

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2011-04-20 20:57:30

Resolution: duplicate


---

Comment by jdemeyer created at 2011-04-20 20:57:30

Fixed by #11084.
