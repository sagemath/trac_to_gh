# Issue 9062: Add support for toric lattices

archive/issues_009062.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  vbraun\n\nToric lattices are ZZ<sup>n</sup>'s with distinction of their roles (in the simplest case - standard dual lattices M and N).\n\nOnce this patch is finished, it will be the first part of the toric varieties framework #8986-#8989, but so far I made it actually on top of those modules. Creation of cones and fans seems to work as expected. More work is needed on matrix multiplication. Working on it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9062\n\n",
    "created_at": "2010-05-27T04:45:06Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "title": "Add support for toric lattices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9062",
    "user": "novoselt"
}
```
Assignee: mhampton

CC:  vbraun

Toric lattices are ZZ<sup>n</sup>'s with distinction of their roles (in the simplest case - standard dual lattices M and N).

Once this patch is finished, it will be the first part of the toric varieties framework #8986-#8989, but so far I made it actually on top of those modules. Creation of cones and fans seems to work as expected. More work is needed on matrix multiplication. Working on it!

Issue created by migration from https://trac.sagemath.org/ticket/9062





---

archive/issue_comments_084070.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-27T04:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84070",
    "user": "novoselt"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_084071.json:
```json
{
    "body": "Looks good, I'll be happy to review the final version!",
    "created_at": "2010-05-27T09:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84071",
    "user": "vbraun"
}
```

Looks good, I'll be happy to review the final version!



---

archive/issue_comments_084072.json:
```json
{
    "body": "Attachment [trac_9062_add_support_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_toric_lattices.patch) by novoselt created at 2010-05-27 23:28:10\n\nFixed version.",
    "created_at": "2010-05-27T23:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84072",
    "user": "novoselt"
}
```

Attachment [trac_9062_add_support_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_toric_lattices.patch) by novoselt created at 2010-05-27 23:28:10

Fixed version.



---

archive/issue_comments_084073.json:
```json
{
    "body": "Attachment [trac_9062_add_support_for_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_for_toric_lattices.patch) by novoselt created at 2010-05-28 00:52:16\n\nApply this patch only.",
    "created_at": "2010-05-28T00:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84073",
    "user": "novoselt"
}
```

Attachment [trac_9062_add_support_for_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_for_toric_lattices.patch) by novoselt created at 2010-05-28 00:52:16

Apply this patch only.



---

archive/issue_comments_084074.json:
```json
{
    "body": "It will probably work without other \"prerequisites,\" but I tested it with them applied since all got positive review already and hopefully will be merged soon...",
    "created_at": "2010-05-28T02:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84074",
    "user": "novoselt"
}
```

It will probably work without other "prerequisites," but I tested it with them applied since all got positive review already and hopefully will be merged soon...



---

archive/issue_comments_084075.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-28T02:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84075",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084076.json:
```json
{
    "body": "Functions `is_ToricLattice` and `__hash__` for elements will be added to these new modules in the coming patch for cones at #8986.",
    "created_at": "2010-05-28T17:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84076",
    "user": "novoselt"
}
```

Functions `is_ToricLattice` and `__hash__` for elements will be added to these new modules in the coming patch for cones at #8986.



---

archive/issue_comments_084077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T19:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84077",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084078.json:
```json
{
    "body": "Very nice. I like it how the M/N lattice elements derive from Vector_integer_dense. Positive review. Applies to Sage 4.4.2.",
    "created_at": "2010-06-03T19:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84078",
    "user": "vbraun"
}
```

Very nice. I like it how the M/N lattice elements derive from Vector_integer_dense. Positive review. Applies to Sage 4.4.2.



---

archive/issue_comments_084079.json:
```json
{
    "body": "Thank you! (I think authors and reviewers should be listed with their full names rather than trac accounts, this simplifies the job of release managers.)",
    "created_at": "2010-06-03T20:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84079",
    "user": "novoselt"
}
```

Thank you! (I think authors and reviewers should be listed with their full names rather than trac accounts, this simplifies the job of release managers.)



---

archive/issue_comments_084080.json:
```json
{
    "body": "While testing I found a heisenbug caused by this patch. If you run \"make ptestlong\", there is a failure in toric_lattice_element.pyx; but it works fine if you doctest just that file.\n\nThe problem is this comparison function:\n\n```\n    def __cmp__(self, right):\n        r\"\"\"\n[...]\n            sage: cmp(n, 1)\n            -1\n        \"\"\"\n        c = cmp(type(self), type(right))\n        if c:\n            return c\n```\n\n\nThe doctest is sensitively dependent on the exact memory locations of different classes, because `cmp(type(self), type(right))` compares on memory addresses. I suggest changing the doctest to \n\n```\nsage: n == 1\nFalse\n```\n\nwhich is much more robust.\n\nDavid",
    "created_at": "2010-07-01T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84080",
    "user": "davidloeffler"
}
```

While testing I found a heisenbug caused by this patch. If you run "make ptestlong", there is a failure in toric_lattice_element.pyx; but it works fine if you doctest just that file.

The problem is this comparison function:

```
    def __cmp__(self, right):
        r"""
[...]
            sage: cmp(n, 1)
            -1
        """
        c = cmp(type(self), type(right))
        if c:
            return c
```


The doctest is sensitively dependent on the exact memory locations of different classes, because `cmp(type(self), type(right))` compares on memory addresses. I suggest changing the doctest to 

```
sage: n == 1
False
```

which is much more robust.

David



---

archive/issue_comments_084081.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84081",
    "user": "davidloeffler"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084082.json:
```json
{
    "body": "Apply this patch over trac_9062_add_support_for_toric_lattices.patch",
    "created_at": "2010-07-01T10:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84082",
    "user": "davidloeffler"
}
```

Apply this patch over trac_9062_add_support_for_toric_lattices.patch



---

archive/issue_comments_084083.json:
```json
{
    "body": "Attachment [trac_9062-cmp_fix.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.patch) by davidloeffler created at 2010-07-01 10:09:46\n\nHere's a tiny patch which makes the fix I suggested.",
    "created_at": "2010-07-01T10:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84083",
    "user": "davidloeffler"
}
```

Attachment [trac_9062-cmp_fix.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.patch) by davidloeffler created at 2010-07-01 10:09:46

Here's a tiny patch which makes the fix I suggested.



---

archive/issue_comments_084084.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-01T10:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84084",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084085.json:
```json
{
    "body": "The same potential issue is in `toric_lattice.py`. Here is an updated patch that fixes this one, too. I think this is fine now, if you agree please set to \"positive review\".",
    "created_at": "2010-07-01T10:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84085",
    "user": "vbraun"
}
```

The same potential issue is in `toric_lattice.py`. Here is an updated patch that fixes this one, too. I think this is fine now, if you agree please set to "positive review".



---

archive/issue_comments_084086.json:
```json
{
    "body": "Updated patch",
    "created_at": "2010-07-01T10:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84086",
    "user": "vbraun"
}
```

Updated patch



---

archive/issue_comments_084087.json:
```json
{
    "body": "Attachment [trac_9062-cmp_fix.2.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.2.patch) by davidloeffler created at 2010-07-01 10:30:55\n\nLooks good to me. Apply `trac_9062_add_support_for_toric_lattices.patch` and `trac_9062-cmp_fix.2.patch`.",
    "created_at": "2010-07-01T10:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84087",
    "user": "davidloeffler"
}
```

Attachment [trac_9062-cmp_fix.2.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.2.patch) by davidloeffler created at 2010-07-01 10:30:55

Looks good to me. Apply `trac_9062_add_support_for_toric_lattices.patch` and `trac_9062-cmp_fix.2.patch`.



---

archive/issue_comments_084088.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-01T10:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84088",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084089.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84089",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_084090.json:
```json
{
    "body": "One or more of #8986, #8987, and #9062 *may* cause the doctest failures listed at #9590.",
    "created_at": "2010-07-24T02:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-84090",
    "user": "mpatel"
}
```

One or more of #8986, #8987, and #9062 *may* cause the doctest failures listed at #9590.
