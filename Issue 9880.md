# Issue 9880: fix the symbolic csgn function on complex input

archive/issues_009880.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nOur wrapper of the csgn function from GiNaC (in `sage/symbolic/expression.pyx`) doesn't reflect it's real definition:\n\n\n```\n  /** Return the complex half-plane (left or right) in which the number lies.\n   *  csgn(x)==0 for x==0, csgn(x)==1 for Re(x)>0 or Re(x)=0 and Im(x)>0,\n   *  csgn(x)==-1 for Re(x)<0 or Re(x)=0 and Im(x)<0.\n   *  */\n```\n\n\nFix this and add doctests.\n\nWe should also consider using GiNaC's `csgn()` function for the top level `sgn()` and `sign()` functions. This should be on a different ticket though.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9881\n\n",
    "created_at": "2010-09-09T09:04:30Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "fix the symbolic csgn function on complex input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9880",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

Our wrapper of the csgn function from GiNaC (in `sage/symbolic/expression.pyx`) doesn't reflect it's real definition:


```
  /** Return the complex half-plane (left or right) in which the number lies.
   *  csgn(x)==0 for x==0, csgn(x)==1 for Re(x)>0 or Re(x)=0 and Im(x)>0,
   *  csgn(x)==-1 for Re(x)<0 or Re(x)=0 and Im(x)<0.
   *  */
```


Fix this and add doctests.

We should also consider using GiNaC's `csgn()` function for the top level `sgn()` and `sign()` functions. This should be on a different ticket though.

Issue created by migration from https://trac.sagemath.org/ticket/9881





---

archive/issue_comments_097776.json:
```json
{
    "body": "Attachment [trac_9881-csgn.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn.patch) by @burcin created at 2010-09-12 11:07:50",
    "created_at": "2010-09-12T11:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97776",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9881-csgn.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn.patch) by @burcin created at 2010-09-12 11:07:50



---

archive/issue_comments_097777.json:
```json
{
    "body": "The new pynac package at #9201 changes the `csgn()` function according to the description. attachment:trac_9881-csgn.patch adds doctests for the new specification.\n\nThe pynac package includes patches for #9394, #9834, #9878, #9879, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.",
    "created_at": "2010-09-12T12:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97777",
    "user": "https://github.com/burcin"
}
```

The new pynac package at #9201 changes the `csgn()` function according to the description. attachment:trac_9881-csgn.patch adds doctests for the new specification.

The pynac package includes patches for #9394, #9834, #9878, #9879, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.



---

archive/issue_comments_097778.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T12:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97778",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097779.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> The new pynac package at #9201 changes the `csgn()` function according to the description. \n\nThat should have been \"at #9901\".",
    "created_at": "2010-09-12T12:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97779",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:1 burcin]:
> The new pynac package at #9201 changes the `csgn()` function according to the description. 

That should have been "at #9901".



---

archive/issue_comments_097780.json:
```json
{
    "body": "Just FYI - this appears to still apply cleanly after the review patch at #9879.",
    "created_at": "2010-10-05T00:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97780",
    "user": "https://github.com/kcrisman"
}
```

Just FYI - this appears to still apply cleanly after the review patch at #9879.



---

archive/issue_comments_097781.json:
```json
{
    "body": "Okay, this looks good on both Pynac and Sage side - with the exception that I think the documentation needed slightly more clarity, and that some of the examples got misplaced to `binomial` for some reason.  Positive review; apply reviewer patch after initial patch.",
    "created_at": "2010-10-05T00:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97781",
    "user": "https://github.com/kcrisman"
}
```

Okay, this looks good on both Pynac and Sage side - with the exception that I think the documentation needed slightly more clarity, and that some of the examples got misplaced to `binomial` for some reason.  Positive review; apply reviewer patch after initial patch.



---

archive/issue_comments_097782.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-05T00:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97782",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097783.json:
```json
{
    "body": "Apply after initial patch.",
    "created_at": "2010-10-05T00:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97783",
    "user": "https://github.com/kcrisman"
}
```

Apply after initial patch.



---

archive/issue_events_024891.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-06T03:20:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9880#event-24891"
}
```



---

archive/issue_comments_097784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97784",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_097785.json:
```json
{
    "body": "Attachment [trac_9881-csgn-reviewer.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn-reviewer.patch) by @qed777 created at 2010-10-06 03:20:19",
    "created_at": "2010-10-06T03:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97785",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9881-csgn-reviewer.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn-reviewer.patch) by @qed777 created at 2010-10-06 03:20:19
