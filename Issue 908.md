# Issue 908: paru/gen.c causes internal compiler error on OpenSuSE 10.2

Issue created by migration from https://trac.sagemath.org/ticket/908

Original creator: wdj

Original creation time: 2007-10-16 16:07:35

Assignee: mabshoff

When building 2.8.7 on suse 10.2 amd64:

> -I/home/wdj/sagefiles/sage-2.8.7/local/include/python2.5 -c
> sage/libs/pari/gen.c -o
> build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w
> sage/libs/pari/gen.c: In function '__pyx_f_py_3gen_3gen_factor':
> sage/libs/pari/gen.c:19784: internal compiler error: in
> merge_alias_info, at tree-ssa-copy.c:235
> Please submit a full bug report,
> with preprocessed source if appropriate.

"gcc blows up ..."

wdj`@`tinah:~/sagefiles/sage-2.8.7> uname -a
Linux tinah 2.6.16.13-4-default #1 Wed May 3 04:53:23 UTC 2006 x86_64 x86_64 x86_64 GNU/Linux
wdj`@`tinah:~/sagefiles/sage-2.8.7> gcc -v
Using built-in specs.
Target: x86_64-suse-linux
Configured with: ../configure --enable-threads=posix --prefix=/usr --with-local-prefix=/usr/local --infodir=/usr/share/info --mandir=/usr/share/man --libdir=/usr/lib64 --libexecdir=/usr/lib64 --enable-languages=c,c++,objc,fortran,java,ada --enable-checking=release --with-gxx-include-dir=/usr/include/c++/4.1.0 --enable-ssp --disable-libssp --enable-java-awt=gtk --enable-gtk-cairo --disable-libjava-multilib --with-slibdir=/lib64 --with-system-zlib --enable-shared --enable-__cxa_atexit --enable-libstdcxx-allocator=new --without-system-libunwind --with-cpu=generic --host=x86_64-suse-linux
Thread model: posix
gcc version 4.1.0 (SUSE Linux)


---

Comment by mabshoff created at 2007-10-16 16:45:30

It is a known regression. See

http://gcc.gnu.org/ml/gcc-bugs/2006-04/msg00700.html
http://lists.debian.org/debian-gcc/2006/05/msg00139.html

I think there is little we can do except to recommend upgrading to a proper compiler.

Cheers,

Michael


---

Comment by was created at 2007-10-16 18:20:24

I disagree that the only solution is to recommend a proper compiler.  We're not the GMP project after all.

Sage-2.8.5 compiled fine on SUSE, so this problem only
occurs with a very recent version of gen.pyx.   I recently modified
the factor function in gen.pyx so that it would do provably-correct
factorization of integers.   Since that's the function causing the compiler
error, probably something I did caused this.    

I'll likely make some attempts to modify my implementation
to see if I can get around the broken compilers on SUSE.

 -- William


---

Comment by was created at 2007-10-16 18:20:28

Changing assignee from mabshoff to was.


---

Comment by was created at 2007-10-16 18:20:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-16 18:54:02

Well, that remark about GMP is just priceless 8).

If you find a workaround that should solve this problem I am obviously fine with it, but recently we have seen more and more issues with gcc throwing in the towel, so I still think that the internal tool chain for Sage has its purpose. And we pretty much agree that this is the only way to go on Solaris, Linux Itanium and so on.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-02 08:57:29

Hello,

good news for SuSE 10.2 user:

```
[09:33] <Syzygy-> Hmph. I cannot get yast to tell me what the g77-package is named. *grmbl*
[09:33] <mabshoff> Which SuSE release?
[09:34] <mabshoff> Hi malb__
[09:34] <malb__> hi
[09:34] <mabshoff> You should probably install gfortran
[09:34] <mabshoff> 10.3 no longer ships g77 or g95, but gfortran.
[09:34] <Syzygy-> OpenSuSE 10.2
[09:34] <Syzygy-> Right.
[09:35] <mabshoff> Really? There is a bug in that gcc that crashes when compiling gen.c
[09:35] <mabshoff> Does Sage start and compute 2+2?
[09:35] <Syzygy-> Yes.
[09:35] <mabshoff> ok, but then you probably update via yast.
[09:35] <Syzygy-> gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)
[09:36] <mabshoff> Thanks
[09:36] <mabshoff> Excellent, you just closed ticket #908.
[09:37] <Syzygy-> Hehe
[09:37] <Syzygy-> Happy to help. :)
```


So we should close this ticket and recommend for people to update via yast to the latest gcc rpms that SuSE provides.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-02 08:57:29

Resolution: fixed
