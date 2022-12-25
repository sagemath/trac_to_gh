# Issue 9978: Cliquer fails to install on AIX 5.3 as getopt.h does not exist

archive/issues_009978.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @fchapoton\n\nUsing the following system: \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* DDS-4 tape drive \n\nCliquer failed to install due to a lack of `getopt.h` It can't determine the platform, which probably does not help the situation. \n\n\n```\nCannot determine your platform or it is not supported\nSince SAGE_PORT is set, setting SAGESOFLAGS to Linux defaults.\nmake[2]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/cliquer-1.2.p7/src'\nmake[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c\ncl.c:7:20: error: getopt.h: No such file or directory\ncl.c: In function 'read_options':\ncl.c:324: error: array type has incomplete element type\ncl.c:325: error: 'no_argument' undeclared (first use in this function)\ncl.c:325: error: (Each undeclared identifier is reported only once\ncl.c:325: error: for each function it appears in.)\ncl.c:328: error: 'required_argument' undeclared (first use in this function)\ncl.c:339: warning: implicit declaration of function 'getopt_long'\ncl.c:324: warning: unused variable 'long_options'\n```\n\n\nIt's quite possible that an installation of an AIX fileset would include the file `getopt.h`, but it looks like its a header will should at least consider checking for. However, comments on #9870 suggest we do not need the Cliquer executable (only the libraries), in which case there's no need for `getopt`. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9979\n\n",
    "created_at": "2010-09-23T15:40:37Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Cliquer fails to install on AIX 5.3 as getopt.h does not exist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9978",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @fchapoton

Using the following system: 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* DDS-4 tape drive 

Cliquer failed to install due to a lack of `getopt.h` It can't determine the platform, which probably does not help the situation. 


```
Cannot determine your platform or it is not supported
Since SAGE_PORT is set, setting SAGESOFLAGS to Linux defaults.
make[2]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/cliquer-1.2.p7/src'
make[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
cl.c:7:20: error: getopt.h: No such file or directory
cl.c: In function 'read_options':
cl.c:324: error: array type has incomplete element type
cl.c:325: error: 'no_argument' undeclared (first use in this function)
cl.c:325: error: (Each undeclared identifier is reported only once
cl.c:325: error: for each function it appears in.)
cl.c:328: error: 'required_argument' undeclared (first use in this function)
cl.c:339: warning: implicit declaration of function 'getopt_long'
cl.c:324: warning: unused variable 'long_options'
```


It's quite possible that an installation of an AIX fileset would include the file `getopt.h`, but it looks like its a header will should at least consider checking for. However, comments on #9870 suggest we do not need the Cliquer executable (only the libraries), in which case there's no need for `getopt`. 



Issue created by migration from https://trac.sagemath.org/ticket/9979





---

archive/issue_comments_100140.json:
```json
{
    "body": "Yes, if we only (properly) build a shared library rather than the executable, we don't need it.\n\nThis will some day be fixed by #9870 I guess.\n\nYou could nevertheless report this upstream. (I think Cliquer should at least check for the presence of `getopt.h`.)",
    "created_at": "2010-09-24T12:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9978#issuecomment-100140",
    "user": "https://github.com/nexttime"
}
```

Yes, if we only (properly) build a shared library rather than the executable, we don't need it.

This will some day be fixed by #9870 I guess.

You could nevertheless report this upstream. (I think Cliquer should at least check for the presence of `getopt.h`.)



---

archive/issue_events_025207.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25207"
}
```



---

archive/issue_events_025208.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25208"
}
```



---

archive/issue_events_025209.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25209"
}
```



---

archive/issue_events_025210.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25210"
}
```



---

archive/issue_events_025211.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25211"
}
```



---

archive/issue_events_025212.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25212"
}
```



---

archive/issue_events_025213.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25213"
}
```



---

archive/issue_events_025214.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-01-15T18:39:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25214"
}
```



---

archive/issue_events_025215.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-01-15T18:39:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25215"
}
```



---

archive/issue_comments_100141.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9978#issuecomment-100141",
    "user": "https://github.com/embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_100142.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9978#issuecomment-100142",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100143.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9978#issuecomment-100143",
    "user": "https://github.com/mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_events_025216.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-23T21:26:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25216"
}
```



---

archive/issue_events_025217.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-23T21:26:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25217"
}
```



---

archive/issue_comments_100144.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T13:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9978#issuecomment-100144",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_025218.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-25T13:33:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9978",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9978#event-25218"
}
```
