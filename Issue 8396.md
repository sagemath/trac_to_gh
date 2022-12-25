# Issue 8396: element_class of Subsets is broken

archive/issues_008396.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  nborie\n\nelement_class of Subsets is broken\n\n```\nsage: s = Subsets(Set([1]))\nsage: e = s.first()\nsage: isinstance(e, s.element_class)\nFalse\n```\n\n\nNote: this should be caught by setting good categories\n\n```\nsage: s.category()\nCategory of objects\n}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/8396\n\n",
    "created_at": "2010-02-28T15:13:10Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "element_class of Subsets is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8396",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```
Assignee: sage-combinat

CC:  nborie

element_class of Subsets is broken

```
sage: s = Subsets(Set([1]))
sage: e = s.first()
sage: isinstance(e, s.element_class)
False
```


Note: this should be caught by setting good categories

```
sage: s.category()
Category of objects
}}

Issue created by migration from https://trac.sagemath.org/ticket/8396





---

archive/issue_comments_075099.json:
```json
{
    "body": "Changing keywords from \"\" to \"Subsets element_class\".",
    "created_at": "2010-02-28T15:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75099",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Changing keywords from "" to "Subsets element_class".



---

archive/issue_comments_075100.json:
```json
{
    "body": "Changing assignee from sage-combinat to giraudo.",
    "created_at": "2010-02-28T15:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75100",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Changing assignee from sage-combinat to giraudo.



---

archive/issue_comments_075101.json:
```json
{
    "body": "There is a little mistake I made a lot with the Trac...\n\nSamuele, you have to export your patch and after upload them to the trac. Clic on your patch on the trac and after, read on the top the information : \n*****************************************************************\n#8367: fix element_class of Subsets\n\ndiff --git a/sage/combinat/subset.py *****************************************************************\n\nIt's to short because you probably just upload the patch from .hg/patches/\n\nuse: sage -hg trac_8396_subsets_element_class_fix-sg.patch > your_favorite_directory/trac_8396_subsets_element_class_fix-sg.patch\n\nand upload to the trac the exported patch, you will see more hg information at the top of the patch.\n\nOnce you do that, I will have a look on your fix!\n\nBye Samuele.",
    "created_at": "2010-02-28T20:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75101",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

There is a little mistake I made a lot with the Trac...

Samuele, you have to export your patch and after upload them to the trac. Clic on your patch on the trac and after, read on the top the information : 
*****************************************************************
#8367: fix element_class of Subsets

diff --git a/sage/combinat/subset.py *****************************************************************

It's to short because you probably just upload the patch from .hg/patches/

use: sage -hg trac_8396_subsets_element_class_fix-sg.patch > your_favorite_directory/trac_8396_subsets_element_class_fix-sg.patch

and upload to the trac the exported patch, you will see more hg information at the top of the patch.

Once you do that, I will have a look on your fix!

Bye Samuele.



---

archive/issue_comments_075102.json:
```json
{
    "body": "use: sage -hg export trac_8396_subsets_element_class_fix-sg.patch > your_favorite_directory/trac_8396_subsets_element_class_fix-sg.patch \n\nsorry!!! I forget the export in the command. And do this command from\nsage-combinat/ directory.",
    "created_at": "2010-02-28T20:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75102",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

use: sage -hg export trac_8396_subsets_element_class_fix-sg.patch > your_favorite_directory/trac_8396_subsets_element_class_fix-sg.patch 

sorry!!! I forget the export in the command. And do this command from
sage-combinat/ directory.



---

archive/issue_comments_075103.json:
```json
{
    "body": "Attachment [trac_8396_subsets_element_class_fix-sg.patch](tarball://root/attachments/some-uuid/ticket8396/trac_8396_subsets_element_class_fix-sg.patch) by giraudo created at 2010-02-28 21:40:14\n\nThanks Nicolas, it is done !",
    "created_at": "2010-02-28T21:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75103",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Attachment [trac_8396_subsets_element_class_fix-sg.patch](tarball://root/attachments/some-uuid/ticket8396/trac_8396_subsets_element_class_fix-sg.patch) by giraudo created at 2010-02-28 21:40:14

Thanks Nicolas, it is done !



---

archive/issue_comments_075104.json:
```json
{
    "body": "Perfect! Now to inform any reviewer that you think your job is over on this problem, you should set your ticket as 'needs review' and thus, some people will download it and test it...\n\nIf you do so, I will review it. If you don't change the status, we will have the impression you are still working on the problem and you don't want the review now.",
    "created_at": "2010-02-28T21:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75104",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Perfect! Now to inform any reviewer that you think your job is over on this problem, you should set your ticket as 'needs review' and thus, some people will download it and test it...

If you do so, I will review it. If you don't change the status, we will have the impression you are still working on the problem and you don't want the review now.



---

archive/issue_comments_075105.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-28T22:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75105",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075106.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-28T23:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75106",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075107.json:
```json
{
    "body": "The patch apply, the tests passed and the patch fix this ticket. Positive review.",
    "created_at": "2010-02-28T23:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75107",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

The patch apply, the tests passed and the patch fix this ticket. Positive review.



---

archive/issue_comments_075108.json:
```json
{
    "body": "Thanks a lot Nicolas for your revision and advices :-)",
    "created_at": "2010-03-01T17:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75108",
    "user": "https://trac.sagemath.org/admin/accounts/users/giraudo"
}
```

Thanks a lot Nicolas for your revision and advices :-)



---

archive/issue_events_008581.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T21:40:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8396#event-8581"
}
```



---

archive/issue_comments_075109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_075110.json:
```json
{
    "body": "Samuele: Mercurial interprets your \"commit message\" as a comment, hence the message itself won't appear as your commit message:\n\n```\n# 8367: fix element_class of Subsets\n```\n\nNotice the white space between \"#\" and \"8367:\". Avoid putting white space between \"#\" and your ticket number. Your commit message should be something like this:\n\n```\n#8367: fix element_class of Subsets\n```\n",
    "created_at": "2010-03-02T21:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8396#issuecomment-75110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Samuele: Mercurial interprets your "commit message" as a comment, hence the message itself won't appear as your commit message:

```
# 8367: fix element_class of Subsets
```

Notice the white space between "#" and "8367:". Avoid putting white space between "#" and your ticket number. Your commit message should be something like this:

```
#8367: fix element_class of Subsets
```

