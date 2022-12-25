# Issue 2135: [with patch, with positive review] allow for specifying initial position in spring layout

archive/issues_002135.json:
```json
{
    "body": "Assignee: @rlmill\n\nsuggested by Peter Jipsen (does he have a track account yet?)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2135\n\n",
    "closed_at": "2008-02-25T01:38:18Z",
    "created_at": "2008-02-10T01:06:42Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, with positive review] allow for specifying initial position in spring layout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2135",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

suggested by Peter Jipsen (does he have a track account yet?)

Issue created by migration from https://trac.sagemath.org/ticket/2135





---

archive/issue_comments_013973.json:
```json
{
    "body": "Attachment [plot_positions_with_spring-graphs.patch](tarball://root/attachments/some-uuid/ticket2135/plot_positions_with_spring-graphs.patch) by @ncalexan created at 2008-02-15 03:50:25\n\nApply.  There are no doctests, but how would one doctest this?  There is a small typo in the docstring, I think -- a missing apostrophe.",
    "created_at": "2008-02-15T03:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-13973",
    "user": "https://github.com/ncalexan"
}
```

Attachment [plot_positions_with_spring-graphs.patch](tarball://root/attachments/some-uuid/ticket2135/plot_positions_with_spring-graphs.patch) by @ncalexan created at 2008-02-15 03:50:25

Apply.  There are no doctests, but how would one doctest this?  There is a small typo in the docstring, I think -- a missing apostrophe.



---

archive/issue_comments_013974.json:
```json
{
    "body": "Actually, maybe one could test it by giving it a stable initial configuration, and then \"...\"-ing out most of the output.",
    "created_at": "2008-02-19T22:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-13974",
    "user": "https://github.com/rlmill"
}
```

Actually, maybe one could test it by giving it a stable initial configuration, and then "..."-ing out most of the output.



---

archive/issue_comments_013975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T01:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-13975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005108.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-25T01:38:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2135#event-5108"
}
```



---

archive/issue_comments_013976.json:
```json
{
    "body": "Attachment [2135-doctest.patch](tarball://root/attachments/some-uuid/ticket2135/2135-doctest.patch) by mabshoff created at 2008-02-25 01:38:18\n\nMerged both patches in Sage 2.10.3.alpha0. I fixed the missing apostrophe in plot_positions_with_spring-graphs.patch.\n\nCheeers,\n\nMichael",
    "created_at": "2008-02-25T01:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2135#issuecomment-13976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [2135-doctest.patch](tarball://root/attachments/some-uuid/ticket2135/2135-doctest.patch) by mabshoff created at 2008-02-25 01:38:18

Merged both patches in Sage 2.10.3.alpha0. I fixed the missing apostrophe in plot_positions_with_spring-graphs.patch.

Cheeers,

Michael
