# Issue 9075: sage.structure.sage_object.unpickle_all improvements

archive/issues_009075.json:
```json
{
    "body": "Assignee: was\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9075\n\n",
    "created_at": "2010-05-28T17:38:25Z",
    "labels": [
        "pickling",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "sage.structure.sage_object.unpickle_all improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9075",
    "user": "nthiery"
}
```
Assignee: was

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/9075





---

archive/issue_comments_084225.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-28T17:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84225",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084226.json:
```json
{
    "body": "Changing keywords from \"\" to \"pickling, testsuite\".",
    "created_at": "2010-05-28T17:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84226",
    "user": "nthiery"
}
```

Changing keywords from "" to "pickling, testsuite".



---

archive/issue_comments_084227.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T00:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84227",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084228.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-17T00:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84228",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_084229.json:
```json
{
    "body": "Hi Mike!\n\nReplying to [comment:2 mhansen]:\n> Looks good to me.\n\nThanks for the review!",
    "created_at": "2010-09-17T09:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84229",
    "user": "nthiery"
}
```

Hi Mike!

Replying to [comment:2 mhansen]:
> Looks good to me.

Thanks for the review!



---

archive/issue_comments_084230.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84230",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_084231.json:
```json
{
    "body": "Actually, I get a docbuild error:\n\n```\ndocstring of sage.structure.sage_object.unpickle_all:39: (ERROR/3) Unknown interpreted text role \"cls\".\n```\n\nI've unmerged the patch.",
    "created_at": "2010-09-28T09:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84231",
    "user": "mpatel"
}
```

Actually, I get a docbuild error:

```
docstring of sage.structure.sage_object.unpickle_all:39: (ERROR/3) Unknown interpreted text role "cls".
```

I've unmerged the patch.



---

archive/issue_comments_084232.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-09-28T09:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84232",
    "user": "mpatel"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_084233.json:
```json
{
    "body": "Attachment [trac_9075_unpickle_all_testsuite-nt.patch](tarball://root/attachments/some-uuid/ticket9075/trac_9075_unpickle_all_testsuite-nt.patch) by nthiery created at 2010-10-13 20:08:32",
    "created_at": "2010-10-13T20:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84233",
    "user": "nthiery"
}
```

Attachment [trac_9075_unpickle_all_testsuite-nt.patch](tarball://root/attachments/some-uuid/ticket9075/trac_9075_unpickle_all_testsuite-nt.patch) by nthiery created at 2010-10-13 20:08:32



---

archive/issue_comments_084234.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Actually, I get a docbuild error:\n> {{{\n> docstring of sage.structure.sage_object.unpickle_all:39: (ERROR/3) Unknown interpreted text role \"cls\".\n> }}}\n> I've unmerged the patch.\n\nArgl; Florent had actually already fixed this, but I forgot to upload the updated version of the patch. Since the only difference between the two patches is the cls -> class change, I am allowing myself to revert back the status to positive review.",
    "created_at": "2010-10-13T20:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84234",
    "user": "nthiery"
}
```

Replying to [comment:5 mpatel]:
> Actually, I get a docbuild error:
> {{{
> docstring of sage.structure.sage_object.unpickle_all:39: (ERROR/3) Unknown interpreted text role "cls".
> }}}
> I've unmerged the patch.

Argl; Florent had actually already fixed this, but I forgot to upload the updated version of the patch. Since the only difference between the two patches is the cls -> class change, I am allowing myself to revert back the status to positive review.



---

archive/issue_comments_084235.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-13T20:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9075#issuecomment-84235",
    "user": "nthiery"
}
```

Changing status from needs_work to positive_review.
