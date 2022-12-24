# Issue 6418: [with patch; needs review] ref manual fixes for 4.1.alpha1

archive/issues_006418.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThis fixes most of the warnings for building the html version of the reference manual in Sage 4.1.alpha1.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6418\n\n",
    "created_at": "2009-06-26T00:28:48Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch; needs review] ref manual fixes for 4.1.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6418",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

This fixes most of the warnings for building the html version of the reference manual in Sage 4.1.alpha1.


Issue created by migration from https://trac.sagemath.org/ticket/6418





---

archive/issue_comments_051540.json:
```json
{
    "body": "Attachment [ref_manual_6418.patch](tarball://root/attachments/some-uuid/ticket6418/ref_manual_6418.patch) by mvngu created at 2009-06-26 00:59:34\n\nI still get about 5 warnings when building the reference manual. That's better than 10 warnings.",
    "created_at": "2009-06-26T00:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51540",
    "user": "mvngu"
}
```

Attachment [ref_manual_6418.patch](tarball://root/attachments/some-uuid/ticket6418/ref_manual_6418.patch) by mvngu created at 2009-06-26 00:59:34

I still get about 5 warnings when building the reference manual. That's better than 10 warnings.



---

archive/issue_comments_051541.json:
```json
{
    "body": "Replying to [comment:1 mvngu]:\n> I still get about 5 warnings when building the reference manual. That's better than 10 warnings.\n\nI only get three warnings: the \"favicon\" message (ticket #5799), and two warnings in sage.misc.misc which I don't know how to fix:\n\n```\nWARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: \"No module named MainClass\", please check your spelling and sys.path\nWARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it reported error: \"No module named MainClass.NestedClass\", please check your spelling and sys.path\n```\n",
    "created_at": "2009-06-26T01:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51541",
    "user": "jhpalmieri"
}
```

Replying to [comment:1 mvngu]:
> I still get about 5 warnings when building the reference manual. That's better than 10 warnings.

I only get three warnings: the "favicon" message (ticket #5799), and two warnings in sage.misc.misc which I don't know how to fix:

```
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: "No module named MainClass", please check your spelling and sys.path
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it reported error: "No module named MainClass.NestedClass", please check your spelling and sys.path
```




---

archive/issue_comments_051542.json:
```json
{
    "body": "See #6419 for a patch to get rid of the sage.misc.misc warnings (rather brutally, but it's the only thing I can figure out).",
    "created_at": "2009-06-26T02:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51542",
    "user": "jhpalmieri"
}
```

See #6419 for a patch to get rid of the sage.misc.misc warnings (rather brutally, but it's the only thing I can figure out).



---

archive/issue_comments_051543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51543",
    "user": "boothby"
}
```

Resolution: fixed
