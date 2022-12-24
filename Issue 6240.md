# Issue 6240: singular interface failure on itanium

archive/issues_006240.json:
```json
{
    "body": "Assignee: @williamstein\n\nI see the following test failure every time on *iras* (SUSE Itanium on skynet).  I do not see it Redhat Itanium.\n\n```\n\nwstein@iras:~/build/iras/sage-4.0.1> ./sage -t  \"devel/sage/doc/en/constructions/polynomials.rst\"\nsage -t  \"devel/sage/doc/en/constructions/polynomials.rst\"  \n**********************************************************************\nFile \"/home/wstein/build/iras/sage-4.0.1/devel/sage/doc/en/constructions/polynomials.rst\", line 322:\n    sage: print \"ignore this\";  J.minimal_associated_primes ()     # slightly random output\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[7]>\", line 1, in <module>\n        print \"ignore this\";  J.minimal_associated_primes ()     # slightly random output###line 322:\n    sage: print \"ignore this\";  J.minimal_associated_primes ()     # slightly random output\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 365, in wrapper\n        return func(*args, **kwds)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 341, in __exit__\n        self.singular.option(\"set\",self.o)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 1074, in option\n        self.eval(\"option(set,%s)\"%val.name())\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 543, in eval\n        raise RuntimeError, 'Singular error:\\n%s'%s\n    RuntimeError: Singular error:\n       ? unknown option `set`\n       ? unknown option `sage44`\n       ? error occurred in STDIN line 3: `option(set,sage44);`\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_14\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/build/iras/sage-4.0.1/tmp/.doctest_polynomials.py\n         [5.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/doc/en/constructions/polynomials.rst\"\nTotal time for all tests: 5.3 seconds\nwstein@iras:~/build/iras/sage-4.0.1> cat /etc/issue\n\nWelcome to SUSE Linux Enterprise Server 10 SP1 (ia64) - Kernel \\r (\\l).\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6240\n\n",
    "created_at": "2009-06-07T13:32:18Z",
    "labels": [
        "interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "singular interface failure on itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6240",
    "user": "@williamstein"
}
```
Assignee: @williamstein

I see the following test failure every time on *iras* (SUSE Itanium on skynet).  I do not see it Redhat Itanium.

```

wstein@iras:~/build/iras/sage-4.0.1> ./sage -t  "devel/sage/doc/en/constructions/polynomials.rst"
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
wstein@iras:~/build/iras/sage-4.0.1> cat /etc/issue

Welcome to SUSE Linux Enterprise Server 10 SP1 (ia64) - Kernel \r (\l).

```


Issue created by migration from https://trac.sagemath.org/ticket/6240





---

archive/issue_comments_049839.json:
```json
{
    "body": "There is also one other related failure on that box:\n\n```\nwstein@iras:~/build/iras/sage-4.0.1> ./sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\nsage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n**********************************************************************\nFile \"/home/wstein/build/iras/sage-4.0.1/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1262:\n    sage: I.minimal_associated_primes ()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[5]>\", line 1, in <module>\n        I.minimal_associated_primes ()###line 1262:\n    sage: I.minimal_associated_primes ()\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 365, in wrapper\n        return func(*args, **kwds)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 341, in __exit__\n        self.singular.option(\"set\",self.o)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 1074, in option\n        self.eval(\"option(set,%s)\"%val.name())\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 543, in eval\n        raise RuntimeError, 'Singular error:\\n%s'%s\n    RuntimeError: Singular error:\n       ? unknown option `set`\n       ? unknown option `sage789`\n       ? error occurred in STDIN line 3: `option(set,sage789);`\n**********************************************************************\nFile \"/home/wstein/build/iras/sage-4.0.1/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1301:\n    sage: I.radical()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_25[8]>\", line 1, in <module>\n        I.radical()###line 1301:\n    sage: I.radical()\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 365, in wrapper\n        return func(*args, **kwds)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 341, in __exit__\n        self.singular.option(\"set\",self.o)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 1074, in option\n        self.eval(\"option(set,%s)\"%val.name())\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 543, in eval\n        raise RuntimeError, 'Singular error:\\n%s'%s\n    RuntimeError: Singular error:\n       ? unknown option `set`\n       ? unknown option `sage816`\n       ? error occurred in STDIN line 3: `option(set,sage816);`\n**********************************************************************\nFile \"/home/wstein/build/iras/sage-4.0.1/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1315:\n    sage: I.radical()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_25[12]>\", line 1, in <module>\n        I.radical()###line 1315:\n    sage: I.radical()\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 365, in wrapper\n        return func(*args, **kwds)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 341, in __exit__\n        self.singular.option(\"set\",self.o)\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 1074, in option\n        self.eval(\"option(set,%s)\"%val.name())\n      File \"/home/wstein/build/iras/sage-4.0.1/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 543, in eval\n        raise RuntimeError, 'Singular error:\\n%s'%s\n    RuntimeError: Singular error:\n       ? unknown option `set`\n       ? unknown option `sage823`\n       ? error occurred in STDIN line 3: `option(set,sage823);`\n**********************************************************************\n2 items had failures:\n   1 of   6 in __main__.example_24\n   2 of  13 in __main__.example_25\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/wstein/build/iras/sage-4.0.1/tmp/.doctest_multi_polynomial_ideal.py\n         [25.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n```\n",
    "created_at": "2009-06-07T13:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49839",
    "user": "@williamstein"
}
```

There is also one other related failure on that box:

```
wstein@iras:~/build/iras/sage-4.0.1> ./sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
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

archive/issue_comments_049840.json:
```json
{
    "body": "We still have these problems with the new singular, in `4.0.2.rc3`. One can trace this through to singular segfaulting when trying to run certain commands; here's a sample session on iras:\n\n\n```\n                     SINGULAR                             /  Development\n A Computer Algebra System for Polynomial Computations   /   version 3-1-0\n                                                       0<\n     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \\   Mar 2009\nFB Mathematik der Universitaet, D-67653 Kaiserslautern    \\\n> ring r = 0,(x,y,z),dp;\n> poly p = z2+1;\n> poly q = z3+2;\n> ideal i = p*q*q,y-z2;\n> LIB \"primdec.lib\";\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/primdec.lib (1.147,2009/04/15)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/absfact.lib (1.7,2008/07/16)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/triang.lib (1.14,2009/04/14)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/matrix.lib (1.48,2009/04/10)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/nctools.lib (1.53,2009/04/15)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/ring.lib (1.34,2009/04/15)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/inout.lib (1.34,2009/04/15)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/random.lib (1.20,2009/04/15)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/poly.lib (1.53,2009/04/15)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/elim.lib (1.34,2009/05/05)\n// ** loaded /home/wstein/build/iras/sage-4.0.2.rc3/local/share/singular/general.lib (1.62,2009/04/15)\n> radical(i);\nSingular : signal 11 (v: 3102/2009061815):\ncurrent line:>>    pr = facstd(i);<<\nSegment fault/Bus error occurred (r:1245365674)\nplease inform the authors\ntrying to restart...\nSingular : signal 11 (v: 3102/2009061815):\ncurrent line:>>  rad=interred(phi(rad));<<\nSegment fault/Bus error occurred (r:1245365674)\nplease inform the authors\ntrying to restart...\n   ? error occurred in primdec.lib::radical line 5609: `  rad=interred(phi(rad));`\nSingular : signal 11 (v: 3102/2009061815):\ncurrent line:>>  rad=interred(phi(rad));<<\nSegment fault/Bus error occurred (r:1245365674)\nplease inform the authors\ntrying to restart...\n   ? error occurred in primdec.lib::radical line 5609: `  rad=interred(phi(rad));`\nSingular : signal 11 (v: 3102/2009061815):\ncurrent line:>>  rad=interred(phi(rad));<<\nSegment fault/Bus error occurred (r:1245365674)\nplease inform the authors\n```\n\n\nWe're going to try compiling with `-O0` to see if that helps; we'll see.",
    "created_at": "2009-06-18T23:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49840",
    "user": "@craigcitro"
}
```

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

archive/issue_comments_049841.json:
```json
{
    "body": "Turning the optimization level down to `-O0` from `-O2` fixes this -- see #6360. We'll merge the new spkg there for now, and hopefully Martin (or someone) will get to the bottom of this before the next release.",
    "created_at": "2009-06-19T04:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49841",
    "user": "@craigcitro"
}
```

Turning the optimization level down to `-O0` from `-O2` fixes this -- see #6360. We'll merge the new spkg there for now, and hopefully Martin (or someone) will get to the bottom of this before the next release.



---

archive/issue_comments_049842.json:
```json
{
    "body": "Note that this is still fixed by lowering the optimization level, so i'm lowering the priority from blocker so we can make this release.",
    "created_at": "2009-07-09T05:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49842",
    "user": "@williamstein"
}
```

Note that this is still fixed by lowering the optimization level, so i'm lowering the priority from blocker so we can make this release.



---

archive/issue_comments_049843.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2009-07-09T05:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49843",
    "user": "@williamstein"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_049844.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-04-20T20:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49844",
    "user": "@jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_049845.json:
```json
{
    "body": "Fixed by #11084.",
    "created_at": "2011-04-20T20:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6240#issuecomment-49845",
    "user": "@jdemeyer"
}
```

Fixed by #11084.
