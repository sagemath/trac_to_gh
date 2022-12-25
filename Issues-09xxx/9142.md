# Issue 9142: construct "fuzzy ball" graphs

archive/issues_009142.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @nathanncohen @rlmill\n\nThe Fuzzy Ball graphs are cospectral with respect to the normalized laplacian matrix.  This patch makes a function to construct such graphs.  I will be adding a reference in a separate patch once we publish our paper :).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9142\n\n",
    "closed_at": "2010-06-06T07:21:51Z",
    "created_at": "2010-06-04T21:18:55Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "construct \"fuzzy ball\" graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9142",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, ncohen, rlm

CC:  @nathanncohen @rlmill

The Fuzzy Ball graphs are cospectral with respect to the normalized laplacian matrix.  This patch makes a function to construct such graphs.  I will be adding a reference in a separate patch once we publish our paper :).

Issue created by migration from https://trac.sagemath.org/ticket/9142





---

archive/issue_comments_085229.json:
```json
{
    "body": "Attachment [trac-9142-fuzzy-ball.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-fuzzy-ball.patch) by @jasongrout created at 2010-06-04 21:20:03",
    "created_at": "2010-06-04T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85229",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9142-fuzzy-ball.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-fuzzy-ball.patch) by @jasongrout created at 2010-06-04 21:20:03



---

archive/issue_comments_085230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-04T21:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85230",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085231.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T21:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85231",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085232.json:
```json
{
    "body": "Positive review to this patch, which will be nicer with a reference :-)\n\nI add a small patch with minor corrections : some math formulas were written plain text, which reflects badly on the indices. \"Anyone but me can review this patch\", as Minh says !\n\nNathann",
    "created_at": "2010-06-04T21:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85232",
    "user": "https://github.com/nathanncohen"
}
```

Positive review to this patch, which will be nicer with a reference :-)

I add a small patch with minor corrections : some math formulas were written plain text, which reflects badly on the indices. "Anyone but me can review this patch", as Minh says !

Nathann



---

archive/issue_comments_085233.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-04T21:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85233",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085234.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-04T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85234",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085235.json:
```json
{
    "body": "Please forget about my patch, as it makes no difference. I can not see why, though O_o",
    "created_at": "2010-06-04T22:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85235",
    "user": "https://github.com/nathanncohen"
}
```

Please forget about my patch, as it makes no difference. I can not see why, though O_o



---

archive/issue_comments_085236.json:
```json
{
    "body": "Only because dvipng was not installed on my machine. Please consider my patch anew, and my excuses for this mistake :-)\n\nNathann",
    "created_at": "2010-06-04T22:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85236",
    "user": "https://github.com/nathanncohen"
}
```

Only because dvipng was not installed on my machine. Please consider my patch anew, and my excuses for this mistake :-)

Nathann



---

archive/issue_comments_085237.json:
```json
{
    "body": "I had forgotten to add the \"r\" in front of \"\"\". Updated !\n\nNathann",
    "created_at": "2010-06-04T22:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85237",
    "user": "https://github.com/nathanncohen"
}
```

I had forgotten to add the "r" in front of """. Updated !

Nathann



---

archive/issue_comments_085238.json:
```json
{
    "body": "Attachment [trac_9142-reviewer.patch](tarball://root/attachments/some-uuid/ticket9142/trac_9142-reviewer.patch) by @jasongrout created at 2010-06-04 22:15:52\n\napply on top of previous patches",
    "created_at": "2010-06-04T22:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85238",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9142-reviewer.patch](tarball://root/attachments/some-uuid/ticket9142/trac_9142-reviewer.patch) by @jasongrout created at 2010-06-04 22:15:52

apply on top of previous patches



---

archive/issue_comments_085239.json:
```json
{
    "body": "Attachment [trac-9142-small-doc-fix.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-small-doc-fix.patch) by @jasongrout created at 2010-06-04 22:16:40\n\nPositive review to your patch.  Can you look at my minor change in the explanation, to make it clear that you pass a list instead of a sum in for the partition?",
    "created_at": "2010-06-04T22:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85239",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9142-small-doc-fix.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-small-doc-fix.patch) by @jasongrout created at 2010-06-04 22:16:40

Positive review to your patch.  Can you look at my minor change in the explanation, to make it clear that you pass a list instead of a sum in for the partition?



---

archive/issue_comments_085240.json:
```json
{
    "body": "Agreed :-)\n\nNathann",
    "created_at": "2010-06-04T22:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85240",
    "user": "https://github.com/nathanncohen"
}
```

Agreed :-)

Nathann



---

archive/issue_comments_085241.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T22:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85241",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022466.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T07:21:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9142#event-22466"
}
```



---

archive/issue_comments_085242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85242",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
