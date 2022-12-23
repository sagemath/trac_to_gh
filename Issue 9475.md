# Issue 9475: update M4RI to newest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/9475

Original creator: malb

Original creation time: 2010-07-11 16:12:22

Assignee: tbd

CC:  mariah

Keywords: M4RI, spkg-check

The new version improves elimination to some extend, comes with a cleaner API and has an option to suppress SSE instructions


---

Comment by malb created at 2010-07-11 16:14:02

Changing status from new to needs_review.


---

Comment by malb created at 2010-07-11 16:14:02

I've uploaded an SPKG to

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.spkg

This SPKG also takes care of #9381 (SAGE_FAT_BINARY not being respected) and the M4RI part of #9281 (spkg-check)


---

Comment by malb created at 2010-07-11 20:17:42

I've run the M4RI self test (not the Sage test suite) on the following machines:

 * x86_64 Linux (Xeon, sage.math and eno);

 * x86 OSX (Xeon, bsd); 

 * ia64 Linux (iras); 

 * UltraSPARC T2 Solaris using GCC (t2.math.washington.edu) 

 * x86 Linux (VirtualBox);


---

Comment by mariah created at 2010-07-13 15:53:13

1. SPKG.txt under "Releases" says latest 
release is libm4ri-20100107, do you mean
libm4ri-20100701?

2. Since spkg-check exists, in spkg-install 
the commented out lines:


```
# $MAKE check
# if [ $? -ne 0 ]; then
#     echo "libm4ri testsuite failed, please report upstream!"
#     exit 1
# fi
```


can be removed.

3. In spkg-install, if SAGE_FAT_BINARY is yes, then
sse2 is disabled.  What about sse3 as was the reported
problem in [#9381](http://trac.sagemath.org/sage_trac/ticket/9381)

4. This version of libm4ri does not appear under the
downloads on the [m4ri](http://m4ri.sagemath.org) web site,
thus no way to tell if the source in the spkg corresponds
to the source under the claimed version.


---

Comment by mariah created at 2010-07-13 15:53:13

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-07-13 18:22:28

Replying to [comment:3 mariah]:

> 1. SPKG.txt under "Releases" says latest  release is libm4ri-20100107, do you mean libm4ri-20100701?

Fixed.

> 2. Since spkg-check exists, in spkg-install  the commented out lines: ` # $MAKE check # if [ $? -ne 0 ]; then #     echo "libm4ri testsuite failed, please report upstream!" #     exit 1 # fi ` can be removed.

Fixed.

> 3. In spkg-install, if SAGE_FAT_BINARY is yes, then sse2 is disabled.  What about sse3 as was the reported problem in [#9381](http://trac.sagemath.org/sage_trac/ticket/9381)

We never use SSE3, but yeah all checks for SSEx instructions are suppressed in that case.

> 4. This version of libm4ri does not appear under the downloads on the [m4ri](http://m4ri.sagemath.org) web site, thus no way to tell if the source in the spkg corresponds to the source under the claimed version.

This is because I am upstream and wanted to wait for portability issues before putting the release on the website. I'm putting it online now, if that makes your life easier.


---

Comment by malb created at 2010-07-13 18:41:20

See 

http://m4ri.sagemath.org

and

http://bitbucket.org/malb/m4ri/wiki/M4RI-20100701  

for the new upstream release.


---

Comment by malb created at 2010-07-13 18:41:20

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-07-14 13:18:40

The changes to `SPKG.txt`, `spkg-install` and `spkg-check` are not checked in.


---

Comment by leif created at 2010-07-14 14:00:54

`SPKG.txt`:
 * _Author_ should be _Author*s*_
 * Is the given e-mail address still up-to-date?
 * I'd substitute _"function names match what the function is doing now"_
   by _"function names *now* match ... is doing"_
 * s/supress/su*p*press/
 * s/SSE2 instruction/SSE2 instruction*s*/

`spkg-install:`
 * Old typo, I guess: s/CLFAGS/CFLAGS/ twice
 * The choice of the variable name `SSE2_SUPPORT` isn't that nice; I'd rather call it `DISABLE_SSE2`, but never mind.

`spkg-check:`
 * Uses `make` rather than `$MAKE` (in contrast to `spkg-install`), but shouldn't be a problem.


---

Comment by leif created at 2010-07-14 15:49:57

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-07-14 15:49:57

I'd suggest adding the (standard) section _Special Update/Build Instructions_ to `SPKG.txt`, with the following:
  * Remove upstream Mercurial repository (directory `src/.hg`, file `src/.hgtags`)
  * Remove directory `src/autom4te.cache`, file `src/m4ri.vcproj`

I've built a p1 spkg with the above mentioned files removed: 392KB vs. 1.2MB

If there are no dependencies on Sage packages (which is the case here), we don't need to add `$SAGE_LOCAL/include` to the preprocessor search path in `spkg-install` (`CFLAGS` and `CPPFLAGS`).

Perhaps touch `src/configure`, because it has the same time stamp as `configure.*`.

Upstream notes:
  * There is no target `clean`.
  * `src/NEWS` and `src/ChangeLog` are *empty* files. ;-)

Tests in progress,

Leif


---

Comment by leif created at 2010-07-14 17:50:56

* Ubuntu 9.04 x86 (P4 Prescott, gcc 4.3.3) Sage 4.5.rc0 (with ECL 10.2.1.p1):

   ptestlong: All tests passed.

 * Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3) Sage 4.5.rc0:

   ptestlong: All tests passed.
   (with my stripped-down M4RI spkg, see above)

I've only installed the new package (dated July 13th) and applied the patch, i.e. did not build Sage from scratch, and haven't (yet) run the testsuite.


---

Comment by leif created at 2010-07-14 18:53:19

Shame on me I missed that one:

```sh
./spkg-install: line 47: [x: command not found
```


```sh
if ["x$SAGE_FAT_BINARY" = "xyes"]; then
    SSE2_SUPPORT="--disable-sse2"
else
    SSE2_SUPPORT=""
fi
```

should be

```sh
if [ "x$SAGE_FAT_BINARY" = "xyes" ]; then
    ...
```

Note that `[` is actually a _command_ (namely an alias for or link to `test`, depending on the shell), and `]` is its last parameter.

----

On both of the above systems, the testsuite passed without errors.

(I reinstalled the package(s) with `SAGE_CHECK="yes"`.)


---

Comment by leif created at 2010-07-14 19:35:43

Just let me know if I should provide (a) reviewer patch(es) to the spkg (after a commit to the changes not yet checked in); I cannot upload an updated spkg to sage.math though.

Leif


---

Comment by malb created at 2010-07-14 20:39:25

Replying to [comment:9 leif]:

> * Remove upstream Mercurial repository (directory `src/.hg`, file `src/.hgtags`)
> * Remove directory `src/autom4te.cache`, file `src/m4ri.vcproj`
> I've built a p1 spkg with the above mentioned files removed: 392KB vs. 1.2MB

It's strange that there was an autom4te.cache, since I rm it in my release script. I'm okay with these changes.


---

Comment by malb created at 2010-07-14 20:41:14

Leif,

I'd appreciate if you could update SPKG according to your suggestions, I'm okay with them all. If you upload the SPKG somewhere or send it my way I can upload it to sage.math.


---

Comment by leif created at 2010-07-14 21:00:56

Replying to [comment:14 malb]:
> I'd appreciate if you could update SPKG according to your suggestions, I'm okay with them all. If you upload the SPKG somewhere or send it my way I can upload it to sage.math. 

Ok, I'll create a cumulative spkg patch and a "stripped-down" p1 package in a few hours and then mail you both.

(I assume your .ac.uk e-mail address in SPKG.txt is still appropriate as upstream contact.)
  

Currently running stress-test builds of 4.5.rc1... ;-)

Leif


---

Comment by malb created at 2010-07-14 21:22:01

Yes, that's still current, however martinralbrecht`@` googleblablabla might be current for a longer time.

Thanks!


---

Attachment

You have to commit Martin's changes ("p0") first to apply this.


---

Comment by leif created at 2010-07-16 02:33:07

Patch for p1 Sage package is up. Remember to commit Martin's changes (of July 13th) first before you apply this patch. (This patch does _not_ remove the unnecessary files in `src/` since they are not under _our_ version control; they are of course deleted from the p1 spkg.)

(Link to) *New libm4ri-20100701.p1.spkg is on the way.*

Tested with both 4.5.rc0 and rc1 (Ubuntu 9.04 x86_64).

Sorry for the delay.

-Leif


---

Comment by leif created at 2010-07-16 02:33:07

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-07-16 09:03:23

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-07-16 09:03:23

I uploaded Leif's SPKG to 

 http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg

and I give it a positive review.


---

Comment by rlm created at 2010-07-18 20:05:49

With a fresh build, sage doesn't start:

```
Traceback (most recent call last):
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval",
line 4, in <module>
   from sage.all import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py",
line 73, in <module>
   from sage.matrix.all     import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py",
line 1, in <module>
   from matrix_space import MatrixSpace, is_MatrixSpace
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py",
line 40, in <module>
   import matrix_mod2_dense
ImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:
undefined symbol: mzd_lqup
Sage failed to startup.
```



---

Comment by rlm created at 2010-07-18 20:05:49

Changing status from positive_review to needs_work.


---

Comment by leif created at 2010-07-18 20:14:08

Replying to [comment:20 rlm]:
> With a fresh build, sage doesn't start:

```
Traceback (most recent call last):
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval",line 4, in <module>
   from sage.all import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py", line 73, in <module>
   from sage.matrix.all     import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py", line 1, in <module>
   from matrix_space import MatrixSpace, is_MatrixSpace
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 40, in <module>
   import matrix_mod2_dense
ImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:
undefined symbol: mzd_lqup
Sage failed to startup.
```


Looks as if you haven't applied the Sage library patch (or didn't do `sage -b` after that).


---

Comment by rlm created at 2010-07-18 20:16:02

Replying to [comment:21 leif]:
> 
> Looks as if you haven't applied the Sage library patch (or didn't do `sage -b` after that).
> 

I've been pretty bad about this lately... Sorry guys.


---

Comment by rlm created at 2010-07-18 20:16:02

Changing status from needs_work to positive_review.


---

Comment by rlm created at 2010-07-18 22:08:38


```
sage -t -long "devel/sage-main/sage/crypto/mq/mpolynomialsystem.py"

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by rlm created at 2010-07-18 22:08:38

Changing status from positive_review to needs_work.


---

Comment by malb created at 2010-07-18 22:19:49

I tried to reproduce your segmentation fault, but I can't.


```
malb@sage:~/scratch_sage/sage-4.4$ ./sage -t -long devel/sage-main/sage/crypto/mq/mpolynomialsystem.py
sage -t -long "devel/sage-main/sage/crypto/mq/mpolynomialsystem.py"
         [16.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 16.8 seconds
malb@sage:~/scratch_sage/sage-4.4$ cd devel/sage
malb@sage:~/scratch_sage/sage-4.4/devel/sage$ hg qap
m4ri_new_version.patch
singular-3-1-1-4.patch

```



---

Comment by leif created at 2010-07-18 22:33:49

Replying to [comment:23 rlm]:

```
sage -t -long "devel/sage-main/sage/crypto/mq/mpolynomialsystem.py"

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
...
```


Machine, OS, platform? Parallel test? Whole library or just that single file?


---

Comment by rlm created at 2010-07-19 07:05:51

On geom.math, with a parallel build, in parallel and serial testing.


---

Comment by rlm created at 2010-07-19 08:25:49


```
Trying:
    C = mq.MPolynomialSystem(r2).connected_components(); C###line 76:_sage_    >>> C = mq.MPolynomialSystem(r2).connecte
d_components(); C
Expecting:
    [Polynomial System with 16 Polynomials in 16 Variables,
     Polynomial System with 16 Polynomials in 16 Variables]
ok
Trying:
    C[Integer(0)].groebner_basis()###line 80:_sage_    >>> C[0].groebner_basis()
Expecting:
    [x111*x110 + w113*x110 + w113*x112 + w113*x113 + w113*w111 + w113*w112 + x111 + x113 + w110 + w111 + w112,
... (more output)
BOOM
```



---

Comment by malb created at 2010-07-19 16:25:22

I executed these steps

 * I got a clean 4.5
 * installed r-2.10.1.p3.spkg #9396
 * installed libm4ri-20100701.p1.spkg #9475 
 * applied m4ri_new_version.patch to devel/sage-main repo #9475 
 * merged trac_9507.patch to local/bin repo #9507 
 * replaced spkg/install with "install.2" from the ticket #9528
 * ./sage -sdist 4.5.1
 * then extracted the tarball...
 * export SAGE_PARALLEL_SPKG_BUILD=yes
 * export MAKE=make -j20
 * make
 * since somehow libm4ri wasn't updated afterwards, I reinstalled libm4ri-20100701.p1.spkg

*Result:*


```
malb@geom:~/scratch_sage/SIGSEGV/sage-4.5.1$ ./sage -t -long devel/sage/sage/crypto/mq/mpolynomialsystem.py 
sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
         [17.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.1 seconds

```



---

Comment by rlm created at 2010-07-19 16:33:45

Well then, maybe it was a cosmic ray...


---

Comment by rlm created at 2010-07-19 16:33:45

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-08-07 02:46:27

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-07 02:46:27

Do I need to apply 

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg

_and_ [attachment:m4ri_new_version.patch]?  Can someone put the ticket number in the commit string?


---

Comment by leif created at 2010-08-07 07:16:34

## Note to the release managers

*Apply only [m4ri_new_version.v2.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9475/m4ri_new_version.v2.patch) to the Sage library* when merging the [new M4RI spkg](http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg); that patch is identical to `m4ri_new_version.patch` except for the commit message. (I don't have the power to replace Martin's attachment.)


---

Comment by leif created at 2010-08-07 07:16:34

Changing status from needs_work to positive_review.


---

Comment by leif created at 2010-08-07 07:24:16

Replying to [comment:30 mpatel]:
> Can someone put the ticket number in the commit string?

Done, but now we have yet another attachment since I couldn't replace Martin's.

(I would have thought his patch's comment was sufficient to conclude that the patch has to be applied to the Sage library repository... ;-) )


---

Comment by mpatel created at 2010-08-09 23:00:04

Note: I haven't merged this ticket into 4.5.3.alpha0, because I noticed some segfaults that appear to stem from the new package and/or patch, when I doctested various trial alpha0s on sage.math.  At the moment, it seems best to put out a 4.5.3.alpha0 with passing doctests and base on this any necessary efforts to merge the new M4RI into alpha1.


---

Comment by mpatel created at 2010-08-10 04:18:41

_Of course_, all long tests now pass (well, there are no reproducible failures) on sage.math with 4.5.3.alpha0 + #9475, so it seems no new efforts are necessary.  I'm checking bsd, redhawk, and t2 now.


---

Comment by mpatel created at 2010-08-10 05:47:06

Replying to [comment:35 mpatel]:
> _Of course_, all long tests now pass (well, there are no reproducible failures) on sage.math with 4.5.3.alpha0 + #9475, so it seems no new efforts are necessary.  I'm checking bsd, redhawk, and t2 now.
The long doctests also pass on bsd, redhawk, and t2.


---

Comment by malb created at 2010-08-10 14:02:05

There definitely is a bug in this new M4RI, I do get SIGSEGVs on my new laptop. I'll investigate.


---

Comment by malb created at 2010-08-10 14:02:05

Changing status from positive_review to needs_work.


---

Comment by malb created at 2010-08-10 14:42:54


```
        while(it!=end){
            Exponent e=*it; 
                from_term_map_type::const_iterator from_it=eliminated2row_number.find(e);
                assert(terms_as_exp_step1[row_start[from_it->second]]==e);
                assert(from_it!=eliminated2row_number.end());
 ===>               int index=from_it->second;//...translate e->line number;
                mzd_write_bit(mat_step2_factor,i,index,1);
            it++;
        }

```

This is where pbori.pyx crashes for me. I installed a new GCC today, so maybe that's to blame?


---

Comment by malb created at 2010-08-10 15:01:33

Changing status from needs_work to positive_review.


---

Comment by malb created at 2010-08-10 15:01:33

I think I got it: The[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) SPKG in 4.5.2 ships its own M4RI (and Boost) which conflicts with this new M4RI SPKG, thus since Leif removed this redundant copy of M4RI in the PolyBoRi, it works in 4.5.3.alpha0 but not before.


---

Comment by leif created at 2010-08-10 15:14:53

Replying to [comment:39 malb]:
> I think I got it: The PolyBoRi SPKG in 4.5.2 ships its own M4RI (and Boost) which conflicts with this new M4RI SPKG, thus since Leif removed this redundant copy of M4RI in the PolyBoRi, it works in 4.5.3.alpha0 but not before.

LOL! (Sometimes little clean-ups make more sense than expected...)


---

Comment by malb created at 2010-08-11 15:50:05

It seems this ticket is incompatible with#9717. On my laptop I always get SIGSEGVs in pbori.pyx


---

Comment by malb created at 2010-08-11 17:58:07

I tracked down the issue. The cause is some assumptions in[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) about M4RI which are not met anymore. This ticket can go in I say


---

Comment by malb created at 2010-08-11 18:04:57

Actually, this ticket can only go in if a fix for[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) is also accepted, cf. #9717


---

Comment by jason created at 2010-08-12 04:34:15

Minor thing: the documentation for rank still says:

On average 'lqup' should be faster than 'm4ri' and hence it is
        the default choice.


---

Comment by malb created at 2010-08-12 18:48:54

#9717 has an updated, fixed[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) SPKG


---

Comment by malb created at 2010-08-12 18:51:34

The updated patch only replaces the mention of LQUP with PLS


---

Comment by mpatel created at 2010-08-12 20:15:41

Should someone review the latest changes?


---

Comment by malb created at 2010-08-12 20:48:50

The only change in the new version compared to the previous version of  m4ri_new_version.v2.patch is that one mention of LQUP was replaced by PLS in a docstring. That's all, this is why I didn't reset the status.


---

Comment by leif created at 2010-08-13 03:05:08

Replying to [comment:48 malb]:
> The only change in the new version compared to the previous version of  m4ri_new_version.v2.patch is that one mention of LQUP was replaced by PLS in a docstring. That's all, this is why I didn't reset the status.

Not 100%:

```patch
--- m4ri_new_version.v2.patch.orig	2010-08-07 09:00:21.000000000 +0200
+++ m4ri_new_version.v2.patch	2010-08-12 20:50:56.000000000 +0200
@@ -1,14 +1,14 @@
 # HG changeset patch
 # User Martin Albrecht <malb@informatik.uni-bremen.de>
 # Date 1277764034 -3600
-# Node ID 3365789479e6d70cb1930b2e97c7874cbd3310db
-# Parent  ba36200d8a2f844179785580245fd95aa6401a51
+# Node ID 3b116dd35a84e0b6bd8ea12a732b8fa1fbda796f
+# Parent  0bb69a98789215c64a81c4602f46a50c0aeca5f0
 #9475 Adapts Sage library interface to new M4RI API (libm4ri-20100701)
 
-diff -r ba36200d8a2f -r 3365789479e6 module_list.py
---- a/module_list.py	Fri Jun 25 10:05:59 2010 +0100
+diff -r 0bb69a987892 -r 3b116dd35a84 module_list.py
+--- a/module_list.py	Tue Aug 10 13:46:10 2010 +0100
 +++ b/module_list.py	Mon Jun 28 23:27:14 2010 +0100
-@@ -783,7 +783,7 @@
+@@ -807,7 +807,7 @@
      Extension('sage.matrix.matrix_mod2_dense',
                sources = ['sage/matrix/matrix_mod2_dense.pyx'],
                libraries = ['gmp','m4ri', 'gd', 'png12', 'z'],
@@ -17,7 +17,7 @@
  
      Extension('sage.matrix.matrix_modn_dense',
                sources = ['sage/matrix/matrix_modn_dense.pyx'],
-@@ -971,7 +971,7 @@
+@@ -995,7 +995,7 @@
      Extension('sage.modules.vector_mod2_dense',
                sources = ['sage/modules/vector_mod2_dense.pyx'],
                libraries = ['gmp','m4ri', 'png12', 'gd'],
@@ -26,8 +26,8 @@
      
      Extension('sage.modules.vector_rational_dense',
                sources = ['sage/modules/vector_rational_dense.pyx'],
-diff -r ba36200d8a2f -r 3365789479e6 sage/libs/m4ri.pxd
---- a/sage/libs/m4ri.pxd	Fri Jun 25 10:05:59 2010 +0100
+diff -r 0bb69a987892 -r 3b116dd35a84 sage/libs/m4ri.pxd
+--- a/sage/libs/m4ri.pxd	Tue Aug 10 13:46:10 2010 +0100
 +++ b/sage/libs/m4ri.pxd	Mon Jun 28 23:27:14 2010 +0100
 @@ -141,6 +141,9 @@
      # reduced row echelon form from upper triangular form
@@ -60,8 +60,8 @@
  
      # reduced row echelon form using PLUQ factorization
      cdef long mzd_echelonize_pluq(mzd_t *A, int full)
-diff -r ba36200d8a2f -r 3365789479e6 sage/matrix/matrix_mod2_dense.pyx
---- a/sage/matrix/matrix_mod2_dense.pyx	Fri Jun 25 10:05:59 2010 +0100
+diff -r 0bb69a987892 -r 3b116dd35a84 sage/matrix/matrix_mod2_dense.pyx
+--- a/sage/matrix/matrix_mod2_dense.pyx	Tue Aug 10 13:46:10 2010 +0100
 +++ b/sage/matrix/matrix_mod2_dense.pyx	Mon Jun 28 23:27:14 2010 +0100
 @@ -1010,15 +1010,16 @@
      #    * Matrix windows -- only if you need strassen for that base
@@ -116,7 +116,28 @@
                  k = 0
  
              _sig_on
-@@ -1681,7 +1691,7 @@
+@@ -1106,6 +1116,20 @@
+             self.cache('rank', r)
+             self.cache('pivots', self._pivots())
+ 
++        elif algorithm == 'top':
++            
++            self.check_mutability()
++            self.clear_cache()        
++
++            _sig_on
++            mzd_top_echelonize_m4ri(self._entries, 0)
++            r = 0
++            _sig_off
++            
++            self.cache('in_echelon_form',True)
++            self.cache('rank', r)
++            self.cache('pivots', self._pivots())
++
+         elif algorithm == 'linbox':
+ 
+             #self._echelonize_linbox()
+@@ -1681,7 +1705,7 @@
              sage: float(d)
              0.63184899999999999
              sage: A.density(approx=True)
@@ -125,7 +146,7 @@
              sage: float(len(A.nonzero_positions())/1000^2)
              0.63184899999999999
          """
-@@ -1691,7 +1701,7 @@
+@@ -1691,18 +1715,18 @@
          else:
              return matrix_dense.Matrix_dense.density(self)
  
@@ -134,7 +155,11 @@
          """
          Return the rank of this matrix.
  
-@@ -1702,7 +1712,7 @@
+-        On average 'lqup' should be faster than 'm4ri' and hence it is
++        On average 'pls' should be faster than 'm4ri' and hence it is
+         the default choice. However, for small - i.e. quite few
+         thousand rows & columns - and sparse matrices 'm4ri' might be
+         a better choice.
  
          INPUT:
  
@@ -143,7 +168,7 @@
  
          EXAMPLE::
  
-@@ -1722,10 +1732,10 @@
+@@ -1722,10 +1746,10 @@
          cdef mzd_t *A = mzd_copy(NULL, self._entries)
          cdef mzp_t *P, *Q
  
@@ -156,7 +181,7 @@
              mzp_free(P)
              mzp_free(Q)
          elif algorithm == 'm4ri':
-@@ -2060,9 +2070,9 @@
+@@ -2060,9 +2084,9 @@
      mzp_free(q)
      return B,P,Q
  
@@ -168,7 +193,7 @@
  
      INPUT:
          A -- matrix
-@@ -2074,14 +2084,14 @@
+@@ -2074,14 +2098,14 @@
  
      EXAMPLE::
  
@@ -185,7 +210,7 @@
          sage: LU
          [1 0 0 1]
          [1 1 0 0]
-@@ -2095,7 +2105,7 @@
+@@ -2095,7 +2119,7 @@
          [0, 1, 2, 3]
  
          sage: A = random_matrix(GF(2),1000,1000)
@@ -194,7 +219,7 @@
          True
      """
      cdef Matrix_mod2_dense B = A.__copy__()
-@@ -2104,15 +2114,15 @@
+@@ -2104,15 +2128,15 @@
  
      if algorithm == 'standard':
          _sig_on
```



---

Comment by malb created at 2010-08-13 08:44:06

Argh, I'm an idiot! I'll update the patch, the 'top' stuff must be removed


---

Comment by malb created at 2010-08-13 08:44:21

Sage library patch - needed to comply with new M4RI API (libm4ri-20100701). (Contains ticket number; apply only this one.)


---

Attachment

Replying to [comment:50 malb]:
> Argh, I'm an idiot! I'll update the patch, the 'top' stuff must be removed

Nevertheless, passed all long tests with Sage 4.5.3.alpha0 and PolyBoRi 0.6.4.p4 from #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

The newly uploaded patch contains only the desired changes.


---

Comment by mpatel created at 2010-08-15 08:03:14

Resolution: fixed
