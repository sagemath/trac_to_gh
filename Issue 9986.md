# Issue 9986: Shared readline library uses a .so extension on AIX when it should be .a

archive/issues_009986.json:
```json
{
    "body": "Assignee: drkirkby\n\nUsing the following system: \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* DDS-4 tape drive \n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* sage-4.6.alpha1\n\nReadline builds, but then if we look at the libraries, one has the wrong extension. \n\n\n```\n-bash-4.1$ ls -l local/lib/libreadline*\n-rwxr-xr-x   1 drkirkby staff       1739661 23 Sep 15:43 local/lib/libreadline.a\nlrwxrwxrwx   1 drkirkby staff            16 23 Sep 15:43 local/lib/libreadline.so -> libreadline.so.6\n-rwxr-xr-x   1 drkirkby staff       1145940 23 Sep 15:43 local/lib/libreadline.so.6\n-bash-4.1$ \n-bash-4.1$ \n-bash-4.1$ file local/lib/libreadline.a     local/lib/libreadline.so    local/lib/libreadline.so.6\nlocal/lib/libreadline.a: archive (big format)\nlocal/lib/libreadline.so: executable (RISC System/6000) or object module not stripped\nlocal/lib/libreadline.so.6: executable (RISC System/6000) or object module not stripped\n\n```\n\n\nI don't know AIX well, but I suspect the .a is a static library here, and the .so is a shared library. But AIX uses .a for shared libraries. (I don't know what it uses for static libraries - it might be .o). \n\nThis is probably a mis-configuration in Sage. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/9987\n\n",
    "created_at": "2010-09-23T21:20:05Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Shared readline library uses a .so extension on AIX when it should be .a",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9986",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

Using the following system: 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* DDS-4 tape drive 
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* sage-4.6.alpha1

Readline builds, but then if we look at the libraries, one has the wrong extension. 


```
-bash-4.1$ ls -l local/lib/libreadline*
-rwxr-xr-x   1 drkirkby staff       1739661 23 Sep 15:43 local/lib/libreadline.a
lrwxrwxrwx   1 drkirkby staff            16 23 Sep 15:43 local/lib/libreadline.so -> libreadline.so.6
-rwxr-xr-x   1 drkirkby staff       1145940 23 Sep 15:43 local/lib/libreadline.so.6
-bash-4.1$ 
-bash-4.1$ 
-bash-4.1$ file local/lib/libreadline.a     local/lib/libreadline.so    local/lib/libreadline.so.6
local/lib/libreadline.a: archive (big format)
local/lib/libreadline.so: executable (RISC System/6000) or object module not stripped
local/lib/libreadline.so.6: executable (RISC System/6000) or object module not stripped

```


I don't know AIX well, but I suspect the .a is a static library here, and the .so is a shared library. But AIX uses .a for shared libraries. (I don't know what it uses for static libraries - it might be .o). 

This is probably a mis-configuration in Sage. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/9987





---

archive/issue_comments_100177.json:
```json
{
    "body": "It appears AIX uses .a for both shared and static libs. But it understands .so too, so this can be closed as invalid.",
    "created_at": "2011-03-22T17:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9986#issuecomment-100177",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It appears AIX uses .a for both shared and static libs. But it understands .so too, so this can be closed as invalid.



---

archive/issue_comments_100178.json:
```json
{
    "body": "Can this be closed ?",
    "created_at": "2014-10-21T14:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9986#issuecomment-100178",
    "user": "https://github.com/fchapoton"
}
```

Can this be closed ?



---

archive/issue_comments_100179.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-10-21T14:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9986#issuecomment-100179",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_events_010110.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-10-25T21:45:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9986",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9986#event-10110"
}
```



---

archive/issue_comments_100180.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-10-25T21:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9986#issuecomment-100180",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid



---

archive/issue_comments_100181.json:
```json
{
    "body": "While this is now closed I should add a couple of comments. AIX doesn't use elf format but xcoff (google it). The .a from aix can contain both static and dynamic libraries. They also can contain both 32 and 64bit objects all at the same type. The linker works out what it needs at linking time.\n\".so\" linux style shared libraries are allowed with recent linkers of AIX (I don't know if it extends as far back as AIX 5.3 it is definitely in 6.1) but you need to know the extra linking flags to use them \"-G\" and \"-brtl\" depending on the case. It is all pretty dangerous and it is best to leave the task of making the libraries to libtool if possible.",
    "created_at": "2014-10-26T05:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9986#issuecomment-100181",
    "user": "https://github.com/kiwifb"
}
```

While this is now closed I should add a couple of comments. AIX doesn't use elf format but xcoff (google it). The .a from aix can contain both static and dynamic libraries. They also can contain both 32 and 64bit objects all at the same type. The linker works out what it needs at linking time.
".so" linux style shared libraries are allowed with recent linkers of AIX (I don't know if it extends as far back as AIX 5.3 it is definitely in 6.1) but you need to know the extra linking flags to use them "-G" and "-brtl" depending on the case. It is all pretty dangerous and it is best to leave the task of making the libraries to libtool if possible.
