# Issue 6418: [with patch, positive review] ref manual fixes for 4.1.alpha1

archive/issues_006418.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThis fixes most of the warnings for building the html version of the reference manual in Sage 4.1.alpha1.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6418\n\n",
    "closed_at": "2009-06-26T17:41:12Z",
    "created_at": "2009-06-26T00:28:48Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, positive review] ref manual fixes for 4.1.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6418",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

This fixes most of the warnings for building the html version of the reference manual in Sage 4.1.alpha1.


Issue created by migration from https://trac.sagemath.org/ticket/6418





---

archive/issue_comments_051443.json:
```json
{
    "body": "Attachment [ref_manual_6418.patch](tarball://root/attachments/some-uuid/ticket6418/ref_manual_6418.patch) by mvngu created at 2009-06-26 00:59:34\n\nI still get about 5 warnings when building the reference manual. That's better than 10 warnings.",
    "created_at": "2009-06-26T00:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [ref_manual_6418.patch](tarball://root/attachments/some-uuid/ticket6418/ref_manual_6418.patch) by mvngu created at 2009-06-26 00:59:34

I still get about 5 warnings when building the reference manual. That's better than 10 warnings.



---

archive/issue_comments_051444.json:
```json
{
    "body": "Replying to [comment:1 mvngu]:\n> I still get about 5 warnings when building the reference manual. That's better than 10 warnings.\n\n\nI only get three warnings: the \"favicon\" message (ticket #5799), and two warnings in sage.misc.misc which I don't know how to fix:\n\n```\nWARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: \"No module named MainClass\", please check your spelling and sys.path\nWARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it reported error: \"No module named MainClass.NestedClass\", please check your spelling and sys.path\n```",
    "created_at": "2009-06-26T01:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51444",
    "user": "https://github.com/jhpalmieri"
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

archive/issue_comments_051445.json:
```json
{
    "body": "See #6419 for a patch to get rid of the sage.misc.misc warnings (rather brutally, but it's the only thing I can figure out).",
    "created_at": "2009-06-26T02:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51445",
    "user": "https://github.com/jhpalmieri"
}
```

See #6419 for a patch to get rid of the sage.misc.misc warnings (rather brutally, but it's the only thing I can figure out).



---

archive/issue_events_015134.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-06-26T17:41:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6418#event-15134"
}
```



---

archive/issue_comments_051446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6418#issuecomment-51446",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed
