# Issue 9997: NTL is building the shared library with the wrong extension on AIX

archive/issues_009997.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @fchapoton\n\n## Hardware and software\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1 (which has ntl-5.4.2.p12)\n\n\n```\nbash-4.1$ ls -l local/lib/libntl*\n-rwxr-xr-x   1 drkirkby staff      26740371 23 Sep 18:12 local/lib/libntl-5.4.2.so\n-rw-r--r--   1 drkirkby staff      29165744 23 Sep 18:12 local/lib/libntl.a\nlrwxrwxrwx   1 drkirkby staff            15 23 Sep 18:12 local/lib/libntl.so -> libntl-5.4.2.so\n```\n\n\n\n```\n-bash-4.1$ file local/lib/libntl*\nlocal/lib/libntl-5.4.2.so: executable (RISC System/6000) or object module not stripped\nlocal/lib/libntl.a: archive (big format)\nlocal/lib/libntl.so: executable (RISC System/6000) or object module not stripped\n-bash-4.1$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9998\n\n",
    "created_at": "2010-09-24T02:33:06Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "NTL is building the shared library with the wrong extension on AIX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9997",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @fchapoton

## Hardware and software
* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fairly wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1 (which has ntl-5.4.2.p12)


```
bash-4.1$ ls -l local/lib/libntl*
-rwxr-xr-x   1 drkirkby staff      26740371 23 Sep 18:12 local/lib/libntl-5.4.2.so
-rw-r--r--   1 drkirkby staff      29165744 23 Sep 18:12 local/lib/libntl.a
lrwxrwxrwx   1 drkirkby staff            15 23 Sep 18:12 local/lib/libntl.so -> libntl-5.4.2.so
```



```
-bash-4.1$ file local/lib/libntl*
local/lib/libntl-5.4.2.so: executable (RISC System/6000) or object module not stripped
local/lib/libntl.a: archive (big format)
local/lib/libntl.so: executable (RISC System/6000) or object module not stripped
-bash-4.1$ 
```


Issue created by migration from https://trac.sagemath.org/ticket/9998





---

archive/issue_comments_100279.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9997#issuecomment-100279",
    "user": "https://github.com/embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100280.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9997#issuecomment-100280",
    "user": "https://github.com/mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_comments_100281.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9997#issuecomment-100281",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100282.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9997#issuecomment-100282",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
