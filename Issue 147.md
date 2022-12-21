# Issue 147: libgd build breaks on sage-1.4.1.2

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2006-10-21 20:51:54

Assignee: was

The build breaks here because of missing headerrs:

    gcc -DHAVE_CONFIG_H -I. -I. -I. -I/SandBox/Justin/sb/sage-1.4/local//include/freetype2 \
         -I/SandBox/Justin/sb/sage-1.4/local//include -g -O2 -MT gdft.lo -MD -MP -MF \
         .deps/gdft.Tpo -c gdft.c  -fno-common -DPIC -o .libs/gdft.lo
    gdft.c:1366:35: error: fontconfig/fontconfig.h: No such file or directory


---

Attachment

build log for gd


---

Comment by was created at 2007-01-12 23:40:04

Resolution: fixed


---

Comment by was created at 2007-01-12 23:40:04

libgd is now a standard component of SAGE and builds everywhere...
