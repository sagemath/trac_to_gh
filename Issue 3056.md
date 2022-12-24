# Issue 3056: bug with polynomials over power series

archive/issues_003056.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  burcin\n\nThe first computation of z^2 is incorrect, whereas the second is correct:\n\n```\nsage: C.<t> = PowerSeriesRing(ZZ)\nsage: D.<s> = PolynomialRing(C)\nsage: z = (1 + O(t)) + t*s^2\nsage: z^2\n t^2*s^4 + 1 + O(t)\nsage: z._mul_generic(z)\n t^2*s^4 + (2*t + O(t^2))*s^2 + 1 + O(t)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3056\n\n",
    "created_at": "2008-04-29T21:04:34Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "bug with polynomials over power series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3056",
    "user": "kedlaya"
}
```
Assignee: mabshoff

CC:  burcin

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

archive/issue_comments_021097.json:
```json
{
    "body": "Changing assignee from mabshoff to dmharvey.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21097",
    "user": "kedlaya"
}
```

Changing assignee from mabshoff to dmharvey.



---

archive/issue_comments_021098.json:
```json
{
    "body": "Changing keywords from \"\" to \"polynomials, power series, Karatsuba\".",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21098",
    "user": "kedlaya"
}
```

Changing keywords from "" to "polynomials, power series, Karatsuba".



---

archive/issue_comments_021099.json:
```json
{
    "body": "Changing component from Cygwin to basic arithmetic.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21099",
    "user": "kedlaya"
}
```

Changing component from Cygwin to basic arithmetic.



---

archive/issue_comments_021100.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21100",
    "user": "kedlaya"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_021101.json:
```json
{
    "body": "A bit of experimentation by David Harvey suggests that _mul_karatsuba is at fault.",
    "created_at": "2008-04-29T21:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21101",
    "user": "kedlaya"
}
```

A bit of experimentation by David Harvey suggests that _mul_karatsuba is at fault.



---

archive/issue_comments_021102.json:
```json
{
    "body": "Changing assignee from dmharvey to roed.",
    "created_at": "2008-04-29T21:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21102",
    "user": "kedlaya"
}
```

Changing assignee from dmharvey to roed.



---

archive/issue_comments_021103.json:
```json
{
    "body": "In my previous example:\n\n```\nsage: (z^2).list()\n [1 + O(t), O(t^1), O(t^1), 0, t^2]\n```\n\nso the output is not actually incorrect, just less precise than it should be. So maybe we should not use Karatsuba for polynomials over an inexact ring? (We already don't for polynomials over a p-adic ring.)",
    "created_at": "2008-04-29T21:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21103",
    "user": "kedlaya"
}
```

In my previous example:

```
sage: (z^2).list()
 [1 + O(t), O(t^1), O(t^1), 0, t^2]
```

so the output is not actually incorrect, just less precise than it should be. So maybe we should not use Karatsuba for polynomials over an inexact ring? (We already don't for polynomials over a p-adic ring.)



---

archive/issue_comments_021104.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2008-04-30T13:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21104",
    "user": "dmharvey"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_021105.json:
```json
{
    "body": "Given that this is a printing problem rather than an incorrect output problem, I'm removing the blocker tag.",
    "created_at": "2008-04-30T13:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21105",
    "user": "dmharvey"
}
```

Given that this is a printing problem rather than an incorrect output problem, I'm removing the blocker tag.



---

archive/issue_comments_021106.json:
```json
{
    "body": "Attachment [3056_kill_karat.patch](tarball://root/attachments/some-uuid/ticket3056/3056_kill_karat.patch) by boothby created at 2009-01-22 07:58:42",
    "created_at": "2009-01-22T07:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21106",
    "user": "boothby"
}
```

Attachment [3056_kill_karat.patch](tarball://root/attachments/some-uuid/ticket3056/3056_kill_karat.patch) by boothby created at 2009-01-22 07:58:42



---

archive/issue_comments_021107.json:
```json
{
    "body": "Attachment [3056-doctest.patch](tarball://root/attachments/some-uuid/ticket3056/3056-doctest.patch) by boothby created at 2009-01-22 09:27:31\n\nChanges doctests to reflect classical multiplication used instead of karatsuba.  Note that in every case (with possible exception of the test in padics/pow_computer_ext.pyx), the result is better (higher precision when inexact; simpler form when exact).  In the case of padics/pow_computer_ext.pyx, it is unclear that the original was correct to any reasonable precision.  David Roe seemed to think that this was ok.\n\nAlso, I added the test that presented this problem to the doctests of polynomial_element.__mul__",
    "created_at": "2009-01-22T09:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21107",
    "user": "boothby"
}
```

Attachment [3056-doctest.patch](tarball://root/attachments/some-uuid/ticket3056/3056-doctest.patch) by boothby created at 2009-01-22 09:27:31

Changes doctests to reflect classical multiplication used instead of karatsuba.  Note that in every case (with possible exception of the test in padics/pow_computer_ext.pyx), the result is better (higher precision when inexact; simpler form when exact).  In the case of padics/pow_computer_ext.pyx, it is unclear that the original was correct to any reasonable precision.  David Roe seemed to think that this was ok.

Also, I added the test that presented this problem to the doctests of polynomial_element.__mul__



---

archive/issue_comments_021108.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-24T12:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21108",
    "user": "craigcitro"
}
```

Looks good.



---

archive/issue_comments_021109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21109",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021110.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T18:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3056",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3056#issuecomment-21110",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2
