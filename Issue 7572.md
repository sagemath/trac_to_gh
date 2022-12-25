# Issue 7572: Memleak in GLPK interface

archive/issues_007572.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nathanncohen\n\nThe GLPK interface `sage_malloc`s various arrays and never frees them. Also the interface uses Python keywords as variable names.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7572\n\n",
    "created_at": "2009-12-01T15:53:33Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Memleak in GLPK interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7572",
    "user": "https://github.com/malb"
}
```
Assignee: tbd

CC:  @nathanncohen

The GLPK interface `sage_malloc`s various arrays and never frees them. Also the interface uses Python keywords as variable names.

Issue created by migration from https://trac.sagemath.org/ticket/7572





---

archive/issue_comments_064333.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-01T15:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64333",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064334.json:
```json
{
    "body": "Attachment [glpk_sage_free.patch](tarball://root/attachments/some-uuid/ticket7572/glpk_sage_free.patch) by @malb created at 2009-12-01 15:54:16\n\nThe attached patch is for the GLPK SPKG.",
    "created_at": "2009-12-01T15:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64334",
    "user": "https://github.com/malb"
}
```

Attachment [glpk_sage_free.patch](tarball://root/attachments/some-uuid/ticket7572/glpk_sage_free.patch) by @malb created at 2009-12-01 15:54:16

The attached patch is for the GLPK SPKG.



---

archive/issue_comments_064335.json:
```json
{
    "body": "Thank you for your help !!! just one question though : on which version of GLPK is your patch based ? The new version of GLPK is available in #7268 and still waiting for review... Could we merge your changes in ? :-)\n\nI had no idea that \"id\" was a python keyword... And thank you for noticing this memory leak !\n\nNathann",
    "created_at": "2009-12-01T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64335",
    "user": "https://github.com/nathanncohen"
}
```

Thank you for your help !!! just one question though : on which version of GLPK is your patch based ? The new version of GLPK is available in #7268 and still waiting for review... Could we merge your changes in ? :-)

I had no idea that "id" was a python keyword... And thank you for noticing this memory leak !

Nathann



---

archive/issue_comments_064336.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-01T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64336",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_064337.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> Thank you for your help !!! just one question though : on which version of GLPK is your patch based ? The new version of GLPK is available in #7268 and still waiting for review... Could we merge your changes in ? :-)\n\nSure, I'll take a look at #7268.\n \n> I had no idea that \"id\" was a python keyword... And thank you for noticing this memory leak !\n \nMe neither, but Emacs noticed it :) I think there's still a memleak there, you `new glp_ioct` but never `delete` it. However, I couldn't find anything on `glp_ioct` anywhere.",
    "created_at": "2009-12-01T16:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64337",
    "user": "https://github.com/malb"
}
```

Replying to [comment:2 ncohen]:
> Thank you for your help !!! just one question though : on which version of GLPK is your patch based ? The new version of GLPK is available in #7268 and still waiting for review... Could we merge your changes in ? :-)

Sure, I'll take a look at #7268.
 
> I had no idea that "id" was a python keyword... And thank you for noticing this memory leak !
 
Me neither, but Emacs noticed it :) I think there's still a memleak there, you `new glp_ioct` but never `delete` it. However, I couldn't find anything on `glp_ioct` anywhere.



---

archive/issue_comments_064338.json:
```json
{
    "body": "This could be deleted as part of the whole GLPK version of the LP syste, though... But it could be good to take a look at it, indeed :-)\n\nNathann",
    "created_at": "2009-12-01T16:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64338",
    "user": "https://github.com/nathanncohen"
}
```

This could be deleted as part of the whole GLPK version of the LP syste, though... But it could be good to take a look at it, indeed :-)

Nathann



---

archive/issue_comments_064339.json:
```json
{
    "body": "This is now fixed in #7268",
    "created_at": "2009-12-01T17:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64339",
    "user": "https://github.com/malb"
}
```

This is now fixed in #7268



---

archive/issue_comments_064340.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-01T17:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7572#issuecomment-64340",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate
