# Issue 3086: Update R to the 2.7 release and split off rpy.spkg

archive/issues_003086.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout\n\nR 2.7 is out, so let's upgrade. We should also more rpy to its own top level spkg and update to rpy 1.0.2\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3086\n\n",
    "created_at": "2008-05-03T03:24:25Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update R to the 2.7 release and split off rpy.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jasongrout

R 2.7 is out, so let's upgrade. We should also more rpy to its own top level spkg and update to rpy 1.0.2

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3086





---

archive/issue_comments_021264.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-03T16:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021265.json:
```json
{
    "body": "R 2.6.1 is also broken on FC3:\n\n```\ngcc -std=gnu99 -I. -I../../src/include -I../../src/include -I/usr/local/include -DHAVE_CONFIG_H   -fpic  -I/root/sage-3.0/lo\ncal/include -L/root/sage-3.0/local/lib/  -c signrank.c -o signrank.o\nmake[5]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/nmath'\nmake[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/nmath'\nmake[4]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'\nconfig.status: creating src/unix/Makefile\nmake[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'\nmake[4]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'\nmake[5]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'\nmaking dynload.d from dynload.c\nmaking edit.d from edit.c\nmaking stubs.d from stubs.c\nmaking system.d from system.c\nmaking sys-unix.d from sys-unix.c\nmaking sys-std.d from sys-std.c\nsys-std.c:401:33: readline/readline.h: No such file or directory\nsys-std.c:431:32: readline/history.h: No such file or directory\nmake[5]: *** [sys-std.d] Error 1\nmake[5]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'\nmake[4]: *** [R] Error 2\nmake[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'\nmake[3]: *** [R] Error 1\nmake[3]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src'\nmake[2]: *** [R] Error 1\nmake[2]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src'\nError building R.\n```\n\nThis is most likely cause by R not using Sage's readline. There is a similar issue with R not picking Sage's libpng, so fix both issues when updating to R 2.7.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T16:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21265",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

R 2.6.1 is also broken on FC3:

```
gcc -std=gnu99 -I. -I../../src/include -I../../src/include -I/usr/local/include -DHAVE_CONFIG_H   -fpic  -I/root/sage-3.0/lo
cal/include -L/root/sage-3.0/local/lib/  -c signrank.c -o signrank.o
make[5]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/nmath'
make[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/nmath'
make[4]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
config.status: creating src/unix/Makefile
make[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[4]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[5]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
making dynload.d from dynload.c
making edit.d from edit.c
making stubs.d from stubs.c
making system.d from system.c
making sys-unix.d from sys-unix.c
making sys-std.d from sys-std.c
sys-std.c:401:33: readline/readline.h: No such file or directory
sys-std.c:431:32: readline/history.h: No such file or directory
make[5]: *** [sys-std.d] Error 1
make[5]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[4]: *** [R] Error 2
make[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[3]: *** [R] Error 1
make[3]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src'
make[2]: *** [R] Error 1
make[2]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src'
Error building R.
```

This is most likely cause by R not using Sage's readline. There is a similar issue with R not picking Sage's libpng, so fix both issues when updating to R 2.7.

Cheers,

Michael



---

archive/issue_comments_021266.json:
```json
{
    "body": "See also #3011 about the related RHOME issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-05T03:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See also #3011 about the related RHOME issue.

Cheers,

Michael



---

archive/issue_comments_021267.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-09-16T13:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21267",
    "user": "https://github.com/jasongrout"
}
```

Changing status from assigned to new.



---

archive/issue_comments_021268.json:
```json
{
    "body": "Changing assignee from mabshoff to @jasongrout.",
    "created_at": "2009-09-16T13:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21268",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from mabshoff to @jasongrout.



---

archive/issue_comments_021269.json:
```json
{
    "body": "Also, R has its own C interface---I think rpy2 is using it, but if not, it might make sense for us to just write a Cython wrapper around the C interface.",
    "created_at": "2009-09-16T13:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21269",
    "user": "https://github.com/jasongrout"
}
```

Also, R has its own C interface---I think rpy2 is using it, but if not, it might make sense for us to just write a Cython wrapper around the C interface.



---

archive/issue_comments_021270.json:
```json
{
    "body": "My draft of an updated R and rpy2 spkg is at \nhttp://sage.math.washington.edu/home/jason/r-2.9.2.spkg.  There are \nunchecked-in changes in the spkg, and I just ignored a bunch of old \npatches to R because I wasn't sure they applied anymore, so the spkg is \nnot finished.",
    "created_at": "2009-09-17T04:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21270",
    "user": "https://github.com/jasongrout"
}
```

My draft of an updated R and rpy2 spkg is at 
http://sage.math.washington.edu/home/jason/r-2.9.2.spkg.  There are 
unchecked-in changes in the spkg, and I just ignored a bunch of old 
patches to R because I wasn't sure they applied anymore, so the spkg is 
not finished.



---

archive/issue_comments_021271.json:
```json
{
    "body": "See #6972 for a continuation of the updated spkg above.",
    "created_at": "2009-09-21T13:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21271",
    "user": "https://github.com/jasongrout"
}
```

See #6972 for a continuation of the updated spkg above.



---

archive/issue_events_006968.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T17:02:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3086#event-6968"
}
```



---

archive/issue_comments_021272.json:
```json
{
    "body": "Closing this ticket as a duplicate of #6972.",
    "created_at": "2009-09-22T17:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21272",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this ticket as a duplicate of #6972.



---

archive/issue_events_006969.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T17:02:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3086#event-6969"
}
```



---

archive/issue_comments_021273.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-22T17:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3086#issuecomment-21273",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate
