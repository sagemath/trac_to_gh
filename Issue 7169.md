# Issue 7169: HP-UX PolyBoRi 0.6.3-20090827  fail to build on HP-UX 11i

Issue created by migration from https://trac.sagemath.org/ticket/7169

Original creator: drkirkby

Original creation time: 2009-10-10 07:29:52

Assignee: tbd

CC:  mkoeppe

Keywords: HP-EX

From an HP C3600, the following errors are noted. A PolyBoRi would be given access to the machine if they wanted to debug this



```
gcc -o M4RI/grayflex.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/grayflex.c
gcc -o M4RI/permutation.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/permutation.c
gcc -o M4RI/packedmatrix.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/packedmatrix.c
gcc -o M4RI/strassen.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/strassen.c
gcc -o M4RI/misc.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/misc.c
gcc -o M4RI/brilliantrussian.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd M4RI/brilliantrussian.c
ar rc groebner/libgroebner.a groebner/src/groebner.o groebner/src/literal_factorization.o groebner/src/randomset.o groebner/src/pairs.o groebner/src/groebner_alg.o groebner/src/fglm.o groebner/src/polynomial_properties.o groebner/src/lexbuckets.o groebner/src/dlex4data.o groebner/src/dp_asc4data.o groebner/src/lp4data.o groebner/src/nf.o groebner/src/interpolate.o M4RI/grayflex.o M4RI/permutation.o M4RI/packedmatrix.o M4RI/strassen.o M4RI/misc.o M4RI/brilliantrussian.o polybori/libpolybori.a
ranlib groebner/libgroebner.a
g++ -o Cudd/obj/cuddObj.o -c -O3 -Wno-long-long -Wreturn-type -g -fPIC -ftemplate-depth-100 -g -fPIC -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd Cudd/obj/cuddObj.cc
gcc -o Cudd/util/texpand.o -c -std=c99 -O3 -Wno-long-long -Wreturn-type -g -fPIC -DNDEBUG -DHAVE_TR1_UNORDERED_MAP -DPACKED -DHAVE_M4RI -DHAVE_GD -DHAVE_IEEE_754 -DBSD -I/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827/src/boost_1_34_1.cropped -I/home/drkirkby/sage-4.1.2.rc0/local/include -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -Ipolybori/include -IM4RI -ICudd/obj -ICudd/util -ICudd/cudd -ICudd/mtr -ICudd/st -ICudd/epd Cudd/util/texpand.c
Cudd/util/texpand.c: In function 'util_tilde_expand':
Cudd/util/texpand.c:39: warning: implicit declaration of function 'getpwuid'
Cudd/util/texpand.c:39: warning: implicit declaration of function 'getuid'
Cudd/util/texpand.c:39: warning: assignment makes pointer from integer without a cast
Cudd/util/texpand.c:40: error: dereferencing pointer to incomplete type
Cudd/util/texpand.c:46: warning: implicit declaration of function 'getpwnam'
Cudd/util/texpand.c:46: warning: assignment makes pointer from integer without a cast
Cudd/util/texpand.c:47: error: dereferencing pointer to incomplete type
scons: *** [Cudd/util/texpand.o] Error 1
scons: building terminated because of errors.
Error building PolyBoRi.

real    10m6.109s
user    9m34.380s
sys     0m18.300s
sage: An error occurred while installing polybori-0.6.3-20090827
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/drkirkby/sage-4.1.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827 and type 'make'.
Instead type "/home/drkirkby/sage-4.1.2.rc0/sage -sh"
in order to set all environment variables correctly, then cd to
/home/drkirkby/sage-4.1.2.rc0/spkg/build/polybori-0.6.3-20090827
(When you are done debugging, you can type "exit" to leave the
subshell.)
*** Error exit code 1

Stop.

real    10m28.223s
user    9m45.180s
sys     0m20.420s
Error building Sage.
```


It looks like pwd.h needs including. You could do that only on HP-UX by 


```
#ifdef hpux
#include <pwd.h>
#endif
```



---

Comment by drkirkby created at 2009-12-03 04:47:30

I've just added the PolyBori-discuss email address on the ticket. It may not appear, as the Trac is probably not subscribed. If is does not appear, I will report via a direct email. 

This looks very easy to fix.


---

Comment by drkirkby created at 2009-12-03 11:04:27

Changing keywords from "HP-EX" to "HP-UX".


---

Comment by drkirkby created at 2009-12-03 11:04:27

The email did not appear on  the polybori-discuss mailing list, so I sent it from my own account, from which I am a subscriber.


---

Comment by kcrisman created at 2011-02-16 22:33:21

Changing component from porting to AIX or HP-UX ports.


---

Comment by chapoton created at 2020-06-25 13:35:53

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-06-25 13:35:53

close as obsolete ?


---

Comment by mkoeppe created at 2020-06-25 17:10:48

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-06-25 17:22:07

Resolution: invalid
