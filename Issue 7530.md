# Issue 7530: corrects simple Laurent-polynomial bug

archive/issues_007530.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: Laurent Polynomial\n\nIt is not possible to form a polynomial ring over a Laurent polynomial ring.  This is because the function `is_integral_domain` for Laurent polynomial rings lacks the optional parameter `proof=True` (unlike every other instance of `is_integral_domain`).  The patch corrects this omission, which solves the problem.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7530\n\n",
    "created_at": "2009-11-25T13:14:29Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "corrects simple Laurent-polynomial bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7530",
    "user": "fwclarke"
}
```
Assignee: @aghitza

Keywords: Laurent Polynomial

It is not possible to form a polynomial ring over a Laurent polynomial ring.  This is because the function `is_integral_domain` for Laurent polynomial rings lacks the optional parameter `proof=True` (unlike every other instance of `is_integral_domain`).  The patch corrects this omission, which solves the problem.


Issue created by migration from https://trac.sagemath.org/ticket/7530





---

archive/issue_comments_063828.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-25T13:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63828",
    "user": "fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063829.json:
```json
{
    "body": "Attachment [trac_7530.patch](tarball://root/attachments/some-uuid/ticket7530/trac_7530.patch) by fwclarke created at 2009-11-25 13:16:14",
    "created_at": "2009-11-25T13:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63829",
    "user": "fwclarke"
}
```

Attachment [trac_7530.patch](tarball://root/attachments/some-uuid/ticket7530/trac_7530.patch) by fwclarke created at 2009-11-25 13:16:14



---

archive/issue_comments_063830.json:
```json
{
    "body": "Patch applies to 4.3.rc0, but:\n\n1. The function does not use the new parameter!\n2. No examples or doctests are given.\n\nso -- needs work!",
    "created_at": "2009-12-17T18:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63830",
    "user": "@JohnCremona"
}
```

Patch applies to 4.3.rc0, but:

1. The function does not use the new parameter!
2. No examples or doctests are given.

so -- needs work!



---

archive/issue_comments_063831.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-17T18:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63831",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063832.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-18T09:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63832",
    "user": "fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063833.json:
```json
{
    "body": "Thanks, John.  \n\nYou're right; the `proof` parameter needs to be passed on to the base ring, which I've done in a replacement patch.  I've included an example verifying that the problem I had with constructing a polynomial ring over a Laurent polynomial ring is solved by the patch.\n\nAs it happens, the Laurent polynomial constructor currently restricts the base ring to be an integral domain.  Of course this isn't (mathematically) necessary, but the current code for taking negative powers of Laurent polynomial generators uses the fraction field of the base ring (producing some bizarre errors in the process).  I'll raise another ticket about this issue.",
    "created_at": "2009-12-18T09:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63833",
    "user": "fwclarke"
}
```

Thanks, John.  

You're right; the `proof` parameter needs to be passed on to the base ring, which I've done in a replacement patch.  I've included an example verifying that the problem I had with constructing a polynomial ring over a Laurent polynomial ring is solved by the patch.

As it happens, the Laurent polynomial constructor currently restricts the base ring to be an integral domain.  Of course this isn't (mathematically) necessary, but the current code for taking negative powers of Laurent polynomial generators uses the fraction field of the base ring (producing some bizarre errors in the process).  I'll raise another ticket about this issue.



---

archive/issue_comments_063834.json:
```json
{
    "body": "Attachment [trac_7530_replacement.patch](tarball://root/attachments/some-uuid/ticket7530/trac_7530_replacement.patch) by fwclarke created at 2009-12-18 09:14:31\n\nreplaces previous patch",
    "created_at": "2009-12-18T09:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63834",
    "user": "fwclarke"
}
```

Attachment [trac_7530_replacement.patch](tarball://root/attachments/some-uuid/ticket7530/trac_7530_replacement.patch) by fwclarke created at 2009-12-18 09:14:31

replaces previous patch



---

archive/issue_comments_063835.json:
```json
{
    "body": "This looks better!  Second patch applies to 4.3.rc0, and tests pass.",
    "created_at": "2009-12-18T15:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63835",
    "user": "@JohnCremona"
}
```

This looks better!  Second patch applies to 4.3.rc0, and tests pass.



---

archive/issue_comments_063836.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-18T15:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63836",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063837.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T21:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7530#issuecomment-63837",
    "user": "@mwhansen"
}
```

Resolution: fixed
