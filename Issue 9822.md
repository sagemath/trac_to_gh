# Issue 9822: desolve_system is broken for a system of one equation

archive/issues_009822.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robert-marik\n\nKeywords: calculus, maxima, symbolics\n\ndesolve_system fails for a system with only one equation:\n\n```\nsage: t = var('t')\nsage: x = function('x', t)\nsage: de1 = diff(x,t) + 1 == 0\nsage: desolve_system([de1], [x]) \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9823\n\n",
    "created_at": "2010-08-27T16:40:56Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "desolve_system is broken for a system of one equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9822",
    "user": "https://github.com/rhinton"
}
```
Assignee: @burcin

CC:  @robert-marik

Keywords: calculus, maxima, symbolics

desolve_system fails for a system with only one equation:

```
sage: t = var('t')
sage: x = function('x', t)
sage: de1 = diff(x,t) + 1 == 0
sage: desolve_system([de1], [x]) 
```

Issue created by migration from https://trac.sagemath.org/ticket/9823





---

archive/issue_comments_096715.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T20:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96715",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096716.json:
```json
{
    "body": "The patch solves the problem by passing to desolve_laplace. Both desoove_laplace and desolve_system use function desolve from Maxima and perhaps bouth could be merged into one function. Perhaps when solving #9824 ?\n\nAlso removes unnecessary spawned Maxima processes.\n\nInstall after the patch for #9835.",
    "created_at": "2010-08-29T20:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96716",
    "user": "https://github.com/robert-marik"
}
```

The patch solves the problem by passing to desolve_laplace. Both desoove_laplace and desolve_system use function desolve from Maxima and perhaps bouth could be merged into one function. Perhaps when solving #9824 ?

Also removes unnecessary spawned Maxima processes.

Install after the patch for #9835.



---

archive/issue_comments_096717.json:
```json
{
    "body": "Depends on Ticket #9835",
    "created_at": "2010-08-30T06:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96717",
    "user": "https://github.com/robert-marik"
}
```

Depends on Ticket #9835



---

archive/issue_comments_096718.json:
```json
{
    "body": "Attachment [trac_9823.patch](tarball://root/attachments/some-uuid/ticket9823/trac_9823.patch) by @robert-marik created at 2010-08-30 06:31:40\n\nUpdated the patch - removed plotting picture from testing, since Sage complains \n\n```\nverbose 0 (3495: plot.py, generate_plot_points) WARNING: When plotting, failed to evaluate function at 200 points.\n```\non one of my computers (Debian, AMD 64 bit).",
    "created_at": "2010-08-30T06:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96718",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_9823.patch](tarball://root/attachments/some-uuid/ticket9823/trac_9823.patch) by @robert-marik created at 2010-08-30 06:31:40

Updated the patch - removed plotting picture from testing, since Sage complains 

```
verbose 0 (3495: plot.py, generate_plot_points) WARNING: When plotting, failed to evaluate function at 200 points.
```
on one of my computers (Debian, AMD 64 bit).



---

archive/issue_comments_096719.json:
```json
{
    "body": "Does this really depend on 9835? It seemed to apply and test fine for me without it.",
    "created_at": "2010-08-30T16:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96719",
    "user": "https://github.com/wdjoyner"
}
```

Does this really depend on 9835? It seemed to apply and test fine for me without it.



---

archive/issue_comments_096720.json:
```json
{
    "body": "You are right, thanks. Both patches touch different part of the same file and I expected numbers from the patch utility. But both patches are independent and #9835 can be installed on the top of this patch. Thanks for mentioning this.",
    "created_at": "2010-08-30T16:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96720",
    "user": "https://github.com/robert-marik"
}
```

You are right, thanks. Both patches touch different part of the same file and I expected numbers from the patch utility. But both patches are independent and #9835 can be installed on the top of this patch. Thanks for mentioning this.



---

archive/issue_comments_096721.json:
```json
{
    "body": "I have tested this without 9835 and it passes fine. Also, the patch is very simple and does as it says and also adds a doctest illustrating the new fix.\n\nPositive review from me, without 9835. I am currently also testing it with 9835.",
    "created_at": "2010-08-30T17:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96721",
    "user": "https://github.com/wdjoyner"
}
```

I have tested this without 9835 and it passes fine. Also, the patch is very simple and does as it says and also adds a doctest illustrating the new fix.

Positive review from me, without 9835. I am currently also testing it with 9835.



---

archive/issue_comments_096722.json:
```json
{
    "body": "All tests passes even with 9835.\n\nPositive review from me but maybe rhinton should look at it?",
    "created_at": "2010-08-30T19:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96722",
    "user": "https://github.com/wdjoyner"
}
```

All tests passes even with 9835.

Positive review from me but maybe rhinton should look at it?



---

archive/issue_comments_096723.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-31T03:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96723",
    "user": "https://github.com/rhinton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096724.json:
```json
{
    "body": "Looks great to me!",
    "created_at": "2010-08-31T03:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96724",
    "user": "https://github.com/rhinton"
}
```

Looks great to me!



---

archive/issue_events_024707.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T08:38:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9822#event-24707"
}
```



---

archive/issue_comments_096725.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9822#issuecomment-96725",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
