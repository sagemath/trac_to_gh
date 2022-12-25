# Issue 4092: [with spkg, positive review] libm4ri-20080904 fails to build on OSX 10.4

archive/issues_004092.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  anakha\n\nI thought we fixed that:\n\n```\nchecking for a BSD-compatible install... /usr/bin/install -c \nchecking mm_malloc.h usability... no \nchecking mm_malloc.h presence... no \nchecking for mm_malloc.h... no \nchecking for a sed that does not truncate output... /usr/bin/sed \nchecking the number of available CPUs... 1 \nchecking the number of available CPUs... 1 \nchecking for x86 cpuid 0x0 output... unknown \nchecking for the processor vendor... Unknown \n262144 \n32768 \nsecond level name l1cachesize in hw.l1cachesize is invalid \nsecond level name l1cachesize in hw.l1cachesize is invalid \n./configure: line 21633: / 1024: syntax error: operand expected (error \ntoken is \"/ 1024\") \nError configuring libm4ri \n```\n\nMalb: any chance we missed a patch that did not make it in?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4092\n\n",
    "closed_at": "2008-09-10T02:47:28Z",
    "created_at": "2008-09-09T18:52:10Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, positive review] libm4ri-20080904 fails to build on OSX 10.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

CC:  anakha

I thought we fixed that:

```
checking for a BSD-compatible install... /usr/bin/install -c 
checking mm_malloc.h usability... no 
checking mm_malloc.h presence... no 
checking for mm_malloc.h... no 
checking for a sed that does not truncate output... /usr/bin/sed 
checking the number of available CPUs... 1 
checking the number of available CPUs... 1 
checking for x86 cpuid 0x0 output... unknown 
checking for the processor vendor... Unknown 
262144 
32768 
second level name l1cachesize in hw.l1cachesize is invalid 
second level name l1cachesize in hw.l1cachesize is invalid 
./configure: line 21633: / 1024: syntax error: operand expected (error 
token is "/ 1024") 
Error configuring libm4ri 
```

Malb: any chance we missed a patch that did not make it in?

Issue created by migration from https://trac.sagemath.org/ticket/4092





---

archive/issue_comments_029462.json:
```json
{
    "body": "I thought so too and it was confirmed over at #4059. Adding anakha (the author of the fixes of #4059) as CC.",
    "created_at": "2008-09-09T18:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29462",
    "user": "https://github.com/malb"
}
```

I thought so too and it was confirmed over at #4059. Adding anakha (the author of the fixes of #4059) as CC.



---

archive/issue_comments_029463.json:
```json
{
    "body": "a autoconf call was missing",
    "created_at": "2008-09-09T19:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29463",
    "user": "https://github.com/malb"
}
```

a autoconf call was missing



---

archive/issue_comments_029464.json:
```json
{
    "body": "New spkg at\n\n  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080909.spkg",
    "created_at": "2008-09-09T19:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29464",
    "user": "https://github.com/malb"
}
```

New spkg at

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080909.spkg



---

archive/issue_comments_029465.json:
```json
{
    "body": "You did miss the v4 patch over at #4059 if this shows up now.  The posted package does integrate it so everything should be alright.  \n\nI can't test it myself, since I don't have any machines with 10.4 though.",
    "created_at": "2008-09-09T19:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29465",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

You did miss the v4 patch over at #4059 if this shows up now.  The posted package does integrate it so everything should be alright.  

I can't test it myself, since I don't have any machines with 10.4 though.



---

archive/issue_comments_029466.json:
```json
{
    "body": "It works for me now on a Dual G5 OSX 10.4 box:\n\n```\nchecking for a sed that does not truncate output... /usr/bin/sed\nchecking the number of available CPUs... 2 \nchecking the number of available CPUs... 2 \nchecking for x86 cpuid 0x0 output... unknown\nchecking for the processor vendor... Unknown\nchecking the L1 cache size... 32768 Bytes\nchecking the L2 cache size... 524288 Bytes\nchecking whether make sets $(MAKE)... (cached) yes\nconfigure: creating ./config.status\n```\n\nI will do some build testing on other machines before giving this a positive review :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T19:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

It works for me now on a Dual G5 OSX 10.4 box:

```
checking for a sed that does not truncate output... /usr/bin/sed
checking the number of available CPUs... 2 
checking the number of available CPUs... 2 
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... 32768 Bytes
checking the L2 cache size... 524288 Bytes
checking whether make sets $(MAKE)... (cached) yes
configure: creating ./config.status
```

I will do some build testing on other machines before giving this a positive review :)

Cheers,

Michael



---

archive/issue_comments_029467.json:
```json
{
    "body": "Builds fine on \n\n* Linux x86, x86-64, Itanium\n* Solaris \n* OSX 10.5 Intel and OSX 10.4 PPC\n\nSo: positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-10T02:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Builds fine on 

* Linux x86, x86-64, Itanium
* Solaris 
* OSX 10.5 Intel and OSX 10.4 PPC

So: positive review.

Cheers,

Michael



---

archive/issue_comments_029468.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-10T02:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29468",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029469.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-10T02:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4092#issuecomment-29469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc2



---

archive/issue_events_009330.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-10T02:47:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4092",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4092#event-9330"
}
```
