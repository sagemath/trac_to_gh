# Issue 8357: Doctesting ell_rational_field.py leaves a file PRIMES in the current directory

Issue created by migration from https://trac.sagemath.org/ticket/8357

Original creator: mpatel

Original creation time: 2010-02-25 06:05:03

Assignee: cremona

From [John Palmieri](http://groups.google.com/group/sage-devel/browse_thread/thread/976cf8ecb4896e7c):

```
When I run doctests on the file ell_rational_field.py, I end up with a
small file called PRIMES in the current directory. This shouldn't
happen: running doctests shouldn't produce files in a non-temporary
directory.  However, I can't figure out how this file gets there.  In
particular, if I delete the following doctests from the rank method,
then the file is not produced:

{{{
diff -r 23241bd151e3 sage/schemes/elliptic_curves/
ell_rational_field.py
--- a/sage/schemes/elliptic_curves/ell_rational_field.py        Thu
Feb 18 14:25:25 2010 -0800
+++ b/sage/schemes/elliptic_curves/ell_rational_field.py        Wed
Feb 24 20:37:09 2010 -0800
@@ -1679,14 +1679,6 @@
             sage: E.minimal_model().rank()
             1

-        A large example where mwrank doesn't determine the result
with certainty::
-
-            sage: EllipticCurve([1,0,0,0,37455]).rank(proof=False)
-            0
-            sage: EllipticCurve([1,0,0,0,37455]).rank(proof=True)
-            Traceback (most recent call last):
-            ...
-            RuntimeError: Rank not provably correct.
         """
         if proof is None:
             from sage.structure.proof.proof import get_flag

}}}

If I run these by hand from the command line, though, I don't see the
file PRIMES anywhere.  Can someone familiar with the elliptic curves
code open a ticket, chase this down, and fix it?
```


This is a follow-up to #7575.  Please see [comment:ticket:7575:24 comment 24+] for some progress.


---

Comment by cremona created at 2010-02-25 09:22:32

The quickest quick fix would be just to comment out line 372 in src/procs/marith.cc (in eclib).

Anything else requires thought and testing, which I don't have time for i nthe next several days.


---

Comment by mpatel created at 2010-02-28 00:24:18

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-28 06:23:01

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-02-28 06:23:01

There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).


---

Attachment

Tweak `MAKEFILE`s for parallel builds.  eclib src repo.


---

Comment by mpatel created at 2010-02-28 13:35:27

Replying to [comment:3 mpatel]:

> There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).

I think the problem is that make sometimes attempts to build a target in `progs` before it's done building a requisite shared library, e.g., `install_so`.  I've updated the "makefiles" patch and spkg with a fix that I'm testing now.


---

Comment by cremona created at 2010-02-28 13:45:11

Replying to [comment:4 mpatel]:
> Replying to [comment:3 mpatel]:
> 
> > There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).
> 
> I think the problem is that make sometimes attempts to build a target in `progs` before it's done building a requisite shared library, e.g., `install_so`.  I've updated the "makefiles" patch and spkg with a fix that I'm testing now.

That sounds likely.  We (I) should probably tidy this up;  there are several useful executables which are built, but the only one actually used by and accessible from Sage after the build is mwrank.  So i should change the targets so that the other progs are only built when doing a make check.


---

Comment by mpatel created at 2010-02-28 14:05:41

Replying to [comment:4 mpatel]:
> [...] I've updated the "makefiles" patch and spkg with a fix that I'm testing now.
It seems to work and it survives a stress test on sage.math, e.g.,

```sh
export MAKE="make -j20"  # And NTL_PREFIX, etc.
make veryclean && make && make so && make veryclean && make && make so && [lots of reps] && ls
```



---

Comment by cremona created at 2010-02-28 20:11:08

mpatel:  if possible could you make he following additional edits to src/procs/Makefile (in eclib...p10):

```
diff -r 809e34b4c146 procs/Makefile
--- a/procs/Makefile	Sat Feb 27 15:42:31 2010 -0800
+++ b/procs/Makefile	Sun Feb 28 20:08:44 2010 +0000
@@ -105,7 +105,7 @@
 	gzip procs.tar
 
 check: $(TESTS)
-	rm -f PRIMES t
+	rm -f PRIMES t 1
 	./vectest1 < vectest.in >  t && diff t vectest.out
 	./vectest2 < vectest.in >  t && diff t vectest.out
 	./mattest1 < mattest.in >  t && diff t mattest.out
@@ -128,7 +128,7 @@
 	./rcubic < rcubic.in > t && diff t rcubic.out
 	./lcubic < lcubic.in > t && diff t lcubic.out
 	./tp2points < tp2points.in > t && diff t tp2points.out
-	rm -f PRIMES t
+	rm -f PRIMES t 1
```

It's another temp file which gets left behind, this time after "make check".

If that's too much hassle I'll do it next time I make changes to the eclib spkg, but it would be convenient to do it now.


---

Comment by mpatel created at 2010-03-01 00:17:49

Diff of `spkg-install`, `SPKG.txt`.  eclib spkg repo.


---

Attachment

Don't write `PRIMES`. Delete `1` after check.  eclib src repo


---

Comment by mpatel created at 2010-03-01 00:51:07

Replying to [comment:7 cremona]:
> If that's too much hassle I'll do it next time I make changes to the eclib spkg, but it would be convenient to do it now.
Done!  I've updated spkg and two patches.


---

Comment by mpatel created at 2010-03-01 00:51:07

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-03-01 04:41:55

I noticed a different problem with `make check` on t2:

```
make[3]: Entering directory `/scratch/mpatel/sage-4.3.0.1/spkg/build/eclib-20080310.p10/src/g0n'
rm -f PRIMES t
./modtest < modtest.in > t 2>/dev/null && diff t modtest.out 
./homtest < homtest.in > t && diff t homtest.out
./hecketest < hecketest.in > t 2>/dev/null && diff t hecketest.out 
./mhcount < mhcount.in > t && diff t  mhcount.out
rm -rf tmp_nf_dir
mkdir tmp_nf_dir
export NF_DIR=tmp_nf_dir && ./tmanin < tmanin.in > t 2>/dev/null && diff t tmanin.out
/bin/sh: NF_DIR=tmp_nf_dir: is not an identifier
make[3]: *** [check] Error 1
make[3]: Leaving directory `/scratch/mpatel/sage-4.3.0.1/spkg/build/eclib-20080310.p10/src/g0n'
```

I think we can fix this with, e.g.,

```sh
env NF_DIR=tmp_nf_dir ./tmanin < tmanin.in > t 2>/dev/null && diff t tmanin.out
```



---

Comment by cremona created at 2010-03-01 14:27:32

I tested the current version of the spkg.  (This does nto have the suggested changes to the handling of NF_DIR).  All was well.

I did not make new changes (for the NF_DIR thing) since I thought that would be too confusing.  But I'll be happy to check the next version of p10 in due course.


---

Comment by cremona created at 2010-03-01 19:52:10

There is a  simpler solution to the problem with "export NF_DIR".  The code uses a default directory name for this, namely "newforms",  which can be over-ridden by the use of the environment variable NF_DIR.  For this test therefore we can replace the 2 lines "rm -rf tmp_nf_dir" by "rm -rf newforms" (strictly only the second one is needed) and remove all the starts of lines of the form "export NF_DIR=tmp_nf_dir && ".
(This is in src/g0n/Makefile).

Here's why I did not do this in the first place: by own private copy of this code has a newforms directory which contains 3.4G of data which took many many processor-years to compute.  I do not want a simple "make check" to delete that so I put in this temporary (and non-default) tmp_nf_dir thing instead.  But for the Sage distribution that is not needed.

I can attach a replacement Makefile here if that would be convenient, for yet another version of p10.


---

Comment by mpatel created at 2010-03-01 21:11:52

Sure, that sounds good.


---

Comment by cremona created at 2010-03-01 22:03:21

replacement src/g0n/Makefile


---

Attachment

Replying to [comment:12 mpatel]:
> Sure, that sounds good.
I have attached the replacement Makefile -- could you update the spkg with it?


---

Comment by mpatel created at 2010-03-02 22:32:56

Done!  The package now builds in parallel and `make check` now works for me on t2 and sage.math.


---

Attachment

Simplify `g0n/Makefile`.  eclib src repo.


---

Comment by mvngu created at 2010-03-06 23:44:01

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-06 23:44:01

The updated eclib package [eclib-20080310.p10.spkg](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.spkg) looks good. It solves the unexpected annoyance introduced by #7575.


---

Comment by mhansen created at 2010-03-07 00:23:05

Resolution: fixed
