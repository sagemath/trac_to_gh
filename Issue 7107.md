# Issue 7107: sage does not build on ppc os x 10.4 anymore, failing with mpfr

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-04 06:15:26

Assignee: tbd

CC:  georgsweber kcrisman

The following is on skynet's varro


```
/bin/sh ../libtool --tag=CC   --mode=link gcc  -O2  -Wl,-search_paths_first  -L/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local/lib -o troot troot.o libfrtests.la -lm ../libmpfr.la -lgmp
libtool: link: gcc -O2 -Wl,-search_paths_first -o .libs/troot troot.o  -L/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local/lib ./.libs/libfrtests.a -lm ../.libs/libmpfr.dylib /home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/local/lib/libgmp.dylib
powerpc-apple-darwin8-gcc-4.0.1: Internal error: Killed (program collect2)
Please submit a full bug report.
See <URL:http://developer.apple.com/bugreporter> for instructions.
make[4]: *** [troot] Error 1
make[3]: *** [check-am] Error 2
make[2]: *** [check-recursive] Error 1
There was a problem during the mpfr tests.

real    6m19.637s
user    2m23.696s
sys     2m28.620s
sage: An error occurred while installing mpfr-2.4.1.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/spkg/build/mpfr-2.4.1.p0 and type 'make'.
Instead type "/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/spkg/build/mpfr-2.4.1.p0
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/mpfr-2.4.1.p0] Error 1

real    62m55.453s
user    34m21.128s
sys     16m39.873s
Error building Sage.
./sage -b
There is no directory '/home/wstein/screen/varro/build/sage-4.1.2.rc1.alpha1/devel/sage'

real    0m0.132s
user    0m0.019s
sys     0m0.060s
make: *** [testlong] Error 1
varro:~/screen/varro wstein$ gcc -v
Using built-in specs.
Target: powerpc-apple-darwin8
Configured with: /var/tmp/gcc/gcc-5370~2/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --target=powerpc-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5370)
```


Note that the above error occurs after mpfr successfully builds during building of the test suite.  Possible fixes:

  * do not run spkg-check on OS X 10.4 (then the build continues fine... for a while -- i only watched a few minutes)

  * fix the source of the problem (probably a compiler bug on OS X, so impossible)

  * deprecate support for OS X 10.4.

I like the first option above. 


---

Comment by kcrisman created at 2009-10-07 16:34:11

The first option also works on the PPC G4 X.4 box I am trying.  Hopefully the build will complete; it's already through mpfi, Cython, Pynac, ... which is a good sign.  

In this case, I guess one would need something like the following at the VERY end of the spkg-install file:

```
-cd ..; ./spkg-check
+if [`uname` = "Darwin" and something else to show it's X.4]; then
+        shell equivalent of pass
+else
+        cd ..; ./spkg-check
+fi
```

Where I have no idea what the shell equivalent of pass is, and where I don't know how to check X.4 - I feel like there is some variable set sometimes that checks for things like 8.11.0 (which is the version of the box I'm running this on), but I can't remember what/where it is.


---

Comment by kcrisman created at 2009-10-07 16:34:11

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-08 00:30:08

Just to confirm that this seems to work.  I can find_root, I can do factor(factorial(100000)), and various other things.  Doesn't mean it's perfect, but at least Sage will build and run if you don't do the spkg-check for mpfr.


---

Comment by kcrisman created at 2009-10-08 11:11:04

Another followup - I changed the script back to include spkg-check, sage -f'ed the spkg, and all mpfr test files built, and all mpfr tests passed.    Again, this is PPC G4 box running OSX.4.  Is it possible to try this again on varro?


---

Comment by was created at 2009-10-14 16:09:48

Resolution: fixed
