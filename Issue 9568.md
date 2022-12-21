# Issue 9568: Update IML to the newest upstream release, and improve spkg-install

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-21 22:17:33

Assignee: tbd

CC:  leif malb

As noted at #9309, the IML library is not current in Sage, and spkg-install could be improved somewhat. 

Dave


---

Comment by leif created at 2010-07-21 22:41:02

Changing type from defect to enhancement.


---

Comment by leif created at 2010-07-21 22:41:02

This is going to be a fun one, since the upstream source tree is not vanilla. Some files have been patched "in-place", others have been added, and (/but?) there's even a Mercurial repository in it (added by Sage)... :)

I'll take a closer look within the next days.

(I can't change the milestone to 4.6!)


---

Comment by drkirkby created at 2010-07-21 22:48:39

Replying to [comment:1 leif]:
> This is going to be a fun one, since the upstream source tree is not vanilla. Some files have been patched "in-place", others have been added, and (/but?) there's even a Mercurial repository in it (added by Sage)... :)
> 
> I'll take a closer look within the next days.
> 
> (I can't change the milestone to 4.6!)

We should also consider whether this package can be built in parallel, so replacing `make` with `$MAKE`. I just built the *current* version 1.0.1) ten times in parallel, using `$MAKE` rather than `make`. It reduced the build time from 13 s to 8 s on my Sun Ultra 27, so hardly a huge benefit.


---

Comment by leif created at 2010-07-21 23:01:17


```
Files iml-1.0.1-vanilla/Makefile.in and iml-1.0.1.p13/src/Makefile.in differ
Only in iml-1.0.1.p13/src/: cblas.h
Files iml-1.0.1-vanilla/configure and iml-1.0.1.p13/src/configure differ
Only in iml-1.0.1.p13/src/examples: build.linux
Only in iml-1.0.1.p13/src/examples: build.osx
Files iml-1.0.1-vanilla/examples/exam-nullspace.c and iml-1.0.1.p13/src/examples/exam-nullspace.c differ
Only in iml-1.0.1.p13/src/examples: exam-nullspace2.c
Only in iml-1.0.1.p13/src/: gsl_cblas.h
Only in iml-1.0.1.p13/src/repl: .libs
Only in iml-1.0.1.p13/src/repl: Makefile
Only in iml-1.0.1.p13/src/repl: librepl.la
Only in iml-1.0.1.p13/src/src: .hg
Files iml-1.0.1-vanilla/src/Makefile.am and iml-1.0.1.p13/src/src/Makefile.am differ
Files iml-1.0.1-vanilla/src/Makefile.in and iml-1.0.1.p13/src/src/Makefile.in differ
Files iml-1.0.1-vanilla/src/RNSop.c and iml-1.0.1.p13/src/src/RNSop.c differ
Files iml-1.0.1-vanilla/src/memalloc.c and iml-1.0.1.p13/src/src/memalloc.c differ
Files iml-1.0.1-vanilla/src/nonsysolve.c and iml-1.0.1.p13/src/src/nonsysolve.c differ
Files iml-1.0.1-vanilla/src/nullspace.c and iml-1.0.1.p13/src/src/nullspace.c differ
Files iml-1.0.1-vanilla/src/padiclift.c and iml-1.0.1.p13/src/src/padiclift.c differ
Files iml-1.0.1-vanilla/src/padiclift.h and iml-1.0.1.p13/src/src/padiclift.h differ
Only in iml-1.0.1.p13/src/src: tinyatlas.h
```

Perhaps not that hard, but do we want to keep the repository?

Also, the "new" 1.0.3 version (from 2008) brings new functionality, so additions/changes to the Sage library are likely.


---

Comment by leif created at 2010-07-21 23:44:23


```sh
sage-4.5$ grep -i -B5 -A1 iml devel/sage/module_list.py

    # TODO -- change to use BLAS at some point.
    Extension('sage.matrix.matrix_integer_dense',
              sources = ['sage/matrix/matrix_integer_dense.pyx'],
              # order matters for cygwin!!
              libraries = ['iml', 'gmp', 'm', 'pari', BLAS, BLAS2]),


```

From `spkg/standard/deps`:

```
all: $(BASE) \
     ...
     $(INST)/$(IML) \
     ...

$(INST)/$(IML): $(BASE) $(INST)/$(MPIR) $(INST)/$(GSL)
	$(INSTALL) "$(SAGE_SPKG) $(IML) 2>&1" "tee -a $(SAGE_LOGS)/$(IML).log"

...

# All components that are linked against extensions need to be listed here
$(INST)/$(SAGE): $(BASE) \
                 ...
                 $(INST)/$(IML) \
                 ...
```

(These are all occurrences of IML, i.e. only the Sage library depends on it.)


---

Comment by leif created at 2010-07-22 19:56:45

FYI/status:

```sh
...
Successfully installed iml-1.0.3.p0
Running the test suite.
Running the IML test suite...
...
PASS: test-smallentry
PASS: test-largeentry
==================
All 2 tests passed
==================
...
The IML test suite passed without errors.
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing iml-1.0.3.p0.spkg

real	4m30.801s
user	0m8.209s
sys	0m3.896s
leif`@`portland:~/Sage/sage-4.5$ ./sage -t devel/sage/sage/matrix/matrix_integer_dense.pyx
sage -t  "devel/sage/sage/matrix/matrix_integer_dense.pyx"  
	 [5.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.5 seconds
leif`@`portland:~/Sage/sage-4.5$ ./sage -t -long devel/sage/sage/matrix/matrix_integer_dense.pyx
sage -t -long "devel/sage/sage/matrix/matrix_integer_dense.pyx"
	 [18.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 18.6 seconds
```


I started with a vanilla 1.0.3, "cleaned up" `spkg-install` (dropping all patches and the Debian stuff) and just looked what happens...
(I configured with `--prefix=$SAGE_LOCAL --enable-shared` and added the appropriate (Sage) dirs to the preprocessor and linker search paths.)

For a Sage build from scratch, we need to change `deps` s.t. IML again(?) depends on ATLAS rather than GSL. Or is ATLAS still(?) considered optional on some systems?

Then I only added a patch for `src/src/nullspace.c`, which uses `mpz_init_ui()` instead of `mpz_init_set_ui()`.

:-)

(Still alpha, though. Looking for what else to carry over.)

-Leif


---

Comment by drkirkby created at 2010-07-23 11:45:40

I'm attaching a log of a failed build of 1.0.1, which may be due to parallel build issues. I think it would be wise to unset MAKE in this case - at least on the 1.0.1 code. Hard to know with the 1.0.3. 

## Build environment
 * [Sun Ultra 27](http://www.sun.com/desktop/workstation/ultra27/) 
 * [Intel W3580 Xeon 3.33 GHz](http://ark.intel.com/Product.aspx?id=39723). Quad core. 8 threads. 
 * 12 GB RAM
 * [128-bit ZFS](http://en.wikipedia.org/wiki/ZFS) file systems
 * 2 x 500 MB mirrored disks for the root file system
 * 2 x Hitachi HUA72202-A20N 2 TB disks mirrored disks for the user file system. 
 * OpenSolaris 2009.06 snv_134 X86
 * Sage 4.5.1
 * gcc 4.4.4 configured to use the Sun linker and GNU assembler
 * A parallel build with `SAGE_PARALLEL_SPKG_BUILD=yes` and `MAKE=make -j1000` 
 * Nothing was set in ulimit to limit processes, memory or similar. 
 

Dave


---

Comment by drkirkby created at 2010-07-23 11:46:39

Build log from a Sun Ultra 27 with an Intel Xeon processor - showing a strange failure.


---

Attachment

I just rebuilt version 1.0.1 in a loop 100 times. It failed to build once in that 100 times! (That's two failures in total I have observed of this). 

Dave


---

Comment by fbissey created at 2010-08-01 10:53:47

Replying to [comment:5 leif]:
> FYI/status:
> {{{
> #!sh
> ...
> Successfully installed iml-1.0.3.p0
> Running the test suite.
> Running the IML test suite...
> ...
> PASS: test-smallentry
> PASS: test-largeentry
> ==================
> All 2 tests passed
> ==================
> ...
> The IML test suite passed without errors.
> Now cleaning up tmp files.
> Making Sage/Python scripts relocatable...
> Making script relocatable
> Finished installing iml-1.0.3.p0.spkg
> 
> real	4m30.801s
> user	0m8.209s
> sys	0m3.896s
> leif`@`portland:~/Sage/sage-4.5$ ./sage -t devel/sage/sage/matrix/matrix_integer_dense.pyx
> sage -t  "devel/sage/sage/matrix/matrix_integer_dense.pyx"  
> 	 [5.5 s]
>  
> ----------------------------------------------------------------------
> All tests passed!
> Total time for all tests: 5.5 seconds
> leif`@`portland:~/Sage/sage-4.5$ ./sage -t -long devel/sage/sage/matrix/matrix_integer_dense.pyx
> sage -t -long "devel/sage/sage/matrix/matrix_integer_dense.pyx"
> 	 [18.6 s]
>  
> ----------------------------------------------------------------------
> All tests passed!
> Total time for all tests: 18.6 seconds
> }}}
> 
> I started with a vanilla 1.0.3, "cleaned up" `spkg-install` (dropping all patches and the Debian stuff) and just looked what happens...
> (I configured with `--prefix=$SAGE_LOCAL --enable-shared` and added the appropriate (Sage) dirs to the preprocessor and linker search paths.)
> 
> For a Sage build from scratch, we need to change `deps` s.t. IML again(?) depends on ATLAS rather than GSL. Or is ATLAS still(?) considered optional on some systems?
> 
> Then I only added a patch for `src/src/nullspace.c`, which uses `mpz_init_ui()` instead of `mpz_init_set_ui()`.
> 
> :-)
> 
> (Still alpha, though. Looking for what else to carry over.)
> 
Actually on sage-on-gentoo we have been using iml-1.0.3 for a while.
But on some setups we have been hit by a doc test failure which seem
to point to iml: 

```
sage -t -force_lib "devel/sage/sage/modular/modsym/space.py"
**********************************************************************
File "/opt/sage/devel/sage/sage/modular/modsym/space.py", line 1573:
    sage: af.intersection_number(ell)
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/opt/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/opt/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_45[8]>", line 1, in <module>
        af.intersection_number(ell)###line 1573:
    sage: af.intersection_number(ell)
      File "/usr/lib/python2.6/site-packages/sage/modular/modsym/space.py", line 1581, in intersection_number
        B = M.integral_structure()
      File "/usr/lib/python2.6/site-packages/sage/modular/modsym/space.py", line 1549, in integral_structure
        J = self.free_module().intersection(I)
      File "/usr/lib/python2.6/site-packages/sage/modules/free_module.py", line 3025, in intersection
        W = B.kernel()
      File "matrix2.pyx", line 2288, in sage.matrix.matrix2.Matrix.kernel (sage/matrix/matrix2.c:12775)
      File "matrix2.pyx", line 2586, in sage.matrix.matrix2.Matrix.left_kernel (sage/matrix/matrix2.c:14030)
      File "matrix_rational_dense.pyx", line 1255, in sage.matrix.matrix_rational_dense.Matrix_rational_dense.right_kernel (sage/matrix/matrix_rational_dense.c:12832)
    RuntimeError
```

And the line called in matrix_rational_dense.pyx is:

```
            K = A._rational_kernel_iml().change_ring(QQ)
```

The tests for matrix_rational_dense.pyx pass.
There is a backtrace as well here: [http://github.com/cschwan/sage-on-gentoo/issues#issue/3](http://github.com/cschwan/sage-on-gentoo/issues#issue/3)

Francois


---

Comment by fbissey created at 2010-10-15 09:09:55

Found out what the issue was in my previous comment. It is not related to iml per see.
There is a bug somewhere in ATLAS-3.9.23 which is the version we currently default on in Gentoo. Using another cblas with iml make the issue disappear completely.
So as far as we know iml-1.0.3 works fine with sage.


---

Comment by leif created at 2011-09-13 09:24:52

I'll close #748 as a duplicate.


---

Comment by kini created at 2012-05-28 04:36:12

Oops, looks like I duplicated this at #13027... Leif, do you have an SPKG I can look at?


---

Comment by drkirkby created at 2012-05-28 05:23:39

See my comment on #748. If this and #13027 are duplicates of #748, then this and #13027 should be closed - not the original ticket. 

Dave


---

Comment by kini created at 2012-05-28 19:01:12

OK.


---

Comment by kini created at 2012-05-28 19:01:12

Changing status from new to needs_review.


---

Comment by kini created at 2012-05-28 19:01:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:40:57

Resolution: duplicate


---

Comment by leif created at 2014-04-16 16:40:15

*Sign of life of IML upstream* on #14648 !!1!111!
