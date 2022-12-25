# Issue 8101: ntl fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set

archive/issues_008101.json:
```json
{
    "body": "Assignee: drkirkby\n\nOn Open Solaris x64 as 64 bit without setting CFLAGS globally build is 32 bit.\n\nA patch is attached.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8101\n\n",
    "closed_at": "2010-02-11T15:13:21Z",
    "created_at": "2010-01-27T23:48:53Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "ntl fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8101",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

On Open Solaris x64 as 64 bit without setting CFLAGS globally build is 32 bit.

A patch is attached.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8101





---

archive/issue_comments_070960.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-27T23:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8101#issuecomment-70960",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070961.json:
```json
{
    "body": "Attachment [ntl-5.4.2.p11.patch](tarball://root/attachments/some-uuid/ticket8101/ntl-5.4.2.p11.patch) by @jaapspies created at 2010-01-27 23:58:42\n\nAn spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/ntl-5.4.2.p11.spkg](http://boxen.math.washington.edu/home/jsp/ports/ntl-5.4.2.p11.spkg)\n\nJaap",
    "created_at": "2010-01-27T23:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8101#issuecomment-70961",
    "user": "https://github.com/jaapspies"
}
```

Attachment [ntl-5.4.2.p11.patch](tarball://root/attachments/some-uuid/ticket8101/ntl-5.4.2.p11.patch) by @jaapspies created at 2010-01-27 23:58:42

An spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/ntl-5.4.2.p11.spkg](http://boxen.math.washington.edu/home/jsp/ports/ntl-5.4.2.p11.spkg)

Jaap



---

archive/issue_comments_070962.json:
```json
{
    "body": "Positive review. All shared libraries are indeed 64-bit now. \n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/lib*ntl*\nlocal/lib/libntl-5.4.2.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libntl.a:\tcurrent ar archive, not a dynamic executable or shared object\nlocal/lib/libntl.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n```",
    "created_at": "2010-01-28T13:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8101#issuecomment-70962",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Positive review. All shared libraries are indeed 64-bit now. 

```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/lib*ntl*
local/lib/libntl-5.4.2.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libntl.a:	current ar archive, not a dynamic executable or shared object
local/lib/libntl.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```



---

archive/issue_comments_070963.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T13:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8101#issuecomment-70963",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070964.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8101#issuecomment-70964",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019385.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T15:13:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8101",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8101#event-19385"
}
```
