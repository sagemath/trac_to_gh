# Issue 8837: the symmetrica Sage library cython code doesn't build on OS X 10.4 PowerPC

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-01 19:12:40

Assignee: GeorgSWeber


```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/usr/include/malloc/ -I/home/wstein/screen/varro/sage-4.4.1.alpha3/local//include -I/home/wstein/screen/varro/sage-4.4.1.alpha3/local//include/csage -I/home/wstein/screen/varro/sage-4.4.1.alpha3/devel//sage/sage/ext -I/home/wstein/screen/varro/sage-4.4.1.alpha3/local/include/python2.6 -c sage/libs/symmetrica/symmetrica.c -o build/temp.macosx-10.4-ppc-2.6/sage/libs/symmetrica/symmetrica.o -w
gcc -L/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.4-ppc-2.6/sage/libs/symmetrica/symmetrica.o -L/home/wstein/screen/varro/sage-4.4.1.alpha3/local//lib -lcsage -lsymmetrica -lstdc++ -lntl -o build/lib.macosx-10.4-ppc-2.6/sage/libs/symmetrica/symmetrica.so
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _content
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _content
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nu.o) definition of _content in section (__TEXT,__text)
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _det
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _det
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nu.o) definition of _det in section (__TEXT,__text)
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _ggt
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _ggt
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nu.o) definition of _ggt in section (__TEXT,__text)
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _rank
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _rank
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(ma.o) definition of _rank in section (__TEXT,__text)
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _jacobi
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _jacobi
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nb.o) definition of _jacobi in section (__TEXT,__text)
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _kronecker
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _kronecker
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nb.o) definition of _kronecker in section (__TEXT,__text)
/usr/libexec/gcc/powerpc-apple-darwin8/4.0.1/ld: multiple definitions of symbol _print
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _print
/home/wstein/screen/varro/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(io.o) definition of _print in section (__TEXT,__text)
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.


real    12m5.293s
user    9m13.212s
sys     1m48.218s
make: *** [testlong] Error 1
varro:~/screen/varro wstein$ 
 }}}


---

Comment by GeorgSWeber created at 2010-05-02 07:19:49

Sage-4.4 did build fine under Mac OS X 10.4.11 on both MacPPC and MacIntel, but Sage-4.4.1.alpha3 fails to build on my MacIntel with the same error as William reported for a MacPPC machine above:


```

gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/Shared/sage/test/sage-4.4.1.alpha3/local//include -I/Users/Shared/sage/test/sage-4.4.1.alpha3/local//include/csage -I/Users/Shared/sage/test/sage-4.4.1.alpha3/devel//sage/sage/ext -I/Users/Shared/sage/test/sage-4.4.1.alpha3/local/include/python2.6 -c sage/libs/mpmath/utils.c -o build/temp.macosx-10.4-i386-2.6/sage/libs/mpmath/utils.o -w
gcc -L/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.4-i386-2.6/sage/libs/symmetrica/symmetrica.o -L/Users/Shared/sage/test/sage-4.4.1.alpha3/local//lib -lcsage -lsymmetrica -lstdc++ -lntl -o build/lib.macosx-10.4-i386-2.6/sage/libs/symmetrica/symmetrica.so
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _content
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _content
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nu.o) definition of _content in section (!__TEXT,!__text)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _det
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _det
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nu.o) definition of _det in section (!__TEXT,!__text)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _ggt
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _ggt
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nu.o) definition of _ggt in section (!__TEXT,!__text)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _rank
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _rank
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(ma.o) definition of _rank in section (!__TEXT,!__text)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _jacobi
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _jacobi
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nb.o) definition of _jacobi in section (!__TEXT,!__text)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _kronecker
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _kronecker
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(nb.o) definition of _kronecker in section (!__TEXT,!__text)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: multiple definitions of symbol _print
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libcsage.dylib(single module) definition of _print
/Users/Shared/sage/test/sage-4.4.1.alpha3/local/lib/libsymmetrica.a(io.o) definition of _print in section (!__TEXT,!__text)
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.

ERROR installing SAGE

real    21m47.890s
user    36m9.048s
sys     3m7.731s
sage: An error occurred while installing sage-4.4.1.alpha3

```



---

Comment by GeorgSWeber created at 2010-05-02 14:08:12

After a hint of William, the problem seems to narrow down on the update from pari-2.3.3.p8.spkg to pari-2.3.5.spkg by trac ticket #8453.

Comparing an install.log from before:

```
Configuring pari-2.3.3 (STABLE) 
Checking echo to see how to suppress newlines...
...using -n.
Looking for some tools first ...
...ld is /usr/bin/ld
...zcat is /usr/bin/zcat
...gzip is /usr/bin/gzip
...ranlib is /usr/bin/ranlib
...perl is /usr/bin/perl
...emacs is /usr/bin/emacs
GNU compiler version 4.0.1 (Apple Computer, Inc. build 5370)
Given the previous choices, sizeof(long) is 4 chars.
The internal word representation of a double is l[1], l[0].
==========================================================================
Building for architecture: i386 running darwin (ix86/GMP kernel) 32-bit version
==========================================================================
C compiler is          gcc -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fno-gcse-after-reload   -fno-common
Executable linker is   gcc  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fno-gcse-after-reload   
Dynamic Lib linker is  gcc  -dynamiclib  $(CFLAGS) $(DLCFLAGS) -Wl,-flat_namespace,-undefined,suppress
Looking in C lib for some symbols...
...Found exp2.
...Found log2.
...Found strftime.
...Found getrusage.
...Found sigaction.
...Found TIOCGWINSZ.
...Found getrlimit.
...Found stat.
...Found vsnprintf.
...Found dlopen.
Checking for optional libraries and headers...
...Found libgmp in /Users/Shared/sage/sage-4.4.rc0/local/lib
...Found gmp header in /Users/Shared/sage/sage-4.4.rc0/local/include
Using GNU MP, version 4.2.1
...Found libX11 in /usr/X11R6/lib
...Found X11 header files in /usr/X11R6/include/X11
Hi-Res Graphics: none
...Found libreadline in /Users/Shared/sage/sage-4.4.rc0/local/lib
...Found readline header in /Users/Shared/sage/sage-4.4.rc0/local/include/readline
...Found history header in /Users/Shared/sage/sage-4.4.rc0/local/include/readline
...Found libncurses in /usr/lib
...Library ncurses needed by readline
Using GNU readline, version 6.0
Installation prefix ? [/Users/Shared/sage/sage-4.4.rc0/local]
...for architecture-independent files (share-prefix) ? [/Users/Shared/sage/sage-4.4.rc0/local/share]
Installation directories for:
...executables (gp, gphelp) ? [/Users/Shared/sage/sage-4.4.rc0/local/bin]
...libraries (libpari) ? [/Users/Shared/sage/sage-4.4.rc0/local/lib]
...include files ? [/Users/Shared/sage/sage-4.4.rc0/local/include]
...manual pages ? [/Users/Shared/sage/sage-4.4.rc0/local/share/man/man1]
...emacs macros ? [/Users/Shared/sage/sage-4.4.rc0/local/share/emacs/site-lisp/pari]
...other system-dependant data ? [/Users/Shared/sage/sage-4.4.rc0/local/lib/pari]
...other system-independant data ? [/Users/Shared/sage/sage-4.4.rc0/local/share/pari]
Default is dynamic executable and shared library
==========================================================================
```

with an install log after this pari spkg update:

```
Configuring pari-2.3.5 (STABLE) 
Checking echo to see how to suppress newlines...
...using -n.
Looking for some tools first ...
...ld is /usr/bin/ld
...zcat is /usr/bin/zcat
...gzip is /usr/bin/gzip
...ranlib is /usr/bin/ranlib
...perl is /usr/bin/perl
...emacs is /usr/bin/emacs
GNU compiler version 4.0.1 (Apple Computer, Inc. build 5370)
Given the previous choices, sizeof(long) is 4 chars.
The internal word representation of a double is l[1], l[0].
==========================================================================
Building for architecture: i386 running darwin (ix86/GMP kernel) 32-bit version
==========================================================================
C compiler is          gcc -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fno-gcse-after-reload   -fno-common
Executable linker is   gcc  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer -fno-gcse-after-reload   
No Dynamic Lib
Looking in C lib for some symbols...
...Found exp2.
...Found log2.
...Found strftime.
...Found getrusage.
...Found sigaction.
...Found TIOCGWINSZ.
...Found getrlimit.
...Found stat.
...Found vsnprintf.
...Found dlopen.
Checking for optional libraries and headers...
...Found libgmp in /Users/Shared/sage/test/sage-4.4.1.alpha1/local/lib
...Found gmp header in /Users/Shared/sage/test/sage-4.4.1.alpha1/local/include
Using GNU MP, version 4.2.1
...Found libX11 in /usr/X11R6/lib
...Found X11 header files in /usr/X11R6/include/X11
Hi-Res Graphics: none
...Found libreadline in /Users/Shared/sage/test/sage-4.4.1.alpha1/local/lib
...Found readline header in /Users/Shared/sage/test/sage-4.4.1.alpha1/local/include/readline
...Found history header in /Users/Shared/sage/test/sage-4.4.1.alpha1/local/include/readline
...Found libncurses in /usr/lib
...Library ncurses needed by readline
Using GNU readline, version 6.0
Installation prefix ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local]
...for architecture-independent files (share-prefix) ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/share]
Installation directories for:
...executables (gp, gphelp) ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/bin]
...libraries (libpari) ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/lib]
...include files ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/include]
...manual pages ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/share/man/man1]
...emacs macros ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/share/emacs/site-lisp/pari]
...other system-dependant data ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/lib/pari]
...other system-independant data ? [/Users/Shared/sage/test/sage-4.4.1.alpha1/local/share/pari]
Default is static executable and archive library
==========================================================================
```

show a difference. Namely, pari seems to be built no longer dynamically, but statically instead. This certainly would be an explanation for the build error seen. I'm investigating further.


---

Comment by wjp created at 2010-05-02 14:39:08

Can you try replacing the line


```
darwin)  DLLD=; DLLDFLAGS='-flat_namespace -undefined suppress' ;;
```


by


```
darwin)  DLLD=gcc; DLLDFLAGS='-flat_namespace -undefined suppress' ;;
```


in `src/config/get_dlld`? (Note that that file is overwritten by `patches/get_dlld`, so you may have to change the version in `patches/`).

That reverts a change made in the spkg between 2.3.3.p8 and 2.3.5.


---

Comment by GeorgSWeber created at 2010-05-02 15:22:06

I've just uploaded:

http://sage.math.washington.edu/home/weberg/spkg/pari-2.3.5.p0.spkg

which does exactly that :-))
But beware, testing this is a bit time-consuming for me, so I did not test it myself yet ... this will take another two hours or more (other duties pending ...), but if you want to review it, go on (you'll need access to some Mac OS X 10.4 machine however, I fear)


---

Comment by GeorgSWeber created at 2010-05-02 17:00:38

Changing status from new to needs_review.


---

Comment by was created at 2010-05-02 17:12:07

Resolution: fixed
