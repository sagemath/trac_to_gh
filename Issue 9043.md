# Issue 9043: lcalc failing to build on OpenSolaris x64.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-25 02:11:14

Assignee: drkirkby

CC:  rishi jsp

# Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_134 X86
 * Sage 4.4.2
 * gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby`@`hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv. 

## How the Sage build was attempted
 * 64-bit build. SAGE64 was set to "yes"
 * #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
 * #9009 update mercurial spkg to build 64-bit.
 * #7982 update sage_fortran so it can build 64-bit binaries.
 * Run 'make -k' so the build process continued even though there were some failures. 

## The problem with lcalc

The C++ compiler g++ is being invoked with the option -m64 to build 64-bit objects (as it should be). g++ is then used as a linker and *may* need the -m64 flag again. There is certainly a problem with 32-bit and 64-bit objects being mixed up, as ''wrong ELF class' always indicates such a problem on Solaris or OpenSolaris. 

lcalc probably needs LDFLAGS to include -m64, though I've not checked this. It may or may not already have it. 


```
g++  -O3  -m64  -g  -Wall  -O3     -ffast-math -fPIC  -I../include -c Lriemannsiegel_blfi.cc
In file included from /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../../../include/c++/4.4.4/backward/strstream:47,
                 from ../include/L.h:34,
                 from Lriemannsiegel_blfi.cc:16:
/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../../../include/c++/4.4.4/backward/backward_warning.h:28:2: warning: #warning This file includes at least one deprecated or antiquated header which may be removed without further notice at a future date. Please use a non-deprecated interface with equivalent functionality instead. For a listing of replacement headers and interfaces, consult the file backward_warning.h. To disable this warning use -Wno-deprecated.
In file included from ../include/L.h:537,
                 from Lriemannsiegel_blfi.cc:16:
../include/Lvalue.h:187: warning: ignoring #pragma omp parallel
../include/Lvalue.h:324: warning: ignoring #pragma omp parallel
../include/Lvalue.h:329: warning: ignoring #pragma omp parallel
Lriemannsiegel_blfi.cc: In function ‘Complex blfi_inter(Double, Double, int, int, int, int&)’:
Lriemannsiegel_blfi.cc:388: warning: unused variable ‘temp10’
Lriemannsiegel_blfi.cc: In function ‘Complex my_zeta(Double, int&)’:
Lriemannsiegel_blfi.cc:913: warning: unused variable ‘denom’
Lriemannsiegel_blfi.cc:913: warning: unused variable ‘temp0’
g++  -O3  -m64  -g  -Wall  -O3     -ffast-math -fPIC  -I../include -c Ldokchitser.cc
In file included from /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../../../include/c++/4.4.4/backward/strstream:47,
                 from ../include/L.h:34,
                 from Ldokchitser.cc:1:
/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../../../include/c++/4.4.4/backward/backward_warning.h:28:2: warning: #warning This file includes at least one deprecated or antiquated header which may be removed without further notice at a future date. Please use a non-deprecated interface with equivalent functionality instead. For a listing of replacement headers and interfaces, consult the file backward_warning.h. To disable this warning use -Wno-deprecated.
In file included from ../include/L.h:537,
                 from Ldokchitser.cc:1:
../include/Lvalue.h:187: warning: ignoring #pragma omp parallel
../include/Lvalue.h:324: warning: ignoring #pragma omp parallel
../include/Lvalue.h:329: warning: ignoring #pragma omp parallel
g++ -shared  -o libLfunction.so Lglobals.o Lgamma.o Lriemannsiegel.o Lriemannsiegel_blfi.o Ldokchitser.o
ld: fatal: file Lglobals.o: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to libLfunction.so
collect2: ld returned 1 exit status
make[3]: *** [libLfunction.so] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23/src/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23/src/src'
Now copying over lcalc binary
cp: cannot access lcalc

real    0m3.200s
user    0m2.855s
sys     0m0.246s
sage: An error occurred while installing lcalc-20100428-1.23
```


## Other problems stopping Sage build on OpenSolaris
See #9026 for a list of issues observed on OpenSolaris x64. Some will affect a 64-bit build on other Solaris platforms.


---

Comment by rishi created at 2010-05-25 14:18:38

I do not have access to opensolaris machine. I am busy with other things also. Can you make appropriate changes to Makefile.sage in patches directory and see if things work.


---

Comment by drkirkby created at 2010-05-28 21:14:40

## The cause  and solution
The problem was that CXXFLAGS was not being imported properly into patches/Makefile.sage. Although CXX was set correctly in spkg-install, the make file did not honor this properly. 

This was simple to fix, by adding 'CXXFLAG64' to the list of variables imported by patches/Makefile.sage. During a 64-bit build with "SAGE64=yes", this is set to -m64 (by default). 

An updated package can be found at

http://boxen.math.washington.edu/home/kirkby/patches/lcalc-20100428-1.23.p0.spkg

Although there are lots of warnings, these are in the original code, so are not a result of the change makefile. 

## Testing of updated 'lcalc' on OpenSolaris x64
Here's is part of the output from the Sun Ultra 27, which showed the problem when building 'lcalc' as 64-bit. As you can see, it now builds. A check was made that all files installed are 64-bit, and this is indeed the case. 


```
cmdline.c:96: warning: deprecated conversion from string constant to ‘char*’
g++  -O3  -m64  -Wall  -O3     -ffast-math -fPIC  -I../include Lglobals.o Lgamma.o Lriemannsiegel.o Lriemannsiegel_blfi.o Ldokchitser.o Lcommandline_globals.o Lcommandline_misc.o Lcommandline_numbertheory.o Lcommandline_values_zeros.o Lcommandline_elliptic.o Lcommandline_twist.o Lcommandline.o cmdline.o -L/export/home/drkirkby/sage-4.4.2/local/lib  -lpari -lmpir -o lcalc 
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23.p0/src/src'
make examples
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23.p0/src/src'
g++  -O3  -m64  -Wall  -O3     -ffast-math -fPIC  -I../include example_programs/example.cc libLfunction.so -o example_programs/example 
In file included from /usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../../../include/c++/4.4.4/backward/strstream:47,
                 from ../include/L.h:34,
                 from example_programs/example.cc:2:
/usr/local/gcc-4.4.4/lib/gcc/i386-pc-solaris2.11/4.4.4/../../../../include/c++/4.4.4/backward/backward_warning.h:28:2: warning: #warning This file includes at least one deprecated or antiquated header which may be removed without further notice at a future date. Please use a non-deprecated interface with equivalent functionality instead. For a listing of replacement headers and interfaces, consult the file backward_warning.h. To disable this warning use -Wno-deprecated.
In file included from ../include/L.h:537,
                 from example_programs/example.cc:2:
../include/Lvalue.h:187: warning: ignoring #pragma omp parallel
../include/Lvalue.h:324: warning: ignoring #pragma omp parallel
../include/Lvalue.h:329: warning: ignoring #pragma omp parallel
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = int]’:
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = int]’
example_programs/example.cc:88:   instantiated from here
../include/Lvalue.h:502: warning: unused variable ‘t_0’
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]’:
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]’
example_programs/example.cc:90:   instantiated from here
../include/Lvalue.h:502: warning: unused variable ‘t_0’
In file included from ../include/L.h:537,
                 from example_programs/example.cc:2:
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::find_delta(Complex, Double) [with ttype = int]’:
../include/Lvalue.h:517:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = int]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = int]’
example_programs/example.cc:88:   instantiated from here
../include/Lvalue.h:37: warning: unused variable ‘f2’
In file included from ../include/L.h:42,
                 from example_programs/example.cc:2:
../include/Lgamma.h: In function ‘Complex gamma_sum(Complex, int, ttype*, int, Double, Complex, Double, Long, Complex, const char*) [with ttype = int]’:
../include/Lvalue.h:526:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = int]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = int]’
example_programs/example.cc:88:   instantiated from here
../include/Lgamma.h:622: warning: unused variable ‘y’
../include/Lgamma.h:622: warning: unused variable ‘y2’
../include/Lgamma.h:622: warning: unused variable ‘y3’
In file included from ../include/L.h:537,
                 from example_programs/example.cc:2:
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::find_delta(Complex, Double) [with ttype = std::complex<double>]’:
../include/Lvalue.h:517:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]’
example_programs/example.cc:90:   instantiated from here
../include/Lvalue.h:37: warning: unused variable ‘f2’
In file included from ../include/L.h:42,
                 from example_programs/example.cc:2:
../include/Lgamma.h: In function ‘Complex gamma_sum(Complex, int, ttype*, int, Double, Complex, Double, Long, Complex, const char*) [with ttype = std::complex<double>]’:
../include/Lvalue.h:526:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]’
example_programs/example.cc:90:   instantiated from here
../include/Lgamma.h:622: warning: unused variable ‘y’
../include/Lgamma.h:622: warning: unused variable ‘y2’
../include/Lgamma.h:622: warning: unused variable ‘y3’
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_Riemann_sum(Complex, const char*) [with ttype = int]’:
../include/Lvalue.h:489: warning: control reaches end of non-void function
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_Riemann_sum(Complex, const char*) [with ttype = std::complex<double>]’:
../include/Lvalue.h:489: warning: control reaches end of non-void function
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23.p0/src/src'
Now copying over lcalc binary
Now copying over lcalc library

real	0m23.105s
user	0m22.026s
sys	0m0.905s
Successfully installed lcalc-20100428-1.23.p0
```


## Building the updated lcalc on OS X
The updated lcalc package was built on OS X.  


```
Now copying over lcalc binary
Now copying over lcalc library

real	0m40.999s
user	0m32.921s
sys	0m2.457s
Successfully installed lcalc-20100428-1.23.p0
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing lcalc-20100428-1.23.p0.spkg
[kirkby`@`bsd sage-4.4.2]$ uname -a
Darwin bsd.local 10.3.0 Darwin Kernel Version 10.3.0: Fri Feb 26 11:58:09 PST 2010; root:xnu-1504.3.12~1/RELEASE_I386 i386 i386 MacPro1,1 Darwin
```


## Building the updated lcalc on Linux


```
g++  -O3  -Wall  -O3     -ffast-math -fPIC  -I../include Lglobals.o Lgamma.o Lriemannsiegel.o Lriemannsiegel_blfi.o Ldokchitser.o Lcommandline_globals.o Lcommandline_misc.o Lcommandline_numbertheory.o Lcommandline_values_zeros.o Lcommandline_elliptic.o Lcommandline_twist.o Lcommandline.o cmdline.o -L/home/kirkby/sage-4.4.2/local/lib  -lpari -lmpir -o lcalc 
make[1]: Leaving directory `/home/kirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23.p0/src/src'
make examples
make[1]: Entering directory `/home/kirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23.p0/src/src'
g++  -O3  -Wall  -O3     -ffast-math -fPIC  -I../include example_programs/example.cc libLfunction.so -o example_programs/example 
In file included from /usr/include/c++/4.2/backward/strstream:51,
                 from ../include/L.h:34,
                 from example_programs/example.cc:2:
/usr/include/c++/4.2/backward/backward_warning.h:32:2: warning: #warning This file includes at least one deprecated or antiquated header. Please consider using one of the 32 headers found in section 17.4.1.2 of the C++ standard. Examples include substituting the <X> header for the <X.h> header for C++ includes, or <iostream> instead of the deprecated header <iostream.h>. To disable this warning use -Wno-deprecated.
In file included from ../include/L.h:537,
                 from example_programs/example.cc:2:
../include/Lvalue.h:187: warning: ignoring #pragma omp parallel
../include/Lvalue.h:324: warning: ignoring #pragma omp parallel
../include/Lvalue.h:329: warning: ignoring #pragma omp parallel
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = int]’:
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = int]’
example_programs/example.cc:88:   instantiated from here
../include/Lvalue.h:502: warning: unused variable ‘t_0’
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]’:
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]’
example_programs/example.cc:90:   instantiated from here
../include/Lvalue.h:502: warning: unused variable ‘t_0’
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::find_delta(Complex, Double) [with ttype = int]’:
../include/Lvalue.h:517:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = int]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = int]’
example_programs/example.cc:88:   instantiated from here
../include/Lvalue.h:37: warning: unused variable ‘f2’
../include/Lgamma.h: In function ‘Complex gamma_sum(Complex, int, ttype*, int, Double, Complex, Double, Long, Complex, const char*) [with ttype = int]’:
../include/Lvalue.h:526:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = int]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = int]’
example_programs/example.cc:88:   instantiated from here
../include/Lgamma.h:622: warning: unused variable ‘y’
../include/Lgamma.h:622: warning: unused variable ‘y2’
../include/Lgamma.h:622: warning: unused variable ‘y3’
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::find_delta(Complex, Double) [with ttype = std::complex<double>]’:
../include/Lvalue.h:517:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]’
example_programs/example.cc:90:   instantiated from here
../include/Lvalue.h:37: warning: unused variable ‘f2’
../include/Lgamma.h: In function ‘Complex gamma_sum(Complex, int, ttype*, int, Double, Complex, Double, Long, Complex, const char*) [with ttype = std::complex<double>]’:
../include/Lvalue.h:526:   instantiated from ‘Complex L_function<ttype>::value_via_gamma_sum(Complex, const char*) [with ttype = std::complex<double>]’
../include/Lvalue.h:627:   instantiated from ‘Complex L_function<ttype>::value(Complex, int, const char*) [with ttype = std::complex<double>]’
example_programs/example.cc:90:   instantiated from here
../include/Lgamma.h:622: warning: unused variable ‘y’
../include/Lgamma.h:622: warning: unused variable ‘y2’
../include/Lgamma.h:622: warning: unused variable ‘y3’
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_Riemann_sum(Complex, const char*) [with ttype = int]’:
../include/Lvalue.h:487: warning: control reaches end of non-void function
../include/Lvalue.h: In member function ‘Complex L_function<ttype>::value_via_Riemann_sum(Complex, const char*) [with ttype = std::complex<double>]’:
../include/Lvalue.h:487: warning: control reaches end of non-void function
make[1]: Leaving directory `/home/kirkby/sage-4.4.2/spkg/build/lcalc-20100428-1.23.p0/src/src'
Now copying over lcalc binary
Now copying over lcalc library

real	0m31.703s
user	0m28.860s
sys	0m2.480s
Successfully installed lcalc-20100428-1.23.p0
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing lcalc-20100428-1.23.p0.spkg
kirkby`@`sage:~/sage-4.4.2$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux

```



---

Comment by drkirkby created at 2010-05-28 21:15:40

Mercurial patch to allow a 64-bit build of 'lcalc' if SAGE64=yes


---

Attachment

Replying to [comment:1 rishi]:
> I do not have access to opensolaris machine. 

You can install it as a virtual machine on Windows or Linux if you wanted. 

> I am busy with other things also. 

I understand.

> Can you make appropriate changes to Makefile.sage in patches directory and see if things work.

Sure, I've done that. The package now builds 64-bit on OpenSolaris when SAGE64 is set to yes. I've also tested this on Linux (sage.math) and OS X (bsd.math). It builds fine on all platforms. 

Dave


---

Comment by drkirkby created at 2010-05-28 21:24:07

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-28 21:24:07

I forgot to say, there were a couple of other changes I did at the same time. 

1) Removed the following 4 binary files from the source distribution. 


```
   ./src/src/.Makefile.old.swp
   ./src/src/.Lcommandline.ggo.swp
   ./src/include/.Lvalue.h.swp
   ./src/include/.Lexplicit_formula.h.swp

```


2) Test for SAGE64 being "yes" and not "yes" or "1" as before, since other code in Sage will only allow SAGE64 to be "yes" or "no". The number "1" is not a legal value, so there was no point checking for it.


---

Comment by jsp created at 2010-06-12 16:23:32

looks good to me. This deserves a positive review.

Jaap


---

Comment by jsp created at 2010-06-12 16:23:32

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:51:39

Resolution: fixed
