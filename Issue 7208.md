# Issue 7208: Refactorisation of families

archive/issues_007208.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: Family, enumerated set\n\nLog of the attached patch:\n\n- Families are parents, in the (Finite/Infinite)EnumeratedSets category\n- New class EnumeratedFamily; Family accept any (Finite)EnumeratedSet as input\n- Improves the output of lazy families, and update accordingly the\n  doctests in CombinatorialFreeModule, ...\n- Clean trailing whitespaces\n- Use TestSuite\n\nIssue created by migration from https://trac.sagemath.org/ticket/7208\n\n",
    "created_at": "2009-10-14T12:44:35Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Refactorisation of families",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7208",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: Family, enumerated set

Log of the attached patch:

- Families are parents, in the (Finite/Infinite)EnumeratedSets category
- New class EnumeratedFamily; Family accept any (Finite)EnumeratedSet as input
- Improves the output of lazy families, and update accordingly the
  doctests in CombinatorialFreeModule, ...
- Clean trailing whitespaces
- Use TestSuite

Issue created by migration from https://trac.sagemath.org/ticket/7208





---

archive/issue_comments_059817.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-14T12:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59817",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059818.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-14T12:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59818",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059819.json:
```json
{
    "body": "We should use the occasion to fix this bug:\n\n\tsage: f = Family([\"c\", \"a\", \"b\"], lambda x: x+x)\n\tsage: list(f)\n\t['aa', 'cc', 'bb']",
    "created_at": "2009-10-16T14:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59819",
    "user": "nthiery"
}
```

We should use the occasion to fix this bug:

	sage: f = Family(["c", "a", "b"], lambda x: x+x)
	sage: list(f)
	['aa', 'cc', 'bb']



---

archive/issue_comments_059820.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-10-16T14:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59820",
    "user": "nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059821.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-16T14:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59821",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059822.json:
```json
{
    "body": "The updated patch is supposed to fix it. Florent: please review!",
    "created_at": "2009-10-16T14:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59822",
    "user": "nthiery"
}
```

The updated patch is supposed to fix it. Florent: please review!



---

archive/issue_comments_059823.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-16T15:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59823",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_059824.json:
```json
{
    "body": "Fixed missing doctests",
    "created_at": "2009-10-16T15:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59824",
    "user": "nthiery"
}
```

Fixed missing doctests



---

archive/issue_comments_059825.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59825",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059826.json:
```json
{
    "body": "Things are *now* ok :-) Positive review.\n\nFlorent",
    "created_at": "2009-10-16T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59826",
    "user": "hivert"
}
```

Things are *now* ok :-) Positive review.

Florent



---

archive/issue_comments_059827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T16:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59827",
    "user": "mhansen"
}
```

Resolution: fixed
