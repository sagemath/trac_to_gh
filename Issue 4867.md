# Issue 4867: optional gcc-4.2.1.spkg doesn't build on sage.math

archive/issues_004867.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -i gcc-4.2.1\n...\nIn file included from /usr/include/features.h:354,\n                 from /usr/include/stdio.h:28,\n                 from ../../gcc-4.2.1/gcc/tsystem.h:90,\n                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:\n/usr/include/gnu/stubs.h:7:27: error: gnu/stubs-32.h: No such file or directory\nIn file included from /usr/include/features.h:354,\n                 from /usr/include/stdio.h:28,\n                 from ../../gcc-4.2.1/gcc/tsystem.h:90,\n                 from ../../gcc-4.2.1/gcc/libgcc2.c:33:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4867\n\n",
    "created_at": "2008-12-24T05:54:21Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "optional gcc-4.2.1.spkg doesn't build on sage.math",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4867",
    "user": "was"
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

archive/issue_comments_036875.json:
```json
{
    "body": "The issue here is that seemingly the 32 bit userspace bits are missing.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T11:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36875",
    "user": "mabshoff"
}
```

The issue here is that seemingly the 32 bit userspace bits are missing.

Cheers,

Michael



---

archive/issue_comments_036876.json:
```json
{
    "body": "The issue is not that bits are missing, the problem is plainly and simply that on Ubuntu multi lib in *any* upstream gcc is broken because the Ubuntu people chose to rename\n\n```\nlib64 -> lib\nlib -> lib32\n```\n\nOne can disable multilib support and get a 64 bit gcc on sage.math that way.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T02:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36876",
    "user": "mabshoff"
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

archive/issue_comments_036877.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-13T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36877",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036878.json:
```json
{
    "body": "Invalid, even just because said package doesn't exist anymore.",
    "created_at": "2013-08-13T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36878",
    "user": "jdemeyer"
}
```

Invalid, even just because said package doesn't exist anymore.



---

archive/issue_comments_036879.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T16:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36879",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036880.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-08-16T11:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4867#issuecomment-36880",
    "user": "jdemeyer"
}
```

Resolution: invalid
