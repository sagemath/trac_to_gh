# Issue 4867: optional gcc-4.2.1.spkg doesn't build on sage.math

archive/issues_004867.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nsage -i gcc-4.2.1\n...\nIn file included from /usr/include/features.h:354,\n                 from /usr/include/stdio.h:28,\n                 from ../../gcc-4.2.1/gcc/tsystem.h:90,\n                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:\n/usr/include/gnu/stubs.h:7:27: error: gnu/stubs-32.h: No such file or directory\nIn file included from /usr/include/features.h:354,\n                 from /usr/include/stdio.h:28,\n                 from ../../gcc-4.2.1/gcc/tsystem.h:90,\n                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4867\n\n",
    "closed_at": "2013-08-16T11:11:46Z",
    "created_at": "2008-12-24T05:54:21Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional gcc-4.2.1.spkg doesn't build on sage.math",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4867",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

```
sage -i gcc-4.2.1
...
In file included from /usr/include/features.h:354,
                 from /usr/include/stdio.h:28,
                 from ../../gcc-4.2.1/gcc/tsystem.h:90,
                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:
/usr/include/gnu/stubs.h:7:27: error: gnu/stubs-32.h: No such file or directory
In file included from /usr/include/features.h:354,
                 from /usr/include/stdio.h:28,
                 from ../../gcc-4.2.1/gcc/tsystem.h:90,
                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:
```

Issue created by migration from https://trac.sagemath.org/ticket/4867





---

archive/issue_comments_036803.json:
```json
{
    "body": "The issue here is that seemingly the 32 bit userspace bits are missing.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T11:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36803",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue here is that seemingly the 32 bit userspace bits are missing.

Cheers,

Michael



---

archive/issue_events_011207.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-24T11:51:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4867#event-11207"
}
```



---

archive/issue_comments_036804.json:
```json
{
    "body": "The issue is not that bits are missing, the problem is plainly and simply that on Ubuntu multi lib in *any* upstream gcc is broken because the Ubuntu people chose to rename\n\n```\nlib64 -> lib\nlib -> lib32\n```\nOne can disable multilib support and get a 64 bit gcc on sage.math that way.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T02:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36804",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue is not that bits are missing, the problem is plainly and simply that on Ubuntu multi lib in *any* upstream gcc is broken because the Ubuntu people chose to rename

```
lib64 -> lib
lib -> lib32
```
One can disable multilib support and get a 64 bit gcc on sage.math that way.

Cheers,

Michael



---

archive/issue_events_011208.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4867#event-11208"
}
```



---

archive/issue_events_011209.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4867#event-11209"
}
```



---

archive/issue_comments_036805.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-13T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36805",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_011210.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:54:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4867#event-11210"
}
```



---

archive/issue_events_011211.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:54:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4867#event-11211"
}
```



---

archive/issue_comments_036806.json:
```json
{
    "body": "Invalid, even just because said package doesn't exist anymore.",
    "created_at": "2013-08-13T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36806",
    "user": "https://github.com/jdemeyer"
}
```

Invalid, even just because said package doesn't exist anymore.



---

archive/issue_comments_036807.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T16:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36807",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036808.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-08-16T11:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36808",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_011212.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-16T11:11:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4867#event-11212"
}
```
