# Issue 6773: Freetype hides warning messages by sending output to /dev/null

Issue created by migration from https://trac.sagemath.org/ticket/6773

Original creator: drkirkby

Original creation time: 2009-08-17 10:11:21

Assignee: tbd

I've not no idea why anyone would want to do this, but freetype (along with lcalc) is one of the guilty parties. 

 /opt/sunstudio12.1/bin/cc -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/objs -I./builds/unix -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/include -c -g -DFT_CONFIG_OPTION_SYSTEM_ZLIB "-DFT_CONFIG_CONFIG_H=<ftconfig.h>" -DFT2_BUILD_LIBRARY "-DFT_CONFIG_MODULES_H=<ftmodule.h>" -I/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/src/pshinter /export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/src/pshinter/pshinter.c -o /export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/freetype-2.3.5.p1/src/objs/pshinter.o >/dev/null 2>&1




---

Comment by drkirkby created at 2009-12-03 04:24:53

This has now been submitted upstream as a bug. 

http://savannah.nongnu.org/bugs/index.php?28153


---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.
