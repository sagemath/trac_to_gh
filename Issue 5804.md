# Issue 5804: Solaris 10/Sparc: number_of_partitions(100000) is broken

archive/issues_005804.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @peterjeremy\n\n\n```\nsage -t  \"devel/sage/sage/combinat/partition.py\"            \n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3440:\n    sage: number_of_partitions(100000)\nExpected:\n    27493510569775696512677516320986352688173429315980054758203125984\n30214732811496417305505074166073662159015784477429624894049306307\n02004617927644930335101160793424571901557189435097253124661084520\n06369558934464248716828789832182345009262853831404597021307130674\n51062441922731123899970228440860937093553162969785156956989219610\n8480158600569421098519\nGot:\n    27493510569775696512677516320986352688173429315980054758203125984\n30214732811496417305505074166073662159015784477429624894049306307\n02004617927644930335101160793424571901557189435097253124661084520\n06369558934464248716828789832182345009262853831404597021307130674\n51062441922731123899970228440860937093553162969785156956989219610\n8480158600569425643053\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3469:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3475:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3478:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3481:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3484:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3487:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3490:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3493:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py\", line 3501:\n    sage: len([n for n in [1..500] if number_of_partitions(n) != number_of_partitions(n,algorithm='pari')])\nExpected:\n    0\nGot:\n    203\n**********************************************************************\n1 items had failures:\n  10 of  40 in __main__.example_119\n***Test Failed*** 10 failures.\nFor whitespace errors, see the file /home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/tmp/.doctest_partition.py\n         [68.3 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5804\n\n",
    "created_at": "2009-04-16T09:49:26Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Solaris 10/Sparc: number_of_partitions(100000) is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5804",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @peterjeremy


```
sage -t  "devel/sage/sage/combinat/partition.py"            
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3440:
    sage: number_of_partitions(100000)
Expected:
    27493510569775696512677516320986352688173429315980054758203125984
30214732811496417305505074166073662159015784477429624894049306307
02004617927644930335101160793424571901557189435097253124661084520
06369558934464248716828789832182345009262853831404597021307130674
51062441922731123899970228440860937093553162969785156956989219610
8480158600569421098519
Got:
    27493510569775696512677516320986352688173429315980054758203125984
30214732811496417305505074166073662159015784477429624894049306307
02004617927644930335101160793424571901557189435097253124661084520
06369558934464248716828789832182345009262853831404597021307130674
51062441922731123899970228440860937093553162969785156956989219610
8480158600569425643053
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3469:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3475:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3478:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3481:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3484:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3487:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3490:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3493:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/combinat/partition.py", line 3501:
    sage: len([n for n in [1..500] if number_of_partitions(n) != number_of_partitions(n,algorithm='pari')])
Expected:
    0
Got:
    203
**********************************************************************
1 items had failures:
  10 of  40 in __main__.example_119
***Test Failed*** 10 failures.
For whitespace errors, see the file /home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/tmp/.doctest_partition.py
         [68.3 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/5804





---

archive/issue_comments_045467.json:
```json
{
    "body": "I suspect that the use of sqrtl() for the computation of some constants causes the trouble here. Note that it also fails on FreeBSD where Peter has to use sqrt() there since sqrtl() is not available. One potential fix I have in mind is to use MPFR to compute those constants, but I have not investigated the problem.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T09:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I suspect that the use of sqrtl() for the computation of some constants causes the trouble here. Note that it also fails on FreeBSD where Peter has to use sqrt() there since sqrtl() is not available. One potential fix I have in mind is to use MPFR to compute those constants, but I have not investigated the problem.

Cheers,

Michael



---

archive/issue_comments_045468.json:
```json
{
    "body": "The issue here is that Sparc/x86 and Sparc/Solaris use different IEEE implementations:\n\n```\n#if defined(__i386) || defined(__amd64)\n\n/* Follows IEEE standards for 80-bit floating point */\n#define LDBL_MANT_DIG   64\n#define LDBL_EPSILON    1.0842021724855044340075E-19L\n#define LDBL_DIG        18\n#define LDBL_MIN_EXP    (-16381)\n#define LDBL_MIN        3.3621031431120935062627E-4932L\n#define LDBL_MIN_10_EXP (-4931)\n#define LDBL_MAX_EXP    (+16384)\n#define LDBL_MAX        1.1897314953572317650213E+4932L\n#define LDBL_MAX_10_EXP (+4932)\n\n#elif defined(__sparc)\n\n/* Follows IEEE standards for 128-bit floating point */\n#define LDBL_MANT_DIG   113\n#define LDBL_EPSILON    1.925929944387235853055977942584927319E-34L\n#define LDBL_DIG        33\n#define LDBL_MIN_EXP    (-16381)\n#define LDBL_MIN        3.362103143112093506262677817321752603E-4932L\n#define LDBL_MIN_10_EXP (-4931)\n#define LDBL_MAX_EXP    (+16384)\n#define LDBL_MAX        1.189731495357231765085759326628007016E+4932L\n#define LDBL_MAX_10_EXP (+4932)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T01:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45468",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue here is that Sparc/x86 and Sparc/Solaris use different IEEE implementations:

```
#if defined(__i386) || defined(__amd64)

/* Follows IEEE standards for 80-bit floating point */
#define LDBL_MANT_DIG   64
#define LDBL_EPSILON    1.0842021724855044340075E-19L
#define LDBL_DIG        18
#define LDBL_MIN_EXP    (-16381)
#define LDBL_MIN        3.3621031431120935062627E-4932L
#define LDBL_MIN_10_EXP (-4931)
#define LDBL_MAX_EXP    (+16384)
#define LDBL_MAX        1.1897314953572317650213E+4932L
#define LDBL_MAX_10_EXP (+4932)

#elif defined(__sparc)

/* Follows IEEE standards for 128-bit floating point */
#define LDBL_MANT_DIG   113
#define LDBL_EPSILON    1.925929944387235853055977942584927319E-34L
#define LDBL_DIG        33
#define LDBL_MIN_EXP    (-16381)
#define LDBL_MIN        3.362103143112093506262677817321752603E-4932L
#define LDBL_MIN_10_EXP (-4931)
#define LDBL_MAX_EXP    (+16384)
#define LDBL_MAX        1.189731495357231765085759326628007016E+4932L
#define LDBL_MAX_10_EXP (+4932)
```


Cheers,

Michael



---

archive/issue_comments_045469.json:
```json
{
    "body": "Attachment [trac_5804.patch](tarball://root/attachments/some-uuid/ticket5804/trac_5804.patch) by @williamstein created at 2009-04-29 01:19:46",
    "created_at": "2009-04-29T01:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45469",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5804.patch](tarball://root/attachments/some-uuid/ticket5804/trac_5804.patch) by @williamstein created at 2009-04-29 01:19:46



---

archive/issue_comments_045470.json:
```json
{
    "body": "Give Bill hart credit too!",
    "created_at": "2009-04-29T01:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45470",
    "user": "https://github.com/williamstein"
}
```

Give Bill hart credit too!



---

archive/issue_events_013626.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-04-29T01:25:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5804#event-13626"
}
```



---

archive/issue_comments_045471.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-04-29T01:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45471",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_045472.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-04-29T01:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45472",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_045473.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T23:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45473",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_045474.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-29T23:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5804#issuecomment-45474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013627.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-29T23:09:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5804",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5804#event-13627"
}
```
