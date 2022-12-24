# Issue 9142: construct "fuzzy ball" graphs

archive/issues_009142.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @nathanncohen @rlmill\n\nThe Fuzzy Ball graphs are cospectral with respect to the normalized laplacian matrix.  This patch makes a function to construct such graphs.  I will be adding a reference in a separate patch once we publish our paper :).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9142\n\n",
    "created_at": "2010-06-04T21:18:55Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "construct \"fuzzy ball\" graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9142",
    "user": "@jasongrout"
}
```
Assignee: jason, ncohen, rlm

CC:  @nathanncohen @rlmill

The Fuzzy Ball graphs are cospectral with respect to the normalized laplacian matrix.  This patch makes a function to construct such graphs.  I will be adding a reference in a separate patch once we publish our paper :).

Issue created by migration from https://trac.sagemath.org/ticket/9142





---

archive/issue_comments_085366.json:
```json
{
    "body": "Attachment [trac-9142-fuzzy-ball.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-fuzzy-ball.patch) by @jasongrout created at 2010-06-04 21:20:03",
    "created_at": "2010-06-04T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85366",
    "user": "@jasongrout"
}
```

Attachment [trac-9142-fuzzy-ball.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-fuzzy-ball.patch) by @jasongrout created at 2010-06-04 21:20:03



---

archive/issue_comments_085367.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-04T21:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85367",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085368.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T21:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85368",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085369.json:
```json
{
    "body": "Positive review to this patch, which will be nicer with a reference :-)\n\nI add a small patch with minor corrections : some math formulas were written plain text, which reflects badly on the indices. \"Anyone but me can review this patch\", as Minh says !\n\nNathann",
    "created_at": "2010-06-04T21:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85369",
    "user": "@nathanncohen"
}
```

Positive review to this patch, which will be nicer with a reference :-)

I add a small patch with minor corrections : some math formulas were written plain text, which reflects badly on the indices. "Anyone but me can review this patch", as Minh says !

Nathann



---

archive/issue_comments_085370.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-04T21:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85370",
    "user": "@nathanncohen"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_085371.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-04T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85371",
    "user": "@nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085372.json:
```json
{
    "body": "Please forget about my patch, as it makes no difference. I can not see why, though O_o",
    "created_at": "2010-06-04T22:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85372",
    "user": "@nathanncohen"
}
```

Please forget about my patch, as it makes no difference. I can not see why, though O_o



---

archive/issue_comments_085373.json:
```json
{
    "body": "Only because dvipng was not installed on my machine. Please consider my patch anew, and my excuses for this mistake :-)\n\nNathann",
    "created_at": "2010-06-04T22:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85373",
    "user": "@nathanncohen"
}
```

Only because dvipng was not installed on my machine. Please consider my patch anew, and my excuses for this mistake :-)

Nathann



---

archive/issue_comments_085374.json:
```json
{
    "body": "I had forgotten to add the \"r\" in front of \"\"\". Updated !\n\nNathann",
    "created_at": "2010-06-04T22:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85374",
    "user": "@nathanncohen"
}
```

I had forgotten to add the "r" in front of """. Updated !

Nathann



---

archive/issue_comments_085375.json:
```json
{
    "body": "Attachment [trac_9142-reviewer.patch](tarball://root/attachments/some-uuid/ticket9142/trac_9142-reviewer.patch) by @jasongrout created at 2010-06-04 22:15:52\n\napply on top of previous patches",
    "created_at": "2010-06-04T22:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85375",
    "user": "@jasongrout"
}
```

Attachment [trac_9142-reviewer.patch](tarball://root/attachments/some-uuid/ticket9142/trac_9142-reviewer.patch) by @jasongrout created at 2010-06-04 22:15:52

apply on top of previous patches



---

archive/issue_comments_085376.json:
```json
{
    "body": "Attachment [trac-9142-small-doc-fix.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-small-doc-fix.patch) by @jasongrout created at 2010-06-04 22:16:40\n\nPositive review to your patch.  Can you look at my minor change in the explanation, to make it clear that you pass a list instead of a sum in for the partition?",
    "created_at": "2010-06-04T22:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85376",
    "user": "@jasongrout"
}
```

Attachment [trac-9142-small-doc-fix.patch](tarball://root/attachments/some-uuid/ticket9142/trac-9142-small-doc-fix.patch) by @jasongrout created at 2010-06-04 22:16:40

Positive review to your patch.  Can you look at my minor change in the explanation, to make it clear that you pass a list instead of a sum in for the partition?



---

archive/issue_comments_085377.json:
```json
{
    "body": "Agreed :-)\n\nNathann",
    "created_at": "2010-06-04T22:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85377",
    "user": "@nathanncohen"
}
```

Agreed :-)

Nathann



---

archive/issue_comments_085378.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T22:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85378",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085379.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9142#issuecomment-85379",
    "user": "@mwhansen"
}
```

Resolution: fixed
