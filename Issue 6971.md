# Issue 6971: port ECL spkg to os x 10.6

archive/issues_006971.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nha1/spkg/build/ecl-9.8.4/src/src/gc/mach_dep.c -o mach_dep.o\nIn file included from /Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/spkg/build/ecl-9.8.4/src/src/gc/mach_dep.c:163:\n/usr/include/ucontext.h:42:2: error: #error ucontext routines are deprecated, and require _XOPEN_SOURCE to be defined\nmake[5]: *** [mach_dep.lo] Error 1\nmake[4]: *** [install-recursive] Error 1\nmake[3]: *** [libeclgc.a] Error 2\nmake[2]: *** [all] Error 2\nFailed to build ECL ... exiting\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6971\n\n",
    "created_at": "2009-09-20T22:28:14Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "port ECL spkg to os x 10.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6971",
    "user": "was"
}
```
Assignee: tbd


```
ha1/spkg/build/ecl-9.8.4/src/src/gc/mach_dep.c -o mach_dep.o
In file included from /Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/spkg/build/ecl-9.8.4/src/src/gc/mach_dep.c:163:
/usr/include/ucontext.h:42:2: error: #error ucontext routines are deprecated, and require _XOPEN_SOURCE to be defined
make[5]: *** [mach_dep.lo] Error 1
make[4]: *** [install-recursive] Error 1
make[3]: *** [libeclgc.a] Error 2
make[2]: *** [all] Error 2
Failed to build ECL ... exiting

```


Issue created by migration from https://trac.sagemath.org/ticket/6971





---

archive/issue_comments_057662.json:
```json
{
    "body": "spkg up here:\n\n    http://sage.math.washington.edu/home/wstein/patches/ecl-9.8.4-20090913cvs.p1.spkg\n\nIt's important that the name be fairly canonical like the above is.",
    "created_at": "2009-09-20T22:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6971#issuecomment-57662",
    "user": "was"
}
```

spkg up here:

    http://sage.math.washington.edu/home/wstein/patches/ecl-9.8.4-20090913cvs.p1.spkg

It's important that the name be fairly canonical like the above is.



---

archive/issue_comments_057663.json:
```json
{
    "body": "See palmieri's and my reports at #6849.",
    "created_at": "2009-09-27T02:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6971#issuecomment-57663",
    "user": "mvngu"
}
```

See palmieri's and my reports at #6849.



---

archive/issue_comments_057664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-27T02:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6971#issuecomment-57664",
    "user": "mvngu"
}
```

Resolution: fixed
