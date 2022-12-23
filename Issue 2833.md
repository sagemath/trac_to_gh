# Issue 2833: Linbox build failure on OSX 10.4 intel

Issue created by migration from https://trac.sagemath.org/ticket/2833

Original creator: jkantor

Original creation time: 2008-04-06 22:09:51

Assignee: cpernet

Building the sage 3.0.alpha1 tarball failed at linbox  on OSX 10.4 intel with gcc
version 4.0.1.




```
/bin/sh ./libtool --tag=CXX   --mode=compile g++ -DPACKAGE_NAME=\"liblinboxwrap\" -DPACKAGE_TARNAME=\"liblinboxwrap\" -DPACKAGE_VERSION=\"0.0.1\" -DPACKAGE_STRING=\"liblinboxwrap\ 0.0.1\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"liblinboxwrap\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I.   -g -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox" -I"/Users/kantor/sage-3.0.alpha1/local"/include  -g -fPIC -I"/Users/kantor/sage-3.0.alpha1/local/include" -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox"  -L"/Users/kantor/sage-3.0.alpha1/local/lib" -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c -o linbox_wrap.lo `test -f 'src/linbox_wrap.cpp' || echo './'`src/linbox_wrap.cpp
mkdir .libs
 g++ -DPACKAGE_NAME=\"liblinboxwrap\" -DPACKAGE_TARNAME=\"liblinboxwrap\" -DPACKAGE_VERSION=\"0.0.1\" "-DPACKAGE_STRING=\"liblinboxwrap 0.0.1\"" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"liblinboxwrap\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I. -g -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -I/Users/kantor/sage-3.0.alpha1/local/include -g -fPIC -I/Users/kantor/sage-3.0.alpha1/local/include -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -L/Users/kantor/sage-3.0.alpha1/local/lib -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c src/linbox_wrap.cpp  -fno-common -DPIC -o .libs/linbox_wrap.o
 g++ -DPACKAGE_NAME=\"liblinboxwrap\" -DPACKAGE_TARNAME=\"liblinboxwrap\" -DPACKAGE_VERSION=\"0.0.1\" "-DPACKAGE_STRING=\"liblinboxwrap 0.0.1\"" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"liblinboxwrap\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_BLAS=1 -I. -g -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -I/Users/kantor/sage-3.0.alpha1/local/include -g -fPIC -I/Users/kantor/sage-3.0.alpha1/local/include -I/Users/kantor/sage-3.0.alpha1/local/include/linbox -L/Users/kantor/sage-3.0.alpha1/local/lib -MT linbox_wrap.lo -MD -MP -MF .deps/linbox_wrap.Tpo -c src/linbox_wrap.cpp -o linbox_wrap.o >/dev/null 2>&1
mv -f .deps/linbox_wrap.Tpo .deps/linbox_wrap.Plo
/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -fPIC -I"/Users/kantor/sage-3.0.alpha1/local/include" -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox"  -L"/Users/kantor/sage-3.0.alpha1/local/lib" -version-info 0:0:0  -o liblinboxwrap.la -rpath /Users/kantor/sage-3.0.alpha1/local/lib linbox_wrap.lo -llinbox /usr/lib/libcblas.dylib 
g++ -dynamiclib -single_module ${wl}-flat_namespace ${wl}-undefined ${wl}suppress -o .libs/liblinboxwrap.0.0.0.dylib  .libs/linbox_wrap.o  -L/Users/kantor/sage-3.0.alpha1/local/lib /Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib  -install_name  /Users/kantor/sage-3.0.alpha1/local/lib/liblinboxwrap.0.dylib -Wl,-compatibility_version -Wl,1 -Wl,-current_version -Wl,1.0
ld: multiple definitions of symbol __ZN6LinBox11commentatorE
.libs/linbox_wrap.o definition of __ZN6LinBox11commentatorE in section (__DATA,__common)
/Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib(single module) definition of __ZN6LinBox11commentatorE
/usr/bin/libtool: internal link edit command failed
make[2]: *** [liblinboxwrap.la] Error 1
Error building linboxwrap
/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -fPIC -I"/Users/kantor/sage-3.0.alpha1/local/include" -I"/Users/kantor/sage-3.0.alpha1/local/include/linbox"  -L"/Users/kantor/sage-3.0.alpha1/local/lib" -version-info 0:0:0  -o liblinboxwrap.la -rpath /Users/kantor/sage-3.0.alpha1/local/lib linbox_wrap.lo -llinbox /usr/lib/libcblas.dylib 
g++ -dynamiclib -single_module ${wl}-flat_namespace ${wl}-undefined ${wl}suppress -o .libs/liblinboxwrap.0.0.0.dylib  .libs/linbox_wrap.o  -L/Users/kantor/sage-3.0.alpha1/local/lib /Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib  -install_name  /Users/kantor/sage-3.0.alpha1/local/lib/liblinboxwrap.0.dylib -Wl,-compatibility_version -Wl,1 -Wl,-current_version -Wl,1.0
ld: multiple definitions of symbol __ZN6LinBox11commentatorE
.libs/linbox_wrap.o definition of __ZN6LinBox11commentatorE in section (__DATA,__common)
/Users/kantor/sage-3.0.alpha1/local/lib/liblinbox.dylib(single module) definition of __ZN6LinBox11commentatorE
/usr/bin/libtool: internal link edit command failed
make[2]: *** [liblinboxwrap.la] Error 1
Error installing linboxwrap
```



---

Comment by cpernet created at 2008-04-09 16:37:30

Proposed patch


---

Attachment

I propose the attached patch. 
However, I still could not test it on a OS-X 10.4 since I only have access on 10.5 boxes.
Let me know if it fixes the bug, and I will post the updated linbox spkg.


---

Comment by jkantor created at 2008-04-09 17:39:36

This patch fixes the problem for my machine. Therefore positive review.


---

Comment by mabshoff created at 2008-04-09 18:17:53

An new spkg which incorporates Clement's fix is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha4/linbox-1.1.5p2.spkg

It builds fine on OSX 10.4, 10.5 and Linux.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-09 18:39:47

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-09 18:39:47

Resolution: fixed
