# Issue 6507: [with patch, needs review] doc sidebar toggle

archive/issues_006507.json:
```json
{
    "body": "Assignee: tba\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725/4807f5553bdbd6b0#4807f5553bdbd6b0) for an early version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6507\n\n",
    "created_at": "2009-07-10T11:05:10Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] doc sidebar toggle",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6507",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725/4807f5553bdbd6b0#4807f5553bdbd6b0) for an early version.

Issue created by migration from https://trac.sagemath.org/ticket/6507





---

archive/issue_comments_052922.json:
```json
{
    "body": "Attachment [trac_6507_sidebar_toggle.patch](tarball://root/attachments/some-uuid/ticket6507/trac_6507_sidebar_toggle.patch) by @qed777 created at 2009-07-10 11:21:47\n\nThe new toggle highlights itself on mouse-over, runs the length of the content, auto-resizes itself, uses cookies, and should work in the live, static, and offline documentation in most browsers.  This includes Firefox, Opera, and the Qt WebKit demo browser on Linux.  Chromium, it seems, does not yet let offline pages set cookies, but more polish is on order.",
    "created_at": "2009-07-10T11:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52922",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6507_sidebar_toggle.patch](tarball://root/attachments/some-uuid/ticket6507/trac_6507_sidebar_toggle.patch) by @qed777 created at 2009-07-10 11:21:47

The new toggle highlights itself on mouse-over, runs the length of the content, auto-resizes itself, uses cookies, and should work in the live, static, and offline documentation in most browsers.  This includes Firefox, Opera, and the Qt WebKit demo browser on Linux.  Chromium, it seems, does not yet let offline pages set cookies, but more polish is on order.



---

archive/issue_comments_052923.json:
```json
{
    "body": "I applied the patch on r12658 (Sage 4.1). There do not appear to be any differences in the UI.",
    "created_at": "2009-07-27T09:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52923",
    "user": "https://github.com/TimDumol"
}
```

I applied the patch on r12658 (Sage 4.1). There do not appear to be any differences in the UI.



---

archive/issue_comments_052924.json:
```json
{
    "body": "Can you be more specific, e.g., about the browser and OS?  Did you rebuild the HTML documentation?\n\nI should add that I don't have access to a machine running Mac OS.  It would be useful to know how it fares in multiple Mac OS browsers in all three scenarios (live, fast static, offline).\n\nBut first, we should try to get it working on some machine other than mine.\n\n(In applying the patch, I got this warning:\n\n```\nHunk #1 succeeded at 9 with fuzz 1 (offset -1 lines).\n```\n\nThis is just a consequence of #6512.)",
    "created_at": "2009-07-27T09:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52924",
    "user": "https://github.com/qed777"
}
```

Can you be more specific, e.g., about the browser and OS?  Did you rebuild the HTML documentation?

I should add that I don't have access to a machine running Mac OS.  It would be useful to know how it fares in multiple Mac OS browsers in all three scenarios (live, fast static, offline).

But first, we should try to get it working on some machine other than mine.

(In applying the patch, I got this warning:

```
Hunk #1 succeeded at 9 with fuzz 1 (offset -1 lines).
```

This is just a consequence of #6512.)



---

archive/issue_comments_052925.json:
```json
{
    "body": "Apart from the \"fuzz\" mentioned above, the patch still appears to work for me.  I'm changing the summary to WPNR, but please let me know...",
    "created_at": "2009-09-02T10:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52925",
    "user": "https://github.com/qed777"
}
```

Apart from the "fuzz" mentioned above, the patch still appears to work for me.  I'm changing the summary to WPNR, but please let me know...



---

archive/issue_comments_052926.json:
```json
{
    "body": "Works as advertised after a doc rebuild. Positive review.",
    "created_at": "2009-09-22T15:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52926",
    "user": "https://github.com/TimDumol"
}
```

Works as advertised after a doc rebuild. Positive review.



---

archive/issue_comments_052927.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T02:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52927",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_052928.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6507#issuecomment-52928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
