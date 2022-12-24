# Issue 6917: [with patch] Minkowsky sum sould work with polyhedra and not only with polytopes

archive/issues_006917.json:
```json
{
    "body": "Assignee: mhampton\n\nThe attached patch makes Minkowsky sum handle unbounded polyhedra.\n\nHowever, as a side effect, it makes bug #6915 blatant, thus doctests don't pass anymore.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6917\n\n",
    "created_at": "2009-09-10T12:48:39Z",
    "labels": [
        "geometry",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "[with patch] Minkowsky sum sould work with polyhedra and not only with polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6917",
    "user": "sbarthelemy"
}
```
Assignee: mhampton

The attached patch makes Minkowsky sum handle unbounded polyhedra.

However, as a side effect, it makes bug #6915 blatant, thus doctests don't pass anymore.

Issue created by migration from https://trac.sagemath.org/ticket/6917





---

archive/issue_comments_057114.json:
```json
{
    "body": "Attachment [mink_sum.patch](tarball://root/attachments/some-uuid/ticket6917/mink_sum.patch) by sbarthelemy created at 2009-09-10 12:49:17",
    "created_at": "2009-09-10T12:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6917#issuecomment-57114",
    "user": "sbarthelemy"
}
```

Attachment [mink_sum.patch](tarball://root/attachments/some-uuid/ticket6917/mink_sum.patch) by sbarthelemy created at 2009-09-10 12:49:17



---

archive/issue_comments_057115.json:
```json
{
    "body": "Is this ready for review? If so, please change the summary to \"[with patch, needs review]\".",
    "created_at": "2009-09-10T18:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6917#issuecomment-57115",
    "user": "mvngu"
}
```

Is this ready for review? If so, please change the summary to "[with patch, needs review]".



---

archive/issue_comments_057116.json:
```json
{
    "body": "I believe this patch is unnecessary because of #7109, which fixed a lot of related problems.",
    "created_at": "2010-04-03T14:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6917#issuecomment-57116",
    "user": "mhampton"
}
```

I believe this patch is unnecessary because of #7109, which fixed a lot of related problems.



---

archive/issue_comments_057117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-03T14:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6917#issuecomment-57117",
    "user": "mhampton"
}
```

Resolution: fixed
