# Issue 7130: libpng 1.2.35 always builds 32-bit libraries on Solaris.

archive/issues_007130.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jaapspies\n\nUsing\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\"\n\nWe can see that libpng is building 32-bit libraries, despite other packages are building 64-bit libraries. \n\n```\nlibpng12.so:    ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\nlibpng12.so.0:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\nlibpng12.so.0.35.0:     ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\nlibreadline.a:  current ar archive, not a dynamic executable or shared object\nlibreadline.so: ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped\nlibreadline.so.6:       ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped\n```\n\nOther packages building 32-bit libraries, even when SAGE64 is set to  yes include, but are probably not limited to. \n* zlib #7128\n* libgpg_error #7129\n\nI will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.\n\nAlthough there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.\n\nIBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nThe sensible way to resolve this is to add the correct flag on every platform. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7130\n\n",
    "closed_at": "2010-06-19T13:17:43Z",
    "created_at": "2009-10-05T23:21:28Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "libpng 1.2.35 always builds 32-bit libraries on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7130",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @jaapspies

Using
* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes"

We can see that libpng is building 32-bit libraries, despite other packages are building 64-bit libraries. 

```
libpng12.so:    ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libpng12.so.0:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libpng12.so.0.35.0:     ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libreadline.a:  current ar archive, not a dynamic executable or shared object
libreadline.so: ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libreadline.so.6:       ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
```

Other packages building 32-bit libraries, even when SAGE64 is set to  yes include, but are probably not limited to. 
* zlib #7128
* libgpg_error #7129

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform. 

Issue created by migration from https://trac.sagemath.org/ticket/7130





---

archive/issue_comments_059026.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-10-05T23:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7130#issuecomment-59026",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_059027.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T21:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7130#issuecomment-59027",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059028.json:
```json
{
    "body": "This is a quick hack, to get this to build only with only gcc and perhaps Sun Studio, as they both take -m64. A more portable solution, which will work for any compiler will be implemented later. \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/libpng-1.2.35.p0/\n\ndave",
    "created_at": "2010-01-02T21:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7130#issuecomment-59028",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This is a quick hack, to get this to build only with only gcc and perhaps Sun Studio, as they both take -m64. A more portable solution, which will work for any compiler will be implemented later. 

http://boxen.math.washington.edu/home/kirkby/portability/libpng-1.2.35.p0/

dave



---

archive/issue_comments_059029.json:
```json
{
    "body": "Attachment [libpng.patch](tarball://root/attachments/some-uuid/ticket7130/libpng.patch) by drkirkby created at 2010-01-28 15:15:14",
    "created_at": "2010-01-28T15:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7130#issuecomment-59029",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [libpng.patch](tarball://root/attachments/some-uuid/ticket7130/libpng.patch) by drkirkby created at 2010-01-28 15:15:14



---

archive/issue_events_016846.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-06-19T13:17:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7130#event-16846"
}
```



---

archive/issue_comments_059030.json:
```json
{
    "body": "This can be closed. The latest version of libpng (libpng-1.2.35.p2) in Sage builds fine without problems. I don't know what ticket number fixed it, but these two log entries \n\n\n```\nchangeset:   13:ae01944f408c\nuser:        Jaap Spies <jaapspies@gmail.com>\ndate:        Thu Feb 04 19:32:51 2010 +0100\nsummary:     Corrected stupid typo I thought I had corrected earlier.\n\nchangeset:   12:329a8eb6dd2e\nuser:        Jaap Spies <jaapspies@gmail.com>\ndate:        Wed Feb 03 19:09:41 2010 +0100\nsummary:     Let SAGE64=yes work not only on OSX, but also on Open Solaris and possibly on other platform\n```\n\nAs such, this can be closed as \"fixed\"",
    "created_at": "2010-06-19T13:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7130#issuecomment-59030",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This can be closed. The latest version of libpng (libpng-1.2.35.p2) in Sage builds fine without problems. I don't know what ticket number fixed it, but these two log entries 


```
changeset:   13:ae01944f408c
user:        Jaap Spies <jaapspies@gmail.com>
date:        Thu Feb 04 19:32:51 2010 +0100
summary:     Corrected stupid typo I thought I had corrected earlier.

changeset:   12:329a8eb6dd2e
user:        Jaap Spies <jaapspies@gmail.com>
date:        Wed Feb 03 19:09:41 2010 +0100
summary:     Let SAGE64=yes work not only on OSX, but also on Open Solaris and possibly on other platform
```

As such, this can be closed as "fixed"



---

archive/issue_comments_059031.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-19T13:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7130",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7130#issuecomment-59031",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Resolution: fixed
