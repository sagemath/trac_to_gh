# Issue 7817: opencdk ignoring SAGE64 except on OS X

archive/issues_007817.json:
```json
{
    "body": "Assignee: drkirkby\n\nLike many packages, opencdk has code which adds -m64 on OS X if SAGE64 is set to yes. It is being ignored on other platforms, with the result the build fails - see below. \n\n\n```\n/home/drkirkby/sage-4.3/local/lib/libgcrypt.so /export/home/drkirkby/sage-4.3/local/lib/libgpg-error.so -lz -lc \nld: fatal: file /export/home/drkirkby/sage-4.3/local/lib/libgcrypt.so: wrong ELF class: ELFCLASS64\nld: fatal: file processing errors. No output written to .libs/libopencdk.so.10.0.6\ncollect2: ld returned 1 exit status\nmake[4]: *** [libopencdk.la] Error 1\nmake[4]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src/src'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src'\nFailed to build OpenCDK\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7817\n\n",
    "created_at": "2010-01-02T08:49:26Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "opencdk ignoring SAGE64 except on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7817",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

Like many packages, opencdk has code which adds -m64 on OS X if SAGE64 is set to yes. It is being ignored on other platforms, with the result the build fails - see below. 


```
/home/drkirkby/sage-4.3/local/lib/libgcrypt.so /export/home/drkirkby/sage-4.3/local/lib/libgpg-error.so -lz -lc 
ld: fatal: file /export/home/drkirkby/sage-4.3/local/lib/libgcrypt.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to .libs/libopencdk.so.10.0.6
collect2: ld returned 1 exit status
make[4]: *** [libopencdk.la] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src'
Failed to build OpenCDK
```




Issue created by migration from https://trac.sagemath.org/ticket/7817





---

archive/issue_comments_067515.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T09:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7817#issuecomment-67515",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067516.json:
```json
{
    "body": "I've updated spkg-install so SAGE64 is used on any platform. \n\nChanges have been checked in. \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/opencdk-0.6.6.p3/",
    "created_at": "2010-01-02T09:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7817#issuecomment-67516",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've updated spkg-install so SAGE64 is used on any platform. 

Changes have been checked in. 

http://boxen.math.washington.edu/home/kirkby/portability/opencdk-0.6.6.p3/



---

archive/issue_comments_067517.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-02T18:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7817#issuecomment-67517",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067518.json:
```json
{
    "body": "Looks good to me. Tested it on Open Solaris and Fedora 11 and 12.\n\nSo positive review.\n\nJaap",
    "created_at": "2010-01-02T18:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7817#issuecomment-67518",
    "user": "https://github.com/jaapspies"
}
```

Looks good to me. Tested it on Open Solaris and Fedora 11 and 12.

So positive review.

Jaap



---

archive/issue_events_008030.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-04T03:42:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7817",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7817#event-8030"
}
```



---

archive/issue_comments_067519.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T03:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7817#issuecomment-67519",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
