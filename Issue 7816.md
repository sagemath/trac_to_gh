# Issue 7816: gd fails to build on Open Solaris - missing header file

Issue created by migration from https://trac.sagemath.org/ticket/7816

Original creator: drkirkby

Original creation time: 2010-01-02 07:22:21

Assignee: drkirkby

gd is not building on Open Solaris due to a missing header file  X11/xpm.h. 

```
gcc -DHAVE_CONFIG_H -I. -I. -I. -I/export/home/drkirkby/sage-4.3/local/include/freetype2 -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include -Wall -m64 -fPIC -g -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include/freetype2/ -MT gdkanji.lo -MD -MP -MF .deps/gdkanji.Tpo -c gdkanji.c -o gdkanji.o >/dev/null 2>&1
if /bin/sh ./libtool --tag=CC --mode=compile gcc -DHAVE_CONFIG_H -I. -I. -I.   -I/export/home/drkirkby/sage-4.3/local/include/freetype2 -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include   -Wall -m64 -fPIC -g -I"/export/home/drkirkby/sage-4.3/local/include" -I/export/home/drkirkby/sage-4.3/local/include/freetype2/ -MT gdtables.lo -MD -MP -MF ".deps/gdtables.Tpo" -c -o gdtables.lo gdtables.c; \
	then mv -f ".deps/gdtables.Tpo" ".deps/gdtables.Plo"; else rm -f ".deps/gdtables.Tpo"; exit 1; fi
 gcc -DHAVE_CONFIG_H -I. -I. -I. -I/export/home/drkirkby/sage-4.3/local/include/freetype2 -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include -Wall -m64 -fPIC -g -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include/freetype2/ -MT gdtables.lo -MD -MP -MF .deps/gdtables.Tpo -c gdtables.c  -fPIC -DPIC -o .libs/gdtables.o
 gcc -DHAVE_CONFIG_H -I. -I. -I. -I/export/home/drkirkby/sage-4.3/local/include/freetype2 -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include -Wall -m64 -fPIC -g -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include/freetype2/ -MT gdtables.lo -MD -MP -MF .deps/gdtables.Tpo -c gdtables.c -o gdtables.o >/dev/null 2>&1
if /bin/sh ./libtool --tag=CC --mode=compile gcc -DHAVE_CONFIG_H -I. -I. -I.   -I/export/home/drkirkby/sage-4.3/local/include/freetype2 -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include   -Wall -m64 -fPIC -g -I"/export/home/drkirkby/sage-4.3/local/include" -I/export/home/drkirkby/sage-4.3/local/include/freetype2/ -MT gdxpm.lo -MD -MP -MF ".deps/gdxpm.Tpo" -c -o gdxpm.lo gdxpm.c; \
	then mv -f ".deps/gdxpm.Tpo" ".deps/gdxpm.Plo"; else rm -f ".deps/gdxpm.Tpo"; exit 1; fi
 gcc -DHAVE_CONFIG_H -I. -I. -I. -I/export/home/drkirkby/sage-4.3/local/include/freetype2 -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include -Wall -m64 -fPIC -g -I/export/home/drkirkby/sage-4.3/local/include -I/export/home/drkirkby/sage-4.3/local/include/freetype2/ -MT gdxpm.lo -MD -MP -MF .deps/gdxpm.Tpo -c gdxpm.c  -fPIC -DPIC -o .libs/gdxpm.o
gdxpm.c:28:21: error: X11/xpm.h: No such file or directory
gdxpm.c: In function 'gdImageCreateFromXpm':
gdxpm.c:32: error: 'XpmInfo' undeclared (first use in this function)
gdxpm.c:32: error: (Each undeclared identifier is reported only once
gdxpm.c:32: error: for each function it appears in.)
gdxpm.c:32: error: expected ';' before 'info'
gdxpm.c:33: error: 'XpmImage' undeclared (first use in this function)
gdxpm.c:33: error: expected ';' before 'image'
gdxpm.c:42: warning: implicit declaration of function 'XpmReadFileToXpmImage'
gdxpm.c:42: error: 'image' undeclared (first use in this function)
gdxpm.c:42: error: 'info' undeclared (first use in this function)
gdxpm.c:43: error: 'XpmSuccess' undeclared (first use in this function)
make[4]: *** [gdxpm.lo] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/gd-2.0.35.p2/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/gd-2.0.35.p2/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/gd-2.0.35.p2/src'
Error building gd.

```



---

Comment by drkirkby created at 2010-01-02 11:43:07

sorry, this is a duplicate of #7162


---

Comment by drkirkby created at 2010-01-02 11:43:07

Resolution: duplicate
