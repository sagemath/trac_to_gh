# Issue 7171: HP-UX failure of libm4ri 20090617 as it attempts to find L1 cache size

archive/issues_007171.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: HP-UX L1 cache\n\nThe code appears to be trying to find information about the number of CPUS, the fails completely trying to find the L1 cache size\n\nIt would seem sensible to me the authors change the code so it does not break if it can't get the information it needs. \n\nHowever, in the case of HP-UX, I can give them access to the box, but even then you could get another Unix system where you don't know what CPUs it has, or the cache size. In which case assume something sensible  \n\n\n```\n\nchecking whether to build shared libraries... yes\nchecking whether to build static libraries... yes\nchecking for a BSD-compatible install... ./install-sh -c\nchecking mm_malloc.h usability... no\nchecking mm_malloc.h presence... no\nchecking for mm_malloc.h... no\nchecking the number of available CPUs... unable to detect (assuming 1)\nchecking the number of available CPUs... unable to detect (assuming 1)\nchecking for x86 cpuid 0x0 output... unknown\nchecking for the processor vendor... Unknown\nchecking the L1 cache size... ./configure[12992]: unknown*1024: The specified number is not valid for this command.\nMake: No arguments or description file.  Stop.\nError building libm4ri\n\nreal    0m18.199s\nuser    0m10.660s\nsys     0m5.770s\nsage: An error occurred while installing libm4ri-20090617\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home/drkirkby/sage-4.1.2.rc0/install.log.  Describe your computer, operating system, etc.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7171\n\n",
    "created_at": "2009-10-10T07:56:59Z",
    "labels": [
        "porting",
        "minor",
        "bug"
    ],
    "title": "HP-UX failure of libm4ri 20090617 as it attempts to find L1 cache size",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7171",
    "user": "drkirkby"
}
```
Assignee: tbd

Keywords: HP-UX L1 cache

The code appears to be trying to find information about the number of CPUS, the fails completely trying to find the L1 cache size

It would seem sensible to me the authors change the code so it does not break if it can't get the information it needs. 

However, in the case of HP-UX, I can give them access to the box, but even then you could get another Unix system where you don't know what CPUs it has, or the cache size. In which case assume something sensible  


```

checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking for a BSD-compatible install... ./install-sh -c
checking mm_malloc.h usability... no
checking mm_malloc.h presence... no
checking for mm_malloc.h... no
checking the number of available CPUs... unable to detect (assuming 1)
checking the number of available CPUs... unable to detect (assuming 1)
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... ./configure[12992]: unknown*1024: The specified number is not valid for this command.
Make: No arguments or description file.  Stop.
Error building libm4ri

real    0m18.199s
user    0m10.660s
sys     0m5.770s
sage: An error occurred while installing libm4ri-20090617
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/drkirkby/sage-4.1.2.rc0/install.log.  Describe your computer, operating system, etc.

```


Issue created by migration from https://trac.sagemath.org/ticket/7171





---

archive/issue_comments_059435.json:
```json
{
    "body": "I have uploaded a new SPKG to #7375",
    "created_at": "2009-11-18T16:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7171#issuecomment-59435",
    "user": "malb"
}
```

I have uploaded a new SPKG to #7375



---

archive/issue_comments_059436.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7171#issuecomment-59436",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059437.json:
```json
{
    "body": "Fixed by #7375",
    "created_at": "2009-11-29T05:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7171#issuecomment-59437",
    "user": "mhansen"
}
```

Fixed by #7375
