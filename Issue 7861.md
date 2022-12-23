# Issue 7861: pynac-0.1.10 not building with Open Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/7861

Original creator: drkirkby

Original creation time: 2010-01-06 23:05:53

Assignee: drkirkby

CC:  jsp robertwb burchin was jhpalmieri

I don't know C++, so are not really going to be a lot of help sorting this out. 

 == Build environment ==
 * Sun Ultra 27 (Intel Xeon, *not* SPARC)
 * Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. 

 == Notes ==
I'll decide whether to report this upstream once I get some feedback from others what it might be. It should also be noted that Sun's compiler on SPARC dislikes some of pynac's code too (#7029). 

 == The problem ==
The error messages are below. 


```
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/include-fixed/sys/feature_tests.h:296:1: warning: this is the location of the previous definition
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from ex.h:31,
                 from container.h:33,
                 from exprseq.h:28,
                 from ncmul.h:26,
                 from ncmul.cpp:27:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1028:1: warning: "_XOPEN_SOURCE" redefined
<built-in>: warning: this is the location of the previous definition
mv -f .deps/ncmul.Tpo .deps/ncmul.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I..   -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6  -m64 -MT normal.lo -MD -MP -MF .deps/normal.Tpo -c -o normal.lo normal.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6 -m64 -MT normal.lo -MD -MP -MF .deps/normal.Tpo -c normal.cpp  -fPIC -DPIC -o .libs/normal.o
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from ex.h:31,
                 from container.h:33,
                 from lst.h:28,
                 from normal.h:29,
                 from normal.cpp:29:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1019:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/include/iso/stdlib_iso.h:48,
                 from /usr/include/stdlib.h:35,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cstdlib:73,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/stl_algo.h:65,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/algorithm:67,
                 from normal.cpp:26:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/include-fixed/sys/feature_tests.h:296:1: warning: this is the location of the previous definition
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from ex.h:31,
                 from container.h:33,
                 from lst.h:28,
                 from normal.h:29,
                 from normal.cpp:29:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1028:1: warning: "_XOPEN_SOURCE" redefined
<built-in>: warning: this is the location of the previous definition
mv -f .deps/normal.Tpo .deps/normal.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I..   -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6  -m64 -MT numeric.lo -MD -MP -MF .deps/numeric.Tpo -c -o numeric.lo numeric.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6 -m64 -MT numeric.lo -MD -MP -MF .deps/numeric.Tpo -c numeric.cpp  -fPIC -DPIC -o .libs/numeric.o
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from numeric.h:48,
                 from numeric.cpp:63:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1019:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/include-fixed/wchar.h:41,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:52,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/postypes.h:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/string:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/stdexcept:44,
                 from numeric.cpp:54:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/include-fixed/sys/feature_tests.h:296:1: warning: this is the location of the previous definition
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from numeric.h:48,
                 from numeric.cpp:63:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1028:1: warning: "_XOPEN_SOURCE" redefined
<built-in>: warning: this is the location of the previous definition
numeric.cpp: In function ‘PyObject* Integer(const long int&)’:
numeric.cpp:259: warning: deprecated conversion from string constant to ‘char*’
numeric.cpp: In function ‘void GiNaC::coerce(GiNaC::Number_T&, GiNaC::Number_T&, const GiNaC::Number_T&, const GiNaC::Number_T&)’:
numeric.cpp:349: warning: deprecated conversion from string constant to ‘char*’
mv -f .deps/numeric.Tpo .deps/numeric.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I..   -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6  -m64 -MT operators.lo -MD -MP -MF .deps/operators.Tpo -c -o operators.lo operators.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6 -m64 -MT operators.lo -MD -MP -MF .deps/operators.Tpo -c operators.cpp  -fPIC -DPIC -o .libs/operators.o
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from numeric.h:48,
                 from operators.cpp:27:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1019:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/include-fixed/wchar.h:41,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:52,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/postypes.h:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/iosfwd:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/ios:44,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/ostream:45,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/iostream:45,
                 from operators.cpp:23:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/include-fixed/sys/feature_tests.h:296:1: warning: this is the location of the previous definition
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from basic.h:38,
                 from numeric.h:48,
                 from operators.cpp:27:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1028:1: warning: "_XOPEN_SOURCE" redefined
<built-in>: warning: this is the location of the previous definition
mv -f .deps/operators.Tpo .deps/operators.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I..   -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6  -m64 -MT power.lo -MD -MP -MF .deps/power.Tpo -c -o power.lo power.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6 -m64 -MT power.lo -MD -MP -MF .deps/power.Tpo -c power.cpp  -fPIC -DPIC -o .libs/power.o
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from power.cpp:25:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1028:1: warning: "_XOPEN_SOURCE" redefined
<built-in>: warning: this is the location of the previous definition
In file included from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/postypes.h:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/iosfwd:47,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/ios:44,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/ostream:45,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/iostream:45,
                 from power.cpp:33:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:148: error: ‘::btowc’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:153: error: ‘::fwide’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:154: error: ‘::fwprintf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:155: error: ‘::fwscanf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:158: error: ‘::mbrlen’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:159: error: ‘::mbrtowc’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:160: error: ‘::mbsinit’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:161: error: ‘::mbsrtowcs’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:164: error: ‘::swprintf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:165: error: ‘::swscanf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:167: error: ‘::vfwprintf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:171: error: ‘::vswprintf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:175: error: ‘::vwprintf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:179: error: ‘::wcrtomb’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:190: error: ‘::wcsrtombs’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:200: error: ‘::wctob’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:201: error: ‘::wmemcmp’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:202: error: ‘::wmemcpy’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:203: error: ‘::wmemmove’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:204: error: ‘::wmemset’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:205: error: ‘::wprintf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:206: error: ‘::wscanf’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:226: error: ‘::wcsstr’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar: In function ‘wchar_t* std::wcsstr(wchar_t*, const wchar_t*)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:230: error: invalid conversion from ‘const wchar_t*’ to ‘wchar_t*’
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:230: error:   initializing argument 1 of ‘wchar_t* std::wcsstr(wchar_t*, const wchar_t*)’
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar: At global scope:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:232: error: ‘::wmemchr’ has not been declared
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar: In function ‘wchar_t* std::wmemchr(wchar_t*, wchar_t, size_t)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:236: error: invalid conversion from ‘const wchar_t*’ to ‘wchar_t*’
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/cwchar:236: error:   initializing argument 1 of ‘wchar_t* std::wmemchr(wchar_t*, wchar_t, size_t)’
In file included from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/ios:46,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/ostream:45,
                 from /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/iostream:45,
                 from power.cpp:33:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h: In static member function ‘static int std::char_traits<wchar_t>::compare(const wchar_t*, const wchar_t*, size_t)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:328: error: ‘wmemcmp’ was not declared in this scope
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h: In static member function ‘static const wchar_t* std::char_traits<wchar_t>::find(const wchar_t*, size_t, const wchar_t&)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:336: error: invalid conversion from ‘const wchar_t*’ to ‘wchar_t*’
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:336: error:   initializing argument 1 of ‘wchar_t* std::wmemchr(wchar_t*, wchar_t, size_t)’
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h: In static member function ‘static wchar_t* std::char_traits<wchar_t>::move(wchar_t*, const wchar_t*, size_t)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:340: error: ‘wmemmove’ was not declared in this scope
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h: In static member function ‘static wchar_t* std::char_traits<wchar_t>::copy(wchar_t*, const wchar_t*, size_t)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:344: error: ‘wmemcpy’ was not declared in this scope
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h: In static member function ‘static wchar_t* std::char_traits<wchar_t>::assign(wchar_t*, size_t, wchar_t)’:
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../../include/c++/4.3.4/bits/char_traits.h:348: error: ‘wmemset’ was not declared in this scope
make[4]: *** [power.lo] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/pynac-0.1.10/src/ginac'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/pynac-0.1.10/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/pynac-0.1.10/src'
Error building pynac.

real	0m27.328s
user	0m22.162s
sys	0m3.783s
sage: An error occurred while installing pynac-0.1.10
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /export/home/drkirkby/sage-4.3.1.alpha1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/pynac-0.1.10 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/pynac-0.1.10' && '/export/home/drkirkby/sage-4.3.1.alpha1/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/pynac-0.1.10] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg'
```



---

Comment by drkirkby created at 2010-06-05 21:33:58

I've updated the title and description completely, to reflect the fact that the ticket was originally opened against a much earlier version of pynac, for which there was a completely different error message.


---

Comment by drkirkby created at 2010-06-28 04:56:52

I've found a workaround for pynac failing to install on OpenSolaris, though it is not ideal. The workaround is only performed on Solaris or OpenSolaris and only for 64-bit builds. 

I've added the directory containing GCC's 64-bit libraries at the front of the linker search path, which for my particular installation is 

/usr/local/gcc-4.4.4-multilib/lib/amd64

On a SPARC system, the 'amd64' would be replaced by 'sparcv9'. The exact directory is determined using 'isainfo -n' and the path to gcc. 

On a SPARC

```
drkirkby@kestrel:~$ isainfo -n
sparcv9
```

On a Xeon

```
drkirkby@hawk:~$ isainfo -n
amd64
```


Libtool, which is used by pynac should take care of all this - it should not be necessary for me to do it. But this works, though it would break if the directories containing the binaries (gcc, g++ etc) did not share the same parent as those containing the libraries. Fortunately, it is rare for people to install gcc that way. 


```
pynac-0.2.0.p4/src/pynac.pc.in
pynac-0.2.0.p4/src/COPYING
pynac-0.2.0.p4/src/aclocal.m4
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: /export/home/drkirkby/gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4-multilib --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.4.4-multilib --with-mpfr=/usr/local/gcc-4.4.4-multilib --disable-nls --enable-checking=release --enable-werror=no --enable-multilib --with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
Building a 64-bit version of pynac
64-bit libraries for GCC are assumed to be in /usr/local/gcc-4.4.4-multilib/lib/amd64
so compiler flags -R/usr/local/gcc-4.4.4-multilib/lib/amd64 and -L/usr/local/gcc-4.4.4-multilib/lib/amd64 will be added
WARNING - these assumptions may be incorrect if GCC was
configured with options like --bindir=DIR or --libdir=DIR
but will be fine for most installations of gcc
Long-term, a better solution needs to be found
Starting build...
Running build_pynac...
checking for a BSD-compatible install... /usr/bin/ginstall -c
<snip>
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
Configuration of GiNaC 0.2.0 done. Now type "make".
make  all-recursive
make[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'
Making all in ginac
make[2]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT py_funcs.lo -MD -MP -MF .deps/py_funcs.Tpo -c -o py_funcs.lo py_funcs.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -MT py_funcs.lo -MD -MP -MF .deps/py_funcs.Tpo -c py_funcs.cpp  -fPIC -DPIC -o .libs/py_funcs.o
mv -f .deps/py_funcs.Tpo .deps/py_funcs.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT add.lo -MD -MP -MF .deps/add.Tpo -c -o add.lo add.cpp
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64 -MT add.lo -MD -MP -MF .deps/add.Tpo -c add.cpp  -fPIC -DPIC -o .libs/add.o
mv -f .deps/add.Tpo .deps/add.Plo
/bin/sh ../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage-4.5.alpha0/local/include/python2.6 -fPIC  -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64   -R/usr/local/gcc-4.4.4-multilib/lib/amd64 -L/usr/local/gcc-4.4.4-multilib/lib/amd64 -m64  -MT archive.lo -MD -MP -MF .deps/archive.Tpo -c -o archive.lo archive.cpp
```


After some time, this builds. The test suite passes without error, though the fact the test suite finishes almost instantly makes me wonder if any tests are actually run. 


```
Done installing pynac.

real	0m39.461s
user	0m33.296s
sys	0m4.679s
Successfully installed pynac-0.2.0.p4
Running the test suite.
Testing a 64-bit version of pynac
Making check in ginac
make[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'
make[1]: Nothing to be done for `check'.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src/ginac'
make[1]: Entering directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.alpha0/spkg/build/pynac-0.2.0.p4
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pynac-0.2.0.p4.spkg
```



---

Comment by drkirkby created at 2010-06-28 05:45:02

This is NOT ready for review. William said running 'make test' was pointless, so I need to remove spkg-check


---

Comment by drkirkby created at 2010-06-28 06:13:56

The package is here awaiting review now.


---

Comment by drkirkby created at 2010-06-28 06:13:56

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-06-28 08:32:08

Oops, I forgot to put the path to the .spkg 


http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p4.spkg


---

Comment by drkirkby created at 2010-07-14 16:09:44

I'm changing this to needs work, as there is a simpler, more elegant and more reliable way to resolve this, by setting CC="gcc -m64", CXX="g++ -m64" as was done on libfplll in ticket #7864. 

I will rewrite this patch, to use the other method. 

Dave


---

Comment by drkirkby created at 2010-07-14 16:10:51

Changing status from needs_review to needs_work.


---

Attachment

Simple change to export CC and CXX properly to build 64-bit on Solaris 10 and OpenSolaris


---

Comment by drkirkby created at 2010-07-16 16:49:55

I'm attaching logs showing builds on Solaris 10 (SPARC) and OpenSolaris x64. The package is ready for review at http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p5.spkg

Dave


---

Comment by drkirkby created at 2010-07-16 16:51:04

Build log from a Sun Blade 2000 with UltraSPARC III+ processors


---

Attachment

Build log from a Sun Ultra 27 with an Intel Xeon processor


---

Comment by drkirkby created at 2010-07-16 16:52:18

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-08-03 21:32:13

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-08-03 21:32:13

The changes look good.  The spkg builds on a number of different machines, both 32-bit and 64-bit, and doctests pass.

By the way, with the old spkg, pynac didn't build properly on 64-bit Solaris (either sparc -- t2 -- or x86 -- fulvia), so it's not exclusively an OpenSolaris issue.  With the new spkg, it works.

(Tested on t2 (32-bit), mark2 (32-bit), Mac OS X 10.6 (64-bit), sage.math (both with SAGE64='yes' and with SAGE64 unset), taurus (both with SAGE64='yes' and SAGE64 unset), cicero (32-bit), fulvia (both settings for SAGE64), and iras (64-bit machine? but with SAGE64 unset).)


---

Comment by jhpalmieri created at 2010-08-03 21:45:20

Is this positive review okay?  I don't have access to an OpenSolaris machine, but I've tested it on lots of other platforms.  I may try to install an OpenSolaris virtual machine, but I don't know how hard it will be to install all of the relevant software (like an up-to-date gcc).


---

Comment by drkirkby created at 2010-08-03 22:17:18

Replying to [comment:12 jhpalmieri]:
> Is this positive review okay?  I don't have access to an OpenSolaris machine, but I've tested it on lots of other platforms.  

I don't believe anyone can fault your positive review due to the fact you have not tested on OpenSolaris. 

First OpenSolaris is not an officially supported system. So that in itself is good enough reason not to fault you. But you have tested on several officially supported systems, as well as some unsupported ones. As you note, it does improve the situation on 64-bit SPARC and 64-bit x86. In fact, virtually all the changes I think that will be needed on one 64-bit variant of Solaris will be needed on another. 

Secondly, I've attached a log of the build on OpenSolaris, so it can be seen working there. 

A lot of reviewers are a lot less thorough than you John! 

I've had the odd people review my HP-UX patches too. I don't think anyone other than Minh has access to HP-UX. (Some of the MPFR developers have used my machine too)

> I may try to install an OpenSolaris virtual machine, but I don't know how hard it will be to install all of the relevant software (like an up-to-date gcc).

OpenSolaris has a package manager with a GUI interface which you can use to install software. By default, it gets packages from the offical Sun resource, which does not tend to have very up to update packages. But one can switch to the development server, and install from there, where there is a wider choice of packages. 

One issue I have hit is that on my laptop (which has a 64-bit processor), I installed a 64-bit version of OpenSolaris as the host operating system. But due to some limitations in the BIOS, which Sony kindly added, they have disabled the instructions which allow one to install a 64-bit guest operating system. While that's not a problem with my XP installation, my Solaris 10 installation is limited to 32-bits when on my laptop. 

On my desktop, there's no such limitation, so I can install 64-bit guest operating systems. 

Anyway, thank you for the review. I need to sort out zn_poly (#9358). I have a patch for that. Just need to upload it and mark it for review. 

Dave


---

Comment by drkirkby created at 2010-08-07 22:31:16

## Note to the release manager

Just add http://boxen.math.washington.edu/home/kirkby/patches/pynac-0.2.0.p5.spkg 

There are no library patches needed, and nothing needs to be added to the package. It should just drop it and go.


---

Comment by mpatel created at 2010-08-09 09:36:53

Resolution: fixed
