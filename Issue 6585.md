# Issue 6585: [with patch, needs review] trivial change to a few docstrings in partition.py

archive/issues_006585.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nCC:  sage-combinat\n\nThis patch changes a few docstrings in partition.py which contain backslashes from\n\n```\n\"\"\"\nblah\n\"\"\"\n```\n\nto\n\n```\nr\"\"\"\nblah\n\"\"\"\n```\n\n(I've been playing with version 0.6.2 of Sphinx, and it barfs without making this change.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6585\n\n",
    "created_at": "2009-07-22T05:04:28Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] trivial change to a few docstrings in partition.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6585",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

CC:  sage-combinat

This patch changes a few docstrings in partition.py which contain backslashes from

```
"""
blah
"""
```

to

```
r"""
blah
"""
```

(I've been playing with version 0.6.2 of Sphinx, and it barfs without making this change.)


Issue created by migration from https://trac.sagemath.org/ticket/6585





---

archive/issue_comments_053802.json:
```json
{
    "body": "Attachment [trac_6585-backslash.patch](tarball://root/attachments/some-uuid/ticket6585/trac_6585-backslash.patch) by jhpalmieri created at 2009-07-22 05:04:57",
    "created_at": "2009-07-22T05:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6585#issuecomment-53802",
    "user": "jhpalmieri"
}
```

Attachment [trac_6585-backslash.patch](tarball://root/attachments/some-uuid/ticket6585/trac_6585-backslash.patch) by jhpalmieri created at 2009-07-22 05:04:57



---

archive/issue_comments_053803.json:
```json
{
    "body": "Attachment [trac_6585-fix-warnings.patch](tarball://root/attachments/some-uuid/ticket6585/trac_6585-fix-warnings.patch) by mvngu created at 2009-07-24 08:17:35\n\nfix warning when building HTML version of sage/combinat/partition.py",
    "created_at": "2009-07-24T08:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6585#issuecomment-53803",
    "user": "mvngu"
}
```

Attachment [trac_6585-fix-warnings.patch](tarball://root/attachments/some-uuid/ticket6585/trac_6585-fix-warnings.patch) by mvngu created at 2009-07-24 08:17:35

fix warning when building HTML version of sage/combinat/partition.py



---

archive/issue_comments_053804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T08:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6585#issuecomment-53804",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053805.json:
```json
{
    "body": "Positive review for the patch `trac_6585-backslash.patch`. After importing the changes in that patch and rebuilding the HTML version of the reference manual, I got the following warning:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/combinat/partition.py:docstring of sage.combinat.partition.Partition_class.conjugate:1: (WARNING/2) Inline literal start-string without end-string.\n```\n\nThis is fixed by `trac_6585-fix-warnings.patch`. Merged both patches.",
    "created_at": "2009-07-24T08:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6585#issuecomment-53805",
    "user": "mvngu"
}
```

Positive review for the patch `trac_6585-backslash.patch`. After importing the changes in that patch and rebuilding the HTML version of the reference manual, I got the following warning:

```
WARNING: /scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/combinat/partition.py:docstring of sage.combinat.partition.Partition_class.conjugate:1: (WARNING/2) Inline literal start-string without end-string.
```

This is fixed by `trac_6585-fix-warnings.patch`. Merged both patches.
