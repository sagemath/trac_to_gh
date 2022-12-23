# Issue 146: Soya build breaks on sage-1.4.1.2

Issue created by migration from https://trac.sagemath.org/ticket/146

Original creator: justin

Original creation time: 2006-10-21 20:49:46

Assignee: was

The build breaks here because of missing includes:

    gcc -fno-strict-aliasing -Wno-long-double -no-cpp-precomp -mno-fused-madd \
         -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -DSOYA_BIG_ENDIAN=big -Iode-0.5/include \
         -I/usr/include -I/usr/local/include -I/usr/X11R6/include -I/usr/include/freetype2 \
         -I/usr/local/include/freetype2 -I/usr/include/cal3d -I/usr/local/include/cal3d \
         -I/sw/include -I/SandBox/Justin/sb/sage-1.4/local/include/python2.5 -c _soya.c \
         -o build/temp.macosx-10.3-ppc-2.5/_soya.o -w
    _soya.c:22:21: error: GL/glew.h: No such file or directory
    _soya.c:23:28: error: SDL/SDL_endian.h: No such file or directory
    _soya.c:24:21: error: SDL/SDL.h: No such file or directory



---

Attachment

Build log for soya build


---

Comment by was created at 2007-01-12 23:38:13

Deprecated this to an experimental package.  We shouldn't be supporting this...


---

Comment by was created at 2007-01-12 23:38:13

Resolution: wontfix
