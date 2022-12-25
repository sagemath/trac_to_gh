# Issue 5020: auto-cells do not automaticall evaluate (or at least update)

archive/issues_005020.json:
```json
{
    "body": "Assignee: boothby\n\nNotebook cells that start with \"#auto\" do not automatically evaluate on the when a worksheet is opened.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5020\n\n",
    "created_at": "2009-01-19T04:17:47Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "auto-cells do not automaticall evaluate (or at least update)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5020",
    "user": "https://github.com/mwhansen"
}
```
Assignee: boothby

Notebook cells that start with "#auto" do not automatically evaluate on the when a worksheet is opened.

Issue created by migration from https://trac.sagemath.org/ticket/5020





---

archive/issue_comments_038168.json:
```json
{
    "body": "They do on sagenb, which is running sage-3.2.3, but do not seem to on my laptop (also running sage-3.2.3)...?",
    "created_at": "2009-01-19T04:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

They do on sagenb, which is running sage-3.2.3, but do not seem to on my laptop (also running sage-3.2.3)...?



---

archive/issue_comments_038169.json:
```json
{
    "body": "As a clarification, #auto seems totally broken for me on an unpatched sage-3.2.3 (on intel OS X 10.5).  That install does have a lot of optional spkgs and the tinymce spkgs, but Dan Drake reports it working with the tinymce patches+spkgs, so I don't know what's going on.",
    "created_at": "2009-01-19T04:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

As a clarification, #auto seems totally broken for me on an unpatched sage-3.2.3 (on intel OS X 10.5).  That install does have a lot of optional spkgs and the tinymce spkgs, but Dan Drake reports it working with the tinymce patches+spkgs, so I don't know what's going on.



---

archive/issue_comments_038170.json:
```json
{
    "body": "Attachment [trac_5020.patch](tarball://root/attachments/some-uuid/ticket5020/trac_5020.patch) by @mwhansen created at 2009-01-19 05:33:54\n\nI've add a test to the notebook selenium test suite which tests this.",
    "created_at": "2009-01-19T05:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38170",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5020.patch](tarball://root/attachments/some-uuid/ticket5020/trac_5020.patch) by @mwhansen created at 2009-01-19 05:33:54

I've add a test to the notebook selenium test suite which tests this.



---

archive/issue_comments_038171.json:
```json
{
    "body": "I should mention why this fixes things :-)\n\nThe cells are evaluated when .sage() is called, but the HTML send to the web browser was generated before that.",
    "created_at": "2009-01-19T05:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38171",
    "user": "https://github.com/mwhansen"
}
```

I should mention why this fixes things :-)

The cells are evaluated when .sage() is called, but the HTML send to the web browser was generated before that.



---

archive/issue_comments_038172.json:
```json
{
    "body": "Looks good. Positive review.",
    "created_at": "2009-01-19T05:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38172",
    "user": "https://github.com/dandrake"
}
```

Looks good. Positive review.



---

archive/issue_events_005264.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-19T06:09:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5020#event-5264"
}
```



---

archive/issue_comments_038173.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T06:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_038174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T06:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
