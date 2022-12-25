# Issue 2140: [with bundle, needs review] enhance search_src and add search_def for easier source navigating.

archive/issues_002140.json:
```json
{
    "body": "Assignee: @ncalexan\n\nCC:  ncalexander@gmail.com\n\nKeywords: sage search_src search_def source search grep\n\nThe attached bundle does two things.\n* makes `search_src` accept more extra arguments\n* adds `search_def` to find the definition of a name in the Sage library.\n\nThe ugly patch is the result of a Python 2.6 bug.\n\nThis was all motivated by Craig Citro's post to `sage-devel` at http://groups.google.com/group/sage-devel/msg/82829f101a6e209b.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2140\n\n",
    "created_at": "2008-02-11T07:30:03Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with bundle, needs review] enhance search_src and add search_def for easier source navigating.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2140",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @ncalexan

CC:  ncalexander@gmail.com

Keywords: sage search_src search_def source search grep

The attached bundle does two things.
* makes `search_src` accept more extra arguments
* adds `search_def` to find the definition of a name in the Sage library.

The ugly patch is the result of a Python 2.6 bug.

This was all motivated by Craig Citro's post to `sage-devel` at http://groups.google.com/group/sage-devel/msg/82829f101a6e209b.

Issue created by migration from https://trac.sagemath.org/ticket/2140





---

archive/issue_comments_013999.json:
```json
{
    "body": "Attachment [2140-ncalexan-search-src-def-1.patch](tarball://root/attachments/some-uuid/ticket2140/2140-ncalexan-search-src-def-1.patch) by @ncalexan created at 2008-02-11 07:31:19",
    "created_at": "2008-02-11T07:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2140#issuecomment-13999",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2140-ncalexan-search-src-def-1.patch](tarball://root/attachments/some-uuid/ticket2140/2140-ncalexan-search-src-def-1.patch) by @ncalexan created at 2008-02-11 07:31:19



---

archive/issue_comments_014000.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2008-02-11T07:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2140#issuecomment-14000",
    "user": "https://github.com/craigcitro"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_014001.json:
```json
{
    "body": "I definitely like the patch. Apparently Nick was channeling Tony the Tiger, though, because the \"library\" became \"librrary\" twice. The extra patch fixes that typo in two places.",
    "created_at": "2008-02-11T07:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2140#issuecomment-14001",
    "user": "https://github.com/craigcitro"
}
```

I definitely like the patch. Apparently Nick was channeling Tony the Tiger, though, because the "library" became "librrary" twice. The extra patch fixes that typo in two places.



---

archive/issue_comments_014002.json:
```json
{
    "body": "Attachment [2140-typo.patch](tarball://root/attachments/some-uuid/ticket2140/2140-typo.patch) by @craigcitro created at 2008-02-11 07:57:23",
    "created_at": "2008-02-11T07:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2140#issuecomment-14002",
    "user": "https://github.com/craigcitro"
}
```

Attachment [2140-typo.patch](tarball://root/attachments/some-uuid/ticket2140/2140-typo.patch) by @craigcitro created at 2008-02-11 07:57:23



---

archive/issue_comments_014003.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-13T08:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2140#issuecomment-14003",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_014004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-13T08:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2140#issuecomment-14004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
