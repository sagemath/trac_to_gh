# Issue 8113: gd-2.0.35.p3 fails to build on Open Solaris x64 as 64 bit without setting CFLAGS=-64 globally

archive/issues_008113.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  drkirkby\n\nBuild will be 32 bit, even when SAGE64=\"yes\".\n\nThere is a simple patch coming up.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8113\n\n",
    "created_at": "2010-01-28T17:24:13Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "gd-2.0.35.p3 fails to build on Open Solaris x64 as 64 bit without setting CFLAGS=-64 globally",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8113",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @aghitza

CC:  drkirkby

Build will be 32 bit, even when SAGE64="yes".

There is a simple patch coming up.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8113





---

archive/issue_comments_071109.json:
```json
{
    "body": "Attachment [gd-2.0.35.p4.patch](tarball://root/attachments/some-uuid/ticket8113/gd-2.0.35.p4.patch) by @jaapspies created at 2010-01-28 17:36:59",
    "created_at": "2010-01-28T17:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71109",
    "user": "https://github.com/jaapspies"
}
```

Attachment [gd-2.0.35.p4.patch](tarball://root/attachments/some-uuid/ticket8113/gd-2.0.35.p4.patch) by @jaapspies created at 2010-01-28 17:36:59



---

archive/issue_comments_071110.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T17:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71110",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071111.json:
```json
{
    "body": "I would say the usual act in spkg-install. See the patch.\n\n\nThe spkg is here:\n[http://boxen.math.washington.edu/home/jsp/ports/gd-2.0.35.p4.spkg](http://boxen.math.washington.edu/home/jsp/ports/gd-2.0.35.p4.spkg)\n\n\n\n```\njaap@opensolaris:~/Downloads/sage-4.3.2.alpha0/local$ file lib/libgd.so\nlib/libgd.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n\n```\n\n\nJaap",
    "created_at": "2010-01-28T17:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71111",
    "user": "https://github.com/jaapspies"
}
```

I would say the usual act in spkg-install. See the patch.


The spkg is here:
[http://boxen.math.washington.edu/home/jsp/ports/gd-2.0.35.p4.spkg](http://boxen.math.washington.edu/home/jsp/ports/gd-2.0.35.p4.spkg)



```
jaap@opensolaris:~/Downloads/sage-4.3.2.alpha0/local$ file lib/libgd.so
lib/libgd.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped

```


Jaap



---

archive/issue_comments_071112.json:
```json
{
    "body": "Changing component from algebra to porting.",
    "created_at": "2010-01-29T16:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71112",
    "user": "https://github.com/jaapspies"
}
```

Changing component from algebra to porting.



---

archive/issue_comments_071113.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-29T18:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71113",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071114.json:
```json
{
    "body": "The files are indeed 64-bit now \n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file local/bin/annotate\nlocal/bin/annotate:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/libgd.so.2.0.0\nlocal/lib/libgd.so.2.0.0:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n```\n",
    "created_at": "2010-01-29T18:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71114",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The files are indeed 64-bit now 


```
drkirkby@hawk:~/sage-4.3.1$ file local/bin/annotate
local/bin/annotate:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgd.so.2.0.0
local/lib/libgd.so.2.0.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```




---

archive/issue_events_008319.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T15:16:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8113#event-8319"
}
```



---

archive/issue_comments_071115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8113",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8113#issuecomment-71115",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
