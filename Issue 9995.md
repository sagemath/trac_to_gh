# Issue 9995: Flint is installing shared library with .so extension on AIX - it should be .a on AIX

archive/issues_009995.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  goodwillhart@googlemail.com jpflori chapoton\n\n## Hardware and software\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1 \n\n## The problem\nFlint builds ok (see attached log), but the shared library has the wrong extension.\n\n\n```\n-bash-4.1$ ls local/lib/*flint*\nlocal/lib/libflint.so\n-bash-4.1$ file local/lib/libflint.so\nlocal/lib/libflint.so: executable (RISC System/6000) or object module not stripped\n```\n\n\nThis is not normal on AIX, where the extension for both shared and archive libraries should be `.a` and not `.so`. See \n[IBM compiler manual](http://publib.boulder.ibm.com/infocenter/comphelp/v7v91/index.jsp?topic=/com.ibm.vacpp7a.doc/getstart/overview/port_aix_obj_lib.htm) and [notes on GCC on AIX](http://www.ibm.com/developerworks/aix/library/au-gnu.html) \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9996\n\n",
    "created_at": "2010-09-24T02:17:14Z",
    "labels": [
        "porting: AIX or HP-UX",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Flint is installing shared library with .so extension on AIX - it should be .a on AIX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9995",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  goodwillhart@googlemail.com jpflori chapoton

## Hardware and software
* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1 

## The problem
Flint builds ok (see attached log), but the shared library has the wrong extension.


```
-bash-4.1$ ls local/lib/*flint*
local/lib/libflint.so
-bash-4.1$ file local/lib/libflint.so
local/lib/libflint.so: executable (RISC System/6000) or object module not stripped
```


This is not normal on AIX, where the extension for both shared and archive libraries should be `.a` and not `.so`. See 
[IBM compiler manual](http://publib.boulder.ibm.com/infocenter/comphelp/v7v91/index.jsp?topic=/com.ibm.vacpp7a.doc/getstart/overview/port_aix_obj_lib.htm) and [notes on GCC on AIX](http://www.ibm.com/developerworks/aix/library/au-gnu.html) 


Issue created by migration from https://trac.sagemath.org/ticket/9996





---

archive/issue_comments_100434.json:
```json
{
    "body": "Can you give me the uname -m or uname -a or whatever will tell me this is an AIX machine. It's only a single line in the flint makefile to fix this.\n\nI assume it is flint 1.6.",
    "created_at": "2012-06-01T18:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9995#issuecomment-100434",
    "user": "wbhart"
}
```

Can you give me the uname -m or uname -a or whatever will tell me this is an AIX machine. It's only a single line in the flint makefile to fix this.

I assume it is flint 1.6.



---

archive/issue_comments_100435.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9995#issuecomment-100435",
    "user": "embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100436.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9995#issuecomment-100436",
    "user": "mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_100437.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9995#issuecomment-100437",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100438.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9995#issuecomment-100438",
    "user": "chapoton"
}
```

Resolution: invalid
