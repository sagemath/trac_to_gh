# Issue 3056: bug with polynomials over power series

archive/issues_003056.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @burcin\n\nThe first computation of z^2 is incorrect, whereas the second is correct:\n\n```\nsage: C.<t> = PowerSeriesRing(ZZ)\nsage: D.<s> = PolynomialRing(C)\nsage: z = (1 + O(t)) + t*s^2\nsage: z^2\n t^2*s^4 + 1 + O(t)\nsage: z._mul_generic(z)\n t^2*s^4 + (2*t + O(t^2))*s^2 + 1 + O(t)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3056\n\n",
    "created_at": "2008-04-29T21:04:34Z",
    "labels": [
        "component: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bug with polynomials over power series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3056",
    "user": "https://github.com/kedlaya"
}
```
Assignee: mabshoff

CC:  @burcin

The first computation of z^2 is incorrect, whereas the second is correct:

```
sage: C.<t> = PowerSeriesRing(ZZ)
sage: D.<s> = PolynomialRing(C)
sage: z = (1 + O(t)) + t*s^2
sage: z^2
 t^2*s^4 + 1 + O(t)
sage: z._mul_generic(z)
 t^2*s^4 + (2*t + O(t^2))*s^2 + 1 + O(t)
```


Issue created by migration from https://trac.sagemath.org/ticket/3056





---

archive/issue_comments_021054.json:
```json
{
    "body": "Changing assignee from mabshoff to dmharvey.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21054",
    "user": "https://github.com/kedlaya"
}
```

Changing assignee from mabshoff to dmharvey.



---

archive/issue_comments_021055.json:
```json
{
    "body": "Changing keywords from \"\" to \"polynomials, power series, Karatsuba\".",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21055",
    "user": "https://github.com/kedlaya"
}
```

Changing keywords from "" to "polynomials, power series, Karatsuba".



---

archive/issue_comments_021056.json:
```json
{
    "body": "Changing component from Cygwin to basic arithmetic.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21056",
    "user": "https://github.com/kedlaya"
}
```

Changing component from Cygwin to basic arithmetic.



---

archive/issue_comments_021057.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21057",
    "user": "https://github.com/kedlaya"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_021058.json:
```json
{
    "body": "A bit of experimentation by David Harvey suggests that _mul_karatsuba is at fault.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21058",
    "user": "https://github.com/kedlaya"
}
```

A bit of experimentation by David Harvey suggests that _mul_karatsuba is at fault.



---

archive/issue_comments_021059.json:
```json
{
    "body": "Changing assignee from dmharvey to @roed314.",
    "created_at": "2008-04-29T21:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21059",
    "user": "https://github.com/kedlaya"
}
```

Changing assignee from dmharvey to @roed314.



---

archive/issue_comments_021060.json:
```json
{
    "body": "In my previous example:\n\n```\nsage: (z^2).list()\n [1 + O(t), O(t^1), O(t^1), 0, t^2]\n```\n\nso the output is not actually incorrect, just less precise than it should be. So maybe we should not use Karatsuba for polynomials over an inexact ring? (We already don't for polynomials over a p-adic ring.)",
    "created_at": "2008-04-29T21:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21060",
    "user": "https://github.com/kedlaya"
}
```

In my previous example:

```
sage: (z^2).list()
 [1 + O(t), O(t^1), O(t^1), 0, t^2]
```

so the output is not actually incorrect, just less precise than it should be. So maybe we should not use Karatsuba for polynomials over an inexact ring? (We already don't for polynomials over a p-adic ring.)



---

archive/issue_comments_021061.json:
```json
{
    "body": "Given that this is a printing problem rather than an incorrect output problem, I'm removing the blocker tag.",
    "created_at": "2008-04-30T13:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21061",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Given that this is a printing problem rather than an incorrect output problem, I'm removing the blocker tag.



---

archive/issue_comments_021062.json:
```json
{
    "body": "Attachment [3056_kill_karat.patch](tarball://root/attachments/some-uuid/ticket3056/3056_kill_karat.patch) by boothby created at 2009-01-22 07:58:42",
    "created_at": "2009-01-22T07:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21062",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3056_kill_karat.patch](tarball://root/attachments/some-uuid/ticket3056/3056_kill_karat.patch) by boothby created at 2009-01-22 07:58:42



---

archive/issue_comments_021063.json:
```json
{
    "body": "Attachment [3056-doctest.patch](tarball://root/attachments/some-uuid/ticket3056/3056-doctest.patch) by boothby created at 2009-01-22 09:27:31\n\nChanges doctests to reflect classical multiplication used instead of karatsuba.  Note that in every case (with possible exception of the test in padics/pow_computer_ext.pyx), the result is better (higher precision when inexact; simpler form when exact).  In the case of padics/pow_computer_ext.pyx, it is unclear that the original was correct to any reasonable precision.  David Roe seemed to think that this was ok.\n\nAlso, I added the test that presented this problem to the doctests of polynomial_element.__mul__",
    "created_at": "2009-01-22T09:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21063",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3056-doctest.patch](tarball://root/attachments/some-uuid/ticket3056/3056-doctest.patch) by boothby created at 2009-01-22 09:27:31

Changes doctests to reflect classical multiplication used instead of karatsuba.  Note that in every case (with possible exception of the test in padics/pow_computer_ext.pyx), the result is better (higher precision when inexact; simpler form when exact).  In the case of padics/pow_computer_ext.pyx, it is unclear that the original was correct to any reasonable precision.  David Roe seemed to think that this was ok.

Also, I added the test that presented this problem to the doctests of polynomial_element.__mul__



---

archive/issue_comments_021064.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-24T12:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21064",
    "user": "https://github.com/craigcitro"
}
```

Looks good.



---

archive/issue_comments_021065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021066.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T18:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2
