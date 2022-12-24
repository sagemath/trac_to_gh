# Issue 9532: fix uncontrolled randomness in sage/graphs

archive/issues_009532.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @rlmill\n\nThere are several places in sage/graphs that use random numbers that aren't under the control of randstate.pyx.  I'm going to fix them now.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9532\n\n",
    "created_at": "2010-07-17T20:12:40Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "fix uncontrolled randomness in sage/graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9532",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  @rlmill

There are several places in sage/graphs that use random numbers that aren't under the control of randstate.pyx.  I'm going to fix them now.


Issue created by migration from https://trac.sagemath.org/ticket/9532





---

archive/issue_comments_091762.json:
```json
{
    "body": "Attachment [trac_9532-graphs-randstate.patch](tarball://root/attachments/some-uuid/ticket9532/trac_9532-graphs-randstate.patch) by cwitty created at 2010-07-17 22:47:44",
    "created_at": "2010-07-17T22:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9532#issuecomment-91762",
    "user": "cwitty"
}
```

Attachment [trac_9532-graphs-randstate.patch](tarball://root/attachments/some-uuid/ticket9532/trac_9532-graphs-randstate.patch) by cwitty created at 2010-07-17 22:47:44



---

archive/issue_comments_091763.json:
```json
{
    "body": "OK, the patch is up.  I fixed all the randomness I found (except for two calls in two versions of random_stress, which I left alone except for a comment).",
    "created_at": "2010-07-17T22:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9532#issuecomment-91763",
    "user": "cwitty"
}
```

OK, the patch is up.  I fixed all the randomness I found (except for two calls in two versions of random_stress, which I left alone except for a comment).



---

archive/issue_comments_091764.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-17T22:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9532#issuecomment-91764",
    "user": "cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091765.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-19T11:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9532#issuecomment-91765",
    "user": "@rlmill"
}
```

Looks good to me.



---

archive/issue_comments_091766.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-19T11:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9532#issuecomment-91766",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T02:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9532#issuecomment-91767",
    "user": "@qed777"
}
```

Resolution: fixed
