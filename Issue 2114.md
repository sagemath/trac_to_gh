# Issue 2114: get gf2x into Sage!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-08 15:12:20

Assignee: somebody

CC:  zimmerma malb jpflori jdemeyer

Check out http://wwwmaths.anu.edu.au/~brent/gf2x.html

It's:
  * by very well respected people
  * GPL'd (v2 or later)
  * Small pure C code:

```
dhcp46-72:gf2x-0.1 was$ ls
BestToom.c          README              ToomSpace.c         gen_bb_mul_code.c   mul-tc3w.c          mul2t.c             tune1               tuneup.c
COPYING             TC.h                cantor              mul-tc3.c           mul-tc4.c           mulfft-bit.c        tunefft.c
HalfGCD.c           Toom.c              factor.c            mul-tc3u.c          mul.c               patch-wrt-ntl-5.3.1 tunetoom.c
dhcp46-72:gf2x-0.1 was$ usage
4	BestToom.c
4	README
4	TC.h
4	Toom.c
4	ToomSpace.c
4	patch-wrt-ntl-5.3.1
4	tune1
4	tuneup.c
8	gen_bb_mul_code.c
8	mul2t.c
8	tunefft.c
12	mul-tc3.c
12	mul-tc3u.c
12	mul-tc3w.c
12	mul-tc4.c
12	tunetoom.c
16	HalfGCD.c
16	mul.c
20	COPYING
28	mulfft-bit.c
40	factor.c
132	cantor
368	total
```

    * and Paul Z. says: 

```
for your information, on http://wwwmaths.anu.edu.au/~brent/gf2x.html you will
find an implementation up to 5 times faster than NTL's GF2X (for degree 2^20).
```



---

Comment by was created at 2008-02-15 04:42:56


```
Emmanuel Thomé to me, Paul, Pierrick
	
show details 2:53 PM (5 hours ago) [gf2x-20070214.tar.gz]
	
	
Reply
	
	
	from	Emmanuel Thomé <Emmanuel.Thome`@`normalesup.org>
to	wstein`@`gmail.com,
cc	Paul Zimmermann <Paul.Zimmermann`@`loria.fr>,
Pierrick Gaudry <gaudry`@`lix.polytechnique.fr>,
date	Thu, Feb 14, 2008 at 2:53 PM
subject	gf2x package
	
hide details 2:53 PM (5 hours ago) [gf2x-20070214.tar.gz]
	
	
Reply
	
	
On Thu, Feb 14, 2008 at 06:12:34PM +0100, Paul Zimmermann wrote:
> http://trac.sagemath.org/sage_trac/ticket/2114

For your information, you might find the attached version more
packageable (it can live outside NTL, for instance). Yet, the build
process is still tricky: Auto tuning and so on. Depending on your
preferred practices for sage, your preferred option could be to
statically save the thresholds file per-machine.

Regards,

E.
```


The "attached version" is here:
   http://sage.math.washington.edu/home/was/tmp/gf2x-20070214.tar.gz


---

Comment by zimmerma created at 2008-10-18 11:43:08

A new version (0.3.1) is available from http://wwwmaths.anu.edu.au/~brent/gf2x.html.


---

Comment by zimmerma created at 2009-11-27 10:13:51

GF2X has now its own development page: http://gf2x.gforge.inria.fr/.
It should be easier to incorporate into Sage now, but maybe it would be better
to include it through NTL, since since NTL 5.5, NTL can be configured to use GF2X as
auxiliary package. In such a way, Sage will benefit from GF2X for all computations with NTL.


---

Comment by zimmerma created at 2010-02-25 09:06:08

Note that since ntl-5.5, NTL can now be configured to use GF2X instead of its own routines.
This is probably the easiest way to get GF2X into Sage.


---

Comment by jpflori created at 2013-06-04 14:10:55

Paul, I'm finally packaging this, only planning to build NTL on top of it, no "native" interface.
Is tuning still highly recommended? Because it really takes a long time.
I was thinking of providing an option (GF2X_TUNE=yes/no, any better idea?) to enable/disable it, not sure what the default should be.
The README suggests it would be yes by default.


---

Comment by jpflori created at 2013-06-04 15:01:38

Changing keywords from "" to "spkg gf2x".


---

Comment by jpflori created at 2013-06-04 15:01:38

Upped spkgs, with the GF2X_TUNE option off by default (took one hour on a quite recent Xeon (with only one thread, but I did not test whether tuning gets parallelized)).
Set it to yes to perform tuning.

I did not check this actually speeds up NTL, anyone wanting to benchmark the new NTL spkg against the old one please go ahead.

As NTL is a standard spkg, not sure what the way to go is.
Jeroen please decide what to do.


---

Comment by jpflori created at 2013-06-04 15:01:38

Changing status from new to needs_review.


---

Comment by jpflori created at 2013-06-04 15:02:16

Spkg diff, for review only.


---

Comment by jdemeyer created at 2013-06-04 20:08:31

Changing status from needs_review to needs_info.


---

Attachment

Replying to [comment:8 jpflori]:
> Jeroen please decide what to do.
Why should I?  _You_ should decide if you want this:
 a. as standard package (which requires a discussion on `sage-devel` and changes to `spkg/standard/deps`)
 b. as optional package (but then NTL needs to work both with and without `gf2x`)
 c. not at all


---

Comment by jpflori created at 2013-06-04 22:11:14

I say we want this as a standard package and would prefer to avoid an optional stage (just imagine we patch ntl inbetween.
But I thought we needed optional before standard for all packages, so in this case this would be complicated.
So I'll post on sage-devel.


---

Comment by vbraun created at 2013-06-04 23:18:10

So does it actually speed up things, considering that we disable tuning? If not then forget about it. If yes then I'd be happy to see it included.


---

Comment by jpflori created at 2013-06-04 23:26:48

Just for hint, my experience playing with FLINT, using gf2x for GF(2) polynomials instead of the basic implementation inside FLINT using long gave an incredible speedup.
And from the maybe 4 years ago comments in the ticket description, it should also seepdup NTL.
I just don't have the time or the motivation to benchmark products of GF(2**n) elements (once you don't use Givaro) right now to prove it is beneficial.


---

Comment by zimmerma created at 2013-06-05 08:21:01

Replying to [comment:7 jpflori]:
> Paul, I'm finally packaging this, only planning to build NTL on top of it, no "native" interface.
> Is tuning still highly recommended? Because it really takes a long time.
> I was thinking of providing an option (GF2X_TUNE=yes/no, any better idea?) to enable/disable it, not sure what the default should be.
> The README suggests it would be yes by default.

Jean-Pierre,

make tune-lowlevel is still highly recommended, since it will choose the best routine up to 9 words.
It takes a little more than one minute on my 4-year-old laptop (including recompiling the library).

Then you can do say `make tune-toom TOOM_TUNING_LIMIT=100` to choose the best algorithm up to say
100 words (i.e., degree < 6400 on a 64-bit computer). It should take a few minutes only.

Paul


---

Comment by jpflori created at 2013-06-05 09:17:49

Ok, I'll do that.
Thanks for the suggestion.


---

Comment by jpflori created at 2013-06-05 09:20:32

Changing status from needs_info to needs_review.


---

Comment by jpflori created at 2013-06-05 09:20:32

Replying to [comment:12 jpflori]:
> Just for hint, my experience playing with FLINT, using gf2x for GF(2) polynomials instead of the basic implementation inside FLINT using long gave an incredible speedup.
> And from the maybe 4 years ago comments in the ticket description, it should also seepdup NTL.
> I just don't have the time or the motivation to benchmark products of GF(2**n) elements (once you don't use Givaro) right now to prove it is beneficial.
On my pc, multiplying two random elements of GF(2**10000) goes from 103us in Sage 5.9 with old NTL to 21.4us in 5.10.rc0 with NTL+gf2x.


---

Comment by jpflori created at 2013-06-05 09:20:39

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-06-05 09:38:28

New spkg up and diff updated.
Pleas ignore the broken tuning.diff I posted.


---

Comment by jpflori created at 2013-06-05 09:39:19

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-05 09:41:55

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-06-05 09:41:55

Wrong spelling...


---

Comment by jpflori created at 2013-06-05 09:44:40

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-05 09:44:40

Should be ok now.


---

Comment by jdemeyer created at 2013-06-05 10:35:18

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2013-06-05 10:35:18

This needs a patch to `spkg/standard/deps` and `spkg/install`.


---

Comment by zimmerma created at 2013-06-05 12:11:03

while trying gf2x-1.1 on my laptop, I hit a bug due to the fact that the tuning gave
`GF2X_MUL_TOOM4_ALWAYS_THRESHOLD=16`, whereas a value at least 30 is required.
The following patch will avoid this problem (or detect it earlier). It is against the development version but should be easily adapted to 1.1:

```
--- toom.c      (revision 148)
+++ toom.c      (working copy)
`@``@` -1,6 +1,6 `@``@`
 /* This file is part of the gf2x library.
 
-   Copyright 2007, 2008, 2009
+   Copyright 2007, 2008, 2009, 2013
    Richard Brent, Pierrick Gaudry, Emmanuel Thome', Paul Zimmermann
 
    This program is free software; you can redistribute it and/or modify it
`@``@` -53,6 +53,9 `@``@`
     if (n < GF2X_MUL_TOOMW_THRESHOLD)
        return GF2X_SELECT_KARA;                // KarMul
 
+#if GF2X_MUL_TOOM4_ALWAYS_THRESHOLD < 30
+#error "GF2X_MUL_TOOM4_ALWAYS_THRESHOLD must be >= 30"
+#endif
     if (n >= GF2X_MUL_TOOM4_ALWAYS_THRESHOLD)
        return GF2X_SELECT_TC4;         // Toom4Mul
```



---

Comment by zimmerma created at 2013-06-05 12:16:37

oh, I understand what happened now. I did `make tune-toom TOOM_TUNING_LIMIT=16` which sets automatically `GF2X_MUL_TOOM4_ALWAYS_THRESHOLD` to 16. When running `make tune-toom TOOM_TUNING_LIMIT=nnn`, one should always have nnn at least 30.

Paul


---

Comment by jpflori created at 2013-06-05 12:37:54

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-05 12:37:54

I've used 100 as a limit so it should be ok.


---

Comment by leif created at 2013-06-05 21:08:51

Waaaaah!  Just created (or rather finished) an NTL 5.5.2.p1 spkg (fixing hardcoded `make`) at #14692... 8-/


---

Comment by leif created at 2013-06-05 21:35:09

Replying to [comment:25 leif]:
> Waaaaah!  Just created (or rather finished) an NTL 5.5.2.p1 spkg (fixing hardcoded `make`) at #14692... 8-/

Ok, I've rebased _your_ `.p1` on mine:

http://boxen.math.washington.edu/home/leif/Sage/spkgs/ntl-5.5.2.p2.spkg


```diff
diff --git a/.hgtags b/.hgtags
--- a/.hgtags
+++ b/.hgtags
`@``@` -1,3 +1,4 `@``@`
 73d22601a79e226c590bb93cc842391e9e8f8d11 ntl-5.5.2
 5cf2d2f43b4d9cf1fc3cf8e9bb54efc58ccf2b4f ntl-5.5.2.p0
 c7af41e56a64bdef778ee579beda9d54943105fe ntl-5.5.2.p1
+4984ca9298a7310c9378ca8cd391dc8a1ba85d9f ntl-5.5.2.p2
diff --git a/SPKG.txt b/SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
`@``@` -18,6 +18,7 `@``@`
 
 == Dependencies ==
  * gmp
+ * gf2x
 
 == Special Update/Build Instructions ==
  * We need to modfiy new.h to accomodate Singular
`@``@` -34,6 +35,9 `@``@`
 
 == Changelog ==
 
+=== ntl-5.5.2.p2 (Jean-Pierre Flori, June 5th 2013) ===
+ * #2114: Build NTL with gf2x support.
+
 === ntl-5.5.2.p1 (Leif Leonhardy, June 5th 2013) ===
  * #14692: Patch upstream to use `$(MAKE)` (instead of `make`) in the generated
    Makefile (and in two scripts called from the Makefile which in turn invoke
diff --git a/spkg-install b/spkg-install
--- a/spkg-install
+++ b/spkg-install
`@``@` -86,7 +86,7 `@``@`
         CC="$CC" CFLAGS="$CFLAGS $SHAREDFLAGS" \
         CXX="$CXX" CXXFLAGS="$CXXFLAGS $SHAREDFLAGS" \
         LDFLAGS="$LDFLAGS" LIBTOOL_LINK_FLAGS="$LIBTOOL_LINK_FLAGS" \
-        NTL_GMP_LIP=on NTL_STD_CXX=on \
+        NTL_GMP_LIP=on NTL_GF2X_LIB=on NTL_STD_CXX=on \
         LIBTOOL=../../libtool/libtool
 
     if [ $? -ne 0 ]; then
```



---

Comment by leif created at 2013-06-05 22:00:15

W.r.t. gf2x:

The following doesn't work (`-O0` never takes effect):

```sh

if [ "$SAGE64" = "yes" ]; then
    echo "Building a 64-bit version of gf2x."
    ABI="64"; export ABI
    CFLAGS="-O2 -g -m64 $CFLAGS"; export CFLAGS
else
    CFLAGS="-O2 -g $CFLAGS"; export CFLAGS
fi

if [ "$SAGE_DEBUG" = "yes" ]; then
    echo "Building a debug version of gf2x."
    CFLAGS="-O0 -g $CFLAGS"; export CFLAGS
fi
```


`$SAGE_LOCAL` should be quoted in the `rm` commands in `spkg-install`.


---

Comment by leif created at 2013-06-05 22:05:11

Minor thing:  "Patching gf2x." gets printed even when no patch gets applied.


---

Comment by leif created at 2013-06-06 01:06:24

P.S.:  For other spkgs, we (currently) use `SAGE_TUNE_<package name>[={yes,no}]` (where `<package name>` can be both upper or lower case).  And the new variable should probably get documented in `devel/sage/doc/en/installation/source.rst` (section "Environment variables").

`GF2X_TUNE=full` really takes ages, and uses *a lot* of memory (so far up to 2 GB resident / 2.5 GB virtual).


---

Comment by leif created at 2013-06-06 04:14:58


```
gf2x.c: In function 'gf2x_mul_pool_init':
gf2x.c:82:24: warning: argument to 'sizeof' in 'memset' call is the same expression as the destination; did you mean to dereference it? [-Wsizeof-pointer-memaccess]
     memset(p, 0, sizeof(p));
                        ^
```


? :-)


---

Comment by leif created at 2013-06-06 04:38:02

Replying to [comment:31 leif]:
> {{{
> gf2x.c: In function 'gf2x_mul_pool_init':
> gf2x.c:82:24: warning: argument to 'sizeof' in 'memset' call is the same expression as the destination; did you mean to dereference it? [-Wsizeof-pointer-memaccess]
>      memset(p, 0, sizeof(p));
>                         ^
> }}}

Harmless, but warning could be avoided by using `sizeof(gf2x_mul_pool_t)` or `sizeof(p[0])` instead in

```c
void gf2x_mul_pool_init(gf2x_mul_pool_t p)
{
    memset(p, 0, sizeof(p));
}
```



---

Comment by leif created at 2013-06-06 04:49:05

Otherwise (i.e., modulo mentioned issues) looks ok (and apparently works; Linux x86 and x86_64, GCC 4.4.3 / 4.7.2 / 4.8.0, with `SAGE_CHECK=yes`, _some_ doctests run).




Building with `GF2X_TUNE=full` finally took more than four and a half hours, admittedly on a not-so-fast (but otherwise almost idle, dual-core) machine...


---

Comment by zimmerma created at 2013-06-06 06:46:00

I've fixed the warning reported in comment [comment:31] upstream, thanks.

Paul


---

Comment by jpflori created at 2013-06-06 09:18:03

Thanks leif, I'll take all these sensible remarks into account.


---

Comment by jdemeyer created at 2013-06-06 09:19:57

Also `$SAGE_ROOT/COPYING.txt` should be updated (keeping in mind #12447).


---

Comment by jdemeyer created at 2013-06-06 09:20:58

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-06-06 09:46:21

I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.

I'm aware that we always print the patching message, it saves a few lines of script...


---

Attachment


---

Comment by jpflori created at 2013-06-06 09:52:56

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-06 09:53:29

If you prefer, I can include Paul's patch so that we will actually be patching gf2x.


---

Comment by zimmerma created at 2013-06-06 09:58:46

my patch (from comment [comment:22]) is not needed if you do `tune-toom TOOM_TUNING_LIMIT=nnn` with nnn at least 30.

Paul


---

Comment by jpflori created at 2013-06-06 10:02:37

I meant leif's patch in fact, the one from comment http://trac.sagemath.org/sage_trac/ticket/2114#comment:32 suppressing a warning.


---

Comment by zimmerma created at 2013-06-06 10:08:16

ok, here is the change I did upstream:

```
--- gf2x.c	(revision 150)
+++ gf2x.c	(working copy)
`@``@` -79,7 +79,7 `@``@`
 
 void gf2x_mul_pool_init(gf2x_mul_pool_t p)
 {
-    memset(p, 0, sizeof(p));
+    memset(p, 0, sizeof(gf2x_mul_pool_t));
 }
 
 void gf2x_mul_pool_clear(gf2x_mul_pool_t p)
```

Paul


---

Comment by jpflori created at 2013-06-06 10:10:59

Thanks Paul.
If leif rants, I'll include it.

But IMHO we can wait for the gf2x 1.2 release to get this warning suppressed.
I think that getting gf2x in Sage quickly is a more important matter.


---

Comment by leif created at 2013-06-06 14:47:00

Replying to [comment:45 jpflori]:
> Thanks Paul.
> If leif rants, I'll include it.

The "rant" addressed upstream, and (as expected) reached it... ;-)

I don't care whether you include a patch here.


---

Comment by leif created at 2013-06-06 14:50:57

P.S.:  There are other warnings where the return value of `fgets()` (IIRC) gets discarded / ignored, in tuning-related code.  (But in those cases it's IMHO more obvious to the user that the warnings can safely be ignored.)


---

Comment by leif created at 2013-06-06 14:56:53

Replying to [comment:39 jpflori]:
> I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.

Hmmm...  If you at least create a meta-ticket to record what has to be documented...




> I'm aware that we always print the patching message, it saves a few lines of script...

I'm using either `ls ../patches/*.patch >/dev/null 2>&1 && ...`, or simply _"Applying patches to upstream (if any) ..."_


---

Comment by leif created at 2013-06-06 14:57:51

Btw., `ptestlong` passed with Sage 5.10.rc0 on Linux x86_64.


---

Comment by jpflori created at 2013-06-06 15:02:57

Replying to [comment:48 leif]:
> Replying to [comment:39 jpflori]:
> > I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.
> 
> Hmmm...  If you at least create a meta-ticket to record what has to be documented...
Done, see #14698 (you're cc'ed there anyway).
> 
> 

> 
> > I'm aware that we always print the patching message, it saves a few lines of script...
> 
> I'm using either `ls ../patches/*.patch >/dev/null 2>&1 && ...`, or simply _"Applying patches to upstream (if any) ..."_
Ok, it's true it's simple enough, I'll change that.


---

Comment by jpflori created at 2013-06-06 15:02:57

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-06-06 15:10:18

Done.

Now the NTL spkg should be rebased when #14692 is done.


---

Comment by jpflori created at 2013-06-06 15:11:37

Or the converse.


---

Comment by jpflori created at 2013-06-06 15:24:31

As #14692 needs more work, let's base it on top of this ticket rather than the other way around.


---

Comment by jpflori created at 2013-06-06 15:24:31

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2013-06-06 17:02:36

Replying to [comment:47 leif]:
> P.S.:  There are other warnings where the return value of `fgets()` (IIRC) gets discarded / ignored, in tuning-related code.  (But in those cases it's IMHO more obvious to the user that the warnings can safely be ignored.) 

Leif, thanks, I've fixed a few upstream. It is always nice to get feedback when a package is used in Sage!

Paul


---

Comment by jdemeyer created at 2013-06-08 11:04:06

I made a few small changes to `gf2x` to make `spkg-install` more like most other standard packages. I also re-downloaded the upstream source, as timestamps got messed up somehow.


---

Comment by jdemeyer created at 2013-06-08 11:06:28

For NTL, I added the `hg tag`.


---

Comment by jdemeyer created at 2013-06-08 11:07:08

Changing component from basic arithmetic to packages: standard.


---

Comment by leif created at 2013-06-08 11:09:51

Replying to [comment:57 jdemeyer]:
> I made a few small changes to `gf2x` to make `spkg-install` more like most other standard packages. I also re-downloaded the upstream source, as timestamps got messed up somehow.

You didn't fix "gf2x is a C/C+ software package" though... ;-)

Could you attach a diff of *your* changes?

I don't want to re-review everything.  Retesting is odd enough.


---

Comment by jdemeyer created at 2013-06-08 11:28:34

Spkg diff, for review only.


---

Attachment


---

Attachment

Replying to [comment:61 leif]:
> You didn't fix "gf2x is a C/C+ software package" though... ;-)
Fixed now.

> Could you attach a diff of *your* changes?
[attachment:gf2x-1.1-jdemeyer.diff]


---

Comment by leif created at 2013-06-08 12:04:00

Replying to [comment:62 jdemeyer]:
> Replying to [comment:61 leif]:
> > You didn't fix "gf2x is a C/C+ software package" though... ;-)
> Fixed now.
> 
> > Could you attach a diff of *your* changes?
> [attachment:gf2x-1.1-jdemeyer.diff]

I would have dropped the "C++"; if gf2x was (partially) implemented in C++, we'd have to set / change `CXXFLAGS` as well.

I'd probably also use `$CFLAG64` instead of hardcoding `-m64`.


---

Comment by leif created at 2013-06-08 12:06:37

Did I mention it also builds with `clang`? ;-)


---

Comment by jdemeyer created at 2013-06-08 12:09:48

Replying to [comment:63 leif]:
> I would have dropped the "C++"
The text was taken verbatim from [upstream](http://gf2x.gforge.inria.fr/).


---

Comment by leif created at 2013-06-08 12:13:11

Replying to [comment:65 jdemeyer]:
> Replying to [comment:63 leif]:
> > I would have dropped the "C++"
> The text was taken verbatim from [upstream](http://gf2x.gforge.inria.fr/).

I think it's covered by the GPL as well.


---

Comment by zimmerma created at 2013-06-08 12:46:04

the C++ part of gf2x is only in the "apps" subdirectory, which contains binaries to be linked with NTL
(we had to use C++ here since NTL is under C++) to check for primitive trinomials. I guess Sage does not use that part, thus indeed only C code is used within Sage.

Paul


---

Comment by leif created at 2013-06-08 13:17:30

Replying to [comment:67 zimmerma]:
> the C++ part of gf2x is only in the "apps" subdirectory, which contains binaries to be linked with NTL
> (we had to use C++ here since NTL is under C++) to check for primitive trinomials.
> 

> 
> I guess Sage does not use that part, thus indeed only C code is used within Sage.

We can't build those apps (at least not immediately), since we decided to let NTL depend on gf2x.


---

Comment by jdemeyer created at 2013-06-08 18:53:49

Positive review to everything except my changes ([attachment:gf2x-1.1-jdemeyer.diff]).


---

Comment by jpflori created at 2013-06-08 18:56:05

I'm ok with them.


---

Comment by jpflori created at 2013-06-08 18:56:05

Changing status from needs_review to positive_review.


---

Comment by leif created at 2013-06-08 19:02:00

FWIW, I was going to give the previous spkgs positive review right when Jeroen started to change both, so I don't insist on fixing the hardcoded `-m64`.


---

Comment by jdemeyer created at 2013-06-10 08:41:43

Resolution: fixed
