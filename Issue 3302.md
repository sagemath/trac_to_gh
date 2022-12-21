# Issue 3302: python_gnutls fails to upgrade on OSX in case Sage was moved

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-25 20:54:34

Assignee: mabshoff

Ok, you seem to have moved the Sage install from

    /Users/saliola/Desktop/sage-3.0.1/

to

    /Users/saliola/sage-3.0.1/

Consequently the linker does not find some libraries:

/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libgpg-error.0.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgcrypt.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libz.1.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgnutls.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: warning can't open dynamic library: /Users/saliola/Desktop/sage-3.0.1/local/lib/libopencdk.10.dylib referenced from: /Users/saliola/sage-3.0.1/local/lib//libgnutls-extra.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)


This can probably be fixed by adding "-L$SAGE_LOCAL/lib" to the build flags.





---

Comment by jdemeyer created at 2012-10-05 09:16:24

Resolution: invalid


---

Comment by jdemeyer created at 2012-10-05 09:16:24

GNUTLS is no longer part of Sage.
