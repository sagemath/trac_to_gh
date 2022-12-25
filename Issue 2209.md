# Issue 2209: gap on itanium - incorporate steve linton's new fixes so gap builds fine with optimizations

archive/issues_002209.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe patch is here:\n\n   http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/2209\n\n",
    "created_at": "2008-02-19T15:19:47Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "gap on itanium - incorporate steve linton's new fixes so gap builds fine with optimizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2209",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

The patch is here:

   http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html

Issue created by migration from https://trac.sagemath.org/ticket/2209





---

archive/issue_comments_014556.json:
```json
{
    "body": "I've created an updated package that:\n \n1. Incorporates this patch and re-enables optimizations on ia64.\n\n2. Copies the html gap docs to SAGE_ROOT/local/doc/\n\nThe new spkg is here:\n\nhttp://sage.math.washington.edu/home/was/patches/gap/gap-4.4.10.p3.spkg\n\nPlease test!",
    "created_at": "2008-02-19T15:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14556",
    "user": "https://github.com/williamstein"
}
```

I've created an updated package that:
 
1. Incorporates this patch and re-enables optimizations on ia64.

2. Copies the html gap docs to SAGE_ROOT/local/doc/

The new spkg is here:

http://sage.math.washington.edu/home/was/patches/gap/gap-4.4.10.p3.spkg

Please test!



---

archive/issue_events_005271.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:07:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2209#event-5271"
}
```



---

archive/issue_comments_014557.json:
```json
{
    "body": "on intel mac 10.5: installed fine, doctests pass in sage/interfaces/ . Needs review on itanium to tell if the fixes actually work.",
    "created_at": "2008-05-12T11:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14557",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

on intel mac 10.5: installed fine, doctests pass in sage/interfaces/ . Needs review on itanium to tell if the fixes actually work.



---

archive/issue_comments_014558.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-15T21:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14558",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_014559.json:
```json
{
    "body": "Note -- reviewing this has to wait until SkyNet isn't down....",
    "created_at": "2008-06-15T22:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14559",
    "user": "https://github.com/williamstein"
}
```

Note -- reviewing this has to wait until SkyNet isn't down....



---

archive/issue_comments_014560.json:
```json
{
    "body": "Note that there have been many small fixes to the GAP.spkg, so the fixes have to be rebased on the current one.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T22:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that there have been many small fixes to the GAP.spkg, so the fixes have to be rebased on the current one.

Cheers,

Michael



---

archive/issue_events_005272.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-09T18:46:15Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2209#event-5272"
}
```



---

archive/issue_events_005273.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-07-09T18:46:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "milestone": "sage-3.0.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2209#event-5273"
}
```



---

archive/issue_comments_014561.json:
```json
{
    "body": "Attachment [itanium.s](tarball://root/attachments/some-uuid/ticket2209/itanium.s) by @williamstein created at 2008-08-27 19:51:23",
    "created_at": "2008-08-27T19:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14561",
    "user": "https://github.com/williamstein"
}
```

Attachment [itanium.s](tarball://root/attachments/some-uuid/ticket2209/itanium.s) by @williamstein created at 2008-08-27 19:51:23



---

archive/issue_comments_014562.json:
```json
{
    "body": "I skimmed Steve Linton's patch from \n\n http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html\n\nthen applied it and tested it on itanium.  It worked perfectly, and also gave a nice 5 times speed up on the first thing I tried:\n\n```\nsage: G = SymmetricGroup(16)\nsage: h = G.normal_subgroups()\n```\n\nI doctested the groups directory, and have started the doctest cycle on everything else.\nI'll post a note here when that is done.",
    "created_at": "2008-08-27T21:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14562",
    "user": "https://github.com/williamstein"
}
```

I skimmed Steve Linton's patch from 

 http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html

then applied it and tested it on itanium.  It worked perfectly, and also gave a nice 5 times speed up on the first thing I tried:

```
sage: G = SymmetricGroup(16)
sage: h = G.normal_subgroups()
```

I doctested the groups directory, and have started the doctest cycle on everything else.
I'll post a note here when that is done.



---

archive/issue_comments_014563.json:
```json
{
    "body": "Second positive review from my end. Doctests on Itanium pass (with exception of the two failures at #3984)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T02:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Second positive review from my end. Doctests on Itanium pass (with exception of the two failures at #3984)

Cheers,

Michael



---

archive/issue_comments_014564.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14564",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_events_005274.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-29T02:58:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2209#event-5274"
}
```



---

archive/issue_comments_014565.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
