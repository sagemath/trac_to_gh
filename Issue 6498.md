# Issue 6498: Compilation of ratpoints in sage-4.1.rc1 fails on 64-bit Gentoo Linux

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2009-07-09 10:57:12

Assignee: tbd

sage-4.1.rc1 doesn't compile on 64-bit Gentoo linux:

```
****************************************************
Host system
uname -a:
Linux massena 2.6.23-gentoo-r6 #1 SMP Wed Feb 6 21:49:58 CET 2008 x86_64 Intel(R) Xeon(R) CPU           X5365  `@` 3.00GHz GenuineIntel GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: x86_64-pc-linux-gnu
Configured with: /var/tmp/portage/sys-devel/gcc-4.1.1-r3/work/gcc-4.1.1/configure --prefix=/usr --bindir=/usr/x86_64-pc-linux-gnu/gcc-bin/4.1.1 --includedir=/usr/lib/gcc/x86_64-pc-linux-gnu/4.1.1/include --datadir=/usr/share/gcc-data/x86_64-pc-linux-gnu/4.1.1 --mandir=/usr/share/gcc-data/x86_64-pc-linux-gnu/4.1.1/man --infodir=/usr/share/gcc-data/x86_64-pc-linux-gnu/4.1.1/info --with-gxx-include-dir=/usr/lib/gcc/x86_64-pc-linux-gnu/4.1.1/include/g++-v4 --host=x86_64-pc-linux-gnu --build=x86_64-pc-linux-gnu --disable-altivec --enable-nls --without-included-gettext --with-system-zlib --disable-checking --disable-werror --enable-secureplt --disable-libunwind-exceptions --enable-multilib --disable-libmudflap --disable-libssp --disable-libgcj --enable-languages=c,c++,fortran --enable-shared --enable-threads=posix --enable-__cxa_atexit --enable-clocale=gnu
Thread model: posix
gcc version 4.1.1 (Gentoo 4.1.1-r3)
****************************************************
make[2]: Entering directory `/home/combi/saliola/Applications/sage-4.1/spkg/build/ratpoints-2.1.2/src'
gcc sift.c -c -o sift.o -I/home/combi/saliola/Applications/sage-4.1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -funroll-loops 
sift.c: In function '_ratpoints_sift0':
sift.c:320: error: unrecognizable insn:
(insn 436 435 437 62 (set (reg:DI 197)
        (vec_select:DI (reg/v:V2DI 109 [ nums ])
            (parallel [
                    (const_int 1 [0x1])
                ]))) -1 (nil)
    (nil))
sift.c:320: internal compiler error: in extract_insn, at recog.c:2084
Please submit a full bug report,
with preprocessed source if appropriate.
See <URL:http://bugs.gentoo.org/> for instructions.
Preprocessed source stored into /tmp/ccwZDjb1.out file, please attach this to your bugreport.
make[2]: *** [sift.o] Error 1
make[2]: Leaving directory `/home/combi/saliola/Applications/sage-4.1/spkg/build/ratpoints-2.1.2/src'
./spkg-install: line 34: [: Linux: integer expression expected
Error building ratpoints

real	0m0.225s
user	0m0.188s
sys	0m0.036s
sage: An error occurred while installing ratpoints-2.1.2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/combi/saliola/Applications/sage-4.1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/combi/saliola/Applications/sage-4.1/spkg/build/ratpoints-2.1.2 and type 'make'.
Instead type "/home/combi/saliola/Applications/sage-4.1/sage -sh"
in order to set all environment variables correctly, then cd to
/home/combi/saliola/Applications/sage-4.1/spkg/build/ratpoints-2.1.2
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/ratpoints-2.1.2] Error 1
make[1]: Leaving directory `/home/combi/saliola/Applications/sage-4.1/spkg'

real	80m22.622s
user	57m31.264s
sys	6m55.218s
Error building Sage.
```




---

Comment by saliola created at 2009-07-09 11:04:49

This seems to be related to #6492. After using the 2.1.2.p1 spkg linked to
from that ticket, ratpoints compiles. (4.1.rc1 is not yet done compiling,
but it made it passed ratpoints.)


---

Comment by saliola created at 2009-07-09 13:08:02

Replying to [comment:1 saliola]:
> This seems to be related to #6492. After using the 2.1.2.p1 spkg linked to
> from that ticket, ratpoints compiles. (4.1.rc1 is not yet done compiling,
> but it made it passed ratpoints.)

4.1.rc1 compiles fine with the proposed ratpoints package.

`make ptest` gave the following timeout errors:


```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/schemes/plane_curves/projective_curve.py # 0 doctests failed
        sage -t  devel/sage/sage/rings/homset.py # 0 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 0 doctests failed
----------------------------------------------------------------------
```


I re-ran the tests several times and `homset.py` and
`projective_curve.py` always passed. `multi_polynomial_ideal.py`,
more often than not, just timed out.

Can these be related to ratpoints?


---

Comment by rlm created at 2009-07-09 18:20:39

Resolution: duplicate


---

Comment by rlm created at 2009-07-09 18:20:39

Since the other ticket provides a fix I am filing this as duplicate.


---

Comment by rlm created at 2009-07-09 18:20:39

Changing component from algebra to distribution.
