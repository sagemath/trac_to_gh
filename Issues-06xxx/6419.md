# Issue 6419: [with patch, positive review] fix ref manual warnings for sage.misc.misc

archive/issues_006419.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @mwhansen\n\nThis patch fixes the warnings\n\n```\nWARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: \n(WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: \n\"No module named MainClass\", please check your spelling and sys.path\nWARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: \n(WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it \nreported error: \"No module named MainClass.NestedClass\", please \ncheck your spelling and sys.path\n```\nproduced by Sphinx when building the html version of the reference manual, by omitting these classes from the documentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6419\n\n",
    "closed_at": "2009-07-04T01:41:48Z",
    "created_at": "2009-06-26T02:14:52Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, positive review] fix ref manual warnings for sage.misc.misc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6419",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @mwhansen

This patch fixes the warnings

```
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: 
(WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: 
"No module named MainClass", please check your spelling and sys.path
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: 
(WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it 
reported error: "No module named MainClass.NestedClass", please 
check your spelling and sys.path
```
produced by Sphinx when building the html version of the reference manual, by omitting these classes from the documentation.

Issue created by migration from https://trac.sagemath.org/ticket/6419





---

archive/issue_comments_051447.json:
```json
{
    "body": "Attachment [misc_ref_6419.patch](tarball://root/attachments/some-uuid/ticket6419/misc_ref_6419.patch) by @loefflerd created at 2009-07-03 09:48:24\n\nLooks good to me. It's a pity that Sphinx can't handle this a bit better, but anyone who needs to know about nested classes is going to be a pretty hardcore Sage hacker who is more than capable of just reading the docs themselves. Positive review.\n\nDavid",
    "created_at": "2009-07-03T09:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6419#issuecomment-51447",
    "user": "https://github.com/loefflerd"
}
```

Attachment [misc_ref_6419.patch](tarball://root/attachments/some-uuid/ticket6419/misc_ref_6419.patch) by @loefflerd created at 2009-07-03 09:48:24

Looks good to me. It's a pity that Sphinx can't handle this a bit better, but anyone who needs to know about nested classes is going to be a pretty hardcore Sage hacker who is more than capable of just reading the docs themselves. Positive review.

David



---

archive/issue_comments_051448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T01:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6419#issuecomment-51448",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_015135.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-04T01:41:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6419",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6419#event-15135"
}
```
