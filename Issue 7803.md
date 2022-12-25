# Issue 7803: DeprecationWarning: the sets module is deprecated

archive/issues_007803.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  sage-combinat\n\nKeywords: warnings\n\nI read this warning everytime I start Sage, so I have prepared a simple patch which replaces \"Set\" with the built-in type set. The patch must be applied inside sage-4.3.spkg and changes the file sage/combinat/matrices/latin.py.\n\nI should mention that I did not built Sage from Sage's makefile alone but from a gentoo ebuild written by myself - using upstream Sage does not yield this warning. Anyway, since \"sets\" was deprecated since Python 2.6 this should be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7803\n\n",
    "created_at": "2010-01-01T12:24:11Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "DeprecationWarning: the sets module is deprecated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7803",
    "user": "https://trac.sagemath.org/admin/accounts/users/cschwan"
}
```
Assignee: GeorgSWeber

CC:  sage-combinat

Keywords: warnings

I read this warning everytime I start Sage, so I have prepared a simple patch which replaces "Set" with the built-in type set. The patch must be applied inside sage-4.3.spkg and changes the file sage/combinat/matrices/latin.py.

I should mention that I did not built Sage from Sage's makefile alone but from a gentoo ebuild written by myself - using upstream Sage does not yield this warning. Anyway, since "sets" was deprecated since Python 2.6 this should be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/7803





---

archive/issue_comments_067390.json:
```json
{
    "body": "Attachment [sage-4.3-fix-deprecation-warning.patch](tarball://root/attachments/some-uuid/ticket7803/sage-4.3-fix-deprecation-warning.patch) by cschwan created at 2010-01-01 12:24:52",
    "created_at": "2010-01-01T12:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67390",
    "user": "https://trac.sagemath.org/admin/accounts/users/cschwan"
}
```

Attachment [sage-4.3-fix-deprecation-warning.patch](tarball://root/attachments/some-uuid/ticket7803/sage-4.3-fix-deprecation-warning.patch) by cschwan created at 2010-01-01 12:24:52



---

archive/issue_comments_067391.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T16:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67391",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067392.json:
```json
{
    "body": "The patch looks good to me. I'll try to launch the doctests shortly, but if someone beats me to it, and finds no issue, feel free to put a positive review.",
    "created_at": "2010-02-16T16:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67392",
    "user": "https://github.com/nthiery"
}
```

The patch looks good to me. I'll try to launch the doctests shortly, but if someone beats me to it, and finds no issue, feel free to put a positive review.



---

archive/issue_comments_067393.json:
```json
{
    "body": "I cannot apply this patch, I get the following:\n\n\n```\nnovoselt@sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7803/sage-4.3-fix-deprecation-warning.patch\nadding sage-4.3-fix-deprecation-warning.patch to series file\nnovoselt@sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qpush\napplying sage-4.3-fix-deprecation-warning.patch\nunable to find 'combinat/matrices/latin.py' for patching\n3 out of 3 hunks FAILED -- saving rejects to file combinat/matrices/latin.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh sage-4.3-fix-deprecation-warning.patch\n\n```\n\n\nI checked that the file is actually still there (and the above commands work fine for other patches).\n\nAlso, it seems that there is no user information and commit message with the ticket number in the patch file.",
    "created_at": "2010-04-17T23:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67393",
    "user": "https://github.com/novoselt"
}
```

I cannot apply this patch, I get the following:


```
novoselt@sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7803/sage-4.3-fix-deprecation-warning.patch
adding sage-4.3-fix-deprecation-warning.patch to series file
novoselt@sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qpush
applying sage-4.3-fix-deprecation-warning.patch
unable to find 'combinat/matrices/latin.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file combinat/matrices/latin.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh sage-4.3-fix-deprecation-warning.patch

```


I checked that the file is actually still there (and the above commands work fine for other patches).

Also, it seems that there is no user information and commit message with the ticket number in the patch file.



---

archive/issue_comments_067394.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-17T23:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67394",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067395.json:
```json
{
    "body": "Replying to [comment:3 novoselt]:\n> I cannot apply this patch, I get the following:\n> \n> {{{\n> novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7803/sage-4.3-fix-deprecation-warning.patch\n> adding sage-4.3-fix-deprecation-warning.patch to series file\n> novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qpush\n> applying sage-4.3-fix-deprecation-warning.patch\n> unable to find 'combinat/matrices/latin.py' for patching\n> 3 out of 3 hunks FAILED -- saving rejects to file combinat/matrices/latin.py.rej\n> patch failed, unable to continue (try -v)\n> patch failed, rejects left in working dir\n> errors during apply, please fix and refresh sage-4.3-fix-deprecation-warning.patch\n> \n> }}}\n> \n> I checked that the file is actually still there (and the above commands work fine for other patches).\n\nThe command fails because the patch was not generated with mercurials diff command (at the time I reported I did not know that you had to use mercurial for generating patches). So the command works if you use the standard patch command: patch < patchfile.patch - which course overwrites the original files. I will upload an hg-ified patch later.\n\nI can also clarify the need of this patch: If one updates ipython and runs testcases without this patch a lot of testcases will fail because python now prints deprecation warnings.\n\n> \n> Also, it seems that there is no user information and commit message with the ticket number in the patch file.",
    "created_at": "2010-04-18T09:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67395",
    "user": "https://trac.sagemath.org/admin/accounts/users/cschwan"
}
```

Replying to [comment:3 novoselt]:
> I cannot apply this patch, I get the following:
> 
> {{{
> novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7803/sage-4.3-fix-deprecation-warning.patch
> adding sage-4.3-fix-deprecation-warning.patch to series file
> novoselt`@`sage:/scratch/novoselt/sage-4.3.5/devel/sage-main$ hg qpush
> applying sage-4.3-fix-deprecation-warning.patch
> unable to find 'combinat/matrices/latin.py' for patching
> 3 out of 3 hunks FAILED -- saving rejects to file combinat/matrices/latin.py.rej
> patch failed, unable to continue (try -v)
> patch failed, rejects left in working dir
> errors during apply, please fix and refresh sage-4.3-fix-deprecation-warning.patch
> 
> }}}
> 
> I checked that the file is actually still there (and the above commands work fine for other patches).

The command fails because the patch was not generated with mercurials diff command (at the time I reported I did not know that you had to use mercurial for generating patches). So the command works if you use the standard patch command: patch < patchfile.patch - which course overwrites the original files. I will upload an hg-ified patch later.

I can also clarify the need of this patch: If one updates ipython and runs testcases without this patch a lot of testcases will fail because python now prints deprecation warnings.

> 
> Also, it seems that there is no user information and commit message with the ticket number in the patch file.



---

archive/issue_comments_067396.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-21T16:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67396",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067397.json:
```json
{
    "body": "Attachment [sage-4.3.4-fix-usage-of-deprecated-sets-module.patch](tarball://root/attachments/some-uuid/ticket7803/sage-4.3.4-fix-usage-of-deprecated-sets-module.patch) by @novoselt created at 2010-05-21 16:44:15\n\nMaking new attachments does not create \"ticket update\" messages, so I didn't know that a new version is added. As I understand, this is now ready for review, so I'll go ahead and change the status.",
    "created_at": "2010-05-21T16:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67397",
    "user": "https://github.com/novoselt"
}
```

Attachment [sage-4.3.4-fix-usage-of-deprecated-sets-module.patch](tarball://root/attachments/some-uuid/ticket7803/sage-4.3.4-fix-usage-of-deprecated-sets-module.patch) by @novoselt created at 2010-05-21 16:44:15

Making new attachments does not create "ticket update" messages, so I didn't know that a new version is added. As I understand, this is now ready for review, so I'll go ahead and change the status.



---

archive/issue_comments_067398.json:
```json
{
    "body": "While I do not see waring messages anyway, the changes are transparent and are for the good. All doctests pass with 4.4.2.",
    "created_at": "2010-05-21T16:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67398",
    "user": "https://github.com/novoselt"
}
```

While I do not see waring messages anyway, the changes are transparent and are for the good. All doctests pass with 4.4.2.



---

archive/issue_comments_067399.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-21T16:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67399",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067400.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7803#issuecomment-67400",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
