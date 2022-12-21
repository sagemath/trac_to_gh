# Issue 238: create a  meataxe-2.4.3.spkg package

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-02 19:28:06

Assignee: was

Just do sage -f -m meataxe-2.4.3.spkg and watch it crash and burn, then follow
the error message and start hacking!

```

...
Compiling library module grtable
Compiling library module homcomp
Compiling library module imatcore
Compiling library module imatread
Compiling library module imatwrite
Compiling library module init
Compiling library module intio
Compiling library module issub
Compiling library module isisom
Compiling library module kernel-0
Compiling library module ldiag
Compiling library module maddmul
Compiling library module mat2vec
Compiling library module matadd
Compiling library module matclean
Compiling library module matcmp
Compiling library module maketabF
maketabF.c:30: error: static declaration of 'tmult' follows non-static declaration
meataxe.h:149: error: previous declaration of 'tmult' was here
maketabF.c:31: error: static declaration of 'tadd' follows non-static declaration
meataxe.h:150: error: previous declaration of 'tadd' was here
maketabF.c:34: error: static declaration of 'taddinv' follows non-static declaration
meataxe.h:151: error: previous declaration of 'taddinv' was here
maketabF.c:35: error: static declaration of 'tmultinv' follows non-static declaration
meataxe.h:151: error: previous declaration of 'tmultinv' was here
make: *** [libmtx.a(maketabF.o)] Error 1

real    0m5.384s
user    0m3.320s
sys     0m1.631s
sage: An error occured while installing meataxe-2.4.3
Please email William Stein <wstein`@`gmail.com> explaining the
problem and send him the relevant part of
of /Users/was/s/install.log.  Don't send the whole thing.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/was/s/spkg/build/meataxe-2.4.3 and type 'make'.
Instead (using bash) type "source local/bin/sage-env" from the directory
/Users/was/s
in order to set all environment variables correctly, then cd to
/Users/was/s/spkg/build/meataxe-2.4.3

```



---

Comment by malb created at 2007-02-02 20:15:08

Resolution: fixed


---

Comment by malb created at 2007-02-02 20:15:08

At

  http://sage.math.washington.edu/home/malb/pkgs/meataxe-2.4.3.spkg

a fixed version may be found which installs fine on Debian Etch AMD64. Thus I tag this as fixed until further notice.
