# Issue 7208: Refactorisation of families

archive/issues_007208.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: Family, enumerated set\n\nLog of the attached patch:\n\n- Families are parents, in the (Finite/Infinite)EnumeratedSets category\n- New class EnumeratedFamily; Family accept any (Finite)EnumeratedSet as input\n- Improves the output of lazy families, and update accordingly the\n  doctests in CombinatorialFreeModule, ...\n- Clean trailing whitespaces\n- Use TestSuite\n\nIssue created by migration from https://trac.sagemath.org/ticket/7208\n\n",
    "created_at": "2009-10-14T12:44:35Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Refactorisation of families",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7208",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

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

archive/issue_comments_059705.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-14T12:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59705",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-14T12:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59706",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059707.json:
```json
{
    "body": "We should use the occasion to fix this bug:\n\n\tsage: f = Family([\"c\", \"a\", \"b\"], lambda x: x+x)\n\tsage: list(f)\n\t['aa', 'cc', 'bb']",
    "created_at": "2009-10-16T14:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59707",
    "user": "https://github.com/nthiery"
}
```

We should use the occasion to fix this bug:

	sage: f = Family(["c", "a", "b"], lambda x: x+x)
	sage: list(f)
	['aa', 'cc', 'bb']



---

archive/issue_comments_059708.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-10-16T14:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59708",
    "user": "https://github.com/nthiery"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059709.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-16T14:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59709",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059710.json:
```json
{
    "body": "The updated patch is supposed to fix it. Florent: please review!",
    "created_at": "2009-10-16T14:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59710",
    "user": "https://github.com/nthiery"
}
```

The updated patch is supposed to fix it. Florent: please review!



---

archive/issue_comments_059711.json:
```json
{
    "body": "Attachment [trac_7208_family_enumset.patch](tarball://root/attachments/some-uuid/ticket7208/trac_7208_family_enumset.patch) by @nthiery created at 2009-10-16 15:01:00",
    "created_at": "2009-10-16T15:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59711",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7208_family_enumset.patch](tarball://root/attachments/some-uuid/ticket7208/trac_7208_family_enumset.patch) by @nthiery created at 2009-10-16 15:01:00



---

archive/issue_comments_059712.json:
```json
{
    "body": "Fixed missing doctests",
    "created_at": "2009-10-16T15:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59712",
    "user": "https://github.com/nthiery"
}
```

Fixed missing doctests



---

archive/issue_comments_059713.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59713",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059714.json:
```json
{
    "body": "Things are *now* ok :-) Positive review.\n\nFlorent",
    "created_at": "2009-10-16T15:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59714",
    "user": "https://github.com/hivert"
}
```

Things are *now* ok :-) Positive review.

Florent



---

archive/issue_comments_059715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T16:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7208#issuecomment-59715",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
