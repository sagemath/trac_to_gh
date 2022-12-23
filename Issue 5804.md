# Issue 5804: Solaris 10/Sparc: number_of_partitions(100000) is broken

Issue created by migration from https://trac.sagemath.org/ticket/5804

Original creator: mabshoff

Original creation time: 2009-04-16 09:49:26

Assignee: mabshoff

CC:  pjeremy


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



---

Comment by mabshoff created at 2009-04-16 09:52:41

I suspect that the use of sqrtl() for the computation of some constants causes the trouble here. Note that it also fails on FreeBSD where Peter has to use sqrt() there since sqrtl() is not available. One potential fix I have in mind is to use MPFR to compute those constants, but I have not investigated the problem.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 01:18:02

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

Attachment


---

Comment by was created at 2009-04-29 01:21:51

Give Bill hart credit too!


---

Comment by was created at 2009-04-29 01:25:36

Changing priority from major to blocker.


---

Comment by mhansen created at 2009-04-29 01:27:25

Looks good to me.


---

Comment by mabshoff created at 2009-04-29 23:09:16

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-29 23:09:16

Resolution: fixed
