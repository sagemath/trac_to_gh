# Issue 9550: Upgrading 4.4.4 binary --> 4.5.1 fails on opencdk

Issue created by migration from https://trac.sagemath.org/ticket/9550

Original creator: rlm

Original creation time: 2010-07-19 12:00:03

Assignee: GeorgSWeber

CC:  was


```
make[1]: Entering directory `/scratch/rlmill/sage-4.4.4-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/spkg/build/opencdk-0.6.6.p5/src'
make  all-recursive
make[2]: Entering directory `/scratch/rlmill/sage-4.4.4-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/spkg/build/opencdk-0.6.6.p5/src'
Making all in src
make[3]: Entering directory `/scratch/rlmill/sage-4.4.4-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/spkg/build/opencdk-0.6.6.p5/src/src'
/bin/bash ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I..  -I/home/wstein/build/sage-4.4.4/local/include -I../lib -I../lib   -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -MT new-packet.lo -MD -MP -MF .deps/new-packet.Tpo -c -o new-packet.lo new-packet.c
mkdir .libs
 gcc -DHAVE_CONFIG_H -I. -I.. -I/home/wstein/build/sage-4.4.4/local/include -I../lib -I../lib -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -MT new-packet.lo -MD -MP -MF .deps/new-packet.Tpo -c new-packet.c  -fPIC -DPIC -o .libs/new-packet.o
In file included from new-packet.c:23:
opencdk.h:23:20: error: gcrypt.h: No such file or directory
```



---

Comment by was created at 2010-07-20 10:16:11

NOTE: this happened when upgrading a binary.  I've upgraded *source* installs with no trouble.


---

Comment by jdemeyer created at 2013-12-19 12:06:09

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-19 12:06:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-12-19 20:10:59

Probably too late to investigate ;-)


---

Comment by vbraun created at 2013-12-19 20:10:59

Resolution: wontfix
