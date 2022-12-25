# Issue 9987: zlib 1.2.5 installs zlib library with a .so extension on AIX when it should be .a

archive/issues_009987.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  madler@alumni.caltech.edu @fchapoton\n\nI'm cc'ing Mark Adler on this, as he is the maintainer of the zlib package. It would appear that zlib is building the shared library with the wrong extension on AIX. Rather unconventionally, AIX uses .a for shared libraries. \n\nIf Mark needs access to an AIX machine, I can the following:\n\n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1\n\n\n```\n-bash-4.1$ ls -l local/lib/libz*       \n-rw-r--r--   1 drkirkby staff        123336 23 Sep 15:37 local/lib/libz.a\nlrwxrwxrwx   1 drkirkby staff            13 23 Sep 15:37 local/lib/libz.so -> libz.so.1.2.5\nlrwxrwxrwx   1 drkirkby staff            13 23 Sep 15:37 local/lib/libz.so.1 -> libz.so.1.2.5\n-rwxr-xr-x   1 drkirkby staff        393465 23 Sep 15:37 local/lib/libz.so.1.2.5\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9988\n\n",
    "created_at": "2010-09-23T21:29:55Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "zlib 1.2.5 installs zlib library with a .so extension on AIX when it should be .a",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9987",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  madler@alumni.caltech.edu @fchapoton

I'm cc'ing Mark Adler on this, as he is the maintainer of the zlib package. It would appear that zlib is building the shared library with the wrong extension on AIX. Rather unconventionally, AIX uses .a for shared libraries. 

If Mark needs access to an AIX machine, I can the following:


* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1


```
-bash-4.1$ ls -l local/lib/libz*       
-rw-r--r--   1 drkirkby staff        123336 23 Sep 15:37 local/lib/libz.a
lrwxrwxrwx   1 drkirkby staff            13 23 Sep 15:37 local/lib/libz.so -> libz.so.1.2.5
lrwxrwxrwx   1 drkirkby staff            13 23 Sep 15:37 local/lib/libz.so.1 -> libz.so.1.2.5
-rwxr-xr-x   1 drkirkby staff        393465 23 Sep 15:37 local/lib/libz.so.1.2.5
```



Issue created by migration from https://trac.sagemath.org/ticket/9988





---

archive/issue_comments_100182.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9987#issuecomment-100182",
    "user": "https://github.com/embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100183.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9987#issuecomment-100183",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100184.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9987#issuecomment-100184",
    "user": "https://github.com/mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_events_010111.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2020-06-25T13:33:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9987",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9987#event-10111"
}
```



---

archive/issue_comments_100185.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9987#issuecomment-100185",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
