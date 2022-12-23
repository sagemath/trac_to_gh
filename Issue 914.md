# Issue 914: NTL wrapper build fails on Ubuntu 7.10

Issue created by migration from https://trac.sagemath.org/ticket/914

Original creator: mhansen

Original creation time: 2007-10-17 17:07:50

Assignee: mabshoff


```
I just upgraded to Ubuntu 7.10, and I have some issues building the NTL wrapper.

g++ -o src/ntl_wrap.os -c -fPIC -I/opt/sage/local/include -I/opt/sage/local/include/python2.5 -I/opt/sage/local/include/NTL -Iinclude src/ntl_wrap.cpp
src/ntl_wrap.cpp: In function ‘NTL::ZZ_pX ZZ_pE_to_ZZ_pX(ZZ_pE)’:
src/ntl_wrap.cpp:794: error: ‘x’ has incomplete type
src/ntl_wrap.cpp:794: error: forward declaration of ‘struct ZZ_pE’
src/ntl_wrap.cpp: At global scope:
src/ntl_wrap.cpp:912: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:923: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:1082: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:1087: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:1092: error: variable or field ‘ZZ_pEContext_restore’ declared void
src/ntl_wrap.cpp:1092: error: ‘ZZ_pEContext’ was not declared in this scope
src/ntl_wrap.cpp:1092: error: ‘ctx’ was not declared in this scope
src/ntl_wrap.cpp:1093: error: expected ‘,’ or ‘;’ before ‘{’ token
scons: *** [src/ntl_wrap.os] Error 1
ERROR: There was an error building c_lib.


Here is the ouput of g++ -v
mike@mike-laptop:/opt/sage$ g++ -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.1.3 --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release x86_64-linux-gnu
Thread model: posix
gcc version 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)
```



---

Comment by mabshoff created at 2007-10-17 17:48:31

Changing status from new to assigned.


---

Comment by mhansen created at 2007-10-17 22:51:24

Here's the steps I took to get it to work.

rm -rf $SAGE_ROOT/devel/sage-main
rm -rf $SAGE_ROOT/spkg/installed/sage-2.8.7
sage -upgrade

This should probably be marked as invalid.


---

Comment by was created at 2007-10-19 01:21:11

There is a problem here, but it's basically probably too hard too fix, and there is an easy workaround (see above).


---

Comment by was created at 2007-10-19 01:21:11

Resolution: fixed


---

Comment by was created at 2007-10-19 01:21:19

Changing status from closed to reopened.


---

Comment by was created at 2007-10-19 01:21:19

Resolution changed from fixed to 


---

Comment by was created at 2007-10-19 01:21:24

Resolution: invalid


---

Comment by was created at 2007-10-19 01:21:30

Changing status from closed to reopened.


---

Comment by was created at 2007-10-19 01:21:30

Resolution changed from invalid to 


---

Comment by was created at 2007-10-19 01:21:38

Resolution: wontfix
