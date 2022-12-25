# Issue 8673: No KeyErrror raised when it should for FiniteWord_callable

archive/issues_008673.json:
```json
{
    "body": "Assignee: @seblabbe\n\nCC:  abmasse\n\n\n```\nLe 10-02-23, Paul Zimmermann a \u00e9crit :\n\nsage: def f(n):\n   return n^2\n\nsage: w = Word(f,length=23)\n\nsage: w[24]\n576\n\nPaul\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8673\n\n",
    "created_at": "2010-04-11T14:00:57Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "No KeyErrror raised when it should for FiniteWord_callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8673",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

CC:  abmasse


```
Le 10-02-23, Paul Zimmermann a écrit :

sage: def f(n):
   return n^2

sage: w = Word(f,length=23)

sage: w[24]
576

Paul
```


Issue created by migration from https://trac.sagemath.org/ticket/8673





---

archive/issue_comments_078798.json:
```json
{
    "body": "Attachment [trac_8673_out_of_range_index-sl.patch](tarball://root/attachments/some-uuid/ticket8673/trac_8673_out_of_range_index-sl.patch) by @seblabbe created at 2011-02-18 19:57:43",
    "created_at": "2011-02-18T19:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78798",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8673_out_of_range_index-sl.patch](tarball://root/attachments/some-uuid/ticket8673/trac_8673_out_of_range_index-sl.patch) by @seblabbe created at 2011-02-18 19:57:43



---

archive/issue_comments_078799.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-18T19:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78799",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078800.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-18T20:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78800",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078801.json:
```json
{
    "body": "Pretty straight-forward. All tests pass! Positive review.",
    "created_at": "2011-02-18T20:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78801",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Pretty straight-forward. All tests pass! Positive review.



---

archive/issue_comments_078802.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-25T12:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78802",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
