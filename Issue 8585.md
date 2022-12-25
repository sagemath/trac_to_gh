# Issue 8585: PermutationGroup and SymmetricGroup on the empty set

archive/issues_008585.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat nborie\n\nKeywords: Empty Set, PermutationGroup\n\nSage can't properly work with SymmetricGroup(0) or PermutationsGroup on the\nempty set.\n\n```\nsage: SymmetricGroup(0)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n[...]\nValueError: min() arg is an empty sequence\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8585\n\n",
    "created_at": "2010-03-23T09:01:45Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "PermutationGroup and SymmetricGroup on the empty set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8585",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat nborie

Keywords: Empty Set, PermutationGroup

Sage can't properly work with SymmetricGroup(0) or PermutationsGroup on the
empty set.

```
sage: SymmetricGroup(0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
[...]
ValueError: min() arg is an empty sequence
```



Issue created by migration from https://trac.sagemath.org/ticket/8585





---

archive/issue_comments_077623.json:
```json
{
    "body": "Should be ready for review.",
    "created_at": "2010-03-23T09:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77623",
    "user": "https://github.com/hivert"
}
```

Should be ready for review.



---

archive/issue_comments_077624.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T09:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77624",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077625.json:
```json
{
    "body": "A comment by e-mail from Nicolas Borie:\n\n> 1. Est-ce qu'on change ce comportement ?\n\nTrans: Should we change this behavior\n\n```\n> sage: SymmetricGroup(-12)\n> Symmetric group of order 0! as a permutation group\n```\n\n\n> 2. Ce serait bien de changer ce message d'erreur :\n\nTrans: This error message is wrong:\n\n```\n> sage: SymmetricGroup('bla')\n>[...]\n> ValueError: n (=bla) must be an integer >= 1 or a list (but n has type\n> <type 'str'>)\n```\n\n\n> --> n must be an integer >= 0 now !!!",
    "created_at": "2010-03-31T10:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77625",
    "user": "https://github.com/hivert"
}
```

A comment by e-mail from Nicolas Borie:

> 1. Est-ce qu'on change ce comportement ?

Trans: Should we change this behavior

```
> sage: SymmetricGroup(-12)
> Symmetric group of order 0! as a permutation group
```


> 2. Ce serait bien de changer ce message d'erreur :

Trans: This error message is wrong:

```
> sage: SymmetricGroup('bla')
>[...]
> ValueError: n (=bla) must be an integer >= 1 or a list (but n has type
> <type 'str'>)
```


> --> n must be an integer >= 0 now !!!



---

archive/issue_comments_077626.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-16T09:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77626",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077627.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-16T10:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77627",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077628.json:
```json
{
    "body": "Attachment [trac_8585-permutation_group_on_empty_set-fh.patch](tarball://root/attachments/some-uuid/ticket8585/trac_8585-permutation_group_on_empty_set-fh.patch) by @hivert created at 2010-04-16 10:20:09\n\nReplying to [comment:4 nborie]:\nOups ! I forgot to reupload the patch after sending my e-mail... Sorry.",
    "created_at": "2010-04-16T10:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77628",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8585-permutation_group_on_empty_set-fh.patch](tarball://root/attachments/some-uuid/ticket8585/trac_8585-permutation_group_on_empty_set-fh.patch) by @hivert created at 2010-04-16 10:20:09

Replying to [comment:4 nborie]:
Oups ! I forgot to reupload the patch after sending my e-mail... Sorry.



---

archive/issue_comments_077629.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-16T11:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77629",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077630.json:
```json
{
    "body": "The patch apply, all tests passed, good behavior with the user. And step by step, the TestSuite design give a nice coherence of \"mathematical tests\" in the sage code... Perfect from me.\n\nI give this patch a positive review.",
    "created_at": "2010-04-16T11:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77630",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

The patch apply, all tests passed, good behavior with the user. And step by step, the TestSuite design give a nice coherence of "mathematical tests" in the sage code... Perfect from me.

I give this patch a positive review.



---

archive/issue_comments_077631.json:
```json
{
    "body": "Merged \"trac_8585-permutation_group_on_empty_set-fh.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77631",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8585-permutation_group_on_empty_set-fh.patch" into 4.4.alpha1.



---

archive/issue_events_020735.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-19T05:14:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8585#event-20735"
}
```



---

archive/issue_comments_077632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8585#issuecomment-77632",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
