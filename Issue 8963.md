# Issue 8963: Make tableau row_stabilizer return group of perms involving all elements of the tableau

archive/issues_008963.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat-devel@googlegroups.com\n\nThe row_stabilizer method of a tableau ignores elements of the tableau which are alone in their row, and this can cause problems.  For example,\n\n\n```\nsage: t = Tableau([[1,2],[3]])\nsage: rs = t.row_stabilizer()\nsage: PermutationGroupElement([(1,2),(3,)]) in rs\nFalse\nsage: rs.one().list()\n[1, 2]\n```\n\n\nThe expected output is \"True\" and \"[1, 2, 3]\".\n\nI will attach a patch fixing this in a few minutes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8963\n\n",
    "created_at": "2010-05-14T15:32:55Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Make tableau row_stabilizer return group of perms involving all elements of the tableau",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8963",
    "user": "jdc"
}
```
Assignee: sage-combinat

CC:  sage-combinat-devel@googlegroups.com

The row_stabilizer method of a tableau ignores elements of the tableau which are alone in their row, and this can cause problems.  For example,


```
sage: t = Tableau([[1,2],[3]])
sage: rs = t.row_stabilizer()
sage: PermutationGroupElement([(1,2),(3,)]) in rs
False
sage: rs.one().list()
[1, 2]
```


The expected output is "True" and "[1, 2, 3]".

I will attach a patch fixing this in a few minutes.

Issue created by migration from https://trac.sagemath.org/ticket/8963





---

archive/issue_comments_082610.json:
```json
{
    "body": "Attachment [trac_8963_row_stabilizer.patch](tarball://root/attachments/some-uuid/ticket8963/trac_8963_row_stabilizer.patch) by jdc created at 2010-05-14 15:41:34\n\nThe attached patch also adds a method called entries() which returns a list containing the entries of the tableau.  All tests pass and coverage for tableau.py is 100%.  The patch is based on sage-4.4.",
    "created_at": "2010-05-14T15:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8963#issuecomment-82610",
    "user": "jdc"
}
```

Attachment [trac_8963_row_stabilizer.patch](tarball://root/attachments/some-uuid/ticket8963/trac_8963_row_stabilizer.patch) by jdc created at 2010-05-14 15:41:34

The attached patch also adds a method called entries() which returns a list containing the entries of the tableau.  All tests pass and coverage for tableau.py is 100%.  The patch is based on sage-4.4.



---

archive/issue_comments_082611.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T02:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8963#issuecomment-82611",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082612.json:
```json
{
    "body": "Looks good to me.\n\nApplies cleanly to sage-4.4.4.alpha0, all tests pass.",
    "created_at": "2010-06-12T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8963#issuecomment-82612",
    "user": "saliola"
}
```

Looks good to me.

Applies cleanly to sage-4.4.4.alpha0, all tests pass.



---

archive/issue_comments_082613.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-12T17:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8963#issuecomment-82613",
    "user": "saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082614.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8963#issuecomment-82614",
    "user": "mpatel"
}
```

Resolution: fixed
