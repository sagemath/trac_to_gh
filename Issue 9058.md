# Issue 9058: Computing the k-core of a graph

archive/issues_009058.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  mvngu\n\nThis patch adds an option to the ``cores`` method, so that it returns both the k-core of a graph and a valid elimination ordering on the vertices out of it (such that their degree is less than k when they are removed)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9058\n\n",
    "closed_at": "2010-10-08T22:31:35Z",
    "created_at": "2010-05-26T22:30:27Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Computing the k-core of a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9058",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  mvngu

This patch adds an option to the ``cores`` method, so that it returns both the k-core of a graph and a valid elimination ordering on the vertices out of it (such that their degree is less than k when they are removed)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9058





---

archive/issue_comments_083910.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83910",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_083911.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-02T15:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83911",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083912.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-06T12:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83912",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083913.json:
```json
{
    "body": "Attachment [trac_9058.patch](tarball://root/attachments/some-uuid/ticket9058/trac_9058.patch) by lsampaio created at 2010-10-06 12:48:59\n\nI verified the patch and I believe it is ok to be merged.",
    "created_at": "2010-10-06T12:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83913",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Attachment [trac_9058.patch](tarball://root/attachments/some-uuid/ticket9058/trac_9058.patch) by lsampaio created at 2010-10-06 12:48:59

I verified the patch and I believe it is ok to be merged.



---

archive/issue_comments_083914.json:
```json
{
    "body": "cool ! Thanks `;-)`\n\nNathann",
    "created_at": "2010-10-06T12:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83914",
    "user": "https://github.com/nathanncohen"
}
```

cool ! Thanks `;-)`

Nathann



---

archive/issue_comments_083915.json:
```json
{
    "body": "Don't forget to update the author and reviewer fields.  lsampaio, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?",
    "created_at": "2010-10-08T21:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83915",
    "user": "https://github.com/qed777"
}
```

Don't forget to update the author and reviewer fields.  lsampaio, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?



---

archive/issue_comments_083916.json:
```json
{
    "body": "ok, I did it =)\nthank you for pointing this!",
    "created_at": "2010-10-08T21:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83916",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

ok, I did it =)
thank you for pointing this!



---

archive/issue_comments_083917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-08T22:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9058#issuecomment-83917",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022203.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-08T22:31:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9058",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9058#event-22203"
}
```
