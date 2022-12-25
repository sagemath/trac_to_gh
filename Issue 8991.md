# Issue 8991: Adjust developer walkthrough for two changes to mercurial queues syntax

archive/issues_008991.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  alubovsky\n\n\n```\nhg qinit\nhg -f qnew\n```\n\n\nare deprecated in newer versions of Mercurial (1.5) which some may be using (ie not using the version distributed with Sage).  This patch includes text to transition to the new state of the syntax without abandoning the old.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8991\n\n",
    "created_at": "2010-05-19T00:09:26Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Adjust developer walkthrough for two changes to mercurial queues syntax",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8991",
    "user": "https://github.com/rbeezer"
}
```
Assignee: mvngu

CC:  alubovsky


```
hg qinit
hg -f qnew
```


are deprecated in newer versions of Mercurial (1.5) which some may be using (ie not using the version distributed with Sage).  This patch includes text to transition to the new state of the syntax without abandoning the old.

Issue created by migration from https://trac.sagemath.org/ticket/8991





---

archive/issue_comments_082981.json:
```json
{
    "body": "Attachment [trac_8991-mq-syntax-for-developers.patch](tarball://root/attachments/some-uuid/ticket8991/trac_8991-mq-syntax-for-developers.patch) by alubovsky created at 2010-05-19 01:33:17",
    "created_at": "2010-05-19T01:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82981",
    "user": "https://trac.sagemath.org/admin/accounts/users/alubovsky"
}
```

Attachment [trac_8991-mq-syntax-for-developers.patch](tarball://root/attachments/some-uuid/ticket8991/trac_8991-mq-syntax-for-developers.patch) by alubovsky created at 2010-05-19 01:33:17



---

archive/issue_comments_082982.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-19T01:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82982",
    "user": "https://trac.sagemath.org/admin/accounts/users/alubovsky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082983.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-19T01:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82983",
    "user": "https://trac.sagemath.org/admin/accounts/users/alubovsky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082984.json:
```json
{
    "body": "alubovsky -\n\nThanks for the quick review.  Probably best to give the release manager (who makes the final decision about adding this into \"official\" Sage) some idea of what testing you did.  Such as something about building the developers manual without warnings, output looks fine, mq changes are accurately reported, etc.\n\nAlso, please put your real name into the \"Reviewer\" field and you'll get credit in the release tour and the Trac reports.  ;-)\n\ncc me when you submit that patch of typos you are collecting!\n\nRob",
    "created_at": "2010-05-19T04:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82984",
    "user": "https://github.com/rbeezer"
}
```

alubovsky -

Thanks for the quick review.  Probably best to give the release manager (who makes the final decision about adding this into "official" Sage) some idea of what testing you did.  Such as something about building the developers manual without warnings, output looks fine, mq changes are accurately reported, etc.

Also, please put your real name into the "Reviewer" field and you'll get credit in the release tour and the Trac reports.  ;-)

cc me when you submit that patch of typos you are collecting!

Rob



---

archive/issue_comments_082985.json:
```json
{
    "body": "Patch output looks fine, no warnings building with\nsage -docbuild developer html\n\npatch applied just fine, (not sure what mq changes are accurately reported means.)",
    "created_at": "2010-05-19T04:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82985",
    "user": "https://trac.sagemath.org/admin/accounts/users/alubovsky"
}
```

Patch output looks fine, no warnings building with
sage -docbuild developer html

patch applied just fine, (not sure what mq changes are accurately reported means.)



---

archive/issue_comments_082986.json:
```json
{
    "body": "I should add, i applied the patch to the latest version of sage-combinat repository, instead of sage-main, hopefully it makes no difference.",
    "created_at": "2010-05-19T04:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82986",
    "user": "https://trac.sagemath.org/admin/accounts/users/alubovsky"
}
```

I should add, i applied the patch to the latest version of sage-combinat repository, instead of sage-main, hopefully it makes no difference.



---

archive/issue_comments_082987.json:
```json
{
    "body": "Replying to [comment:4 alubovsky]:\n> (not sure what mq changes are accurately reported means.)\n\nI was just suggesting you might note the *content* of the changes was correct.  I don't have Mercurial 1.5 installed anywhere, so was working off documantation I could find online (which wsn't always helpful).\n\nIn this case, I think the sage-combinat repo is probably OK.",
    "created_at": "2010-05-19T05:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82987",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:4 alubovsky]:
> (not sure what mq changes are accurately reported means.)

I was just suggesting you might note the *content* of the changes was correct.  I don't have Mercurial 1.5 installed anywhere, so was working off documantation I could find online (which wsn't always helpful).

In this case, I think the sage-combinat repo is probably OK.



---

archive/issue_comments_082988.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-19T07:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8991#issuecomment-82988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
