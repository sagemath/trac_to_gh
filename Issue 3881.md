# Issue 3881: [with patch, needs review] Quiet three MPolynomialRing deprecation warnings

archive/issues_003881.json:
```json
{
    "body": "Assignee: mabshoff\n\nCurrently we have:\n\n```\nsage -t -long devel/sage/sage/rings/fraction_field_element.py\n/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_fraction_field_element.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!\n  # -*- coding: utf-8 -*-\n\n\nsage -t -long devel/sage/sage/modules/free_quadratic_module.py\n/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_free_quadratic_module.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!\n  # -*- coding: utf-8 -*-\n/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_free_quadratic_module.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!\n  # -*- coding: utf-8 -*-\n```\n\nThe attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3881\n\n",
    "created_at": "2008-08-16T21:20:17Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] Quiet three MPolynomialRing deprecation warnings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3881",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Currently we have:

```
sage -t -long devel/sage/sage/rings/fraction_field_element.py
/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_fraction_field_element.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  # -*- coding: utf-8 -*-


sage -t -long devel/sage/sage/modules/free_quadratic_module.py
/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_free_quadratic_module.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  # -*- coding: utf-8 -*-
/scratch/mabshoff/release-cycle/sage-3.1.rc0/tmp/.doctest_free_quadratic_module.py:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  # -*- coding: utf-8 -*-
```

The attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3881





---

archive/issue_comments_027688.json:
```json
{
    "body": "Attachment [trac_3881.patch](tarball://root/attachments/some-uuid/ticket3881/trac_3881.patch) by mabshoff created at 2008-08-16 21:23:31",
    "created_at": "2008-08-16T21:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3881#issuecomment-27688",
    "user": "mabshoff"
}
```

Attachment [trac_3881.patch](tarball://root/attachments/some-uuid/ticket3881/trac_3881.patch) by mabshoff created at 2008-08-16 21:23:31



---

archive/issue_comments_027689.json:
```json
{
    "body": "Merged in Sage 3.1.final",
    "created_at": "2008-08-16T21:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3881#issuecomment-27689",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.final



---

archive/issue_comments_027690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-16T21:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3881#issuecomment-27690",
    "user": "mabshoff"
}
```

Resolution: fixed
