# Issue 9323: Remove devel/sage/doc/en/faq/Makefile

archive/issues_009323.json:
```json
{
    "body": "Assignee: mvngu\n\nWhy?  'cause Mike Hansen says so.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9323\n\n",
    "created_at": "2010-06-24T03:43:49Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Remove devel/sage/doc/en/faq/Makefile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9323",
    "user": "https://github.com/williamstein"
}
```
Assignee: mvngu

Why?  'cause Mike Hansen says so.

Issue created by migration from https://trac.sagemath.org/ticket/9323





---

archive/issue_comments_087784.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-24T16:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087785.json:
```json
{
    "body": "It is removed in Sage 4.4.4:\n\n```\n[mvngu@sage faq]$ pwd\n/dev/shm/mvngu/sandbox/sage-4.4.4/devel/sage-main/doc/en/faq\n[mvngu@sage faq]$ hg st\n! doc/en/faq/Makefile\n```\n\nThis has not effect on building the HTML or PDF versions of the FAQ. Both of these versions build fine. The release manager can close this ticket as fixed.",
    "created_at": "2010-06-24T16:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

It is removed in Sage 4.4.4:

```
[mvngu@sage faq]$ pwd
/dev/shm/mvngu/sandbox/sage-4.4.4/devel/sage-main/doc/en/faq
[mvngu@sage faq]$ hg st
! doc/en/faq/Makefile
```

This has not effect on building the HTML or PDF versions of the FAQ. Both of these versions build fine. The release manager can close this ticket as fixed.



---

archive/issue_comments_087786.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T16:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87786",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087787.json:
```json
{
    "body": "It appears that someone has already removed the FAQ `Makefile`.",
    "created_at": "2010-07-21T03:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87787",
    "user": "https://github.com/qed777"
}
```

It appears that someone has already removed the FAQ `Makefile`.



---

archive/issue_comments_087788.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T03:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87788",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009479.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T03:22:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9323#event-9479"
}
```



---

archive/issue_comments_087789.json:
```json
{
    "body": "Just to check:  Should we keep `doc/en/tutorial/Makefile`?",
    "created_at": "2010-07-21T03:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87789",
    "user": "https://github.com/qed777"
}
```

Just to check:  Should we keep `doc/en/tutorial/Makefile`?



---

archive/issue_comments_087790.json:
```json
{
    "body": "Minh, should I select a different resolution and/or milestone?",
    "created_at": "2010-07-21T03:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87790",
    "user": "https://github.com/qed777"
}
```

Minh, should I select a different resolution and/or milestone?



---

archive/issue_comments_087791.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Minh, should I select a different resolution and/or milestone?\n\nThe file `doc/en/faq/Makefile` was removed from revision control in Sage 4.5.alpha1:\n\n```sh\n[mvngu@sage sage-main]$ hg tags | grep '4.5.alpha'\n4.5.alpha4                     14585:31da167254fd\n4.5.alpha3                     14573:8bb71030944a\n4.5.alpha2                     14567:1be02074cf97\n4.5.alpha1                     14563:c25e907dc34d\n4.5.alpha0                     14531:8dec8b43ccca\n[mvngu@sage sage-main]$ hg export 14532 | head\n# HG changeset patch\n# User Robert Miller <rlm@rlmiller.org>\n# Date 1277467893 25200\n# Node ID c3719ae4c319132134fc1ff501e134d9930648d8\n# Parent  8dec8b43ccca5f104b1e280cb33c8f4c2c1b8f85\nAdded tag 4.5.alpha0 for changeset 8dec8b43ccca\n\ndiff --git a/.hgtags b/.hgtags\n--- a/.hgtags\n+++ b/.hgtags\n[mvngu@sage sage-main]$ hg export 14534 | head\n# HG changeset patch\n# User Robert Miller <rlm@rlmiller.org>\n# Date 1277743380 25200\n# Node ID ddd5427e99b9d7ba94842c479bf3bfd5b3e08ff9\n# Parent  5c14ca9acdd371af75f7e9cc8fc342c8bbd2ed05\nRemove doc/en/faq/Makefile from revision control\n\ndiff --git a/doc/en/faq/Makefile b/doc/en/faq/Makefile\ndeleted file mode 100644\n--- a/doc/en/faq/Makefile\n[mvngu@sage sage-main]$ hg export 14564 | head\n# HG changeset patch\n# User Robert Miller <rlm@rlmiller.org>\n# Date 1277828988 25200\n# Node ID 995b80b5b58b0374c04d891c35159cce5c48a0a6\n# Parent  c25e907dc34d83f4ed0b0edf0fdfb06cc5eba957\nAdded tag 4.5.alpha1 for changeset c25e907dc34d\n\ndiff --git a/.hgtags b/.hgtags\n--- a/.hgtags\n+++ b/.hgtags\n```\n\nThe ticket then should be resolved as fixed in milestone 4.5 and merged in 4.5.alpha1.",
    "created_at": "2010-07-21T06:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:5 mpatel]:
> Minh, should I select a different resolution and/or milestone?

The file `doc/en/faq/Makefile` was removed from revision control in Sage 4.5.alpha1:

```sh
[mvngu@sage sage-main]$ hg tags | grep '4.5.alpha'
4.5.alpha4                     14585:31da167254fd
4.5.alpha3                     14573:8bb71030944a
4.5.alpha2                     14567:1be02074cf97
4.5.alpha1                     14563:c25e907dc34d
4.5.alpha0                     14531:8dec8b43ccca
[mvngu@sage sage-main]$ hg export 14532 | head
# HG changeset patch
# User Robert Miller <rlm@rlmiller.org>
# Date 1277467893 25200
# Node ID c3719ae4c319132134fc1ff501e134d9930648d8
# Parent  8dec8b43ccca5f104b1e280cb33c8f4c2c1b8f85
Added tag 4.5.alpha0 for changeset 8dec8b43ccca

diff --git a/.hgtags b/.hgtags
--- a/.hgtags
+++ b/.hgtags
[mvngu@sage sage-main]$ hg export 14534 | head
# HG changeset patch
# User Robert Miller <rlm@rlmiller.org>
# Date 1277743380 25200
# Node ID ddd5427e99b9d7ba94842c479bf3bfd5b3e08ff9
# Parent  5c14ca9acdd371af75f7e9cc8fc342c8bbd2ed05
Remove doc/en/faq/Makefile from revision control

diff --git a/doc/en/faq/Makefile b/doc/en/faq/Makefile
deleted file mode 100644
--- a/doc/en/faq/Makefile
[mvngu@sage sage-main]$ hg export 14564 | head
# HG changeset patch
# User Robert Miller <rlm@rlmiller.org>
# Date 1277828988 25200
# Node ID 995b80b5b58b0374c04d891c35159cce5c48a0a6
# Parent  c25e907dc34d83f4ed0b0edf0fdfb06cc5eba957
Added tag 4.5.alpha1 for changeset c25e907dc34d

diff --git a/.hgtags b/.hgtags
--- a/.hgtags
+++ b/.hgtags
```

The ticket then should be resolved as fixed in milestone 4.5 and merged in 4.5.alpha1.



---

archive/issue_comments_087792.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Just to check:  Should we keep `doc/en/tutorial/Makefile`?\nI think it can safely be deleted. We need to ensure that its removal has no effect on building the HTML and PDF versions of the documentation.",
    "created_at": "2010-07-21T06:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87792",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:4 mpatel]:
> Just to check:  Should we keep `doc/en/tutorial/Makefile`?
I think it can safely be deleted. We need to ensure that its removal has no effect on building the HTML and PDF versions of the documentation.



---

archive/issue_comments_087793.json:
```json
{
    "body": "Thanks, Minh!  (Yes, I should have figured that out myself.)  Do you mind being listed as the reviewer, possibly/albeit after the fact?\n\nI've opened #9563 for removing `doc/en/tutorial/Makefile`.",
    "created_at": "2010-07-21T11:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9323#issuecomment-87793",
    "user": "https://github.com/qed777"
}
```

Thanks, Minh!  (Yes, I should have figured that out myself.)  Do you mind being listed as the reviewer, possibly/albeit after the fact?

I've opened #9563 for removing `doc/en/tutorial/Makefile`.
