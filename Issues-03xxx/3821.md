# Issue 3821: [with patch, positive review] bernmm shouldn't depend on pyport.h

archive/issues_003821.json:
```json
{
    "body": "Assignee: mabshoff\n\nI'd rather not have bernmm dependent on pyport.h.\n\nPatch will be up momentarily; should be applied on top of #3807 patch; I've only tested this on my laptop.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3821\n\n",
    "closed_at": "2008-08-12T21:38:10Z",
    "created_at": "2008-08-12T16:27:35Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, positive review] bernmm shouldn't depend on pyport.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3821",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: mabshoff

I'd rather not have bernmm dependent on pyport.h.

Patch will be up momentarily; should be applied on top of #3807 patch; I've only tested this on my laptop.


Issue created by migration from https://trac.sagemath.org/ticket/3821





---

archive/issue_comments_027117.json:
```json
{
    "body": "Attachment [trac_3821.patch](tarball://root/attachments/some-uuid/ticket3821/trac_3821.patch) by dmharvey created at 2008-08-12 16:29:10",
    "created_at": "2008-08-12T16:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27117",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [trac_3821.patch](tarball://root/attachments/some-uuid/ticket3821/trac_3821.patch) by dmharvey created at 2008-08-12 16:29:10



---

archive/issue_events_008764.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-12T16:38:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3821#event-8764"
}
```



---

archive/issue_comments_027118.json:
```json
{
    "body": "The patch seems to go in the right direction, but gcc 4.3.1 is still unhappy with bern_modp_util.cpp while two other files are fine:\n\n```\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -I/tmp/foo/sage-3.1.alpha1/local//include -I/tmp/foo/sage-3.1.alpha1/local//include/csage -I/tmp/foo/sage-3.1.alpha1/devel//sage/sage/ext -I/tmp/foo/sage-3.1.alpha1/local/include/python2.5 -c sage/rings/bernmm/bern_modp_util.cpp -o build/temp.linux-x86_64-2.5/sage/rings/bernmm/bern_modp_util.o -w -w\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\nIn file included from sage/rings/bernmm/bern_modp_util.cpp:24:\nsage/rings/bernmm/bern_modp_util.h:32:2: error: #error Oops! Unsigned long is neither 32 nor 64 bits.\nsage/rings/bernmm/bern_modp_util.h:33:2: error: #error You need to update bern_modp_util.h.\nIn file included from sage/rings/bernmm/bern_modp_util.cpp:24:\nsage/rings/bernmm/bern_modp_util.h: In member function \u2018bool bernmm::PrimeTable::get(long int) const\u2019:\nsage/rings/bernmm/bern_modp_util.h:91: error: \u2018ULONG_BITS\u2019 was not declared in this scope\nsage/rings/bernmm/bern_modp_util.h: In member function \u2018void bernmm::PrimeTable::set(long int)\u2019:\nsage/rings/bernmm/bern_modp_util.h:97: error: \u2018ULONG_BITS\u2019 was not declared in this scope\nsage/rings/bernmm/bern_modp_util.cpp: In constructor \u2018bernmm::PrimeTable::PrimeTable(long int)\u2019:\nsage/rings/bernmm/bern_modp_util.cpp:92: error: \u2018ULONG_BITS\u2019 was not declared in this scope\nerror: command 'gcc' failed with exit status 1\nsage: There was an error installing modified sage library code.\n```\n\nI am looking into this.",
    "created_at": "2008-08-12T16:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch seems to go in the right direction, but gcc 4.3.1 is still unhappy with bern_modp_util.cpp while two other files are fine:

```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -I/tmp/foo/sage-3.1.alpha1/local//include -I/tmp/foo/sage-3.1.alpha1/local//include/csage -I/tmp/foo/sage-3.1.alpha1/devel//sage/sage/ext -I/tmp/foo/sage-3.1.alpha1/local/include/python2.5 -c sage/rings/bernmm/bern_modp_util.cpp -o build/temp.linux-x86_64-2.5/sage/rings/bernmm/bern_modp_util.o -w -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from sage/rings/bernmm/bern_modp_util.cpp:24:
sage/rings/bernmm/bern_modp_util.h:32:2: error: #error Oops! Unsigned long is neither 32 nor 64 bits.
sage/rings/bernmm/bern_modp_util.h:33:2: error: #error You need to update bern_modp_util.h.
In file included from sage/rings/bernmm/bern_modp_util.cpp:24:
sage/rings/bernmm/bern_modp_util.h: In member function ‘bool bernmm::PrimeTable::get(long int) const’:
sage/rings/bernmm/bern_modp_util.h:91: error: ‘ULONG_BITS’ was not declared in this scope
sage/rings/bernmm/bern_modp_util.h: In member function ‘void bernmm::PrimeTable::set(long int)’:
sage/rings/bernmm/bern_modp_util.h:97: error: ‘ULONG_BITS’ was not declared in this scope
sage/rings/bernmm/bern_modp_util.cpp: In constructor ‘bernmm::PrimeTable::PrimeTable(long int)’:
sage/rings/bernmm/bern_modp_util.cpp:92: error: ‘ULONG_BITS’ was not declared in this scope
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

I am looking into this.



---

archive/issue_comments_027119.json:
```json
{
    "body": "Moving the climits include before the macro\n\n```\n#if ULONG_MAX == 4294967295U\n#define ULONG_BITS 32\n#elif ULONG_MAX == 18446744073709551615U\n#define ULONG_BITS 64\n#else\n#error Oops! Unsigned long is neither 32 nor 64 bits.\n#error You need to update bern_modp_util.h.\n#endif\n```\nin devel/sage/sage/rings/bernmm/bern_modp_util.h fixes the issue for me. Now doctesting the install.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-12T16:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27119",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Moving the climits include before the macro

```
#if ULONG_MAX == 4294967295U
#define ULONG_BITS 32
#elif ULONG_MAX == 18446744073709551615U
#define ULONG_BITS 64
#else
#error Oops! Unsigned long is neither 32 nor 64 bits.
#error You need to update bern_modp_util.h.
#endif
```
in devel/sage/sage/rings/bernmm/bern_modp_util.h fixes the issue for me. Now doctesting the install.

Cheers,

Michael



---

archive/issue_comments_027120.json:
```json
{
    "body": "Arggh, I'm sorry, I'm an idiot. Of course the #include needs to go before the macro.",
    "created_at": "2008-08-12T17:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27120",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Arggh, I'm sorry, I'm an idiot. Of course the #include needs to go before the macro.



---

archive/issue_comments_027121.json:
```json
{
    "body": "Hi David,\n\nReplying to [comment:4 dmharvey]:\n> Arggh, I'm sorry, I'm an idiot. Of course the #include needs to go before the macro.\n\n\n:) - I do the same thing on a pretty regular basis. Do you want to update the patch or should I post a follow up patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-12T17:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi David,

Replying to [comment:4 dmharvey]:
> Arggh, I'm sorry, I'm an idiot. Of course the #include needs to go before the macro.


:) - I do the same thing on a pretty regular basis. Do you want to update the patch or should I post a follow up patch?

Cheers,

Michael



---

archive/issue_comments_027122.json:
```json
{
    "body": "Attachment [trac_3821-2.patch](tarball://root/attachments/some-uuid/ticket3821/trac_3821-2.patch) by dmharvey created at 2008-08-12 17:24:31",
    "created_at": "2008-08-12T17:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27122",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [trac_3821-2.patch](tarball://root/attachments/some-uuid/ticket3821/trac_3821-2.patch) by dmharvey created at 2008-08-12 17:24:31



---

archive/issue_comments_027123.json:
```json
{
    "body": "Positive review. Thanks David for the quick fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-12T21:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. Thanks David for the quick fix.

Cheers,

Michael



---

archive/issue_comments_027124.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-12T21:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027125.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha2",
    "created_at": "2008-08-12T21:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3821#issuecomment-27125",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.alpha2



---

archive/issue_events_008765.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-12T21:38:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3821",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3821#event-8765"
}
```
