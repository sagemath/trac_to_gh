# Issue 3339: tachyon spkg is not clean upstream

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-30 17:38:05

Assignee: mabshoff

CC:  mhampton jdemeyer

The tachyon spkg is not clean upstream sources:

[tabbott`@`debuild export$] diff -ur tmp/tachyon tmp/tachyon-0.98~beta/
Only in tmp/tachyon/demosrc: CVS
Only in tmp/tachyon/docs: CVS
Only in tmp/tachyon/librtvi: CVS
Only in tmp/tachyon/msvc: CVS
Only in tmp/tachyon/msvc/tachyon: CVS
Only in tmp/tachyon/msvc/tachyon/libtachyon: CVS
Only in tmp/tachyon/msvc/tachyon/tachyon: CVS
Only in tmp/tachyon/msvc/tachyon/tachyon_ogl: CVS
Only in tmp/tachyon: scenes
Only in tmp/tachyon/src: CVS
Only in tmp/tachyon/unix: CVS
diff -ur tmp/tachyon/unix/Make-arch tmp/tachyon-0.98~beta/unix/Make-arch
--- tmp/tachyon/unix/Make-arch  2007-02-13 04:00:36.000000000 -0500
+++ tmp/tachyon-0.98~beta/unix/Make-arch        2007-05-06 01:12:48.000000000 -0400
`@``@` -873,12 +873,15 `@``@`
        $(MAKE) all \
        "ARCH = macosx-thr" \
        "CC = cc" \
-       "CFLAGS = -Os -ffast-math -DBsd -DTHR -F/System/Library/Frameworks $(MISCFLAGS)" \
+       "CFLAGS = -Os -ffast-math -DTHR $(MISCFLAGS)" \
        "AR = ar" \
        "ARFLAGS = r" \
        "STRIP = strip" \
        "RANLIB = ranlib" \
-       "LIBS = -L. -ltachyon $(MISCLIB) -lpthread -framework Carbon"
+       "LIBS = -L. -ltachyon $(MISCLIB) -lpthread"
+
+#"CFLAGS = -Os -ffast-math -DBsd -DTHR -F/System/Library/Frameworks $(MISCFLAGS)" \
+#"LIBS = -L. -ltachyon $(MISCLIB) -lpthread -framework Carbon"

 macosx-altivec:
        $(MAKE) all \
diff -ur tmp/tachyon/unix/Make-config tmp/tachyon-0.98~beta/unix/Make-config
--- tmp/tachyon/unix/Make-config        2007-01-24 03:35:44.000000000 -0500
+++ tmp/tachyon-0.98~beta/unix/Make-config      2007-05-06 00:55:52.000000000 -0400
`@``@` -127,15 +127,9 `@``@`
 # LibPNG can be downlaoded from:
 #   http://www.libpng.org/
 ##########################################################################
-# Uncomment the following lines to disable PNG support
-USEPNG=
-PNGINC=
-PNGLIB=
-
-# Uncomment the following lines to enable PNG support
-#USEPNG= -DUSEPNG
-#PNGINC= -I/usr/local/include
-#PNGLIB= -L/usr/local/lib -lpng -lz
+USEPNG= -DUSEPNG
+PNGINC= -I$(SAGE_LOCAL)/include
+PNGLIB= -L$(SAGE_LOCAL)/lib -lpng -lz


 ##########################################################################


The PNG change can be replaced without a patch by using
make USEPNG=-DUSEPNG PNGINC=-I$(SAGE_LOCAL)/include PNGLIB=-L$(SAGE_LOCAL)/lib -lpng -lz
though it's a bit ugly.

while the other change is OS X stuff which I don't understand, so maybe we'll have to keep that change.

There isn't a new upstream release out yet, though.


---

Comment by kcrisman created at 2011-02-16 22:28:37

Tachyon has been upgraded fairly recently - is this maybe no longer an issue?


---

Comment by kcrisman created at 2011-06-28 16:32:23

I just tried the same command, and now the only problem is that which is documented in the SPKG.txt

```
Only in Downloads/TestTachyon/tachyon/: msvc
Only in Downloads/TestTachyon/tachyon/: scenes
```

So this ticket can be closed.


---

Comment by kcrisman created at 2011-06-28 16:32:23

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-28 16:32:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-07-05 10:06:20

Resolution: worksforme
