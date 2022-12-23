# Issue 7398: Improved mantra to find whether an object is iterable (and get an iterator out it)

archive/issues_007398.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat was\n\nKeywords: iterators\n\nThe following mantra occurs at three places in Sage's code to test whether v is an iterator:\n\n     if hasattr(v, 'next'):\n\nThis patches replaces them with:\n\n     if hasattr(v, '__iter__')\n\nwhich is safer (some sage objects have a next method without being iterable, or with a different semantic)\n\nif not just, when appropriate:\n\n     v = iter(v)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7398\n\n",
    "created_at": "2009-11-05T18:15:27Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "Improved mantra to find whether an object is iterable (and get an iterator out it)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7398",
    "user": "nthiery"
}
```
Assignee: hivert

CC:  sage-combinat was

Keywords: iterators

The following mantra occurs at three places in Sage's code to test whether v is an iterator:

     if hasattr(v, 'next'):

This patches replaces them with:

     if hasattr(v, '__iter__')

which is safer (some sage objects have a next method without being iterable, or with a different semantic)

if not just, when appropriate:

     v = iter(v)

Issue created by migration from https://trac.sagemath.org/ticket/7398





---

archive/issue_comments_062200.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-05T22:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62200",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062201.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-05T22:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62201",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_062202.json:
```json
{
    "body": "Attachment\n\nUpdated patch after review by Nicolas (uses itertools to simplify further  sage.server.interact.list_of_first_n)",
    "created_at": "2009-11-06T13:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62202",
    "user": "nthiery"
}
```

Attachment

Updated patch after review by Nicolas (uses itertools to simplify further  sage.server.interact.list_of_first_n)



---

archive/issue_comments_062203.json:
```json
{
    "body": "William: this makes a small edit to sage.server.notebook.interact.list_of_first_n\n\nYou may want to check/backport to the notebook code",
    "created_at": "2009-11-06T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62203",
    "user": "nthiery"
}
```

William: this makes a small edit to sage.server.notebook.interact.list_of_first_n

You may want to check/backport to the notebook code



---

archive/issue_comments_062204.json:
```json
{
    "body": "Changing keywords from \"iterators\" to \"iterators, itertools\".",
    "created_at": "2009-11-06T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62204",
    "user": "nthiery"
}
```

Changing keywords from "iterators" to "iterators, itertools".



---

archive/issue_comments_062205.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62205",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062206.json:
```json
{
    "body": "The given patch actually breaks somme code... I'm uploading a new one.",
    "created_at": "2009-11-06T21:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62206",
    "user": "hivert"
}
```

The given patch actually breaks somme code... I'm uploading a new one.



---

archive/issue_comments_062207.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-06T21:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62207",
    "user": "hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062208.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-06T21:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62208",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062209.json:
```json
{
    "body": "Attachment\n\nNicolas : can you re-review this patch...\nI commented out some line saying that it was never user and actually is was quite a lot... I don't understand why we didn't caught it by the tests. Anyway, Massena did.\n\nSorry for the mess,\n\nFlorent",
    "created_at": "2009-11-06T21:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62209",
    "user": "hivert"
}
```

Attachment

Nicolas : can you re-review this patch...
I commented out some line saying that it was never user and actually is was quite a lot... I don't understand why we didn't caught it by the tests. Anyway, Massena did.

Sorry for the mess,

Florent



---

archive/issue_comments_062210.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-09T16:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62210",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_062211.json:
```json
{
    "body": "The patch trac_7398_iter_detect-fh.3.patch broke something in graph_generators. \nthe patch trac_7398_combclass_set_compat-fh.patch should fix it. \n\nApply those two patches in that order.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-09T16:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62211",
    "user": "hivert"
}
```

The patch trac_7398_iter_detect-fh.3.patch broke something in graph_generators. 
the patch trac_7398_combclass_set_compat-fh.patch should fix it. 

Apply those two patches in that order.

Cheers,

Florent



---

archive/issue_comments_062212.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T17:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62212",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62213",
    "user": "mhansen"
}
```

Resolution: fixed
