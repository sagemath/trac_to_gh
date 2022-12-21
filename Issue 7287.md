# Issue 7287: [needs review] Update Maxima spkg to build ECL library

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2009-10-25 07:05:24

Assignee: mabshoff

CC:  alexghitza mhansen

In order to use Maxima as a library via ECL, we need to have maxima as a lisp library rather than a stand-alone executable.

http://sage.math.washington.edu/home/nbruin/maxima-5.19.1.p1.spkg

implements this change. With this package properly installed, one can have the following session:

```
$ sage -ecl
ECL (Embeddable Common-Lisp) 9.8.4
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  
Top level.
> (require `maxima)

;;; Loading #P"/usr/local/sage/4.1.2/local/lib/ecl/maxima.fas"
("MAXIMA")
> (in-package :maxima)

#<"MAXIMA" package>
MAXIMA> #$integrate(cos(x),x)$

((%SIN SIMP) $X)
```

Attached is the patch between maxima-5.19.1.p0.spkg and maxima-5.19.1.p1.spkg


---

Comment by nbruin created at 2009-10-25 07:06:35

Patch for maxima spkg


---

Comment by nbruin created at 2009-10-25 07:09:11

Changing assignee from mabshoff to nbruin.


---

Attachment


---

Comment by nbruin created at 2009-10-25 07:09:26

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-02 15:54:48

After loading up #6781, I try to sage -f this package.    All seems well until the actual build process, which returns a typically enigmatic response 

```
Summary:
ECL enabled. Executable name: "ecl"
default lisp: ecl
wish executable name: "wish"
Now building maxima; this takes a few minutes
Since we're using OS X and there is a very weird
bug with buffered output while building maxima,
you will not be able to see the output of the build
as it occurs.  Don't worry, the build process did
not hang.
***********************************************************
Failed to make Maxima.
***********************************************************

real	1m8.617s
user	0m27.392s
sys	0m38.775s
sage: An error occurred while installing maxima-5.19.1.p1
```

which really, according to spkg-install, just means

```
check_error "Failed to make Maxima." 
```

Which could be any kind of error.  And oddly, 

```
sage -t  "devel/sage/sage/calculus/calculus.py"             
	 [18.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 18.4 seconds
```

So apparently nothing "bad" happens to the current Maxima executable, and perhaps this is completely unrelated to the spkg.  However, I get the same thing once I try to revert to the previous spkg, and in general even removing ecl.so doesn't fix this; Maxima stays working within Sage, but I cannot get Maxima to rebuild.  Could this have something to do with #6781?

So needless to say, I don't think the script gets to the library Maxima, and I can't load it:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from sage.libs.ecl import  *
sage: ecl_eval("(require 'asdf)")
;;; Loading #P"/Users/.../sage-4.2/local/lib/ecl/ASDF.fas"
;;; Loading #P"/Users/.../sage-4.2/local/lib/ecl/CMP.fas"
;;; Loading #P"/Users/.../sage-4.2/local/lib/ecl/sysfun.lsp"
<ECL: ("ASDF" "CMP")>
sage: ecl_eval("(require `maxima)")
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
/Users/.../sage-4.2/local/lib/python2.6/site-packages/sage/libs/ecl.so in ecl.ecl_eval (sage/libs/ecl/ecl.c:5718)()

/Users/.../sage-4.2/local/lib/python2.6/site-packages/sage/libs/ecl.so in ecl.ecl_eval (sage/libs/ecl/ecl.c:5672)()

/Users/.../sage-4.2/local/lib/python2.6/site-packages/sage/libs/ecl.so in ecl.ecl_safe_eval (sage/libs/ecl/ecl.c:2448)()

RuntimeError: ECL says: Module error: Don't know how to REQUIRE MAXIMA.
sage: ecl_eval('(load "%s")'%(SAGE_ROOT+"/local/lib/maxima/maxima.fasb"))
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/.../sage-4.2/local/lib/python2.6/site-packages/sage/libs/ecl.so in ecl.ecl_eval (sage/libs/ecl/ecl.c:5718)()

/Users/.../sage-4.2/local/lib/python2.6/site-packages/sage/libs/ecl.so in ecl.ecl_eval (sage/libs/ecl/ecl.c:5672)()

/Users/.../sage-4.2/local/lib/python2.6/site-packages/sage/libs/ecl.so in ecl.ecl_safe_eval (sage/libs/ecl/ecl.c:2448)()

RuntimeError: ECL says: Filesystem error with pathname #P"/Users/.../sage-4.2/local/lib/maxima/maxima.fasb".
Either
 1) the file does not exist, or
 2) we are not allow to access the file, or
 3) the pathname points to a broken symbolic link.
```


This is on OSX 10.5 Intel.


---

Comment by kcrisman created at 2009-11-02 15:54:48

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-11-02 16:07:41

Here is the console log, which seems helpful:

```
/Users/.../sage-4.2/spkg/build/maxima-5.19.1.p1/src/missing: line 52: automake-1.9: command not found
WARNING: `automake-1.9' is missing on your system.  You should only need it if
         you modified `Makefile.am', `acinclude.m4' or `configure.in'.
         You might want to install the `Automake' and `Perl' packages.
         Grab them from any GNU archive site.
An error occurred during initialization:
Filesystem error with pathname #P"/Users/.../sage-4.2/spkg/build/maxima-5.19.1.p1/src/src/binary-ecl/maxima-package.fas".
Either
 1) the file does not exist, or
 2) we are not allow to access the file, or
 3) the pathname points to a broken symbolic link..
make[1]: *** [binary-ecl/maxima] Error 1
make: *** [all-recursive] Error 1
```

Note that my machine has automake-1.10, for what it's worth, so in some sense that is not the problem - but why is it asking for a specific version? Or is it?


---

Comment by nbruin created at 2009-11-02 17:55:42

In the above transcript, the fact that (require 'maxima) fails indeed indicates that the install failed. The other attempts to load maxima fail because the library "maxima.fas" now gets installed in a different place.

If you take a look at the patch that was made to spkg-install,
you can see that the four lines added can't possibly lead to
maxima failing so badly. One guess I can make is that I packaged the spkg in the wrong way (I actually followed the instructions in spkg-dist!). The resulting spkg is quite a bit smaller than "p0" that Ghitza provided, so perhaps maxima automake files got deleted by that script?

To test this hypothesis:
 - Unpack the original maxima spkg (or install with -s)
 - apply the attached patch, or paste in the relevant lines into spkg-install
 - install again

If that works, then one should probably just repackage the spkg. Otherwise, I don't know what the problem is.


---

Comment by kcrisman created at 2009-11-02 19:00:13

Replying to [comment:5 nbruin]:
> In the above transcript, the fact that (require 'maxima) fails indeed indicates that the install failed. The other attempts to load maxima fail because the library "maxima.fas" now gets installed in a different place.
> 

I guess what I meant was that Maxima still works as an executable within Sage.

> If you take a look at the patch that was made to spkg-install,
> you can see that the four lines added can't possibly lead to
> maxima failing so badly. 

Yes, I noticed that.  Of course, Maxima itself isn't failing per se...
> One guess I can make is that I packaged the spkg in the wrong way (I actually followed the instructions in spkg-dist!). The resulting spkg is quite a bit smaller than "p0" that Ghitza provided, so perhaps maxima automake files got deleted by that script?
> 

That seems very likely; the size should be exactly the same, one would think.

> To test this hypothesis:
>  - Unpack the original maxima spkg (or install with -s)
>  - apply the attached patch, or paste in the relevant lines into spkg-install
>  - install again
> 
> If that works, then one should probably just repackage the spkg. Otherwise, I don't know what the problem is.

Unfortunately, although repackaging it did seem to solve the size issue, I still get the same error as above.  In particular, I get the following in a different log:

```
;;; Note: Creating tag: "_eclLn4HfWn8_QUH5U1z" for #P"binary-ecl/maxima-package.o"
;;; Internal error: Unable to find include directory
;      - Binary file binary-ecl/maxima-package.fas is old or does not exist. 
;        Compile (and load) source file /Users/.../sage-4.2/spkg/build/maxima-5.19.1.p1/src/src/maxima-package.lisp instead? y
;      - Should I bother you if this happens again? y
;      - Compiling source file
;        "/Users/.../sage-4.2/spkg/build/maxima-5.19.1.p1/src/src/maxima-package.lisp"
;;; Compiling /Users/.../sage-4.2/spkg/build/maxima-5.19.1.p1/src/src/maxima-package.lisp.
;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2
;;; End of Pass 1.
;;; Note: Creating tag: "_eclLn4HfWn8_1eX5U1z" for #P"binary-ecl/maxima-package.o"
;;; Internal error: Unable to find include directory
;      - Loading binary file "binary-ecl/maxima-package.fas"  
```

So it's not finding that even upon normal building.   Is the .fas file what we typically use, though?  My sense is that it's /local/lib/maxima/5.19.1/binary-ecl/maxima.  I don't know that the automake message is as important, as apparently there is a Maxima executable still there:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 3+3
6
sage: integrate(x^3)
1/4*x^4
```



---

Comment by kcrisman created at 2009-11-02 20:04:31

Weirdly, just putting the (bigger) spkg in to a clean build of 4.1.2 did as it was supposed to - right down to making the right .fas file, and it works!!!  Note that I did the spkg upgrade first, and only then added the ecl library access from #6781, just in case that makes a difference - I don't know why it would, but at any rate there were no weird complaints about makefiles etc. 

[Here](http://sage.math.washington.edu/home/kcrisman/maxima-5.19.1.p1.spkg) is the skpg.  I am going to try the same thing on a PPC machine next.  If someone else can do it on a couple Linux boxes, perhaps with different distros, that would be very helpful to getting this reviewed positively.


---

Comment by kcrisman created at 2009-11-02 20:04:31

Changing status from needs_work to needs_review.


---

Comment by nbruin created at 2009-11-02 20:39:19

Replying to [comment:7 kcrisman]:
> Weirdly, just putting the (bigger) spkg in to a clean build of 4.1.2 did as it was supposed to - right down to making the right .fas file, and it works!!!  Note that I did the spkg upgrade first, and only then added the ecl library access from #6781, just in case that makes a difference - I don't know why it would, but at any rate there were no weird complaints about makefiles etc. 

Ticket #6781 does not touch anything that can influence maxima's build.

I think the problem is in spkg-dist, which SPKG.txt instructs you to run prior to packaging the spkg:


```
for X in ['es', 'es.utf8', 'pt', 'pt.utf8', 'pt_BR', 'pt_BR.utf8']:
    cmd('rm -rf "src/doc/info/%s/"*'%X)
    open('src/doc/info/%s/Makefile.in'%X,'w').write('all:\n\tls\n\n')
```


This must delete some files that were "automake" generated. The build process of Maxima detects that, tries to run automake, bails on a wrong version number, and the spkg install fails. This problem had nothing to do with the patch, but everything with the instructions on how to build a new spkg. Anyone with experience with the maxima spkg interested in weighing in?


---

Comment by kcrisman created at 2009-11-02 21:05:15

You are right, the .in files are changed, which calls automake, etc.  Yuck.  So the "foreign-language" files add about 4 MB, interesting... maybe there is some way to get rid of these without doing something weird like that?  

This SPKG.txt is a little dated, anyway - it still has instructions for clisp!  Let's see what Alex has to say, if he's available.


---

Comment by kcrisman created at 2009-11-04 13:46:15

Works fine on PPC as well.

A final reviewer should test (a correct) spkg on a couple varieties of Linux, probably, but it shouldn't make too much difference (?).


---

Comment by mvngu created at 2009-12-03 01:46:01

An updated Maxima spkg is available at

http://sage.math.washington.edu/home/mhansen/maxima-5.19.1.p2.spkg

I have built Sage 4.3.alpha0 from scratch with that package. The compilation process went OK on the following platforms:

 * sage.math --- Ubuntu 8.04.3 LTS. All doctests pass, except the known failure with the Maxima interface.
 * rosemary.math --- Red Hat Enterprise Linux Server 5.4. All doctests pass, except the known failure with the Maxima interface.
 * bsd.math --- Mac OS X 10.6.2. Numerous doctest failures as expected as this platform is not yet completely supported.

After the build and doctests, you could run ECL and using Maxima as a library. Do either "./sage -ecl" or from a Sage command line session, do "!ecl":

```
[mvngu`@`sage sage-4.3.alpha0-maxima]$ ./sage -ecl
ECL (Embeddable Common-Lisp) 9.10.2
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.
Top level.
> (require 'maxima)

;;; Loading #P"/scratch/mvngu/sandbox/sage-4.3.alpha0-maxima/local/lib/ecl/maxima.fas"
("MAXIMA")
> #$integrate(cos(x), x)$

((MAXIMA::%SIN MAXIMA::SIMP) MAXIMA::$X)
> #$ratsimp((2*x + 3*x^3) / 5*x^2)$

((MAXIMA::MTIMES MAXIMA::SIMP) ((MAXIMA::RAT MAXIMA::SIMP) 1 5)
 ((MAXIMA::MPLUS MAXIMA::SIMP)
  ((MAXIMA::MTIMES MAXIMA::SIMP) 2
   ((MAXIMA::MEXPT MAXIMA::SIMP MAXIMA::RATSIMP) MAXIMA::$X 3))
  ((MAXIMA::MTIMES MAXIMA::SIMP) 3
   ((MAXIMA::MEXPT MAXIMA::SIMP MAXIMA::RATSIMP) MAXIMA::$X 5))))
> (quit)
```

So by this stage, Maxima can be built as a Lisp library. I'm doing more build/tests on other Linux boxes.


---

Comment by kcrisman created at 2009-12-03 02:49:56

Can I ask what the differences are with this spkg p2?  Is there a specific ticket this is related to?  In particular, if it is the latest CVS, this should fix a few other random tickets which have been waiting for a new Maxima version.


---

Comment by mhansen created at 2009-12-03 03:02:36

This .p2 package also has the changes from 7325 in it as well.


---

Comment by mvngu created at 2009-12-03 14:47:22

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-12-03 14:47:22

I have only been able to access the 32-bit Mandriva virtual machine on boxen.math. I can't ssh to most Linux virtual machines on boxen.math. On some boxes that I could ssh to (as wstein), the build process hangs for hours and seems to go nowhere. Building Sage 4.3.alpha0 on the 32-bit Mandriva virtual machine went OK. The following doctests failed:

```
sage -t -long "devel/sage/sage/interfaces/maxima.py"
sage -t -long "devel/sage/sage/interfaces/ecm.py"
sage -t -long "devel/sage/sage/tests/benchmark.py"
```

The Maxima failure is the following known failure:

```
sage -t -long "devel/sage-main/sage/interfaces/maxima.py"
**********************************************************************
File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/devel/sage-main/sage/interfaces/maxima.py", line 2172:
    sage: latex(maxima(derivative(ceil(x*y*d), d,x,x,y)))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_68[4]>", line 1, in <module>
        latex(maxima(derivative(ceil(x*y*d), d,x,x,y)))###line 2172:
    sage: latex(maxima(derivative(ceil(x*y*d), d,x,x,y)))
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/interfaces/expect.py", line 1033, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/interfaces/expect.py", line 1057, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "expression.pyx", line 429, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3324)
      File "sage_object.pyx", line 364, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3327)
      File "sage_object.pyx", line 453, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5036)
      File "expression.pyx", line 452, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3414)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 214, in __call__
        return self.arithmetic(ex, operator)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 553, in arithmetic
        args = ["(%s)"%self(op) for op in ex.operands()]
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 214, in __call__
        return self.arithmetic(ex, operator)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 553, in arithmetic
        args = ["(%s)"%self(op) for op in ex.operands()]
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 218, in __call__
        return self.derivative(ex, operator)
      File "/scratch/wstein/mvngu/sage-4.3.alpha0-maxima/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 541, in derivative
        raise NotImplementedError, "cannot convert expression to Maxima"
    NotImplementedError: cannot convert expression to Maxima
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_68
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_maxima.py
         [33.1 s]
exit code: 1024
```

As far as I'm concerned, the updated Maxima spkg looks good to me. One could make a Sage 4.3.alpha1 for testing on more platforms.


---

Comment by mhansen created at 2009-12-04 04:27:21

Merge maxima-5.19.1.p2.spkg


---

Comment by mhansen created at 2009-12-04 04:27:21

Resolution: fixed
