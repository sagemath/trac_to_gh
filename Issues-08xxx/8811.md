# Issue 8811: Translation for elements of a root lattice and related features and fixes

archive/issues_008811.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: root systems, affine weyl groups, translations\n\nThis patch implements translation for elements of a root lattice and related features and fixes::\n\n- New method `translation` for elements of a root lattice\n\n- New methods `reduced_word_of_alcove_morphism`, `dynkin_diagram_automorphism_of_alcove_morphism`, `reduced_word_of_translation`, `_test_reduced_word_of_translation`\n\n- Added extensive TESTS to compare with Kashiwara's private notes\n\n- Fixed dynkin diagram for type BC\n\n- Fixed CartanType.translation_factors to implement its specification correctly in affine type BC. Imported the full test suite from MuPAD-Combinat. Also fixes and tests for proper typing of the coefficients (ZZ/QQ).\n\n- Bug fix in WeylGroup: the matrices were defined over QQ instead of the base ring of the underlying root lattice realization.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8811\n\n",
    "closed_at": "2010-06-05T22:27:23Z",
    "created_at": "2010-04-28T22:57:34Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Translation for elements of a root lattice and related features and fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8811",
    "user": "https://github.com/anneschilling"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: root systems, affine weyl groups, translations

This patch implements translation for elements of a root lattice and related features and fixes::

- New method `translation` for elements of a root lattice

- New methods `reduced_word_of_alcove_morphism`, `dynkin_diagram_automorphism_of_alcove_morphism`, `reduced_word_of_translation`, `_test_reduced_word_of_translation`

- Added extensive TESTS to compare with Kashiwara's private notes

- Fixed dynkin diagram for type BC

- Fixed CartanType.translation_factors to implement its specification correctly in affine type BC. Imported the full test suite from MuPAD-Combinat. Also fixes and tests for proper typing of the coefficients (ZZ/QQ).

- Bug fix in WeylGroup: the matrices were defined over QQ instead of the base ring of the underlying root lattice realization.


Issue created by migration from https://trac.sagemath.org/ticket/8811





---

archive/issue_events_021494.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2010-05-21T15:11:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8811#event-21494"
}
```



---

archive/issue_comments_080755.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-21T15:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80755",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_080756.json:
```json
{
    "body": "Changing keywords from \"\" to \"root systems, affine weyl groups, translations\".",
    "created_at": "2010-05-21T15:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80756",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "root systems, affine weyl groups, translations".



---

archive/issue_comments_080757.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-02T11:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80757",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080758.json:
```json
{
    "body": "Attachment [trac_8811_reduced_word_of_translations-nt.patch](tarball://root/attachments/some-uuid/ticket8811/trac_8811_reduced_word_of_translations-nt.patch) by @nthiery created at 2010-06-02 20:04:38",
    "created_at": "2010-06-02T20:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80758",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8811_reduced_word_of_translations-nt.patch](tarball://root/attachments/some-uuid/ticket8811/trac_8811_reduced_word_of_translations-nt.patch) by @nthiery created at 2010-06-02 20:04:38



---

archive/issue_comments_080759.json:
```json
{
    "body": "I carefully checked the results of translation_factor, adding extra tests to compare with Kashiwara's private notes. Nicolas and I discussed at length the correct factors for type BC (see the corresponding doc in the code).\n\nAll tests passed on massena and all tests in combinat/root_systems passed on my machine.\n\nPositive review.",
    "created_at": "2010-06-02T21:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80759",
    "user": "https://github.com/anneschilling"
}
```

I carefully checked the results of translation_factor, adding extra tests to compare with Kashiwara's private notes. Nicolas and I discussed at length the correct factors for type BC (see the corresponding doc in the code).

All tests passed on massena and all tests in combinat/root_systems passed on my machine.

Positive review.



---

archive/issue_comments_080760.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-02T21:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80760",
    "user": "https://github.com/anneschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8811#issuecomment-80761",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021495.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:27:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8811",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8811#event-21495"
}
```
