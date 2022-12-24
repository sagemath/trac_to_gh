# Issue 6138: SymmetricGroupAlgebra: updates w.r.t. categories and free modules

archive/issues_006138.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: symmetric group, free module\n\nSee: http://combinat.sagemath.org/patches/file/tip/categories-symmetric_group_algebra-6138-nt.patch\n\nDepends on #6136\n\nIssue created by migration from https://trac.sagemath.org/ticket/6138\n\n",
    "created_at": "2009-05-27T05:38:44Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "SymmetricGroupAlgebra: updates w.r.t. categories and free modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6138",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: symmetric group, free module

See: http://combinat.sagemath.org/patches/file/tip/categories-symmetric_group_algebra-6138-nt.patch

Depends on #6136

Issue created by migration from https://trac.sagemath.org/ticket/6138





---

archive/issue_comments_049014.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-16T11:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49014",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049015.json:
```json
{
    "body": "Attachment [categories-symmetric_group_algebra-6138-nt.patch](tarball://root/attachments/some-uuid/ticket6138/categories-symmetric_group_algebra-6138-nt.patch) by hivert created at 2009-10-16 11:10:33",
    "created_at": "2009-10-16T11:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49015",
    "user": "hivert"
}
```

Attachment [categories-symmetric_group_algebra-6138-nt.patch](tarball://root/attachments/some-uuid/ticket6138/categories-symmetric_group_algebra-6138-nt.patch) by hivert created at 2009-10-16 11:10:33



---

archive/issue_comments_049016.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T11:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49016",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049017.json:
```json
{
    "body": "For this, isn't it possible to lazily add the coercion using coerce_map_from?",
    "created_at": "2009-10-31T16:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49017",
    "user": "mhansen"
}
```

For this, isn't it possible to lazily add the coercion using coerce_map_from?



---

archive/issue_comments_049018.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> For this, isn't it possible to lazily add the coercion using coerce_map_from?\n\nProbably so. It would be best handled by some \"templated coercion declarations\", as I had started to implement in MuPAD. Let's just leave it as is for the moment, until we have enough use cases to come up with the right design.",
    "created_at": "2009-11-01T12:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49018",
    "user": "nthiery"
}
```

Replying to [comment:3 mhansen]:
> For this, isn't it possible to lazily add the coercion using coerce_map_from?

Probably so. It would be best handled by some "templated coercion declarations", as I had started to implement in MuPAD. Let's just leave it as is for the moment, until we have enough use cases to come up with the right design.



---

archive/issue_comments_049019.json:
```json
{
    "body": "Updated patch fixes two missing doctests (apply only this one)",
    "created_at": "2009-11-06T14:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49019",
    "user": "nthiery"
}
```

Updated patch fixes two missing doctests (apply only this one)



---

archive/issue_comments_049020.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49020",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049021.json:
```json
{
    "body": "Attachment [trac_6138-categories-symmetric_group_algebra-6138-nt.patch](tarball://root/attachments/some-uuid/ticket6138/trac_6138-categories-symmetric_group_algebra-6138-nt.patch) by mhansen created at 2009-11-19 17:00:03",
    "created_at": "2009-11-19T17:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6138#issuecomment-49021",
    "user": "mhansen"
}
```

Attachment [trac_6138-categories-symmetric_group_algebra-6138-nt.patch](tarball://root/attachments/some-uuid/ticket6138/trac_6138-categories-symmetric_group_algebra-6138-nt.patch) by mhansen created at 2009-11-19 17:00:03
