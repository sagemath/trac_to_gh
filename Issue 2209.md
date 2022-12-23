# Issue 2209: gap on itanium - incorporate steve linton's new fixes so gap builds fine with optimizations

archive/issues_002209.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe patch is here:\n\n   http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/2209\n\n",
    "created_at": "2008-02-19T15:19:47Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "gap on itanium - incorporate steve linton's new fixes so gap builds fine with optimizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2209",
    "user": "was"
}
```
Assignee: mabshoff

The patch is here:

   http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html

Issue created by migration from https://trac.sagemath.org/ticket/2209





---

archive/issue_comments_014587.json:
```json
{
    "body": "I've created an updated package that:\n \n1. Incorporates this patch and re-enables optimizations on ia64.\n\n2. Copies the html gap docs to SAGE_ROOT/local/doc/\n\nThe new spkg is here:\n\nhttp://sage.math.washington.edu/home/was/patches/gap/gap-4.4.10.p3.spkg\n\nPlease test!",
    "created_at": "2008-02-19T15:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14587",
    "user": "was"
}
```

I've created an updated package that:
 
1. Incorporates this patch and re-enables optimizations on ia64.

2. Copies the html gap docs to SAGE_ROOT/local/doc/

The new spkg is here:

http://sage.math.washington.edu/home/was/patches/gap/gap-4.4.10.p3.spkg

Please test!



---

archive/issue_comments_014588.json:
```json
{
    "body": "on intel mac 10.5: installed fine, doctests pass in sage/interfaces/ . Needs review on itanium to tell if the fixes actually work.",
    "created_at": "2008-05-12T11:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14588",
    "user": "broune"
}
```

on intel mac 10.5: installed fine, doctests pass in sage/interfaces/ . Needs review on itanium to tell if the fixes actually work.



---

archive/issue_comments_014589.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-15T21:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14589",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_014590.json:
```json
{
    "body": "Note -- reviewing this has to wait until SkyNet isn't down....",
    "created_at": "2008-06-15T22:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14590",
    "user": "was"
}
```

Note -- reviewing this has to wait until SkyNet isn't down....



---

archive/issue_comments_014591.json:
```json
{
    "body": "Note that there have been many small fixes to the GAP.spkg, so the fixes have to be rebased on the current one.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T22:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14591",
    "user": "mabshoff"
}
```

Note that there have been many small fixes to the GAP.spkg, so the fixes have to be rebased on the current one.

Cheers,

Michael



---

archive/issue_comments_014592.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-27T19:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14592",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_014593.json:
```json
{
    "body": "I skimmed Steve Linton's patch from \n\n http://www.gap-system.org/Faq/Hardware-OS/hardware-os8.html\n\nthen applied it and tested it on itanium.  It worked perfectly, and also gave a nice 5 times speed up on the first thing I tried:\n\n```\nsage: G = SymmetricGroup(16)\nsage: h = G.normal_subgroups()\n```\n\n\nI doctested the groups directory, and have started the doctest cycle on everything else.\nI'll post a note here when that is done.",
    "created_at": "2008-08-27T21:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14593",
    "user": "was"
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

archive/issue_comments_014594.json:
```json
{
    "body": "Second positive review from my end. Doctests on Itanium pass (with exception of the two failures at #3984)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T02:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14594",
    "user": "mabshoff"
}
```

Second positive review from my end. Doctests on Itanium pass (with exception of the two failures at #3984)

Cheers,

Michael



---

archive/issue_comments_014595.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14595",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_014596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2209#issuecomment-14596",
    "user": "mabshoff"
}
```

Resolution: fixed
