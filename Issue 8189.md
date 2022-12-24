# Issue 8189: hg.py: fix some docstrings

archive/issues_008189.json:
```json
{
    "body": "Assignee: mvngu\n\nIn hg.py, strings like `ssh://[user`@`]host[:port]/[path]` appear in docstrings, and Sphinx turns them into active links in the html documentation (which are obviously broken), and Sphinx produces warnings when producing the latex/pdf documentation:\n\n```\n.../devel/sage/doc/en/reference/sage/misc/hg.rst:: WARNING: unusable reference target found: ssh://[user@]host[:port]/[path\n```\n\nThis patch puts these links into double backquotes, fixing both of these issues.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8189\n\n",
    "created_at": "2010-02-05T04:54:39Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "hg.py: fix some docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8189",
    "user": "jhpalmieri"
}
```
Assignee: mvngu

In hg.py, strings like `ssh://[user`@`]host[:port]/[path]` appear in docstrings, and Sphinx turns them into active links in the html documentation (which are obviously broken), and Sphinx produces warnings when producing the latex/pdf documentation:

```
.../devel/sage/doc/en/reference/sage/misc/hg.rst:: WARNING: unusable reference target found: ssh://[user@]host[:port]/[path
```

This patch puts these links into double backquotes, fixing both of these issues.


Issue created by migration from https://trac.sagemath.org/ticket/8189





---

archive/issue_comments_072181.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T04:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8189#issuecomment-72181",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072182.json:
```json
{
    "body": "Attachment [trac_8189-hg.patch](tarball://root/attachments/some-uuid/ticket8189/trac_8189-hg.patch) by jhpalmieri created at 2010-02-05 04:55:30",
    "created_at": "2010-02-05T04:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8189#issuecomment-72182",
    "user": "jhpalmieri"
}
```

Attachment [trac_8189-hg.patch](tarball://root/attachments/some-uuid/ticket8189/trac_8189-hg.patch) by jhpalmieri created at 2010-02-05 04:55:30



---

archive/issue_comments_072183.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T06:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8189#issuecomment-72183",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8189#issuecomment-72184",
    "user": "mpatel"
}
```

Resolution: fixed
