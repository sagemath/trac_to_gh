# Issue 5985: cPickle: adds support for class pickling customizing  and for nested classes

archive/issues_005985.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat cwitty @saliola @burcin @craigcitro\n\nKeywords: cPickle, pickling classes\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5985\n\n",
    "created_at": "2009-05-05T05:54:04Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "cPickle: adds support for class pickling customizing  and for nested classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5985",
    "user": "@nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat cwitty @saliola @burcin @craigcitro

Keywords: cPickle, pickling classes



Issue created by migration from https://trac.sagemath.org/ticket/5985





---

archive/issue_comments_047549.json:
```json
{
    "body": "I just rebased the first patch upon 3.4.2 final. Please ignore (or better delete) the old version  cPickle-5985-import.patch",
    "created_at": "2009-05-06T23:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47549",
    "user": "@nthiery"
}
```

I just rebased the first patch upon 3.4.2 final. Please ignore (or better delete) the old version  cPickle-5985-import.patch



---

archive/issue_comments_047550.json:
```json
{
    "body": "Note: the cPickle imports in dsage will need to be updated as well.",
    "created_at": "2009-05-07T01:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47550",
    "user": "@nthiery"
}
```

Note: the cPickle imports in dsage will need to be updated as well.



---

archive/issue_comments_047551.json:
```json
{
    "body": "Updated patch:\n- Fixes a trivially failing doctest (don't know why I did not see them earlier)\n- Adds some more doctest",
    "created_at": "2009-05-12T22:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47551",
    "user": "@nthiery"
}
```

Updated patch:
- Fixes a trivially failing doctest (don't know why I did not see them earlier)
- Adds some more doctest



---

archive/issue_comments_047552.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47552",
    "user": "@nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047553.json:
```json
{
    "body": "This patch needs an explicit addition of sage/misc/cPickle.c to MANIFEST.in for -sdist to work. It is also listed to have a positive review in the [CategoriesRoadMap](CategoriesRoadMap), but it isn't on the ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T14:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47553",
    "user": "mabshoff"
}
```

This patch needs an explicit addition of sage/misc/cPickle.c to MANIFEST.in for -sdist to work. It is also listed to have a positive review in the [CategoriesRoadMap](CategoriesRoadMap), but it isn't on the ticket.

Cheers,

Michael



---

archive/issue_comments_047554.json:
```json
{
    "body": "Followup at #5986",
    "created_at": "2009-05-22T23:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47554",
    "user": "@robertwb"
}
```

Followup at #5986



---

archive/issue_comments_047555.json:
```json
{
    "body": "Attachment [cPickle-5985-import-submitted.patch](tarball://root/attachments/some-uuid/ticket5985/cPickle-5985-import-submitted.patch) by @nthiery created at 2009-05-23 07:42:38",
    "created_at": "2009-05-23T07:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47555",
    "user": "@nthiery"
}
```

Attachment [cPickle-5985-import-submitted.patch](tarball://root/attachments/some-uuid/ticket5985/cPickle-5985-import-submitted.patch) by @nthiery created at 2009-05-23 07:42:38



---

archive/issue_comments_047556.json:
```json
{
    "body": "Replying to [comment:10 mabshoff]:\n> This patch needs an explicit addition of sage/misc/cPickle.c to MANIFEST.in for -sdist to work.\n\nThe updated patch hopefully fixes this (please double check).\n\n> It is also listed to have a positive review in the [CategoriesRoadMap](CategoriesRoadMap), but it isn't on the ticket.\n\nOops, fixed. Someone was supposed to give a positive review, but apparently this has not occurred yet.",
    "created_at": "2009-05-23T07:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47556",
    "user": "@nthiery"
}
```

Replying to [comment:10 mabshoff]:
> This patch needs an explicit addition of sage/misc/cPickle.c to MANIFEST.in for -sdist to work.

The updated patch hopefully fixes this (please double check).

> It is also listed to have a positive review in the [CategoriesRoadMap](CategoriesRoadMap), but it isn't on the ticket.

Oops, fixed. Someone was supposed to give a positive review, but apparently this has not occurred yet.



---

archive/issue_comments_047557.json:
```json
{
    "body": "I've rolled an spkg with the patch by Nicolas incorporated -- it's here:\n\n  http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg\n\nIt's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. \n\nI should have more time to look at this tonight (and give it a review, assuming it works).",
    "created_at": "2009-07-08T22:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47557",
    "user": "@craigcitro"
}
```

I've rolled an spkg with the patch by Nicolas incorporated -- it's here:

  http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg

It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. 

I should have more time to look at this tonight (and give it a review, assuming it works).



---

archive/issue_comments_047558.json:
```json
{
    "body": "Replying to [comment:13 craigcitro]:\n> I've rolled an spkg with the patch by Nicolas incorporated -- it's here:\n> \n>   http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg\n> \n> It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. \n> \n> I should have more time to look at this tonight (and give it a review, assuming it works).\n\nThanks for working on this!\n\nThe patch cPickle-5985-copy_reg_classes-submitted.patch includes a fairly complete testsuite (see the addition to sage/misc/test_cpickle_sage.py)",
    "created_at": "2009-07-09T10:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47558",
    "user": "@nthiery"
}
```

Replying to [comment:13 craigcitro]:
> I've rolled an spkg with the patch by Nicolas incorporated -- it's here:
> 
>   http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg
> 
> It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. 
> 
> I should have more time to look at this tonight (and give it a review, assuming it works).

Thanks for working on this!

The patch cPickle-5985-copy_reg_classes-submitted.patch includes a fairly complete testsuite (see the addition to sage/misc/test_cpickle_sage.py)



---

archive/issue_comments_047559.json:
```json
{
    "body": "Attachment [cPickle-5985-copy_reg_classes-submitted.patch](tarball://root/attachments/some-uuid/ticket5985/cPickle-5985-copy_reg_classes-submitted.patch) by @nthiery created at 2009-07-11 22:48:25\n\nReplying to [comment:14 nthiery]:\n> Replying to [comment:13 craigcitro]:\n> > I've rolled an spkg with the patch by Nicolas incorporated -- it's here:\n> > \n> >   http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg\n> > \n> > It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. \n> > \n> > I should have more time to look at this tonight (and give it a review, assuming it works).\n> \n> Thanks for working on this!\n> \n> The patch cPickle-5985-copy_reg_classes-submitted.patch includes a fairly complete testsuite (see the addition to sage/misc/test_cpickle_sage.py)\n\nOops, this testsuite used type.__new__(...) which apparently does not work anymore with Python 2.6. I just rewrote the testsuite so that it does not use this feature anymore. See attached patch.\n\nLuckily enough, the real applications of this patch readily did not use this feature anymore!",
    "created_at": "2009-07-11T22:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47559",
    "user": "@nthiery"
}
```

Attachment [cPickle-5985-copy_reg_classes-submitted.patch](tarball://root/attachments/some-uuid/ticket5985/cPickle-5985-copy_reg_classes-submitted.patch) by @nthiery created at 2009-07-11 22:48:25

Replying to [comment:14 nthiery]:
> Replying to [comment:13 craigcitro]:
> > I've rolled an spkg with the patch by Nicolas incorporated -- it's here:
> > 
> >   http://sage.math.washington.edu/home/craigcitro/four-one/python-2.6.2.p2.spkg
> > 
> > It's not ready to be merged (I need to commit the changes in hg), but I'd like Nicolas to confirm that it still works before I play with it too much. Or, if there's an easy testcase, post that and I'll play with it. 
> > 
> > I should have more time to look at this tonight (and give it a review, assuming it works).
> 
> Thanks for working on this!
> 
> The patch cPickle-5985-copy_reg_classes-submitted.patch includes a fairly complete testsuite (see the addition to sage/misc/test_cpickle_sage.py)

Oops, this testsuite used type.__new__(...) which apparently does not work anymore with Python 2.6. I just rewrote the testsuite so that it does not use this feature anymore. See attached patch.

Luckily enough, the real applications of this patch readily did not use this feature anymore!



---

archive/issue_comments_047560.json:
```json
{
    "body": "Replying to [comment:15 nthiery]:\n> Oops, this testsuite used type.__new__(...) which apparently does not work anymore with Python 2.6. I just rewrote the testsuite so that it does not use this feature anymore. See attached patch.\n\nFor the record:\n\nzephyr-/opt/sage-4.0.2>./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: combinat           \nsage: class metaclass(type):\n....:     def __new__(cls):\n....:         return type.__new__(cls, \"bla\", (object,), dict())\n....:\nsage: metaclass()                                                                                                     \n<class '__main__.bla'>\n| Sage Version 4.0.2, Release Date: 2009-06-18                       |\n| Type notebook() for the GUI, and license() for information.        |\nzephyr-~>sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: combinat\nsage: class metaclass(type):\n....:     def __new__(cls):\n....:         return type.__new__(cls, \"bla\", (object,), dict())\n....:\nsage: metaclass()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\nTypeError: type.__init__() takes 1 or 3 arguments\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\nApparently type.__new__ now calls type.__init__. And I assume that can only be a change in python, not in Sage.",
    "created_at": "2009-07-11T22:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47560",
    "user": "@nthiery"
}
```

Replying to [comment:15 nthiery]:
> Oops, this testsuite used type.__new__(...) which apparently does not work anymore with Python 2.6. I just rewrote the testsuite so that it does not use this feature anymore. See attached patch.

For the record:

zephyr-/opt/sage-4.0.2>./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat           
sage: class metaclass(type):
....:     def __new__(cls):
....:         return type.__new__(cls, "bla", (object,), dict())
....:
sage: metaclass()                                                                                                     
<class '__main__.bla'>
| Sage Version 4.0.2, Release Date: 2009-06-18                       |
| Type notebook() for the GUI, and license() for information.        |
zephyr-~>sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: class metaclass(type):
....:     def __new__(cls):
....:         return type.__new__(cls, "bla", (object,), dict())
....:
sage: metaclass()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
TypeError: type.__init__() takes 1 or 3 arguments
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
Apparently type.__new__ now calls type.__init__. And I assume that can only be a change in python, not in Sage.



---

archive/issue_comments_047561.json:
```json
{
    "body": "I'm uploading a new python spkg, which is the same as the previous one I posted, but based on the most recent python spkg in Sage. It's here:\n\n  http://sage.math.washington.edu/home/craigcitro/python-2.6.2.p4.spkg\n\nThis fixes the issue by patching the files in our python spkg instead of importing and using our own copy of `cPickle`. It also makes the corresponding changes to `pickle`.",
    "created_at": "2009-10-09T08:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47561",
    "user": "@craigcitro"
}
```

I'm uploading a new python spkg, which is the same as the previous one I posted, but based on the most recent python spkg in Sage. It's here:

  http://sage.math.washington.edu/home/craigcitro/python-2.6.2.p4.spkg

This fixes the issue by patching the files in our python spkg instead of importing and using our own copy of `cPickle`. It also makes the corresponding changes to `pickle`.



---

archive/issue_comments_047562.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-10-11T08:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47562",
    "user": "@nthiery"
}
```

Changing priority from major to critical.



---

archive/issue_comments_047563.json:
```json
{
    "body": "Replying to [comment:17 craigcitro]:\n> I'm uploading a new python spkg, which is the same as the previous one I posted, but based on the most recent python spkg in Sage. It's here:\n> \n>   http://sage.math.washington.edu/home/craigcitro/python-2.6.2.p4.spkg\n> \n> This fixes the issue by patching the files in our python spkg instead of importing and using our own copy of `cPickle`. It also makes the corresponding changes to `pickle`. \n\nSounds good to me! Positive review, up to someone double checking the new patch I attached which imports the test file from the original version of the patch.\n\nCarl, Craig, Robert, please do it soon! William is ok integrating this in 4.1.2 (see IRC).\nI set back the release to 4.1.2\n\nFor the author / reviewer, I don't know exactly what to do since I wrote the first version, Craig reviewed it, wrote the second version which I reviewed :-) Please set whatever you feel appropriate",
    "created_at": "2009-10-11T08:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47563",
    "user": "@nthiery"
}
```

Replying to [comment:17 craigcitro]:
> I'm uploading a new python spkg, which is the same as the previous one I posted, but based on the most recent python spkg in Sage. It's here:
> 
>   http://sage.math.washington.edu/home/craigcitro/python-2.6.2.p4.spkg
> 
> This fixes the issue by patching the files in our python spkg instead of importing and using our own copy of `cPickle`. It also makes the corresponding changes to `pickle`. 

Sounds good to me! Positive review, up to someone double checking the new patch I attached which imports the test file from the original version of the patch.

Carl, Craig, Robert, please do it soon! William is ok integrating this in 4.1.2 (see IRC).
I set back the release to 4.1.2

For the author / reviewer, I don't know exactly what to do since I wrote the first version, Craig reviewed it, wrote the second version which I reviewed :-) Please set whatever you feel appropriate



---

archive/issue_comments_047564.json:
```json
{
    "body": "I'm happy with Nicolas's patch to test the new python spkg -- let's finally get this merged! Yay!",
    "created_at": "2009-10-15T06:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47564",
    "user": "@craigcitro"
}
```

I'm happy with Nicolas's patch to test the new python spkg -- let's finally get this merged! Yay!



---

archive/issue_comments_047565.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-15T06:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47565",
    "user": "@craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047566.json:
```json
{
    "body": "Attachment [trac_5985_test_class_pickling.patch](tarball://root/attachments/some-uuid/ticket5985/trac_5985_test_class_pickling.patch) by @mwhansen created at 2009-10-15 06:55:09\n\nApply only this patch, after updating the python spkg linked to below",
    "created_at": "2009-10-15T06:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47566",
    "user": "@mwhansen"
}
```

Attachment [trac_5985_test_class_pickling.patch](tarball://root/attachments/some-uuid/ticket5985/trac_5985_test_class_pickling.patch) by @mwhansen created at 2009-10-15 06:55:09

Apply only this patch, after updating the python spkg linked to below



---

archive/issue_comments_047567.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T06:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47567",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_047568.json:
```json
{
    "body": "I updated the patch to do \"import cPickle\" instead of importing it from sage.misc.  After that, everything passes.",
    "created_at": "2009-10-15T06:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5985",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5985#issuecomment-47568",
    "user": "@mwhansen"
}
```

I updated the patch to do "import cPickle" instead of importing it from sage.misc.  After that, everything passes.
