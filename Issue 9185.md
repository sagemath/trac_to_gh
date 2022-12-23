# Issue 9185: Update Singular's spkg-install for building multiple spkgs in parallel

Issue created by migration from https://trac.sagemath.org/ticket/9185

Original creator: mpatel

Original creation time: 2010-06-08 08:40:36

Assignee: tbd

CC:  drkirkby jhpalmieri leif mhansen

To build the Singular spkg with `SAGE_PARALLEL_SPKG_BUILD="yes"` on Mac OS X, we need to add, e.g.,

```sh
MAKEFLAGS=
export MAKEFLAGS
```

to the package's `spkg-install`.

Please see #8306 about building spkgs in parallel.  For `MAKEFLAGS`, see [the GNU Make manual](http://www.gnu.org/software/make/manual/html_node/Options_002fRecursion.html).


---

Comment by mpatel created at 2010-06-08 09:17:26

I think we should work from #9160.


---

Attachment

spkg patch. Set empty `MAKEFLAGS`.


---

Comment by mpatel created at 2010-06-09 02:35:01

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-06-09 02:35:01

I've put a new spkg at

 * http://sage.math.washington.edu/home/mpatel/trac/9185/singular-3.1.0.4.p7.spkg

It's based on the package mentioned in [comment:ticket:9160:18 this comment] at #9160.  If there are more changes at that ticket, I can reapply the patch above and make a new spkg.


---

Comment by mpatel created at 2010-06-12 08:51:00

I'm not sure why `unset MAKE` in `spkg-install` doesn't suppress parallel intra-spkg builds/installs for Singular (#9185), R (#9186), or ECL (#9187) on OS X.  In particular, I don't know whether the source of the problem is in `make`, OS X, or the Sage/spkg `Makefile`s.  But setting an empty `MAKEFLAGS` variable seems to work without causing problems on other platforms.


---

Comment by leif created at 2010-06-12 11:27:28

Not directly related to this ticket, but to Singular's `spkg-install`:

We have *two* "patches" to `src/Singular/Makefile.in`; both are copied, the newer after the older one:

```
    # work-around patches
    cp patches/mminit.cc src/kernel/
    cp patches/assert.h src/factory/
    cp patches/kernel.rmodulon.cc src/kernel/rmodulon.cc
    cp patches/src.Singular.Makefile.in src/Singular/Makefile.in
    cp patches/Singular.libsingular.h src/Singular/libsingular.h
    cp patches/factory.GNUmakefile.in src/factory/GNUmakefile.in
    cp patches/libfac.charset.alg_factor.cc src/libfac/charset/alg_factor.cc
    cp patches/kernel.Makefile.in src/kernel/Makefile.in
    cp patches/Singular.Makefile.in src/Singular/Makefile.in
    cp patches/Singular.tesths.cc src/Singular/tesths.cc

```


Some Solaris stuff seems to be lost (obsolete?):

```
--- patches/src.Singular.Makefile.in	2009-06-11 12:23:38.000000000 +0200
+++ patches/Singular.Makefile.in	2010-01-20 18:30:21.000000000 +0100
@@ -130,12 +130,6 @@
 LIBSINGULAR_LIBS = -lsingfac -lsingcf -lntl -lreadline -lgmp -lomalloc  -lhtmlhelp
 endif
 
-ifeq ($(SINGUNAME),ix86-SunOS)
-SO_SUFFIX  = so
-LIBSINGULAR_FLAGS = -shared
-LIBSINGULAR_LIBS = -lsingfac -lsingcf -lntl -lreadline -lgmp -lomalloc
-endif
-
 #
 # End libSINGULAR
 #
@@ -534,12 +528,18 @@
 	${INSTALL_DATA} `pwd`/LIB/gftables/* ${slibdir}/gftables/
 
 install-libsingular: libsingular
+	${MKINSTALLDIRS} ${includedir}/singular
 	for file in *.$(SO_SUFFIX); do \
 	  ${INSTALL_PROGRAM}  $$file ${libdir}; \
 	done
 	${INSTALL_PROGRAM} libsingular.h ${includedir}
-
-
+	${INSTALL_PROGRAM} subexpr.h ${includedir}/singular
+	${INSTALL_PROGRAM} tok.h ${includedir}/singular
+	${INSTALL_PROGRAM} grammar.h ${includedir}/singular
+	${INSTALL_PROGRAM} ipid.h ${includedir}/singular
+	${INSTALL_PROGRAM} ipshell.h ${includedir}/singular
+	${INSTALL_PROGRAM} lists.h ${includedir}/singular
+	${INSTALL_PROGRAM} attrib.h ${includedir}/singular
 
 uninstall: uninstallbin
```


If appropriate, we should merge them, and delete the older one (including the `cp` line of course).

Dave?


---

Comment by drkirkby created at 2010-06-12 15:49:30

Replying to [comment:3 mpatel]:
> I'm not sure why `unset MAKE` in `spkg-install` doesn't suppress parallel intra-spkg builds/installs for Singular (#9185), R (#9186), or ECL (#9187) on OS X.  In particular, I don't know whether the source of the problem is in `make`, OS X, or the Sage/spkg `Makefile`s.  But setting an empty `MAKEFLAGS` variable seems to work without causing problems on other platforms.

IMHO, unsetting MAKE is a bad idea. 

It is quite common for people to specify something like 


```
MAKE=/usr/sfw/bin/gmake -j 10
export MAKE
```


with the vague hope of using 'gmake' rather than 'make'. 

Rather than unsetting, one other possibility is 


```
MAKE="$MAKE -j1"
```


if the aim is to stop more than one thread. 

Of course, all this relies on people referring to variables and non hard-coded names like 'make'. 

I don't know if MAKEFLAGS is portable or not, but for now at least I guess it will do.


---

Comment by drkirkby created at 2010-06-12 16:15:11

Two questions:

 * Will this impact the speed of building singular? 
 * Is the observed problem only on OS X?
 * Do you have any idea why singular has built in parallel for some time without issue, but as soon as the packages are tested in parallel, so a problem arises? 


I'm just wondering if this might not be better in something like 


```
if [ "x`uname`" = xDarwin ] ; then 
   MAKEFLAGS=
   export MAKEFLAGS
fi 
```

so it only slows down on OS X. If we find there's issues on other platforms (and we soon will I think if there are any), then revisit this. 

I think your parallel building is a great idea, but it would be a shame to see the benefits eroded by having to get various packages to build serially, if they built ok in parallel before.
 

As for Leif's comment about the Solaris changes, I'd just let them die. This package is such a mess, any attempt at reason will lead to insanity. If its building on Solaris with those fixes missing, we might as well leave them missing. 


Dave


---

Comment by mpatel created at 2010-06-13 06:21:03

We already build Singular, ECL, and some other packages (e.g., Maxima and ATLAS) serially.  I'm pretty sure that this ticket and its related tickets (#9186, #9187) don't change that.  In particular, Singular's `spkg-install` already contains

```sh
# since parallel make breaks the singular build
MAKE="make"
export MAKE
```

and ECL's `spkg-install` already contains

```sh
# 'export MAKE='make -j n' where n>1, breaks ECL builds, so unset make
unset MAKE
```

R's `spkg-install` already contains

```sh
#parallel make install is broken
export MAKE=make
```


I don't know the details about why we don't build/install these packages in parallel.  Perhaps their upstream build systems (`Makefiles`, etc.) have too many "serialisms"?  It would be great if `make -jN` did work for ATLAS, ECL, Maxima, and Singular, since these packages seem to contribute significantly to the overall build time.

Isn't `-j` a non-[POSIX](http://www.opengroup.org/onlinepubs/009695399/utilities/make.html) argument for make?  The MAKEFLAGS change, which is also GNU make-specific, hasn't affected my builds on t2 and sage.math, but we could certainly restrict it to OS X.

Mike, do you happen to know how #8306 fares on Cygwin?


---

Comment by mhansen created at 2010-06-13 06:49:33

I haven't tried out #8306 on Cygwin, but I'll try it in the next day or two.


---

Comment by drkirkby created at 2010-06-13 09:06:42

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-13 09:06:42

I did not notice before that there was already an attempt to disable this package building in parallel on every platform. In which case, there is no point making this specific to OS X. 

I can't see what harm the change can do on any platform. 

In general, it would be good to resolve the issues of things building in parallel somewhat better. 't2' has 128 threads, but vary rarely are more than a few used. 

Positive review.


---

Comment by rlm created at 2010-06-25 15:46:50

Resolution: fixed
