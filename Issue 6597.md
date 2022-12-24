# Issue 6597: [with patch, needs review] SetMorphism: 100% doctest + equality + pickling

archive/issues_006597.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  sage-combinat cwitty saliola\n\nKeywords: doctest, SetMorphism, pickling\n\nThis patch raises SetMorphism to 100% doctest, and implements equality and pickling.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6597\n\n",
    "created_at": "2009-07-23T08:51:13Z",
    "labels": [
        "coercion",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] SetMorphism: 100% doctest + equality + pickling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6597",
    "user": "nthiery"
}
```
Assignee: robertwb

CC:  sage-combinat cwitty saliola

Keywords: doctest, SetMorphism, pickling

This patch raises SetMorphism to 100% doctest, and implements equality and pickling.

Issue created by migration from https://trac.sagemath.org/ticket/6597





---

archive/issue_comments_054009.json:
```json
{
    "body": "Changing assignee from robertwb to nthiery.",
    "created_at": "2009-09-02T15:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6597#issuecomment-54009",
    "user": "nthiery"
}
```

Changing assignee from robertwb to nthiery.



---

archive/issue_comments_054010.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-02T15:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6597#issuecomment-54010",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054011.json:
```json
{
    "body": "Attachment [trac_6597_set_morphism_doc_pickling.patch](tarball://root/attachments/some-uuid/ticket6597/trac_6597_set_morphism_doc_pickling.patch) by nthiery created at 2009-09-02 15:17:04",
    "created_at": "2009-09-02T15:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6597#issuecomment-54011",
    "user": "nthiery"
}
```

Attachment [trac_6597_set_morphism_doc_pickling.patch](tarball://root/attachments/some-uuid/ticket6597/trac_6597_set_morphism_doc_pickling.patch) by nthiery created at 2009-09-02 15:17:04



---

archive/issue_comments_054012.json:
```json
{
    "body": "Looks good to me.  All tests pass with it once #6343 is applied to Sage 4.1.1.\n\nNote it takes awhile to build everything.",
    "created_at": "2009-09-08T19:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6597#issuecomment-54012",
    "user": "mhansen"
}
```

Looks good to me.  All tests pass with it once #6343 is applied to Sage 4.1.1.

Note it takes awhile to build everything.



---

archive/issue_comments_054013.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> Looks good to me.  All tests pass with it once #6343 is applied to Sage 4.1.1.\n\nThanks Mike for the review!\n\n> Note it takes awhile to build everything.\n\nYeah, I had to modify the .pxd of Map (or Morphism) to get pickling to work.\n\nI am glad this will be soon in so that we don't have this patch anymore in Sage-Combinat.",
    "created_at": "2009-09-08T20:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6597#issuecomment-54013",
    "user": "nthiery"
}
```

Replying to [comment:3 mhansen]:
> Looks good to me.  All tests pass with it once #6343 is applied to Sage 4.1.1.

Thanks Mike for the review!

> Note it takes awhile to build everything.

Yeah, I had to modify the .pxd of Map (or Morphism) to get pickling to work.

I am glad this will be soon in so that we don't have this patch anymore in Sage-Combinat.



---

archive/issue_comments_054014.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T08:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6597#issuecomment-54014",
    "user": "mvngu"
}
```

Resolution: fixed
