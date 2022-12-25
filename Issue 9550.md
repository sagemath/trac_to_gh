# Issue 9550: Upgrading 4.4.4 binary --> 4.5.1 fails on opencdk

archive/issues_009550.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @williamstein\n\n```\nmake[1]: Entering directory `/scratch/rlmill/sage-4.4.4-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/spkg/build/opencdk-0.6.6.p5/src'\nmake  all-recursive\nmake[2]: Entering directory `/scratch/rlmill/sage-4.4.4-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/spkg/build/opencdk-0.6.6.p5/src'\nMaking all in src\nmake[3]: Entering directory `/scratch/rlmill/sage-4.4.4-linux-64bit-ubuntu_8.04.4_lts-x86_64-Linux/spkg/build/opencdk-0.6.6.p5/src/src'\n/bin/bash ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I..  -I/home/wstein/build/sage-4.4.4/local/include -I../lib -I../lib   -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -MT new-packet.lo -MD -MP -MF .deps/new-packet.Tpo -c -o new-packet.lo new-packet.c\nmkdir .libs\n gcc -DHAVE_CONFIG_H -I. -I.. -I/home/wstein/build/sage-4.4.4/local/include -I../lib -I../lib -g -O2 -Wall -Wcast-align -Wshadow -Wstrict-prototypes -MT new-packet.lo -MD -MP -MF .deps/new-packet.Tpo -c new-packet.c  -fPIC -DPIC -o .libs/new-packet.o\nIn file included from new-packet.c:23:\nopencdk.h:23:20: error: gcrypt.h: No such file or directory\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9550\n\n",
    "created_at": "2010-07-19T12:00:03Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Upgrading 4.4.4 binary --> 4.5.1 fails on opencdk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9550",
    "user": "https://github.com/rlmill"
}
```
Assignee: GeorgSWeber

CC:  @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/9550





---

archive/issue_comments_091903.json:
```json
{
    "body": "NOTE: this happened when upgrading a binary.  I've upgraded *source* installs with no trouble.",
    "created_at": "2010-07-20T10:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9550#issuecomment-91903",
    "user": "https://github.com/williamstein"
}
```

NOTE: this happened when upgrading a binary.  I've upgraded *source* installs with no trouble.



---

archive/issue_events_023759.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9550#event-23759"
}
```



---

archive/issue_events_023760.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-19T12:06:09Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9550#event-23760"
}
```



---

archive/issue_events_023761.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-19T12:06:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9550#event-23761"
}
```



---

archive/issue_comments_091904.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-19T12:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9550#issuecomment-91904",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091905.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-19T12:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9550#issuecomment-91905",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091906.json:
```json
{
    "body": "Probably too late to investigate ;-)",
    "created_at": "2013-12-19T20:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9550#issuecomment-91906",
    "user": "https://github.com/vbraun"
}
```

Probably too late to investigate ;-)



---

archive/issue_events_023762.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2013-12-19T20:10:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9550#event-23762"
}
```



---

archive/issue_comments_091907.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-12-19T20:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9550#issuecomment-91907",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
