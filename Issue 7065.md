# Issue 7065: lcalc fails - Sun Studio compiler does not accept code. (I'm not surprised)

Issue created by migration from https://trac.sagemath.org/ticket/7065

Original creator: drkirkby

Original creation time: 2009-09-29 12:33:30

Assignee: tbd

CC:  dimpase

lcalc fails with Sun Studio as below. 

Having looked at lcalc in the past, I am at all surprised. The code previously had tried to suppress assembler warnings with a GNU-specific flag. Once I removed that, and added -Wall with gcc, then gcc reported a huge number of warnings. The Sun compiler considers at least some errors, so lcalc does not build. 

I think the developer of lcalc should look over his code, as it clearly has many problems. 



```
lcalc-20080205.p3/src/src/Lriemannsiegel.cc
lcalc-20080205.p3/src/src/._.DS_Store
lcalc-20080205.p3/src/src/cmdline.c
lcalc-20080205.p3/src/src/Lglobals.cc
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Building a 32-bit version of lcalc
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
Using CC=/opt/xxxsunstudio12.1/bin/cc
Using CXX=/opt/xxxsunstudio12.1/bin/CC
Using FC=
Using F77=
Using SAGE_FORTRAN=/opt/xxxsunstudio12.1/bin/f95
Using SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.1-sun-linker/lib/libgfortran.so
The following environment variables will be exported
Using CFLAGS= -O2  -g
Using CXXFLAGS= -O2  -g
Using FCFLAGS= -O2  -g
Using F77FLAGS= -O2  -g
Using CPPFLAGS= -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include
Using LDFLAGS= -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib
Using ABI=
configure scripts and/or makefiles might override these later

Using LCALC_LIBS=-lpari -lmpfr -lgmpxx -lgmp -liberty
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/lcalc-20080205.p3/src/src'
/opt/xxxsunstudio12.1/bin/CC  -O2  -g  -DINCLUDE_PARI   \
      -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include/pari -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include\
      -I ../include/ -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib \
      cmdline.c \
      Lcommandline.cc Lcommandline_elliptic.cc Lcommandline_globals.cc \
      Lcommandline_misc.cc Lcommandline_numbertheory.cc \
      Lcommandline_twist.cc Lcommandline_values_zeros.cc \
      Lgamma.cc Lglobals.cc Lmisc.cc Lriemannsiegel.cc \
            -o lcalc -lpari -lmpfr -lgmpxx -lgmp -liberty
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
"../include/Lcomplex.h", line 48: Error: Could not open include file<bits/c++config.h>.
"../include/Lcomplex.h", line 767: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 768: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 770: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 778: Error: __real__ is not defined.
"../include/Lcomplex.h", line 778: Error: Badly formed expression.
"../include/Lcomplex.h", line 782: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 782: Error: Badly formed expression.
"../include/Lcomplex.h", line 787: Error: __real__ is not defined.
"../include/Lcomplex.h", line 787: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 788: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 788: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 788: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 794: Error: __real__ is not defined.
"../include/Lcomplex.h", line 794: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 795: Error: __imag__ is not defined.
"../include/Lcomplex.h", line 795: Error: Multiple declaration for _M_value.
"../include/Lcomplex.h", line 795: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: __real__ is not defined.
"../include/Lcomplex.h", line 802: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 802: Error: "," expected instead of "+=".
"../include/Lcomplex.h", line 809: Error: __real__ is not defined.
"../include/Lcomplex.h", line 809: Warning: _M_value hides std::complex<float>::_M_value.
"../include/Lcomplex.h", line 809: Error: "," expected instead of "-=".
"../include/Lcomplex.h", line 913: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Use ";" to terminate declarations.
"../include/Lcomplex.h", line 914: Error: Type name expected instead of "_ComplexT".
"../include/Lcomplex.h", line 916: Error: _ComplexT is not defined.
"../include/Lcomplex.h", line 924: Error: __real__ is not defined.
"../include/Lcomplex.h", line 924: Error: Badly formed expression.
Compilation aborted, too many Error messages.
cmdline.c:
Lcommandline.cc:
Lcommandline_elliptic.cc:
Lcommandline_globals.cc:
Lcommandline_misc.cc:
Lcommandline_numbertheory.cc:
Lcommandline_twist.cc:
Lcommandline_values_zeros.cc:
Lgamma.cc:
Lglobals.cc:
Lmisc.cc:
Lriemannsiegel.cc:
make[2]: *** [lcalc] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/lcalc-20080205.p3/src/src'
Now copying over lcalc binary
cp: cannot access lcalc

real    0m11.295s
user    0m8.269s
sys     0m1.135s
sage: An error occurred while installing lcalc-20080205.p3

```




---

Comment by chapoton created at 2018-03-03 08:39:23

Changing keywords from "" to "lcalc".


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mjo created at 2020-07-12 20:24:16

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2020-07-12 20:24:16

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
