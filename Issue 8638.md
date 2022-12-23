# Issue 8638: iconv -- make with SAGE_CHECK="yes" fails on iconv with x86_64 ubuntu

Issue created by migration from https://trac.sagemath.org/ticket/8638

Original creator: was

Original creation time: 2010-04-01 00:09:47

Assignee: kirkby


```

I just downloaded the source. and it includes your recent "don't make
iconv unless it's the right system"

export MAKE="make -j4"
export SAGE_CHECK="yes"
make

... lots of things...

****************************************************
Host system
uname -a:
Linux dellbees 2.6.31-20-generic #58-Ubuntu SMP Fri Mar 12 04:38:19
UTC 2010 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu
4.4.1-4ubuntu9'
--with-bugurl=file:///usr/share/doc/gcc-4.4/README.Bugs
--enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr
--enable-shared --enable-multiarch --enable-linker-build-id
--with-system-zlib --libexecdir=/usr/lib --without-included-gettext
--enable-threads=posix --with-gxx-include-dir=/usr/include/c++/4.4
--program-suffix=-4.4 --enable-nls --enable-clocale=gnu
--enable-libstdcxx-debug --enable-objc-gc --disable-werror
--with-arch-32=i486 --with-tune=generic --enable-checking=release
--build=x86_64-linux-gnu --host=x86_64-linux-gnu
--target=x86_64-linux-gnu
Thread model: posix
gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu9)
****************************************************
Removing old iconv files if they exist
iconv will not be installed, as it is only installed on
Solaris and Cygwin - see:
http://trac.sagemath.org/sage_trac/ticket/8567

real    0m0.043s
user    0m0.000s
sys     0m0.010s
Successfully installed iconv-1.13.1.p0
Running the test suite.
make[2]: Entering directory
`/home/wjlaffin/_sage/spkg/build/iconv-1.13.1.p0/src'
make[2]: *** No rule to make target `check'.  Stop.
make[2]: Leaving directory `/home/wjlaffin/_sage/spkg/build/iconv-1.13.1.p0/src'
Error encountered while running the iconv testsuite ... exiting
*************************************
Error testing package ** iconv-1.13.1.p0 **
*************************************
sage: An error occurred while testing iconv-1.13.1.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wjlaffin/_sage/install.log.  Describe your computer,
operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/home/wjlaffin/_sage/spkg/build/iconv-1.13.1.p0 and type 'make check'
or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/home/wjlaffin/_sage/spkg/build/iconv-1.13.1.p0' &&
'/home/wjlaffin/_sage/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/iconv-1.13.1.p0] Error 1
make[1]: Leaving directory `/home/wjlaffin/_sage/spkg'

real    0m2.142s
user    0m1.950s
sys     0m0.140s
Error building Sage.
wjlaffin@dellbees:~/_sage$
```



---

Comment by jhpalmieri created at 2010-04-01 01:34:18

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-01 01:34:18

Try the spkg here:

[http://sage.math.washington.edu/home/palmieri/SPKG/iconv-1.13.1.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/iconv-1.13.1.p2.spkg)


---

Comment by ddrake created at 2010-04-01 23:21:22

This spkg works properly on Linux (Ubuntu) and on t2.math and the change is simple enough. I haven't tested this on Cygwin, though. I think if someone tries this on Cygwin, we can call this a positive review. Or, if someone can confirm that the $UNAME variable in Cygwin is literally "CYGWIN", I think we could also make this a positive review, since that's the string that spkg-check tests for.


---

Comment by was created at 2010-04-02 13:36:14

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-02 13:36:14

Replying to [comment:2 ddrake]:
>  Or, if someone can confirm that the $UNAME variable in Cygwin is literally "CYGWIN",
>  I think we could also make this a positive review, since that's the string that spkg-check tests for.

I can confirm that, since I wrote the code (which is in sage-env) to set UNAME, and that's what it is set to.

 -- William


---

Comment by jhpalmieri created at 2010-04-16 17:23:31

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 17:23:31

Merged in 4.4.alpha0.
