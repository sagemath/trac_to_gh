# Issue 9133: sage-4.4.3.alpha2: pynac build failure on an itanium box (easy autoconf issue)

archive/issues_009133.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\n```\n\ncd . && /bin/sh /home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src/missing --run autoconf\n/home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src/missing: line 54: autoconf: command not found\nWARNING: `autoconf' is missing on your system.  You should only need it if\n         you modified `configure.ac'.  You might want to install the\n         `Autoconf' and `GNU m4' packages.  Grab them from any GNU\n         archive site.\n/bin/sh ./config.status --recheck\nrunning CONFIG_SHELL=/bin/sh /bin/sh ./configure --disable-static --prefix=/home/wstein/screen/iras/sage-4.4.3.alpha2/local CC=gcc LDFL\nAGS= CXX=g++ --no-create --no-recursion\nchecking for a BSD-compatible install... /usr/bin/install -c\nchecking whether build environment is sane... configure: error: newly created file is older than distributed files!\nCheck your system clock\nmake[2]: *** [config.status] Error 1\nmake[2]: Leaving directory `/home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src'\nError building pynac.\n\nreal    0m13.248s\nuser    0m5.660s\nsys     0m2.400s\nsage: An error occurred while installing pynac-0.2.0.p1\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9133\n\n",
    "created_at": "2010-06-03T16:08:35Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "sage-4.4.3.alpha2: pynac build failure on an itanium box (easy autoconf issue)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9133",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

```

cd . && /bin/sh /home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src/missing --run autoconf
/home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src/missing: line 54: autoconf: command not found
WARNING: `autoconf' is missing on your system.  You should only need it if
         you modified `configure.ac'.  You might want to install the
         `Autoconf' and `GNU m4' packages.  Grab them from any GNU
         archive site.
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure --disable-static --prefix=/home/wstein/screen/iras/sage-4.4.3.alpha2/local CC=gcc LDFL
AGS= CXX=g++ --no-create --no-recursion
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... configure: error: newly created file is older than distributed files!
Check your system clock
make[2]: *** [config.status] Error 1
make[2]: Leaving directory `/home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src'
Error building pynac.

real    0m13.248s
user    0m5.660s
sys     0m2.400s
sage: An error occurred while installing pynac-0.2.0.p1
```

Issue created by migration from https://trac.sagemath.org/ticket/9133





---

archive/issue_comments_084988.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T16:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9133#issuecomment-84988",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084989.json:
```json
{
    "body": "The new spkg here works fine:\n\n   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p2.spkg\n\nAll I did was type \"autoreconf\" in src, and also update the SPKG.txt.",
    "created_at": "2010-06-03T16:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9133#issuecomment-84989",
    "user": "https://github.com/williamstein"
}
```

The new spkg here works fine:

   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p2.spkg

All I did was type "autoreconf" in src, and also update the SPKG.txt.



---

archive/issue_comments_084990.json:
```json
{
    "body": "The above package builds fine on iras:\n\n```\nDone installing pynac.\n\nreal    7m5.748s\nuser    6m28.244s\nsys     0m9.272s\nSuccessfully installed pynac-0.2.0.p2\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing pynac-0.2.0.p2.spkg\nwstein@iras:~/screen/iras/sage-4.4.3.alpha2>  \n```",
    "created_at": "2010-06-03T16:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9133#issuecomment-84990",
    "user": "https://github.com/williamstein"
}
```

The above package builds fine on iras:

```
Done installing pynac.

real    7m5.748s
user    6m28.244s
sys     0m9.272s
Successfully installed pynac-0.2.0.p2
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pynac-0.2.0.p2.spkg
wstein@iras:~/screen/iras/sage-4.4.3.alpha2>  
```



---

archive/issue_comments_084991.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T18:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9133#issuecomment-84991",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084992.json:
```json
{
    "body": "Looks good to to me.  This builds on both Cygwin and my linux box.",
    "created_at": "2010-06-03T18:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9133#issuecomment-84992",
    "user": "https://github.com/mwhansen"
}
```

Looks good to to me.  This builds on both Cygwin and my linux box.



---

archive/issue_comments_084993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-04T15:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9133#issuecomment-84993",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_022445.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-04T15:18:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9133",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9133#event-22445"
}
```
