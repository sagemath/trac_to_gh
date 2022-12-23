# Issue 7867: GCC reports incorrect flags compiling descent_two_isogeny.c on Solaris 10

Issue created by migration from https://trac.sagemath.org/ticket/7867

Original creator: drkirkby

Original creation time: 2010-01-07 07:25:19

Assignee: drkirkby

CC:  rlm cremona was robertwb jsp

*== The build environment ==
 * Sun T5240. 2 x 1167 MHz T2+ SPARC processors 32 GB RAM (t2.math.washington.edu)
 * Solaris 10 update 6 (released in 05/2009)
 * gcc 4.4.1 configured to use both the Sun assembler and linker. 

## The problem


```
sage-4.3.1.alpha1/.hg/store/data/c__lib/include/ccobject.h.i
sage-4.3.1.alpha1/.hg/store/data/c__lib/include/_z_z__pylong.h.i
sage-4.3.1.alpha1/.hg/store/data/build/
sage-4.3.1.alpha1/.hg/store/data/build/sage/
sage-4.3.1.alpha1/.hg/store/data/build/sage/coding/
sage-4.3.1.alpha1/.hg/store/data/build/sage/coding/code__constructions.py.i
Finished extraction
****************************************************
Host system
uname -a:
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.1/configure --prefix=/usr/local/gcc-4.4.1-sun-linker/ --with-as=/usr/ccs/bin/as --without-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran --with-mpfr-include=/usr/local/include --with-mpfr-lib=/usr/local/lib --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib CC=/usr/sfw/bin/gcc CXX=/usr/sfw/bin/g++
Thread model: posix
gcc version 4.4.1 (GCC)
****************************************************
gcc -o src/convert.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/convert.c
gcc -o src/interrupt.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/interrupt.c
gcc -o src/mpn_pylong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/mpn_pylong.c
gcc -o src/mpz_pylong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/mpz_pylong.c
gcc -o src/mpz_longlong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/mpz_longlong.c
gcc -o src/stdsage.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/stdsage.c
gcc -o src/gmp_globals.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/gmp_globals.c
g++ -o src/ZZ_pylong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/ZZ_pylong.cpp
g++ -o src/ntl_wrap.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/ntl_wrap.cpp
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from include/ntl_wrap.h:32,
                 from src/ntl_wrap.cpp:5:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1004:1: warning: "_FILE_OFFSET_BITS" redefined
In file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/wchar.h:20,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/cwchar:47,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/bits/postypes.h:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iosfwd:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ios:39,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ostream:40,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iostream:40,
                 from src/ntl_wrap.cpp:1:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:197:1: warning: this is the location of the previous definition
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from include/ntl_wrap.h:32,
                 from src/ntl_wrap.cpp:5:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1019:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/wchar.h:20,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/cwchar:47,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/bits/postypes.h:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iosfwd:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ios:39,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ostream:40,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iostream:40,
                 from src/ntl_wrap.cpp:1:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:275:1: warning: this is the location of the previous definition
g++ -o libcsage.so -shared src/convert.pic.o src/interrupt.pic.o src/mpn_pylong.pic.o src/mpz_pylong.pic.o src/mpz_longlong.pic.o src/stdsage.pic.o src/gmp_globals.pic.o src/ZZ_pylong.pic.o src/ntl_wrap.pic.o -L/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/lib -lntl -lgmp -lpari
pulling from /rootpool2/local/kirkby/sage-4.3.1.alpha1/spkg/build/sage-4.3.1.alpha1
searching for changes
no changes found
abort: can't merge with ancestor
nothing changed
0 files updated, 0 files merged, 0 files removed, 0 files unresolved
Deleting the scons target.
Removed src/convert.pic.o
Removed src/interrupt.pic.o
Removed src/mpn_pylong.pic.o
Removed src/mpz_pylong.pic.o
Removed src/mpz_longlong.pic.o
Removed src/stdsage.pic.o
Removed src/gmp_globals.pic.o
Removed src/ZZ_pylong.pic.o
Removed src/ntl_wrap.pic.o
Removed libcsage.so
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Cleaning targets ...
scons: done cleaning targets.

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/convert.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/convert.c
gcc -o src/interrupt.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/interrupt.c
gcc -o src/mpn_pylong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/mpn_pylong.c
gcc -o src/mpz_pylong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/mpz_pylong.c
gcc -o src/mpz_longlong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/mpz_longlong.c
gcc -o src/stdsage.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/stdsage.c
gcc -o src/gmp_globals.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/gmp_globals.c
g++ -o src/ZZ_pylong.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/ZZ_pylong.cpp
g++ -o src/ntl_wrap.pic.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/NTL -Iinclude src/ntl_wrap.cpp
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from include/ntl_wrap.h:32,
                 from src/ntl_wrap.cpp:5:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1004:1: warning: "_FILE_OFFSET_BITS" redefined
In file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/wchar.h:20,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/cwchar:47,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/bits/postypes.h:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iosfwd:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ios:39,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ostream:40,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iostream:40,
                 from src/ntl_wrap.cpp:1:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:197:1: warning: this is the location of the previous definition
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:8,
                 from include/ntl_wrap.h:32,
                 from src/ntl_wrap.cpp:5:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/pyconfig.h:1019:1: warning: "_POSIX_C_SOURCE" redefined
In file included from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/wchar.h:20,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/cwchar:47,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/bits/postypes.h:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iosfwd:42,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ios:39,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/ostream:40,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/../../../../include/c++/4.4.1/iostream:40,
                 from src/ntl_wrap.cpp:1:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:275:1: warning: this is the location of the previous definition
g++ -o libcsage.so -shared src/convert.pic.o src/interrupt.pic.o src/mpn_pylong.pic.o src/mpz_pylong.pic.o src/mpz_longlong.pic.o src/stdsage.pic.o src/gmp_globals.pic.o src/ZZ_pylong.pic.o src/ntl_wrap.pic.o -L/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/lib -lntl -lgmp -lpari
warning: /rootpool2/local/kirkby/sage-4.3.1.alpha1/devel/sage-main/sage/symbolic/../libs/ginac/decl.pxi:113:33: Function signature does not match previous declaration
warning: /rootpool2/local/kirkby/sage-4.3.1.alpha1/devel/sage-main/sage/symbolic/../libs/ginac/decl.pxi:114:29: Function signature does not match previous declaration
warning: /rootpool2/local/kirkby/sage-4.3.1.alpha1/devel/sage-main/sage/symbolic/../libs/ginac/decl.pxi:115:18: Function signature does not match previous declaration
warning: /rootpool2/local/kirkby/sage-4.3.1.alpha1/devel/sage-main/sage/symbolic/../libs/ginac/decl.pxi:206:24: Function signature does not match previous declaration
warning: /rootpool2/local/kirkby/sage-4.3.1.alpha1/devel/sage-main/sage/symbolic/../libs/ginac/decl.pxi:322:60: Function signature does not match previous declaration
Updating Cython code....
Building modified file sage/symbolic/constants_c.pyx.
python `which cython` --embed-positions --directive cdivision=True -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/devel/sage-main -o sage/symbolic/constants_c.cpp sage/symbolic/constants_c.pyx
sage/symbolic/constants_c.pyx --> /rootpool2/local/kirkby/sage-4.3.1.alpha1/local//lib/python/site-packages//sage/symbolic/constants_c.pyx
Time to execute 1 commands: 5.11293005943 seconds
Finished compiling Cython code (time = 8.45891094208 seconds)
running install
running build
running build_py
copying sage/symbolic/constants.py -> build/lib.solaris-2.10-sun4v-2.6/sage/symbolic
running build_ext
building 'sage.schemes.elliptic_curves.descent_two_isogeny' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/FLINT/ -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -c sage/schemes/elliptic_curves/descent_two_isogeny.c -o build/temp.solaris-2.10-sun4v-2.6/sage/schemes/elliptic_curves/descent_two_isogeny.o -std=c99 -w
In file included from /usr/include/limits.h:18,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/limits.h:122,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/syslimits.h:7,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/limits.h:11,
                 from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:19,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:4:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:341:2: error: #error "Compiler or options invalid for pre-UNIX 03 X/Open applications     and pre-2001 POSIX applications"
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.


real    0m49.907s
user    0m38.843s
sys     0m8.405s
Error building new version of SAGE.
You might try typing 'sage -ba' or write to sage-support with as much information as possible.

real    2m10.215s
user    1m41.154s
sys     0m23.024s
sage: An error occurred while installing sage-4.3.1.alpha1 
```


 == Possible reasons ==
#6583 could possibly be the reason, but I am probably mistaken. The changes were committed only recently, which makes me think it might be the problem. 



---

Comment by drkirkby created at 2010-01-07 08:41:53

The last option on the gcc command line '-w' is there to suppress all warnings. (*A really really bad idea IMHO*). If I remove that horrid -w option, some more warnings are shown. Whether these aid in solving the problem I do not know, but they do indicate a lot of potential problems are being masked. This unfortunately is quite common in Sage, with numerous bits of code using all sorts of tricks to hide warning messages.  


```
sage subshell$ 
/rootpool2/local/kirkby/sage-4.3.1.alpha1
sage subshell$ 
/rootpool2/local/kirkby/sage-4.3.1.alpha1
sage subshell$ gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/FLINT/ -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/devel//sage/sage/ext -I/rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6 -c sage/schemes/elliptic_curves/descent_two_isogeny.c -o build/temp.solaris-2.10-sun4v-2.6/sage/schemes/elliptic_curves/descent_two_isogeny.o -std=c99 
In file included from /usr/include/limits.h:18,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/limits.h:122,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/syslimits.h:7,
                 from /usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/limits.h:11,
                 from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local/include/python2.6/Python.h:19,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:4:
/usr/local/gcc-4.4.1-sun-linker/bin/../lib/gcc/sparc-sun-solaris2.10/4.4.1/include-fixed/sys/feature_tests.h:341:2: error: #error "Compiler or options invalid for pre-UNIX 03 X/Open applications      and pre-2001 POSIX applications"
In file included from sage/schemes/elliptic_curves/descent_two_isogeny.c:148:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage/ntl_wrap.h:142: warning: function declaration isn’t a prototype
In file included from sage/schemes/elliptic_curves/descent_two_isogeny.c:148:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage/ntl_wrap.h:310: warning: ‘struct GF2X_c’ declared inside parameter list
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage/ntl_wrap.h:310: warning: its scope is only this definition or declaration, which is probably not what you want
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage/ntl_wrap.h:319: warning: ‘struct GF2E’ declared inside parameter list
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/csage/ntl_wrap.h:327: warning: ‘struct GF2’ declared inside parameter list
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/fmpz.h:36,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:150:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/memory-manager.h:41: warning: function declaration isn’t a prototype
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/memory-manager.h:43: warning: function declaration isn’t a prototype
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/memory-manager.h:45: warning: function declaration isn’t a prototype
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/fmpz.h:38,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:150:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/long_extras.h:287: warning: function declaration isn’t a prototype
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/long_extras.h:288: warning: function declaration isn’t a prototype
In file included from /rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/fmpz.h:39,
                 from sage/schemes/elliptic_curves/descent_two_isogeny.c:150:
/rootpool2/local/kirkby/sage-4.3.1.alpha1/local//include/FLINT/zn_poly/src/zn_poly.h:47: warning: function declaration isn’t a prototype
/rootpool2/local/kirkby/sage-4.3.1.alpha1
sage subshell$ 
```



---

Comment by rlm created at 2010-02-10 01:12:08

Based on random googling, I'd suspect the flag `-std=c99`, which is required since the file depends on FLINT. This thread* seems to suggest replacing that flag with `-xc99`. Other threads suggest adding `-xc99=%none`: this flag may be required because it is trying to link in ratpoints, and is the first thing in Sage to try to do so. See this thread^ for more details.

* - http://www.mathworks.com/support/solutions/en/data/1-14ZQS4/index.html?solution=1-14ZQS4

^ - http://mail.python.org/pipermail/python-bugs-list/2005-September/030452.html

In particular, the relevant part of limits.h says

```
/*
 * It is invalid to compile an XPG3, XPG4, XPG4v2, or XPG5 application
 * using c99.  The same is true for POSIX.1-1990, POSIX.2-1992, POSIX.1b,
 * and POSIX.1c applications. Likewise, it is invalid to compile an XPG6
 * or a POSIX.1-2001 application with anything other than a c99 or later
 * compiler.  Therefore, we force an error in both cases.
 */
```


This is where my understanding reaches its boundaries, but maybe I've said something helpful to someone. The ratpoints code is fairly old, and it wouldn't surprise me if the above comment was relevant.


---

Comment by rlm created at 2010-02-10 01:14:53

Actually, this could bode poorly: if ratpoints can't be compiled with c99 but FLINT must be, how to compile descent_(...).c, which depends on both?


---

Comment by drkirkby created at 2010-02-10 14:43:02

This is really *excellent* news that Minh has tracked this down. 

First, it should be noted that the Mathworks link published is about the Sun compiler, The compiler option -xc99=none (without the % sign), is a Sun compiler flag. I've no idea where the $ sign comes from. 

This does not look as bad as perhaps Robert thinks. I need to double check this, but it would appear ratpoints will build on Solaris SPARC with -std=c99 added, so if the only issue is that, then I believe it is a trivial fix. However, if building ratpoints with this option does not allow this to work, and we can find no fix, then we are in a more serious situation. 

Dave


---

Comment by wjp created at 2010-02-22 13:24:46

I haven't verified this at all, but this webpage suggests that a `-D_XOPEN_SOURCE=600` compile flag might be needed in some cases when using `-std=c99` on Solaris: http://wiki.netbsd.se/index.php/Feature_test_macros


---

Comment by drkirkby created at 2010-02-24 20:51:35

Changing priority from major to blocker.


---

Comment by drkirkby created at 2010-02-24 20:51:35

I've tried building ratpoints with

 * -D_XOPEN_SOURCE=600
 * -std=c99
 * -std=c99 -D_XOPEN_SOURCE=600

All 3 allow ratpoints to build, but none of them allow the Sage library to build. 

Ratpoints also currently builds with the option 


```
-DUSE_SSE
}}} 

on SPARC, which is a bit silly, as the SPARC processor does not support SSE instructions. Removing that (as is done on OS X already), still does not allow the Sage library to build. 

Ratpoints seems to build with pretty much any options I throw at it - getting it work with the Sage library is not proving so easy. 

I have not tried adding -D_XOPEN_SOURCE=600 to the Sage library. I do not know how to do this. 

Dave


---

Comment by wjp created at 2010-02-24 20:54:14

What errors do you get when building the Sage library?


---

Comment by drkirkby created at 2010-02-24 21:05:33

The error message is shown when I created the ticket. However, you need to use the horizontal scroll facility in trac to see it, as it is on the far right. 

Dave


---

Comment by wjp created at 2010-02-24 21:15:10

Ah, I mistakenly thought that was already where you were adding the `-D_XOPEN_SOURCE=600` since that was the error you reported.

The patch at #6583 adds the `sage.schemes.elliptic_curves.descent_two_isogeny` extension that's failing with a `-std=c99` flag. (Right at the top of the patch at http://trac.sagemath.org/sage_trac/attachment/ticket/6583/trac_6583-rebase.patch .) That would be the place to add the extra `-D_XOPEN_SOURCE=600` option (if it works...), I think.


---

Comment by drkirkby created at 2010-02-28 22:15:14

Thanks to Jaap Spies, who found a solution on the python web site, this has been solved by a small patch to python. 

The patch itself only affects Solaris, but to make double sure, you can see I only copied the patch on Solaris. So there is no fear of it breaking on any operating system. 

Unfortunately, the small patch needs a revised configure.in, and a revised configure script, as well as the directory autoconf makes (sometimes copying the configure script alone is not sufficient). 

As such, the Mercurial patch is 1 MB in size. I've attached it here, but you can't view it on trac due to its size. 

I've also attached the smaller patch downloaded from the python web site. 

All files can be found here. 

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p6/


---

Comment by drkirkby created at 2010-02-28 22:18:42

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-03-02 02:47:04

Replying to [comment:11 drkirkby]:
> All files can be found here. 
> 
> http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p6/

I see a possible conflict between the current ticket and #7761. Ticket #7761 already has a positive review and its updated Python spkg is `python-2.6.4.p6.spkg`. However, the current ticket (i.e. #7867) also has an updated Python spkg `python-2.6.4.p6.spkg`. Is it possible for you to base your updated Python spkg on top of that at #7761?


---

Comment by mvngu created at 2010-03-02 02:47:04

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-03-02 03:01:24

Replying to [comment:13 mvngu]:
> ... already has a ... `python-2.6.4.p6.spkg` ...

Good catch, Minh!


---

Comment by drkirkby created at 2010-03-02 09:08:54

Updated Mercurial patch to avoid clash with 7761


---

Attachment

Updated spkg-install to avoid clash with 7761


---

Attachment

Updated SPKG.txt  patch to avoid clash with 7761


---

Comment by drkirkby created at 2010-03-02 09:13:25

Patch downloaded from Python web site - date changed to today


---

Attachment

Thank you Minh. 

I've created a .p7, based on the ticket at #7761. It may be found here. 

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.4.p7/python-2.6.4.p7.spkg

I've updated all the files on this ticket. 

Despite the fact patch downloaded from the Python web site is unchanged, I decided to 'touch' it to bring the date upto date, as it was previously dated much earlier. I thought it might be a bit confusing if someone looks in the patches directory. I reattached it to this ticket, which was probably unnecessary, but can do no harm. As such, it should


---

Comment by drkirkby created at 2010-03-02 09:49:15

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-03-03 16:01:51

I see no problems with other architectures (tested on Fedora 11 and 12), as it only effects SunOS.

This is a great step forward on the Solaris port!

On open Solaris I now could build matplotlib for instance.

So positive review.

Jaap


---

Comment by jsp created at 2010-03-03 16:01:51

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-03-05 03:30:02

#8440 sorts out another issue with Python. That ticket depends on this one.


---

Comment by mhansen created at 2010-03-06 08:18:44

Resolution: fixed
