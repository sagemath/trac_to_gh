# Issue 6564: ecl will not build on Solaris - looks like make exiting when it tries to delete non-existant file.

Issue created by migration from https://trac.sagemath.org/ticket/6564

Original creator: drkirkby

Original creation time: 2009-07-20 00:23:56

Assignee: tbd

Keywords: solaris ecl config.h

I've not looked into debugging this yet, but ecl fails on Solaris. This is on a Sun Blade 2000 - not 't2' though I expect it would fail on that too. 

It looks like a failure to remove the non-existant file config.h is causing this. Perhaps rm -f would be acceptable?? It's possible that rm on Solaris exits with a non-zero exit code if it can't delete a file, but on other systems this does not happen. I don't know, and have not investigated yet. 

See below.


```
sed '/-CUT-/,$d' ./ecl/config.h > ./ecl/config-install.h
/export/home/drkirkby/sage/sage-4.1/spkg/build/ecl-9.4.1/src/src/install.sh -c -m 644 ./ecl/*.h /export/home/drkirkby/sage/sage-4.1/local/include//ecl
if (echo c | grep gc); then \
 /bin/bash /export/home/drkirkby/sage/sage-4.1/spkg/build/ecl-9.4.1/src/src/mkinstalldirs /export/home/drkirkby/sage/sage-4.1/local/include//ecl/gc/private; \
  /export/home/drkirkby/sage/sage-4.1/spkg/build/ecl-9.4.1/src/src/install.sh -c -m 644 ./ecl/gc/*.h /export/home/drkirkby/sage/sage-4.1/local/include//ecl/gc; \
  /export/home/drkirkby/sage/sage-4.1/spkg/build/ecl-9.4.1/src/src/install.sh -c -m 644 ./ecl/gc/private/*.h /export/home/drkirkby/sage/sage-4.1/local/include//ecl/gc/private; \
fi
rm /export/home/drkirkby/sage/sage-4.1/local/include//ecl/config.h
/export/home/drkirkby/sage/sage-4.1/local/include//ecl/config.h: No such file or directory
make[3]: *** [install-base] Error 2
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1/spkg/build/ecl-9.4.1/src/build'
make[2]: *** [install] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1/spkg/build/ecl-9.4.1/src'
Failed to install ECL ... exiting

real    8m24.691s
user    7m7.665s
sys     1m2.739s
sage: An error occurred while installing ecl-9.4.1
```



---

Comment by drkirkby created at 2009-07-25 11:41:05

Creating an empty file $SAGE_HOME/local/include/ecl/config.h does allow the build of ECL to progress further, but it does not result in a working ecl installation. The build of ecl still fails. Whether that is a result of this problem I do not know, but I suspect not. Hence that error will be reported as another trac ticket.


---

Comment by drkirkby created at 2009-07-25 11:41:05

Changing assignee from tbd to drkirkby.


---

Attachment

install.log showing ecl failure due to missing config.h


---

Comment by drkirkby created at 2009-07-25 12:56:34

The attached install.log was created on 't2', a Sun T5240, with Sage-4.1.1.alpha0, whereas the first output I showed was created on my own Sun Blade 2000 with Sage-4.1. (Both used the same version of Solaris)

(Note the Blade 2000 took about half the time of the T5240 to do this task), which shows the T5240 is not ideally suited to the sort of things currently being used for, but with more users, its performance will shine.)

I see a few warnings - see below. What is clear is that the build often complains about things redefined in {{{
$SAGE_HOMEspkg/build/ecl-9.4.1/src/build/ecl/config.h
}}} 
but I see no record of that file ever being copied to 

```
$SAGE_HOME/local/include//ecl/config.
```


Anyways, here are some warnings noted.

```
1)
Unknown symbol: mp::*current-process*
Unknown symbol: mp::+load-compile-lock+
Unknown symbol: mp::+load-compile-lock+
Unknown symbol: si::pretty-print-format


2)  warning: "ecl_int16_t" redefined
3)  warning: "ecl_int32_t" redefined

4) ;;; Removing unused variable PPN

5) ;;; Warning: in file src:lsp;setf.lsp, position 4, and form
;;;   (FSET 'GET-SETF-EXPANSION #'(LAMBDA-BLOCK GET-SETF-EXPANSION # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP

6) Quite a few reports of ";;; Note: Eliminating unreachable code"

7) ;;; Too few arguments for proclaimed function GET-SYSPROP

8) ;;; Warning: in file src:lsp;assert.lsp, position 9, and form
;;;   (FSET 'ACCUMULATE-CASES #'(LAMBDA-BLOCK ACCUMULATE-CASES # ...))
;;; The variable MACRO-NAME is not used.

9)
;;; Note: in file src:lsp;seqlib.lsp, position 3, and form
;;;   (FSET 'UNSAFE-FUNCALL1 #'(LAMBDA-BLOCK UNSAFE-FUNCALL1 # ...))
;;; In function UNSAFE-FUNCALL1, checking types of arguments X F.
;;; Note: in file src:lsp;seqlib.lsp, position 3, and form
;;;   (FSET 'UNSAFE-FUNCALL1 #'(LAMBDA-BLOCK UNSAFE-FUNCALL1 # ...))
;;; Unable to emit check for variable (OPTIONAL-CHECK-TYPE F FUNCTION)

10) 
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP
;;; Warning: in file src:lsp;describe.lsp, position 31, and form
;;;   (FSET 'PRINT-DOC #'(LAMBDA-BLOCK PRINT-DOC # ...))
;;; Too few arguments for proclaimed function GET-SYSPROP

11)

;;; Warning: in file src:lsp;top.lsp, position 43, and form
;;;   (FSET 'TPL-LAMBDA-EXPRESSION-COMMAND #'(LAMBDA-BLOCK TPL-LAMBDA-EXPRESSION-COMMAND # ...))
;;; The variable NO-VALUES is not used.

```



---

Attachment

A second attampt after touching the missing file. The build stops earlier, which is odd


---

Comment by drkirkby created at 2009-07-25 13:49:13

I attached a copy of the complete ecl part of install.log, but this time after I touched the file $SAGE_HOME/local/include/ecl/config.h first

What is odd, is that the build process aborted earlier (the log file is 379 kB, rather than the 0.7 MB ealier). 

I've tried downloading version 9.4.1 of ECL (as used in Sage) from the site at http://ecls.sourceforge.net/ The build of that failed. (I can't recall exactly where). I also downloaded the latest ECL (9.7.1) and that failed too. Finally I tried the latest snaphot via CVS and that would not build. 

I've reported this on the ECL tracker 
https://sourceforge.net/tracker/index.php?func=detail&aid=2824044&group_id=30035&atid=398054

and the ECL mailing list
https://sourceforge.net/tracker/index.php?func=detail&aid=2824200&group_id=30035&atid=398054

Neither has received any response in the 4 to 5 days since I reported this. 

Has anyone got any idea what we might do to resolve this issue? 

Dave


---

Comment by drkirkby created at 2009-08-08 21:21:43

A new version of ECL (9.8.1) has been released. I've created a package at 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/ecl-9.8.1.spkg

It is NOT ready for review yet, as I know Maxima will break with this, due to a bug in Maxima. 

Dave


---

Comment by drkirkby created at 2009-08-09 08:03:28

Here is an updated .spkg for ECL, which fixes the bugs which prevent ECL building on Solaris SPARC.

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/ecl-9.8.1.spkg

I've created a new Maxima.spkg based on the latest 5.19.0 (trac #6999)

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg

If this updated ECL is applied, then the update to Maxima *must* be made, as this new ECL will not build Maxima due to a 35-year old bug in Maxima (confirmed by the Maxima developers).


---

Comment by drkirkby created at 2009-08-10 19:43:18

There is a bug in ECL which is causing test failures. The bug has been identified by Juan Jose Garcia-Ripoll and I intend implementing his change and making a new .spkg within the next 18 hours (at the very most - probably less than 3 hours). 

Dave


---

Comment by drkirkby created at 2009-08-11 07:45:03

The bug has been corrected. Some other changes were made to spkg-install too. See relevant files at

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1

The ecl spkg file is:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.1/ecl-9.8.1.spkg


---

Comment by drkirkby created at 2009-08-13 06:55:37

There has been another update to ECL - it is now version 9.8.3 The files may be found at

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.3


---

Comment by wdj created at 2009-08-14 11:34:52

The latest version installs on an intel macbook running 10.4.11.


---

Comment by AlexGhitza created at 2009-08-16 08:31:06

Changing component from solaris to packages.


---

Comment by awebb created at 2009-08-17 10:02:20

I don't have access to solaris but I tried on 32-bit scientific linux. I had problems with ecl-9.8.1 but ecl-9.8.3.spkg installed without problems. I used it to compile maxima-5.19.0 (#6699) and fricas-1.0.7. Both packages compiled and installed. The tests in various interface files: lisp.py, fricas.py, axiom.py all passed. There were issues with maxima.py but I think that is a maxima problem and not an ecl one.

Adam


---

Comment by awebb created at 2009-08-17 19:48:28

I got similar positive results with 64 bit Ubuntu 9.04. A.


---

Comment by awebb created at 2009-08-18 17:59:03

Two small things.
1. There is already an ecl 9.8.4 which has some bug fixes and can be dropped into the spkg.
2. There are uncommitted changes to the mercurial repository in the spkg. 

Adam


---

Comment by drkirkby created at 2009-08-21 06:12:41

I've updated the .spkg file to the latest http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/ release. I've not committed this since I don't know exactly how to - I've had a few problems. It is something I need to look at again. If someone could do that bit for me.


---

Comment by AlexGhitza created at 2009-08-23 14:43:02

Replying to [comment:15 drkirkby]:
> I've updated the .spkg file to the latest http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4/ release. I've not committed this since I don't know exactly how to - I've had a few problems. It is something I need to look at again. If someone could do that bit for me. 
> 

Done, and placed the new spkg at

http://sage.math.washington.edu/home/ghitza/ecl-9.8.4.spkg


---

Comment by awebb created at 2009-08-25 07:07:33

I ran the same tests with the new package and everything worked. The package built and ran both maxima and fricas on 32 and 64 bit linux. Someone might want to check on Solaris and Mac but it looks good to me.

Adam


---

Attachment

full log of doctest failures due to new ecl + maxima


---

Comment by mvngu created at 2009-08-31 16:22:13

I've copied AlexGhitza's ECL and Maxima packages to my home directory: 



http://sage.math.washington.edu/home/mvngu/patch/ecl-9.8.4.spkg 


http://sage.math.washington.edu/home/mvngu/patch/maxima-5.19.1.p0.spkg



These updated spkg's build fine on sage.math. But I get the following doctest failures:

```
sage -t -long devel/sage-main/sage/misc/sagedoc.py # 1 doctests failed
sage -t -long devel/sage-main/sage/symbolic/expression.pyx # 1 doctests failed
sage -t -long devel/sage-main/sage/calculus/calculus.py # 1 doctests failed
sage -t -long devel/sage-main/sage/interfaces/maxima.py # 17 doctests failed
sage -t -long devel/sage-main/doc/en/constructions/plotting.rst # 1 doctests failed
sage -t -long devel/sage-main/doc/fr/tutorial/tour_algebra.rst # 4 doctests failed
sage -t -long devel/sage-main/doc/en/tutorial/tour_algebra.rst # 4 doctests failed
sage -t -long devel/sage-main/sage/symbolic/assumptions.py # 1 doctests failed
sage -t -long devel/sage-main/doc/en/constructions/interface_issues.rst # 3 doctests failed
sage -t -long devel/sage-main/sage/calculus/functional.py # 2 doctests failed
sage -t -long devel/sage-main/doc/en/constructions/linear_algebra.rst # 3 doctests failed
sage -t -long devel/sage-main/doc/en/constructions/calculus.rst # 1 doctests failed
sage -t -long devel/sage-main/doc/fr/tutorial/interfaces.rst # 11 doctests failed
sage -t -long devel/sage-main/doc/en/tutorial/interfaces.rst # 11 doctests failed
```

A full doctest log is attached to this ticket; see `doctest-mvngu.log`. I'm marking this ticket and #6699 as "needs work". Once the doctest failures are resolved, both of these tickets can be restored to "positive review".


---

Comment by mvngu created at 2009-08-31 16:25:51

Oh... I didn't apply the patch at #6699. No wonder I got the doctest failures.


---

Comment by mvngu created at 2009-09-02 10:45:01

Resolution: fixed


---

Comment by mvngu created at 2009-09-02 10:45:01

Here are the results of my test on various platforms. For each of the reported platforms, I first installed ecl-9.8.4.spkg, then maxima-5.19.1.spkg, followed by applying the patch `maxima_doctests.patch` at #6699.

 * sage.math --- compile: yes; doctests pass: yes.

 * t2.math --- compile: yes; doctests pass: I don't know. I compiled Sage 4.1.1 on t2.math using GCC 4.4.1 with the Sun linker. As I reported before on sage-devel, the compilation fails when building the package sage-4.1.1.spkg. It's good enough that both ecl-9.8.4.spkg and maxima-5.19.1.spkg built successfully.

 * bsd.math 32-bit Mac OS X 10.5.8 --- compile: yes; doctests pass: yes.

 * bsd.math Mac OS X 10.5.8 in 64-bit mode --- compile: yes. The following doctests failed:

```
sage -t -long "64/sage-4.1.1/devel/sage-main/build/lib.macosx-10.3-i386-2.6/sage/graphs/graph.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/build/lib.macosx-10.3-i386-2.6/sage/graphs/graph_coloring.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/build/sage/graphs/cliquer.pyx"
sage -t -long "64/sage-4.1.1/devel/sage-main/build/sage/graphs/graph.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/build/sage/graphs/graph_coloring.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/build/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx"
sage -t -long "64/sage-4.1.1/devel/sage-main/build/sage/interfaces/sage0.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst"
sage -t -long "64/sage-4.1.1/devel/sage-main/sage/graphs/cliquer.pyx"
sage -t -long "64/sage-4.1.1/devel/sage-main/sage/graphs/graph.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/sage/graphs/graph_coloring.py"
sage -t -long "64/sage-4.1.1/devel/sage-main/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx"
```

 The failures relating to graph theory modules are expected failures, as cliquer is known to fail to build under OS X 10.5.8 in 64-bit mode and under various 64-bit platforms. At least I'm glad that ecl-9.8.4.spkg and maxima-5.19.1.spkg successfully compile in 64-bit mode.

 * Fedora 9 x86 GCC 4.4.1 (cicero on SkyNet) --- compile: yes; doctests pass: no, I got some doctest failures:

```
sage -t -long "devel/sage-main/sage/misc/randstate.pyx"
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/misc/randstate.pyx", line 124:
    : s = ZZ(subsage('initial_seed()'))
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[32]>", line 1, in <module>
        s = ZZ(subsage('initial_seed()'))###line 124:
    : s = ZZ(subsage('initial_seed()'))
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 1726, in _integer_
        return sage.rings.all.Integer(repr(self))
      File "integer.pyx", line 569, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6444)
    TypeError: unable to convert x (=---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/15775/_home_mvngu__sage_init_sage_0.py in <module>()

    /home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python2.6/site-packages/sage/misc/functional.pyc in gen(x)
        353     Return the generator of x.
        354     """
    --> 355     return x.gen()
        356
        357 def gens(x):

    AttributeError: 'int' object has no attribute 'gen') to an integer
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/misc/randstate.pyx", line 131:
    : r == ZZ.random_element(2^200)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   2 of  62 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/bin/sage-4.1.1/tmp/.doctest_randstate.py
         [19.7 s]

sage -t -long "devel/sage-main/sage/interfaces/expect.py"
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/expect.py", line 805:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    ^[[0m
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/bin/sage-4.1.1/tmp/.doctest_expect.py
         [14.7 s]

sage -t -long "devel/sage-main/sage/interfaces/sage0.py"
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 55:
    sage: a^3
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 62:
    sage: V.gens()
Expected:
    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 75:
    sage: g = V.0;  g
Expected:
    (1, 0, 0, 0)
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 85:
    sage: s('%s.parent()'%g.name())
Expected:
    Vector space of dimension 4 over Rational Field
Got:
    (1, 0, 0, 0)
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 93:
    sage: s('x = 5')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 97:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 105:
    sage: a
Expected:
    10
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 114:
    sage: s3('"x"')
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 116:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 320:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 334:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '4'
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 364:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    '2'
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 373:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 397:
    sage: sage0.version()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[2]>", line 1, in <module>
        sage0.version()###line 397:
    sage: sage0.version()
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 402, in version
        return sage0_version()
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 547, in sage0_version
        return str(sage0('version()'))
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 263, in __call__
        return SageElement(self, x)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 1433, in __init__
        raise TypeError, x
    TypeError: Error executing code in Sage
    CODE:
        sage0=version()
    Sage ERROR:
        ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/10033/_home_mvngu__sage_init_sage_0.py in <module>()

    NameError: name 'x' is not defined
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 399:
    sage: sage0.version() == version()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[3]>", line 1, in <module>
        sage0.version() == version()###line 399:
    sage: sage0.version() == version()
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 402, in version
        return sage0_version()
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 547, in sage0_version
        return str(sage0('version()'))
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/expect.py", line 1592, in __repr__
        s =  s.replace(self._name, self.__dict__['__custom_name'])
    KeyError: '__custom_name'
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 417:
    sage: sage0.new(2)
Expected:
    2
Got:
    Sage Version 4.1.1, Release Date: 2009-08-14
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 445:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 445:
    sage: F == sage0(F)._sage_()
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 455, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)
    IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//temp/cicero/9862//interface//tmp9862.sobj'
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 463:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 486:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 512:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 544:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: invalid literal for float(): e(None
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 176:
    sage: sage0('factor(2^157-1)')
Expected:
    852133201 * 60726444167 * 1654058017289 * 2134387368610417
Got:
    4.3093440000000003
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 192:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 192:
    sage: len(t) > 100
    TypeError: object of type 'long' has no len()
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 194:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/bin/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 194:
    sage: 'gcd' in t
    TypeError: argument of type 'long' is not iterable
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/sage0.py", line 204:
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
For whitespace errors, see the file /home/mvngu/usr/cicero/bin/sage-4.1.1/tmp/.doctest_sage0.py
         [20.5 s]

sage -t -long "devel/sage-main/sage/interfaces/maxima.py"
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/maxima.py", line 934:
    sage: 'gcd' in t
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/bin/sage-4.1.1/devel/sage-main/sage/interfaces/maxima.py", line 2182:
    sage: 'gcd' in m.trait_names()
Expected:
    True
Got:
    False
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_18
   1 of   4 in __main__.example_68
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/bin/sage-4.1.1/tmp/.doctest_maxima.py
         [32.9 s]
```


 * Fedora 9 x86_64 GCC 4.4.1 (eno on SkyNet) --- compile: yes; doctests pass: no, I got some doctest failures:

```
sage -t -long "devel/sage-main/sage/matrix/matrix_space.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [0.9 s]

sage -t -long "devel/sage-main/sage/interfaces/maxima.py"
**********************************************************************
File "/home/mvngu/usr/eno/bin/sage-4.1.1/devel/sage-main/sage/interfaces/maxima.py", line 934:
    sage: 'gcd' in t
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/eno/bin/sage-4.1.1/devel/sage-main/sage/interfaces/maxima.py", line 2182:
    sage: 'gcd' in m.trait_names()
Expected:
    True
Got:
    False
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_18
   1 of   4 in __main__.example_68
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/eno/bin/sage-4.1.1/tmp/.doctest_maxima.py
         [14.5 s]
```


 * RHEL Server 5.3 x86_64-k10 GeForce GPUs GCC 4.4.1 (lena on SkyNet) --- compile: yes; doctests pass: no, I got some doctest failures:

```
sage -t -long "devel/sage-main/sage/interfaces/maxima.py"
**********************************************************************
File "/home/mvngu/usr/lena/bin/sage-4.1.1/devel/sage-main/sage/interfaces/maxima.py", line 934:
    sage: 'gcd' in t
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/lena/bin/sage-4.1.1/devel/sage-main/sage/interfaces/maxima.py", line 2182:
    sage: 'gcd' in m.trait_names()
Expected:
    True
Got:
    False
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_18
   1 of   4 in __main__.example_68
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/lena/bin/sage-4.1.1/tmp/.doctest_maxima.py
         [15.8 s]
```

For each of the above Fedora/Red Hat platforms, the common failure is in this file:

```
sage -t -long "devel/sage-main/sage/interfaces/maxima.py"
```

The relevant doctests that result in the failures are:

```
    def trait_names(self, verbose=True, use_disk_cache=True):
        """                                                                     
        Return all Maxima commands, which is useful for tab completion.         
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: t = maxima.trait_names(verbose=False)                         
            sage: 'gcd' in t                                                    
            True                                                                
            sage: len(t)    # random output                                     
            1840                                                                
        """
```

and

```
    def trait_names(self, verbose=False):
        """                                                                     
        Return all Maxima commands, which is useful for tab completion.         
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: m = maxima(2)                                                 
            sage: 'gcd' in m.trait_names()                                      
            True                                                                
        """
```

A work around is to change the first doctest to:

```
    def trait_names(self, verbose=True, use_disk_cache=True):
        """                                                                     
        Return all Maxima commands, which is useful for tab completion.         
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: t = maxima.trait_names(verbose=False, use_disk_cache=False)                         
            sage: 'gcd' in t                                                    
            True                                                                
            sage: len(t)    # random output                                     
            1840                                                                
        """
```

But overall, I'm happy that the updated ECL and Maxima packages at least build on sage.math, OS X in both 32- and 64-bit modes, Solaris on t2.math, and various Fedora/Red Hat platforms. Merged the package `ecl-9.8.4.spkg` in the standard packages repository.


---

Comment by AlexGhitza created at 2009-09-02 11:35:10

The failures of the type "gcd in t" are due to the fact that the new Maxima spkg has more commands than the old, but the old list is cached in the user's .sage directory.  So one solution is to remove that file, then test again (if the file is not found, it is generated automatically, this time with the correct contents).


---

Comment by mvngu created at 2009-09-04 06:37:33

See #6883 for a follow-up to this ticket.
