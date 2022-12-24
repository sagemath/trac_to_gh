# Issue 3663: add support for affine crystals

archive/issues_003663.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat bump@match.stanford.edu\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3663\n\n",
    "created_at": "2008-07-16T00:41:55Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "add support for affine crystals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3663",
    "user": "@mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat bump@match.stanford.edu



Issue created by migration from https://trac.sagemath.org/ticket/3663





---

archive/issue_comments_025887.json:
```json
{
    "body": "Changing keywords from \"\" to \"affine crystals\".",
    "created_at": "2009-05-27T21:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25887",
    "user": "@anneschilling"
}
```

Changing keywords from "" to "affine crystals".



---

archive/issue_comments_025888.json:
```json
{
    "body": "Changing assignee from @mwhansen to @anneschilling.",
    "created_at": "2009-05-27T21:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25888",
    "user": "@anneschilling"
}
```

Changing assignee from @mwhansen to @anneschilling.



---

archive/issue_comments_025889.json:
```json
{
    "body": "Attachment [affine-crystal-3663-as.2.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.2.patch) by @anneschilling created at 2009-05-27 21:32:37",
    "created_at": "2009-05-27T21:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25889",
    "user": "@anneschilling"
}
```

Attachment [affine-crystal-3663-as.2.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.2.patch) by @anneschilling created at 2009-05-27 21:32:37



---

archive/issue_comments_025890.json:
```json
{
    "body": "Attachment [affine-crystal-3663-as.3.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.3.patch) by @anneschilling created at 2009-06-05 19:04:42",
    "created_at": "2009-06-05T19:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25890",
    "user": "@anneschilling"
}
```

Attachment [affine-crystal-3663-as.3.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.3.patch) by @anneschilling created at 2009-06-05 19:04:42



---

archive/issue_comments_025891.json:
```json
{
    "body": "Attachment [affine-crystal-3663-as.4.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.4.patch) by @anneschilling created at 2009-06-08 06:48:58",
    "created_at": "2009-06-08T06:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25891",
    "user": "@anneschilling"
}
```

Attachment [affine-crystal-3663-as.4.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.4.patch) by @anneschilling created at 2009-06-08 06:48:58



---

archive/issue_comments_025892.json:
```json
{
    "body": "Attachment [affine-crystal-3663-as.5.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.5.patch) by @anneschilling created at 2009-06-10 18:24:11\n\nimproved documentation links added",
    "created_at": "2009-06-10T18:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25892",
    "user": "@anneschilling"
}
```

Attachment [affine-crystal-3663-as.5.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.5.patch) by @anneschilling created at 2009-06-10 18:24:11

improved documentation links added



---

archive/issue_comments_025893.json:
```json
{
    "body": "Attachment [affine-crystal-3663-as.6.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.6.patch) by @anneschilling created at 2009-07-14 22:48:00\n\ncorrected problems with documentation in crystal_morphism",
    "created_at": "2009-07-14T22:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25893",
    "user": "@anneschilling"
}
```

Attachment [affine-crystal-3663-as.6.patch](tarball://root/attachments/some-uuid/ticket3663/affine-crystal-3663-as.6.patch) by @anneschilling created at 2009-07-14 22:48:00

corrected problems with documentation in crystal_morphism



---

archive/issue_comments_025894.json:
```json
{
    "body": "I am reviewing the version of the patch that is in the combinat queue, running under sage 4.1.1.\n\nI ran `sage -testall`.\nThe patch introduces no new failures. (Where it appears in the queue there are some failures, but the same failures still occur if you qpop the patch, rebuild and run testall again, so they are not caused by this patch.)\n\nAll new methods have docstrings and tests.\n\nKirillov-Reshetikhin crystals for are crystal bases on modules of quantized enveloping algebras of affine Kac-Moody Lie algebras. They had their origin in the observation that it was sometimes possible to define crystal bases on the data parametrizing the eigenstates in the Bethe Ansatz. Beyond that, they tend to be perfect crystals, from which all integrable modules of the quantum group can be constructed. There is one Kirillov-Reshetikhin crystal `B(r,s)` based on tableaux of rectangular shape `s^r` for every positive integer s and index r of the underlying classical crystal.\n\nConstructions of all for the classical untwisted and untwisted types are summarized in Fourier, Schilling and Okado\nhttp://front.math.ucdavis.edu/0811.1604. Most but all of these are implemented in sage by this patch.\n\nThe unimplemented crystals are listed here: http://groups.google.com/group/sage-combinat-devel/msg/9571cf3991bca4db?hl=en\n\nI generated quite a few of these and ran `C.check()` on them. I looked at a few of them more closely. I am confident that the patch is correct. It is also an important advance to have these affine crystals in sage.\n\nSome useful functionality is also added in `crystals.py`. Namely, morphisms of crystals and some root string operations.",
    "created_at": "2009-10-20T01:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25894",
    "user": "@dwbump"
}
```

I am reviewing the version of the patch that is in the combinat queue, running under sage 4.1.1.

I ran `sage -testall`.
The patch introduces no new failures. (Where it appears in the queue there are some failures, but the same failures still occur if you qpop the patch, rebuild and run testall again, so they are not caused by this patch.)

All new methods have docstrings and tests.

Kirillov-Reshetikhin crystals for are crystal bases on modules of quantized enveloping algebras of affine Kac-Moody Lie algebras. They had their origin in the observation that it was sometimes possible to define crystal bases on the data parametrizing the eigenstates in the Bethe Ansatz. Beyond that, they tend to be perfect crystals, from which all integrable modules of the quantum group can be constructed. There is one Kirillov-Reshetikhin crystal `B(r,s)` based on tableaux of rectangular shape `s^r` for every positive integer s and index r of the underlying classical crystal.

Constructions of all for the classical untwisted and untwisted types are summarized in Fourier, Schilling and Okado
http://front.math.ucdavis.edu/0811.1604. Most but all of these are implemented in sage by this patch.

The unimplemented crystals are listed here: http://groups.google.com/group/sage-combinat-devel/msg/9571cf3991bca4db?hl=en

I generated quite a few of these and ran `C.check()` on them. I looked at a few of them more closely. I am confident that the patch is correct. It is also an important advance to have these affine crystals in sage.

Some useful functionality is also added in `crystals.py`. Namely, morphisms of crystals and some root string operations.



---

archive/issue_comments_025895.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T16:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25895",
    "user": "@mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025896.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T16:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25896",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025897.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T17:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3663#issuecomment-25897",
    "user": "@mwhansen"
}
```

Resolution: fixed
