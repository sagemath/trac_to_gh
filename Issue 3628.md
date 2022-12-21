# Issue 3628: [with spkg; needs review] (take 2) building sage on opensuse x86_64 fails with readline detection error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-10 00:36:06

Assignee: mabshoff

This is take two of #3597.  We were using --with-readline but should have used --with-readline-prefix, as is clearly stated in ./configure --help. 


---

Comment by was created at 2008-07-10 00:39:52

The spkg here:

http://sage.math.washington.edu/home/was/patches/clisp-2.46.p3.spkg


does this

```
sage`@`modular:~/build/sage-3.0.4.rc2/spkg/standard/clisp-2.46.p2$ hg export tip
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1215650285 25200
# Node ID 894ef09f7493ecb498cfabae78c94ccadf74e50c
# Parent  3fb5fefd13e4d8acf4eff5c963397554f9df2574
Add -prefix to with-readline option; get rid of stupid fallback.

diff -r 3fb5fefd13e4 -r 894ef09f7493 spkg-install
--- a/spkg-install      Mon Jul 07 19:51:11 2008 -0400
+++ b/spkg-install      Wed Jul 09 17:38:05 2008 -0700
`@``@` -26,12 +26,7 `@``@` cd src/

 unset CPPFLAGS   # do this; since otherwise build will fail if CPPFLAGS was se

-CFLAGS="-O0 -g" ./configure --with-readline="$SAGE_LOCAL" --prefix="$SAGE_LOCAL" --ignore-absence-of-libsigsegv --without-libintl
-
-if [ $? -ne 0 ]; then
-    echo "Building without readline."
-    CFLAGS="-O0 -g" ./configure --without-readline --prefix="$SAGE_LOCAL" --ignore-absence-of-libsigsegv --without-libintl
-fi
+CFLAGS="-O0 -g" ./configure --with-readline-prefix="$SAGE_LOCAL" --prefix="$SAGE_LOCAL" --ignore-absence-of-libsigsegv --without-libintl

 #if [ $UNAME = "CYGWIN" ]; then
     # This is a hack to get around a bug in the build process under Cygwin.
```



---

Comment by was created at 2008-07-10 00:42:48

WAIT -- this doesn't actually find readline.  So this is no good.


---

Comment by was created at 2008-07-10 01:05:31

OK, this works perfectly and it *does* fix the hang integrating certain things with maxima too:

http://sage.math.washington.edu/home/was/patches/clisp-2.46.p4.spkg


---

Comment by mabshoff created at 2008-07-10 01:57:22

Positive review. Thanks for reading the documentation :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-10 02:01:54

Resolution: fixed


---

Comment by mabshoff created at 2008-07-10 02:01:54

Merged in Sage 3.0.4.rc3
