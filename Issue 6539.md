# Issue 6539: MPIR determines linker is GNU when it's Sun on OpenSolaris - x86 NOT Sparc.

Issue created by migration from https://trac.sagemath.org/ticket/6539

Original creator: drkirkby

Original creation time: 2009-07-16 00:27:17

Assignee: tbd

CC:  david.kirkby@onetel.net dimpase

Keywords: OpenSolaris x86

Thommy Malmstrom, thommy.m.malmstrom`@`gmail.com reported a problem to me with a failed build of Sage on an OpenSolaris (AMD or Intel processor).

```
Host system
uname -a:
SunOS bigblue 5.11 snv_101b i86pc i386 i86pc Solaris
```

What can be seen in the configure script's output is the linker is determined to be the GNU linker:


```
checking for ld used by gcc -std=gnu99... ld
checking if the linker (ld) is GNU ld... yes
```


But this is incorrect, as the output from the compiler shows:

```
Configured with: /builds2/sfwnv-gate/usr/src/cmd/gcc/gcc-3.4.3/configure
--prefix=/usr/sfw --with-as=/usr/sfw/bin/gas --with-gnu-as
--with-ld=/usr/ccs/bin/ld --without-gnu-ld
--enable-languages=c,c++,f77,objc --enable-shared
Thread model: posix
gcc version 3.4.3 (csl-sol210-3_4-20050802)
```


The error is a result of sending the -soname to the Sun linker, which generates an error - clearly this is nothing like you would expect from a GNU tool, and is the Sun linker:


```
usage: ld [-6:abc:d:e:f:h:il:mo:p:rstu:z:B:CD:F:GI:L:M:N:P:Q:R:S:VW:Y:?]
file(s)
        [-64]           enforce a 64-bit link-edit
        [-a]            create an absolute file
        [-b]            do not do special PIC relocations in a.out
        [-B direct | nodirect]
                        establish direct bindings, or inhibit direct binding
                        to, the object being created
        [-B dynamic | static]
                        search for shared libraries|archives
        [-B eliminate]  eliminate unqualified global symbols from the
                        symbol table
        [-B group]      relocate object from within group
        [-B local]      reduce unqualified global symbols to local

```

I've attached the part of the log connected with the building of mpir. 

The configure script was generated using autoconf 2.61, which is about (Nov 2006), so is around two and a half years old. It might be that the old version does not perform too well on OpenSolaris, so I would suggest a later version is used to generate the configure script. 

Dave 


---

Attachment

The output shown while building mpir.


---

Comment by drkirkby created at 2009-07-22 01:34:28

I've just tried to build mpir on what I believe is the same OS as above - the 11/2008 release of OpenSolaris and do not see this issue - the configure  script reconises this as a non-GNU linker properly. It is not clear why it should get it wrong on another system with the same OS


```
$ cat /etc/release
                       OpenSolaris 2008.11 snv_101b_rc2 X86
           Copyright 2008 Sun Microsystems, Inc.  All Rights Reserved.
                        Use is subject to license terms.
                           Assembled 19 November 2008
```



Here's the output of configure of mpir-1.2.p4


```
./configure 
<SNIP>
checking for a sed that does not truncate output... /usr/bin/gsed
checking for ld used by gcc -std=gnu99... /usr/ccs/bin/ld
checking if the linker (/usr/ccs/bin/ld) is GNU ld... no
checking for /usr/ccs/bin/ld option to reload object files... -r

```



---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by dimpase created at 2020-07-09 13:37:59

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
