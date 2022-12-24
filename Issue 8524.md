# Issue 8524: DisjointUnionEnumeratedSets should have a private __classcall__ method

archive/issues_008524.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: DisjointUnionEnumeratedSets, inheritance\n\nIn order to be easily inherited from, `DisjointUnionEnumeratedSets` should have a private `__classcall__` method. Indeed most of the time, when inheriting from it, the family used in the union will be constructed in the `__init__` method of the subclass. Having `__classcall__` inherited force the user to have its own `__classcall__`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8524\n\n",
    "created_at": "2010-03-13T14:53:53Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "DisjointUnionEnumeratedSets should have a private __classcall__ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8524",
    "user": "hivert"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: DisjointUnionEnumeratedSets, inheritance

In order to be easily inherited from, `DisjointUnionEnumeratedSets` should have a private `__classcall__` method. Indeed most of the time, when inheriting from it, the family used in the union will be constructed in the `__init__` method of the subclass. Having `__classcall__` inherited force the user to have its own `__classcall__`.

Issue created by migration from https://trac.sagemath.org/ticket/8524





---

archive/issue_comments_077037.json:
```json
{
    "body": "Changing assignee from sage-combinat to hivert.",
    "created_at": "2010-03-13T16:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77037",
    "user": "hivert"
}
```

Changing assignee from sage-combinat to hivert.



---

archive/issue_comments_077038.json:
```json
{
    "body": "The patch should be ready for review. I've one question: There is a very long doc in the class but nothing in the `__init__` nor in the file itself. Any idea about what is best here ?\n\nFlorent",
    "created_at": "2010-03-13T16:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77038",
    "user": "hivert"
}
```

The patch should be ready for review. I've one question: There is a very long doc in the class but nothing in the `__init__` nor in the file itself. Any idea about what is best here ?

Florent



---

archive/issue_comments_077039.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-13T16:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77039",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077040.json:
```json
{
    "body": "Rebased against 4.3.4",
    "created_at": "2010-03-20T09:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77040",
    "user": "hivert"
}
```

Rebased against 4.3.4



---

archive/issue_comments_077041.json:
```json
{
    "body": "Attachment [trac_8524-disjoint_union_classcall_private-fh.patch](tarball://root/attachments/some-uuid/ticket8524/trac_8524-disjoint_union_classcall_private-fh.patch) by hivert created at 2010-03-20 09:47:25\n\nI just rebased this patch against 4.3.4. \nNicolas: Please don't forget reviewing it. It is needed by #8519 which is close to be positive reviewed.",
    "created_at": "2010-03-20T09:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77041",
    "user": "hivert"
}
```

Attachment [trac_8524-disjoint_union_classcall_private-fh.patch](tarball://root/attachments/some-uuid/ticket8524/trac_8524-disjoint_union_classcall_private-fh.patch) by hivert created at 2010-03-20 09:47:25

I just rebased this patch against 4.3.4. 
Nicolas: Please don't forget reviewing it. It is needed by #8519 which is close to be positive reviewed.



---

archive/issue_comments_077042.json:
```json
{
    "body": "Attachment [trac_8524-disjoint_union_classcall_private-fh.2.patch](tarball://root/attachments/some-uuid/ticket8524/trac_8524-disjoint_union_classcall_private-fh.2.patch) by nthiery created at 2010-04-16 21:18:58\n\nReplaces the previous ones",
    "created_at": "2010-04-16T21:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77042",
    "user": "nthiery"
}
```

Attachment [trac_8524-disjoint_union_classcall_private-fh.2.patch](tarball://root/attachments/some-uuid/ticket8524/trac_8524-disjoint_union_classcall_private-fh.2.patch) by nthiery created at 2010-04-16 21:18:58

Replaces the previous ones



---

archive/issue_comments_077043.json:
```json
{
    "body": "Positive review (finally!)\n\nFlorent: I made a couple little changes in place (mostly doc). Please re-proofread, and set the positive review status.",
    "created_at": "2010-04-16T21:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77043",
    "user": "nthiery"
}
```

Positive review (finally!)

Florent: I made a couple little changes in place (mostly doc). Please re-proofread, and set the positive review status.



---

archive/issue_comments_077044.json:
```json
{
    "body": "Your change are ok with me. Thanks for the review.",
    "created_at": "2010-04-16T23:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77044",
    "user": "hivert"
}
```

Your change are ok with me. Thanks for the review.



---

archive/issue_comments_077045.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-16T23:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77045",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077046.json:
```json
{
    "body": "Merged \"trac_8524-disjoint_union_classcall_private-fh.2.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77046",
    "user": "jhpalmieri"
}
```

Merged "trac_8524-disjoint_union_classcall_private-fh.2.patch" into 4.4.alpha1.



---

archive/issue_comments_077047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8524#issuecomment-77047",
    "user": "jhpalmieri"
}
```

Resolution: fixed
