# Issue 3989: [with spkg, needs review] autotools issues with gd-2.0.35

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-29 08:54:08

Assignee: mabshoff

The new hg package has various issues and we need to run a bunch of autohell and libtool commands to create proper sources. The spkg at

http://sage.math.washington.edu/home/mabshoff/gd-2.0.35.p1.spkg

fixes that issue. It builds on the Itanium boxen that up to now failed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-29 08:54:14

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-29 08:57:41

The problem is the following with gd *2.0.35*:

```

** Configuration summary for gd 2.0.34:

   Support for PNG library:          yes
   Support for JPEG library:         no
   Support for Freetype 2.x library: yes
   Support for Fontconfig library:   no
   Support for Xpm library:          no
   Support for pthreads:             yes

configure: creating ./config.status
config.status: creating Makefile
config.status: creating config/Makefile
config.status: creating config/gdlib-config
config.status: creating test/Makefile
config.status: creating config.h
config.status: executing depfiles commands
make[2]: Entering directory `/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src'
cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run aclocal-1.9 -I config
cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run autoconf
 cd . && /bin/sh /scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/spkg/build/gd-2.0.35/src/config/missing --run automake-1.9 --foreign 
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure  --prefix=/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local --without-jpeg --without-x --with-zlib=/scratch/mabs
hoff/release-cycle/sage-3.1.2.alpha1/local --with-freetype2=/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local CC=gcc CFLAGS= -fPIC -g -I"/scratch/mabshoff/releas
e-cycle/sage-3.1.2.alpha1/local/include" -I/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/include/freetype2/ LDFLAGS= CXX=g++  --no-create --no-recursion
checking
```

With the fix:

```
** Configuration summary for gd 2.0.35:

   Support for PNG library:          yes
   Support for JPEG library:         no
   Support for Freetype 2.x library: yes
   Support for Fontconfig library:   no
   Support for Xpm library:          no
   Support for pthreads:             yes

configure: creating ./config.status
config.status: creating Makefile
config.status: creating config/Makefile
config.status: creating config/gdlib-config
config.status: creating test/Makefile
config.status: creating config.h
config.status: executing depfiles commands
make[2]: Entering directory `/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src'
cd . && /bin/sh /home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src/config/missing --run autoheader
/home/mabshoff/build-3.1.2.alpha2/sage-3.1.2.alpha1-iras-gcc-4.3.1/spkg/build/gd-2.0.35.p1/src/config/missing: line 46: autoheader: command not found
WARNING: `autoheader' is missing on your system.  You should only need it if
         you modified `acconfig.h' or `configure.ac'.  You might want
         to install the `Autoconf' and `GNU m4' packages.  Grab them
         from any GNU archive site.
rm -f stamp-h1
```


Cheers,

Michael


---

Comment by craigcitro created at 2008-08-29 09:05:24

Looks good. I don't have an Itanium to test on, but Michael assures me that it works on the machine where it had previously failed. I also looked at the only change in the spkg, which seems reasonable, and built it on my machine, which doesn't seem to cause any trouble.


---

Comment by mabshoff created at 2008-08-29 09:11:14

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-29 09:11:14

Resolution: fixed
