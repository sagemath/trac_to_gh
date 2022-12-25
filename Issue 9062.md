# Issue 9062: Add support for toric lattices

archive/issues_009062.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @vbraun\n\nToric lattices are ZZ<sup>n</sup>'s with distinction of their roles (in the simplest case - standard dual lattices M and N).\n\nOnce this patch is finished, it will be the first part of the toric varieties framework #8986-#8989, but so far I made it actually on top of those modules. Creation of cones and fans seems to work as expected. More work is needed on matrix multiplication. Working on it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9062\n\n",
    "created_at": "2010-05-27T04:45:06Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Add support for toric lattices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9062",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

CC:  @vbraun

Toric lattices are ZZ<sup>n</sup>'s with distinction of their roles (in the simplest case - standard dual lattices M and N).

Once this patch is finished, it will be the first part of the toric varieties framework #8986-#8989, but so far I made it actually on top of those modules. Creation of cones and fans seems to work as expected. More work is needed on matrix multiplication. Working on it!

Issue created by migration from https://trac.sagemath.org/ticket/9062





---

archive/issue_comments_083934.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-27T04:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83934",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_083935.json:
```json
{
    "body": "Looks good, I'll be happy to review the final version!",
    "created_at": "2010-05-27T09:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83935",
    "user": "https://github.com/vbraun"
}
```

Looks good, I'll be happy to review the final version!



---

archive/issue_comments_083936.json:
```json
{
    "body": "Attachment [trac_9062_add_support_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_toric_lattices.patch) by @novoselt created at 2010-05-27 23:28:10\n\nFixed version.",
    "created_at": "2010-05-27T23:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83936",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9062_add_support_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_toric_lattices.patch) by @novoselt created at 2010-05-27 23:28:10

Fixed version.



---

archive/issue_comments_083937.json:
```json
{
    "body": "Attachment [trac_9062_add_support_for_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_for_toric_lattices.patch) by @novoselt created at 2010-05-28 00:52:16\n\nApply this patch only.",
    "created_at": "2010-05-28T00:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83937",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9062_add_support_for_toric_lattices.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062_add_support_for_toric_lattices.patch) by @novoselt created at 2010-05-28 00:52:16

Apply this patch only.



---

archive/issue_comments_083938.json:
```json
{
    "body": "It will probably work without other \"prerequisites,\" but I tested it with them applied since all got positive review already and hopefully will be merged soon...",
    "created_at": "2010-05-28T02:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83938",
    "user": "https://github.com/novoselt"
}
```

It will probably work without other "prerequisites," but I tested it with them applied since all got positive review already and hopefully will be merged soon...



---

archive/issue_comments_083939.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-28T02:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83939",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083940.json:
```json
{
    "body": "Functions `is_ToricLattice` and `__hash__` for elements will be added to these new modules in the coming patch for cones at #8986.",
    "created_at": "2010-05-28T17:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83940",
    "user": "https://github.com/novoselt"
}
```

Functions `is_ToricLattice` and `__hash__` for elements will be added to these new modules in the coming patch for cones at #8986.



---

archive/issue_comments_083941.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T19:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83941",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083942.json:
```json
{
    "body": "Very nice. I like it how the M/N lattice elements derive from Vector_integer_dense. Positive review. Applies to Sage 4.4.2.",
    "created_at": "2010-06-03T19:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83942",
    "user": "https://github.com/vbraun"
}
```

Very nice. I like it how the M/N lattice elements derive from Vector_integer_dense. Positive review. Applies to Sage 4.4.2.



---

archive/issue_comments_083943.json:
```json
{
    "body": "Thank you! (I think authors and reviewers should be listed with their full names rather than trac accounts, this simplifies the job of release managers.)",
    "created_at": "2010-06-03T20:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83943",
    "user": "https://github.com/novoselt"
}
```

Thank you! (I think authors and reviewers should be listed with their full names rather than trac accounts, this simplifies the job of release managers.)



---

archive/issue_comments_083944.json:
```json
{
    "body": "While testing I found a heisenbug caused by this patch. If you run \"make ptestlong\", there is a failure in toric_lattice_element.pyx; but it works fine if you doctest just that file.\n\nThe problem is this comparison function:\n\n```\n    def __cmp__(self, right):\n        r\"\"\"\n[...]\n            sage: cmp(n, 1)\n            -1\n        \"\"\"\n        c = cmp(type(self), type(right))\n        if c:\n            return c\n```\n\n\nThe doctest is sensitively dependent on the exact memory locations of different classes, because `cmp(type(self), type(right))` compares on memory addresses. I suggest changing the doctest to \n\n```\nsage: n == 1\nFalse\n```\n\nwhich is much more robust.\n\nDavid",
    "created_at": "2010-07-01T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83944",
    "user": "https://github.com/loefflerd"
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

archive/issue_comments_083945.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-01T09:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83945",
    "user": "https://github.com/loefflerd"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083946.json:
```json
{
    "body": "Apply this patch over trac_9062_add_support_for_toric_lattices.patch",
    "created_at": "2010-07-01T10:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83946",
    "user": "https://github.com/loefflerd"
}
```

Apply this patch over trac_9062_add_support_for_toric_lattices.patch



---

archive/issue_comments_083947.json:
```json
{
    "body": "Attachment [trac_9062-cmp_fix.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.patch) by @loefflerd created at 2010-07-01 10:09:46\n\nHere's a tiny patch which makes the fix I suggested.",
    "created_at": "2010-07-01T10:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83947",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9062-cmp_fix.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.patch) by @loefflerd created at 2010-07-01 10:09:46

Here's a tiny patch which makes the fix I suggested.



---

archive/issue_comments_083948.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-01T10:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83948",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083949.json:
```json
{
    "body": "The same potential issue is in `toric_lattice.py`. Here is an updated patch that fixes this one, too. I think this is fine now, if you agree please set to \"positive review\".",
    "created_at": "2010-07-01T10:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83949",
    "user": "https://github.com/vbraun"
}
```

The same potential issue is in `toric_lattice.py`. Here is an updated patch that fixes this one, too. I think this is fine now, if you agree please set to "positive review".



---

archive/issue_comments_083950.json:
```json
{
    "body": "Updated patch",
    "created_at": "2010-07-01T10:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83950",
    "user": "https://github.com/vbraun"
}
```

Updated patch



---

archive/issue_comments_083951.json:
```json
{
    "body": "Attachment [trac_9062-cmp_fix.2.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.2.patch) by @loefflerd created at 2010-07-01 10:30:55\n\nLooks good to me. Apply `trac_9062_add_support_for_toric_lattices.patch` and `trac_9062-cmp_fix.2.patch`.",
    "created_at": "2010-07-01T10:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83951",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9062-cmp_fix.2.patch](tarball://root/attachments/some-uuid/ticket9062/trac_9062-cmp_fix.2.patch) by @loefflerd created at 2010-07-01 10:30:55

Looks good to me. Apply `trac_9062_add_support_for_toric_lattices.patch` and `trac_9062-cmp_fix.2.patch`.



---

archive/issue_comments_083952.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-01T10:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83952",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083953.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83953",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_083954.json:
```json
{
    "body": "One or more of #8986, #8987, and #9062 *may* cause the doctest failures listed at #9590.",
    "created_at": "2010-07-24T02:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9062#issuecomment-83954",
    "user": "https://github.com/qed777"
}
```

One or more of #8986, #8987, and #9062 *may* cause the doctest failures listed at #9590.
