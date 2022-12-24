# Issue 1879: notebook -- registering redirects to annoying url

archive/issues_001879.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nOn Jan 21, 2008 7:24 AM, Martin Albrecht <> wrote:\n>\n> > I also made it so the notebook doesn't require a funny port, so it should\n> > work fine if you're behind some sort of firewall  that doesn't allow\n> > connections to ports.   Finally, I  reduced the number of security\n> > warnings.\n>\n> I am behind such a funny firewall and it doesn't work for me. I don't have an\n> account on this particular NB server yet and registering times out because it\n> redirects to http:sage.math.washington.edu:8101/register. This is where the\n> firewall won't let me connect.\n\nThat's annoying.  I wonder why that happens.  In any case, if you register you\nonly get sent to 8101 *after* you register -- your registration should still go\nthrough fine.  You can then login by manually going to sagenb.org (or going\nback with the browser back button).\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1879\n\n",
    "created_at": "2008-01-21T18:36:29Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "notebook -- registering redirects to annoying url",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1879",
    "user": "@williamstein"
}
```
Assignee: boothby


```
On Jan 21, 2008 7:24 AM, Martin Albrecht <> wrote:
>
> > I also made it so the notebook doesn't require a funny port, so it should
> > work fine if you're behind some sort of firewall  that doesn't allow
> > connections to ports.   Finally, I  reduced the number of security
> > warnings.
>
> I am behind such a funny firewall and it doesn't work for me. I don't have an
> account on this particular NB server yet and registering times out because it
> redirects to http:sage.math.washington.edu:8101/register. This is where the
> firewall won't let me connect.

That's annoying.  I wonder why that happens.  In any case, if you register you
only get sent to 8101 *after* you register -- your registration should still go
through fine.  You can then login by manually going to sagenb.org (or going
back with the browser back button).

```


Issue created by migration from https://trac.sagemath.org/ticket/1879





---

archive/issue_comments_011892.json:
```json
{
    "body": "Attachment [1879-relativelinks.patch](tarball://root/attachments/some-uuid/ticket1879/1879-relativelinks.patch) by boothby created at 2008-03-16 19:29:30",
    "created_at": "2008-03-16T19:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1879#issuecomment-11892",
    "user": "boothby"
}
```

Attachment [1879-relativelinks.patch](tarball://root/attachments/some-uuid/ticket1879/1879-relativelinks.patch) by boothby created at 2008-03-16 19:29:30



---

archive/issue_comments_011893.json:
```json
{
    "body": "Excellent!\n\nWorks perfectly for me.",
    "created_at": "2008-03-17T04:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1879#issuecomment-11893",
    "user": "@williamstein"
}
```

Excellent!

Works perfectly for me.



---

archive/issue_comments_011894.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-17T04:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1879#issuecomment-11894",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.final



---

archive/issue_comments_011895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-17T04:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1879#issuecomment-11895",
    "user": "mabshoff"
}
```

Resolution: fixed
