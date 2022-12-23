# Issue 5776: sage-location ought to rewrite loads of files in $SAGE_LOCAL/bin

Issue created by migration from https://trac.sagemath.org/ticket/5776

Original creator: mabshoff

Original creation time: 2009-04-13 07:55:44

Assignee: mabshoff

CC:  leif

The following is from a 3.4.1.rc3 build that was -bdisted from 3.4.1.rc2. There are *loads* of files that still have 3.4.1.rc2 in various config files:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/local/bin$ grep -r "sage-3.4.1.rc2" *  | grep --invert-match Binary
freetype-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
freetype-config:    major=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \
freetype-config:    minor=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \
freetype-config:    patch=`grep define /scratch/mabshoff/sage-3.4.1.rc2/local/include/freetype2/freetype/freetype.h \
gdlib-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
gdlib-config:	echo  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -Wl,--rpath -Wl,/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib 
gdlib-config:	echo "ldflags:     -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -Wl,--rpath -Wl,/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib "
ghmm-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
givaro-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
givaro-config:       	echo -I${includedir} -I/scratch/mabshoff/sage-3.4.1.rc2/local//include
givaro-config:       	echo -L${libdir} -lgivaro -L/scratch/mabshoff/sage-3.4.1.rc2/local//lib -lgmp 
givaro-makefile:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
givaro-makefile:OPTFLAGS = -I/scratch/mabshoff/sage-3.4.1.rc2/local//include  -fPIC -I"/scratch/mabshoff/sage-3.4.1.rc2/local/include"
givaro-makefile:GMP_CFLAGS = -I/scratch/mabshoff/sage-3.4.1.rc2/local//include
givaro-makefile:GMP_LIBS   = -L/scratch/mabshoff/sage-3.4.1.rc2/local//lib -lgmp
gpg-error-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
gphelp:$datadir= "/scratch/mabshoff/sage-3.4.1.rc2/local/share/pari";
gsl-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
libgcrypt-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
libgcrypt-config:gpg_error_libs="-L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgpg-error"
libgcrypt-config:gpg_error_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include"
libgnutls-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
libgnutls-config:gnutls_libs="-L${exec_prefix}/lib -lgnutls  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error "
libgnutls-config:gnutls_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include  -I${prefix}/include"
libgnutls-extra-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
libgnutls-extra-config:gnutls_libs="-L${exec_prefix}/lib -lgnutls-extra -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lopencdk -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgpg-error -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lz -R/scratch/mabshoff/sage-3.4.1.rc2/local/lib  -L${exec_prefix}/lib -lgnutls  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error "
libgnutls-extra-config:gnutls_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I${prefix}/include"
libpng12-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
libpng-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
linbox-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
linbox-config:       	echo -I${includedir} -I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I/scratch/mabshoff/sage-3.4.1.rc2/local/include   
linbox-config:       	echo -L${libdir} -llinbox   -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lntl -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgivaro  -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgmpxx -lgmp -lcblas -latlas
maxima:  prefix=`unixize "/scratch/mabshoff/sage-3.4.1.rc2/local"`
maxima:  top_srcdir=`unixize "/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/maxima-5.16.3/src"`
opencdk-config:prefix=/scratch/mabshoff/sage-3.4.1.rc2/local
opencdk-config:opencdk_libs="-L${exec_prefix}/lib -lopencdk -L/scratch/mabshoff/sage-3.4.1.rc2/local/lib -lgcrypt -lgpg-error  -lz"
opencdk-config:opencdk_cflags="-I/scratch/mabshoff/sage-3.4.1.rc2/local/include -I${prefix}/include"
qd-config:prefix="/scratch/mabshoff/sage-3.4.1.rc2/local"
qd-config:srcdir="/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/quaddouble-2.2.p9/src"
qd-config:builddir="/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/quaddouble-2.2.p9/src"
qd-config:configure_args=" '--prefix=/scratch/mabshoff/sage-3.4.1.rc2/local' '--enable-fortran=no' 'CXX=g++' 'CXXFLAGS=-fPIC -O3 -Dx86' 'LDFLAGS=' 'CC=gcc'"
R:R_HOME_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R
R:#R_HOME_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R
R:R_SHARE_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/share
R:R_INCLUDE_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/include
R:R_DOC_DIR=/scratch/mabshoff/sage-3.4.1.rc2/local/lib/R/doc
rmaxima:  MAXIMA_SHAREDIR=/scratch/mabshoff/sage-3.4.1.rc2/local/share/maxima/5.16.3/share
rmaxima:  MAXIMA_SHAREDIR=/scratch/mabshoff/sage-3.4.1.rc2/spkg/build/maxima-5.16.3/src/share
xmaxima:set autoconf(prefix) "/scratch/mabshoff/sage-3.4.1.rc2/local"
xmaxima:set autoconf(exec_prefix) "/scratch/mabshoff/sage-3.4.1.rc2/local"
xmaxima:set autoconf(libdir) "/scratch/mabshoff/sage-3.4.1.rc2/local/lib"
xmaxima:set autoconf(libexecdir) "/scratch/mabshoff/sage-3.4.1.rc2/local/libexec"
xmaxima:set autoconf(datadir) "/scratch/mabshoff/sage-3.4.1.rc2/local/share"
xmaxima:set autoconf(infodir) "/scratch/mabshoff/sage-3.4.1.rc2/local/info"
```


This causes loads of odd bugs when installing/upgrading from a bdist build, i.e. the location to R_HOME is hardcoded which might be involved with #5246 and #5634.

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:24:56

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by was created at 2009-06-15 23:24:56

Changing priority from blocker to critical.


---

Comment by jason created at 2010-06-11 06:41:16

See #9210 for a rewrite of sage-location that takes care of resetting pkg-config files.


---

Comment by jason created at 2010-06-11 19:34:21

See http://blogs.sun.com/dipol/entry/dynamic_libraries_rpath_and_mac for some suggestions on how to make things relocateable.


---

Comment by leif created at 2010-10-20 12:44:17

Changing keywords from "" to "relocation move moving SAGE_ROOT".


---

Comment by leif created at 2010-10-20 12:44:17

Remove assignee mabshoff.


---

Comment by kcrisman created at 2011-06-21 14:51:13

Is this ticket still necessary?  It might be helpful to break this into tickets by spkg or something.

R is already probably on the docket - se #8274 and #10967, for instance.


---

Comment by jdemeyer created at 2016-04-11 09:29:34

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-04-11 09:29:34

`sage-location` is obsolete


---

Comment by jdemeyer created at 2016-04-11 09:29:38

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
