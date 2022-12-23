# Issue 9859: Port changes in PARI 2.3.5.p4 (#9722) to current 2.4.3

Issue created by migration from https://trac.sagemath.org/ticket/9860

Original creator: leif

Original creation time: 2010-09-06 11:47:15

Assignee: leif

Some fixes to PARI 2.3.5.p2 from #9722 had to be ported to the current [NewPARI](http://wiki.sagemath.org/wiki/NewPARI) spkg. The new PARI 2.4.3.p5 spkg here contains some further changes (including some on Sage's side, mostly clean-up), while other issues have meanwhile been fixed upstream.

----

### pari-2.4.3.svn-12577.p5 (Leif Leonhardy, September 5th, 2010)
 * Added patches to:
   - config/get_config_options:
     * Make invalid arguments to "--graphic" a "Configure" error
       (rather than potentially running into *compilation* errors
       later).
   - config/get_fltk: (see also/ported from #9722)
     * Add libstdc++ to the libraries (to support Fedora 13 et al.).
     * Also check the presence of the FLTK include directory to
       prevent compilation errors on broken installations.
   - config/get_X11: (see also/ported from #9722)
     * Also search */lib64/* directories when doing a 64-bit build.
     * Give more specific messages.
 * Slightly extended existing patch to src/kernel/gmp/mp.c:
   - Allow disabling PARI's use of "GMP internals" by preprocessor
     directive (i.e. by adding "-DPARI_DONT_USE_GMP_INTERNALS" to
     CFLAGS). Brief explanation added.
 * spkg-install:
   - Don't override user-specified CFLAGS (w.r.t. optimization, unless
     SAGE_DEBUG=yes).
   - Handle PARI_EXTRA_OPTS properly, and print informative messages
     (regarding graphics support for plotting).
   - Recognize SAGE_TUNE_PARI in addition to SAGE_TUNE_pari, and
     add "--tune" to PARI_EXTRA_OPTS if self-tuning was requested.
   - Clear/unset lots of (environment) variables used by PARI that might
     unintentionally get their values from user settings.
   - Quote *all* occurrences of SAGE_LOCAL (and some other expressions).
   - Use $UNAME instead of `uname` everywhere, use "elif ...".
   - *Always* use $MAKE (changed for "install-data").
   - Begin all error messages with "Error".
   - Removed useless tests of $? at end.
   - Some clean-up (typos, formatting); some comments, some messages added.
 * spkg-check:
   - Use $MAKE instead of "make".
   - Don't override user-specified CFLAGS (w.r.t. optimization, unless
     SAGE_DEBUG=yes).
   - Begin error message with "Error".
   - Some clean-up.
 * Slight corrections to SPKG.txt.
 * Updated patches/README.txt, some cosmetic changes.


---

Comment by leif created at 2010-09-06 11:59:21

Apply to pari-2.4.3.svn-12577.p4.spkg. Note that added/changed files in `patches/files` are not included here!


---

Attachment

Diff of files in `patches/files`. Apply with `patch -p1` inside spkg directory.


---

Comment by leif created at 2010-09-06 12:38:46

Changing status from new to needs_review.


---

Attachment


---

Comment by leif created at 2010-09-06 12:54:50

I've only tested this with a couple of variations on parameters and installed libraries / graphics packages on Ubuntu 10.04 x86_64 and Fedora 13 x86.

_Should_ work on other systems as well... ;-)


---

Comment by drkirkby created at 2010-09-06 15:59:47

What do I need to do to test this - *just* download the package - do I need to patch anything else? 

I've done:

 * Downloaded and installed  http://spkg-upload.googlecode.com/files/pari-2.4.3.svn-12577.p5.spkg
 * Nothing else changed from 4.5.3.alpha2
 * No attempt to tune code
 

```
drkirkby@hawk:~/5/sage-4.5.3.alpha2$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/convert.pic.o -c -fPIC -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include/python2.6 -I/export/home/drkirkby/5/sage-4.5.3.alpha2/local/include/NTL -Iinclude src/convert.c
g++ -o libcsage.so -shared src/convert.pic.o src/interrupt.pic.o src/mpn_pylong.pic.o src/mpz_pylong.pic.o src/mpz_longlong.pic.o src/stdsage.pic.o src/gmp_globals.pic.o src/ZZ_pylong.pic.o src/ntl_wrap.pic.o -L/export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib -L/export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
Updating Cython code....
Execute 0 commands (using 0 threads)
Time to execute 0 commands: 0.0976297855377 seconds
Finished compiling Cython code (time = 3.07916307449 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  0.913223028183 seconds.
running install_lib
running install_egg_info
Removing /export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /export/home/drkirkby/5/sage-4.5.3.alpha2/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m8.727s
user	0m1.339s
sys	0m0.727s
drkirkby@hawk:~/5/sage-4.5.3.alpha2$ make ptestlong
cd spkg && ./install all 2>&1 | tee -a ../install.log
make[1]: Entering directory `/export/home/drkirkby/5/sage-4.5.3.alpha2/spkg'
make[1]: Nothing to be done for `all'.
make[1]: Leaving directory `/export/home/drkirkby/5/sage-4.5.3.alpha2/spkg'

real	0m0.018s
user	0m0.003s
sys	0m0.003s
To install gap, gp, singular, etc., scripts
in a standard bin directory, start sage and
type something like
   sage: install_scripts('/usr/local/bin')
at the Sage command prompt.

To build the documentation, run
   make doc

Sage build/upgrade complete!
./sage -docbuild all html  2>&1 | tee -a dochtml.log
sphinx-build -b html -d /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/output/doctrees/en/website    /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/en/website /export/home/drkirkby/5/sage-4.5.3.alpha2/devel/sage/doc/output/html/en/website
  ***   bug in PARI/GP (Segmentation Fault), please report
^Cmake: *** [doc-html] Interrupt
```


IIRC, the changes from `sage-4.5.3.alpha2` to `sage-4.5.3.rc0` were just a few Solaris-specific changes which would not all all doc tests to pass, but were not need to actually get things working. 

This is on an OpenSolaris (Xeon processor) machine. I've not tried on anything else. 

I'm rather hoping I've forgot something - in which case you have time to review #9603 !

Dave


---

Comment by jdemeyer created at 2010-09-06 16:14:45

Replying to [comment:3 drkirkby]:
> What do I need to do to test this - *just* download the package - do I need to patch anything else? 
You also need to apply the sagelib and extcode patches from #9343.  Or easier: download [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar), install that and _then_ install the new pari spkg.


---

Comment by jdemeyer created at 2010-09-06 16:21:40

I have made a few small changes to the pari spkg and put the result at  http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg (I kept the p5 version number).


---

Comment by drkirkby created at 2010-09-06 16:26:15

Replying to [comment:4 jdemeyer]:
> Replying to [comment:3 drkirkby]:
> > What do I need to do to test this - *just* download the package - do I need to patch anything else? 
> You also need to apply the sagelib and extcode patches from #9343.  Or easier: download [http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar](http://sage.math.washington.edu/home/jdemeyer/dist/sage-4.6.prealpha3.tar), install that and _then_ install the new pari spkg.

It would be good if you could make a new tar file with all the changes in place - i.e. make a `sage-4.6.prealpha4.tar`



Dave


---

Comment by jdemeyer created at 2010-09-06 16:32:46

Replying to [comment:7 drkirkby]:
> It would be good if you could make a new tar file with all the changes in place - i.e. make a `sage-4.6.prealpha4.tar`

I will now make a new 4.6-prealpha4 based on 4.5.3-rc0 with the new spkgs (I will also update genus2reduction, see #9591 and lcalc, see #9845).


---

Attachment

Additional spkg patches by me


---

Comment by leif created at 2010-09-07 07:52:54

Replying to [comment:6 jdemeyer]:
> I have made a few small changes to the pari spkg and put the result at  http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p5.spkg (I kept the p5 version number).

I'm ok with your changes ("positive review"). Not very surprisingly Sage 4.6.prealpha4 also passed all tests. Tuning on a Core2 worked, too, at least did pass without errors. ;-)

The way we handle the patches now (without the patched _replacement files_ being under revision control) is a bit dangerous though. Perhaps we should also add some script to _generate the patches_ from `patches/files/*` and one to just make sure they're in sync.


---

Comment by jdemeyer created at 2010-09-07 10:05:36

Leif: your patch looks good on visual inspection.  Since it fixes all known build issues, I give it positive review.


---

Comment by jdemeyer created at 2010-09-07 10:05:36

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-07 10:28:52

Otherwise looks a bit funny. Thanks though. ;-)

I think we should report some of the changes upstream when our PARI has successfully reached some Sage 4.6.{alpha,rc}.


---

Comment by jdemeyer created at 2010-09-07 10:36:55

Replying to [comment:12 leif]:
> I think we should report some of the changes upstream when our PARI has successfully reached some Sage 4.6.{alpha,rc}.

Agreed.


---

Comment by leif created at 2010-09-07 10:38:30

P.S.: Attempting to build with Qt as the graphics back-end is still broken in some constellations (i.e. may lead to build errors, too), since the code apparently expects Qt <= 3 and some (Qt) tools PARI doesn't look for. I haven't yet worked on `config/get_Qt` though.


---

Comment by mpatel created at 2010-09-10 10:45:26

Resolution: fixed
