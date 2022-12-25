# Issue 6539: MPIR determines linker is GNU when it's Sun on OpenSolaris - x86 NOT Sparc.

archive/issues_006539.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.net @dimpase\n\nKeywords: OpenSolaris x86\n\nThommy Malmstrom, thommy.m.malmstrom`@`gmail.com reported a problem to me with a failed build of Sage on an OpenSolaris (AMD or Intel processor).\n\n```\nHost system\nuname -a:\nSunOS bigblue 5.11 snv_101b i86pc i386 i86pc Solaris\n```\n\nWhat can be seen in the configure script's output is the linker is determined to be the GNU linker:\n\n\n```\nchecking for ld used by gcc -std=gnu99... ld\nchecking if the linker (ld) is GNU ld... yes\n```\n\n\nBut this is incorrect, as the output from the compiler shows:\n\n```\nConfigured with: /builds2/sfwnv-gate/usr/src/cmd/gcc/gcc-3.4.3/configure\n--prefix=/usr/sfw --with-as=/usr/sfw/bin/gas --with-gnu-as\n--with-ld=/usr/ccs/bin/ld --without-gnu-ld\n--enable-languages=c,c++,f77,objc --enable-shared\nThread model: posix\ngcc version 3.4.3 (csl-sol210-3_4-20050802)\n```\n\n\nThe error is a result of sending the -soname to the Sun linker, which generates an error - clearly this is nothing like you would expect from a GNU tool, and is the Sun linker:\n\n\n```\nusage: ld [-6:abc:d:e:f:h:il:mo:p:rstu:z:B:CD:F:GI:L:M:N:P:Q:R:S:VW:Y:?]\nfile(s)\n        [-64]           enforce a 64-bit link-edit\n        [-a]            create an absolute file\n        [-b]            do not do special PIC relocations in a.out\n        [-B direct | nodirect]\n                        establish direct bindings, or inhibit direct binding\n                        to, the object being created\n        [-B dynamic | static]\n                        search for shared libraries|archives\n        [-B eliminate]  eliminate unqualified global symbols from the\n                        symbol table\n        [-B group]      relocate object from within group\n        [-B local]      reduce unqualified global symbols to local\n\n```\n\nI've attached the part of the log connected with the building of mpir. \n\nThe configure script was generated using autoconf 2.61, which is about (Nov 2006), so is around two and a half years old. It might be that the old version does not perform too well on OpenSolaris, so I would suggest a later version is used to generate the configure script. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/6539\n\n",
    "created_at": "2009-07-16T00:27:17Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "MPIR determines linker is GNU when it's Sun on OpenSolaris - x86 NOT Sparc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6539",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.net @dimpase

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

Issue created by migration from https://trac.sagemath.org/ticket/6539





---

archive/issue_comments_053214.json:
```json
{
    "body": "Attachment [install-mpir.log](tarball://root/attachments/some-uuid/ticket6539/install-mpir.log) by drkirkby created at 2009-07-16 00:28:31\n\nThe output shown while building mpir.",
    "created_at": "2009-07-16T00:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53214",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [install-mpir.log](tarball://root/attachments/some-uuid/ticket6539/install-mpir.log) by drkirkby created at 2009-07-16 00:28:31

The output shown while building mpir.



---

archive/issue_comments_053215.json:
```json
{
    "body": "I've just tried to build mpir on what I believe is the same OS as above - the 11/2008 release of OpenSolaris and do not see this issue - the configure  script reconises this as a non-GNU linker properly. It is not clear why it should get it wrong on another system with the same OS\n\n\n```\n$ cat /etc/release\n                       OpenSolaris 2008.11 snv_101b_rc2 X86\n           Copyright 2008 Sun Microsystems, Inc.  All Rights Reserved.\n                        Use is subject to license terms.\n                           Assembled 19 November 2008\n```\n\n\n\nHere's the output of configure of mpir-1.2.p4\n\n\n```\n./configure \n<SNIP>\nchecking for a sed that does not truncate output... /usr/bin/gsed\nchecking for ld used by gcc -std=gnu99... /usr/ccs/bin/ld\nchecking if the linker (/usr/ccs/bin/ld) is GNU ld... no\nchecking for /usr/ccs/bin/ld option to reload object files... -r\n\n```\n",
    "created_at": "2009-07-22T01:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53215",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_053216.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53216",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053217.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53217",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_053218.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-09T13:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53218",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006775.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2020-07-15T07:18:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6539#event-6775"
}
```



---

archive/issue_comments_053219.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53219",
    "user": "https://github.com/fchapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.



---

archive/issue_comments_053220.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6539#issuecomment-53220",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
