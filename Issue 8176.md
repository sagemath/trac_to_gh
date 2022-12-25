# Issue 8176: libpng fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

archive/issues_008176.json:
```json
{
    "body": "Assignee: drkirkby\n\nSetting SAGE64=yes is only working on Darwin. To make it work on Open Solaris and possibly on other platforms a small edit of spkg-install is needed.\n\nA patch is coming up.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8176\n\n",
    "created_at": "2010-02-03T18:01:21Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "libpng fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8176",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

Setting SAGE64=yes is only working on Darwin. To make it work on Open Solaris and possibly on other platforms a small edit of spkg-install is needed.

A patch is coming up.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8176





---

archive/issue_comments_071912.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T18:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71912",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071913.json:
```json
{
    "body": "Attachment [libpng-1.2.35.p0.patch](tarball://root/attachments/some-uuid/ticket8176/libpng-1.2.35.p0.patch) by @jaapspies created at 2010-02-03 18:19:44\n\nAn spkgs can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg)\n\n\n\n\n```\nlib/libpng12.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlib/libpng12.so.0:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlib/libpng12.so.0.35.0:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n\n```\n\n\nJaap",
    "created_at": "2010-02-03T18:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71913",
    "user": "https://github.com/jaapspies"
}
```

Attachment [libpng-1.2.35.p0.patch](tarball://root/attachments/some-uuid/ticket8176/libpng-1.2.35.p0.patch) by @jaapspies created at 2010-02-03 18:19:44

An spkgs can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg)




```
lib/libpng12.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
lib/libpng12.so.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
lib/libpng12.so.0.35.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped

```


Jaap



---

archive/issue_comments_071914.json:
```json
{
    "body": "This line makes no sence whatsovever\n\n\n```\nif [ `uname` = \"x$SAGE64\" = xyes ]; then \n```\n\n\nYou must have a typo there. uname will return SunOS, not yes. \n\nDave",
    "created_at": "2010-02-04T17:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71914",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This line makes no sence whatsovever


```
if [ `uname` = "x$SAGE64" = xyes ]; then 
```


You must have a typo there. uname will return SunOS, not yes. 

Dave



---

archive/issue_comments_071915.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-04T17:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71915",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071916.json:
```json
{
    "body": "Attachment [libpng-1.2.35.p0+.patch](tarball://root/attachments/some-uuid/ticket8176/libpng-1.2.35.p0+.patch) by @jaapspies created at 2010-02-04 18:44:05\n\nSome stupid error I had corrected I thought.\n\n[http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg)\n\nDidn't change the patch level.\n\nJaap",
    "created_at": "2010-02-04T18:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71916",
    "user": "https://github.com/jaapspies"
}
```

Attachment [libpng-1.2.35.p0+.patch](tarball://root/attachments/some-uuid/ticket8176/libpng-1.2.35.p0+.patch) by @jaapspies created at 2010-02-04 18:44:05

Some stupid error I had corrected I thought.

[http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/libpng-1.2.35.p0.spkg)

Didn't change the patch level.

Jaap



---

archive/issue_comments_071917.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T18:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71917",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071918.json:
```json
{
    "body": "That looks fine now. I see the -m64 flag is added, and it builds as 64-bit. I even checked it on a 64-bit SPARC, and see it builds as 64-bit there too. \n\n\n```\ndrkirkby@swan:[~/sage-4.3.2.rc0] $ file  local/lib/libpng12.so.0.35.0\nlocal/lib/libpng12.so.0.35.0:   ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped\n```\n\n\nso positive review. \n\nPS, for future reference, someone mentioned the other day it would be useful if the patch number was in the Mercurial commit message. That sounds quite logical to me. But there is nothing wrong with this.",
    "created_at": "2010-02-04T19:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71918",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That looks fine now. I see the -m64 flag is added, and it builds as 64-bit. I even checked it on a 64-bit SPARC, and see it builds as 64-bit there too. 


```
drkirkby@swan:[~/sage-4.3.2.rc0] $ file  local/lib/libpng12.so.0.35.0
local/lib/libpng12.so.0.35.0:   ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
```


so positive review. 

PS, for future reference, someone mentioned the other day it would be useful if the patch number was in the Mercurial commit message. That sounds quite logical to me. But there is nothing wrong with this.



---

archive/issue_comments_071919.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T19:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71919",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008379.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T15:17:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8176#event-8379"
}
```



---

archive/issue_comments_071920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8176#issuecomment-71920",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
