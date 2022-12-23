# Issue 8117: zodb3 fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

archive/issues_008117.json:
```json
{
    "body": "Assignee: drkirkby\n\nIf CFLAGS not contains -m64 zodb3-3.7.0.2 fails to build on Open Solaris x64. This works only on OSX 64 bit.\n\nA patch is coming up.\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8117\n\n",
    "created_at": "2010-01-29T13:36:51Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "zodb3 fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8117",
    "user": "jsp"
}
```
Assignee: drkirkby

If CFLAGS not contains -m64 zodb3-3.7.0.2 fails to build on Open Solaris x64. This works only on OSX 64 bit.

A patch is coming up.

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/8117





---

archive/issue_comments_071301.json:
```json
{
    "body": "Attachment\n\nAdded spkg.\n\n[http://boxen.math.washington.edu/home/jsp/ports/zodb3-3.7.0.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zodb3-3.7.0.p3.spkg)\n\n\n\n```\nlocal/lib/python2.6/site-packages/ZODB/winlock.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ \n\n\n```\n\n\nJaap",
    "created_at": "2010-01-29T13:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8117#issuecomment-71301",
    "user": "jsp"
}
```

Attachment

Added spkg.

[http://boxen.math.washington.edu/home/jsp/ports/zodb3-3.7.0.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/zodb3-3.7.0.p3.spkg)



```
local/lib/python2.6/site-packages/ZODB/winlock.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0$ 


```


Jaap



---

archive/issue_comments_071302.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T13:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8117#issuecomment-71302",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071303.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-29T18:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8117#issuecomment-71303",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071304.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8117#issuecomment-71304",
    "user": "mpatel"
}
```

Resolution: fixed
