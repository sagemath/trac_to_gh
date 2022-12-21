# Issue 7782: cliquer build fails on HP-UX

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-12-29 06:22:11

Assignee: drkirkby

CC:  ncohen

cliquer is failing on HP-UX 11.11 on a HP C3600 workstation. The spkg-install has code which applies different flags to build the shared library on different platforms, but does not have any for HP-UX. The spkg-install exits with a message saying: 

*Cannot determine your platform or it is not supported... exiting*

This needs to be changed. Once the files testcc.sh and testcxx.sh at #7505 are included in Sage, doing this will be a lot easier. 


```
cliquer-1.2.p2/src/cliquerconf.h
cliquer-1.2.p2/src/testcase-large-w-60-64-mxml.h
cliquer-1.2.p2/src/testcase-large.b
cliquer-1.2.p2/src/set.h
cliquer-1.2.p2/src/graph.h
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.3.3 (GCC) 
****************************************************
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
No Fortran compiler has been defined. This is not normally a problem.
Using CC=gcc
Using CXX=g++
Using FC=
Using F77=
Using SAGE_FORTRAN=
Using SAGE_FORTRAN_LIB=
The following environment variables will be exported
Using CFLAGS= -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC 
Using CXXFLAGS= -O2  -g  -Wall 
Using FCFLAGS= -O2  -g  -Wall 
Using F77FLAGS= -O2  -g  -Wall 
Using CPPFLAGS= -I/home/drkirkby/sage-4.3/local/include 
Using LDFLAGS= -L/home/drkirkby/sage-4.3/local/lib 
Using ABI=
configure scripts and/or makefiles might override these later
 
Cannot determine your platform or it is not supported... exiting

real	0m0.076s
user	0m0.050s
sys	0m0.020s
sage: An error occurred while installing cliquer-1.2.p2
```



---

Comment by ncohen created at 2009-12-29 08:33:28

cc me


---

Comment by drkirkby created at 2009-12-29 13:07:08

There appears to be around 5 issues when building with gcc, all of which look solvable without too much difficulty. I've not got this to build, but believe it will not be rocket science to do so with gcc. 

If anyone wants an account on an HP-UX machine to fix these, I'll give you one, as I personally own an HP C3600. Otherwise, I'll sort the package out at some time. While doing so, it is wise to consider other platforms at the same time. The issues I'm aware of are:

 *  spkg-install calls 'uname' then tests for Linux, Darwin (OS X) and SunOS (Solaris), but exits with anything else. We should at last consider the possibility of other Unix platforms. The most likely ones for which a port of Sage could take place would be Cygwin (some are working on that), HP-UX and AIX. Cygwin is actively maintain (last release is December 2009). Both HP-UX and AIX are current operating systems, actively maintained. Less likely, but worth considering are Tru64 and IRIX. Tru64 is still maintained by HP, but HP are trying to move customers to HP-UX. Rather than exit on these rarer platforms, we should just assume the same flags as gcc and issue a warning. The variable SAGE_PORT needs to be exported to build on any of these rarer platforms, so anyone building will be aware they might need to fix things. 
 * spkg-install has code which checks for the Sun compiler and otherwise assumes GCC. On other platforms like AIX, HP-UX, IRIX and Tru64, the possibility exists of the compiler being something other than gcc or Sun Studio. #7505 (currently awaiting review), is a very easy and robust means of determining the compiler. It actually checks what the compiler defines, and totally ignores the operating system it is running on. So even if Sun Studio is run on Linux, it works (Sun Studio exists for Linux). 
 * The code:

```
# Enable long options for cl (eg. "cl --help"), comment out to disable.
# Requires getopt_long(3)  (a GNU extension)
LONGOPTS = -DENABLE_LONG_OPTIONS
```

in the Makefile is causing a failure, as HP-UX does not have the GNU extension. François Bissey has said cliquer is only used as a library. In which case, that LONGOPT can simply be commented out. 
 * The extension for shared libraries on HP-UX is .sl, not the more common .so. One way to possibly handle that would be to set a variable like SHARED_LIB_EXTENSION in spkg-install, then use that in the Makefile. 

I've personally been guilty of assuming operating systems other than OS X, Linux and Solaris simply do not exist. In practice, in many cases things simply work on HP-UX and I believe would work on other platforms too if gcc is used. 

Using native compilers on other platforms would no doubt present more problems, but building Sage on HP-UX with gcc does not look to be very difficult. 

*Portability notes*

It is safer to use $UNAME rather than 'uname' as the output on Cywin from uname is a bit complex. Sage's sage-env has this:

```
UNAME=`uname`
if [ `uname | sed -e 's/WIN.\+/WIN/'` = "CYGWIN" ]; then
    UNAME="CYGWIN"
fi
```

so if $UNAME is used, it will not break on Cygwin. The output of the 'uname' command are on rarer platforms are:

 * AIX:  AIX
 * HP-UX: HP-UX
 * Tru64: Tru64
 * Cywgin: A bit complex, but $UNAME is set to CYGWIN and so can be used on *any* platform
 * IRIX: Can be either IRIX or IRIX64, the latter obviously for a 64-bit build.


---

Comment by drkirkby created at 2010-01-11 04:37:15

I also found the cliquer build fails on Solaris 8, for exactly the same reasons as on HP-UX. 


```
bash-2.03$ uname -a
SunOS solaris8 5.8 Generic_108528-11 sun4u sparc SUNW,Sun-Blade-1000
bash-2.03$ cat /etc/release
                       Solaris 8 10/01 s28s_u6wos_08a SPARC
           Copyright 2001 Sun Microsystems, Inc.  All Rights Reserved.
                           Assembled 12 September 2001
```


As discussed above, the spkg-install can be simplified a lot, but it will be easier to wait until the sage-env #7818 is fully merged into 4.3.1 (it has positive review). As such, the only significant change here, which permits the build on Solaris 8 (but not HP-UX) is just simply commenting out one line in the Makefile. The actual changes are

 * Commented out the long options in the Makefile
 * Change the name of the patch directory with the Makefile from 'patch' to 'patches' to be consistent with other packages. 
 * Added patches/Makefile to the Mercurial as it was not there before. 
 * I changed the title of the ticket, to reflect the fact that the problem also exists on Solaris 8, but is fixed there, but not on HP-UX. 

An updated cliquer-1.2.p3.spkg can be found here. 
http://boxen.math.washington.edu/home/kirkby/portability/cliquer-1.2.p3/cliquer-1.2.p3.spkg

Some other files which might be relevent can be found in the directory
http://boxen.math.washington.edu/home/kirkby/portability/cliquer-1.2.p3/

Reviewing this should be easy. I appologise if the information in the repository is not exactly as it should be, but the Makefile was not there before, so I can't do a diff against it. I just added it to the repository.

Dave


---

Comment by drkirkby created at 2010-01-11 04:37:15

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-07-27 20:42:51

Please fill in your real name as Author.


---

Comment by jdemeyer created at 2013-02-05 19:38:12

Closing since Cliquer has been updated and I have no idea whether or not it builds on HP-UX...


---

Comment by jdemeyer created at 2013-02-05 19:38:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-08 13:22:59

Resolution: invalid
