# Issue 6963: follow up to #3133: fix ReST formatting

archive/issues_006963.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @jasongrout @kcrisman\n\nThis is a follow up to #3133 to fix some ReST formatting issues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6963\n\n",
    "created_at": "2009-09-19T20:01:53Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "follow up to #3133: fix ReST formatting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6963",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  @jasongrout @kcrisman

This is a follow up to #3133 to fix some ReST formatting issues.

Issue created by migration from https://trac.sagemath.org/ticket/6963





---

archive/issue_comments_057502.json:
```json
{
    "body": "depends on #3133",
    "created_at": "2009-09-19T20:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6963#issuecomment-57502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

depends on #3133



---

archive/issue_comments_057503.json:
```json
{
    "body": "Attachment [trac_6963-rest.patch](tarball://root/attachments/some-uuid/ticket6963/trac_6963-rest.patch) by mvngu created at 2009-09-19 20:06:14",
    "created_at": "2009-09-19T20:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6963#issuecomment-57503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6963-rest.patch](tarball://root/attachments/some-uuid/ticket6963/trac_6963-rest.patch) by mvngu created at 2009-09-19 20:06:14



---

archive/issue_comments_057504.json:
```json
{
    "body": "I didn't apply this, but I think it's probably simple enough that I can give it positive review just by looking at it.\n\nMinh---I would have thought that this was a change small enough that you could have just added this as a \"reviewer\" patch on the original ticket.",
    "created_at": "2009-09-20T05:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6963#issuecomment-57504",
    "user": "https://github.com/jasongrout"
}
```

I didn't apply this, but I think it's probably simple enough that I can give it positive review just by looking at it.

Minh---I would have thought that this was a change small enough that you could have just added this as a "reviewer" patch on the original ticket.



---

archive/issue_comments_057505.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Minh---I would have thought that this was a change small enough that you could have just added this as a \"reviewer\" patch on the original ticket.\nYes and no. \n\n\n\n\n\nWhy \"yes\"? --- The patch is about reviewing ticket #3133.\n\n\n\n\n\nWhy \"no\"? --- I wanted to merge #3133, or any ticket with a positive review, as soon as possible without any unnecessary delay. It was only after merging #3133 that I created this follow up ticket. In cases where a ticket has positive review and is ready to be merged seamlessly, I think it can be a waste of time to upload another reviewer patch and get someone to review that patch. It's better to get stuff in as soon as possible where merging it results in no doctest or hunk failures. And indeed some people would find it a waste of time and unnecessary work if I had uploaded another reviewer patch that addresses a micro-bug. Better off to isolate the micro-bug to another ticket, while first merging the ticket with positive review.",
    "created_at": "2009-09-20T20:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6963#issuecomment-57505",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 jason]:
> Minh---I would have thought that this was a change small enough that you could have just added this as a "reviewer" patch on the original ticket.
Yes and no. 





Why "yes"? --- The patch is about reviewing ticket #3133.





Why "no"? --- I wanted to merge #3133, or any ticket with a positive review, as soon as possible without any unnecessary delay. It was only after merging #3133 that I created this follow up ticket. In cases where a ticket has positive review and is ready to be merged seamlessly, I think it can be a waste of time to upload another reviewer patch and get someone to review that patch. It's better to get stuff in as soon as possible where merging it results in no doctest or hunk failures. And indeed some people would find it a waste of time and unnecessary work if I had uploaded another reviewer patch that addresses a micro-bug. Better off to isolate the micro-bug to another ticket, while first merging the ticket with positive review.



---

archive/issue_events_007186.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T22:07:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6963#event-7186"
}
```



---

archive/issue_comments_057506.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-22T22:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6963#issuecomment-57506",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057507.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6963#issuecomment-57507",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
