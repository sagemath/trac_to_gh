# Issue 9880: fix the symbolic csgn function on complex input

archive/issues_009880.json:
```json
{
    "body": "Assignee: burcin\n\nKeywords: pynac\n\nOur wrapper of the csgn function from GiNaC (in `sage/symbolic/expression.pyx`) doesn't reflect it's real definition:\n\n\n```\n  /** Return the complex half-plane (left or right) in which the number lies.\n   *  csgn(x)==0 for x==0, csgn(x)==1 for Re(x)>0 or Re(x)=0 and Im(x)>0,\n   *  csgn(x)==-1 for Re(x)<0 or Re(x)=0 and Im(x)<0.\n   *  */\n```\n\n\nFix this and add doctests.\n\nWe should also consider using GiNaC's `csgn()` function for the top level `sgn()` and `sign()` functions. This should be on a different ticket though.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9881\n\n",
    "created_at": "2010-09-09T09:04:30Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "fix the symbolic csgn function on complex input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9880",
    "user": "burcin"
}
```
Assignee: burcin

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

archive/issue_comments_097938.json:
```json
{
    "body": "Attachment [trac_9881-csgn.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn.patch) by burcin created at 2010-09-12 11:07:50",
    "created_at": "2010-09-12T11:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97938",
    "user": "burcin"
}
```

Attachment [trac_9881-csgn.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn.patch) by burcin created at 2010-09-12 11:07:50



---

archive/issue_comments_097939.json:
```json
{
    "body": "The new pynac package at #9201 changes the `csgn()` function according to the description. attachment:trac_9881-csgn.patch adds doctests for the new specification.\n\nThe pynac package includes patches for #9394, #9834, #9878, #9879, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.",
    "created_at": "2010-09-12T12:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97939",
    "user": "burcin"
}
```

The new pynac package at #9201 changes the `csgn()` function according to the description. attachment:trac_9881-csgn.patch adds doctests for the new specification.

The pynac package includes patches for #9394, #9834, #9878, #9879, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.



---

archive/issue_comments_097940.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T12:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97940",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097941.json:
```json
{
    "body": "Replying to [comment:1 burcin]:\n> The new pynac package at #9201 changes the `csgn()` function according to the description. \n\nThat should have been \"at #9901\".",
    "created_at": "2010-09-12T12:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97941",
    "user": "burcin"
}
```

Replying to [comment:1 burcin]:
> The new pynac package at #9201 changes the `csgn()` function according to the description. 

That should have been "at #9901".



---

archive/issue_comments_097942.json:
```json
{
    "body": "Just FYI - this appears to still apply cleanly after the review patch at #9879.",
    "created_at": "2010-10-05T00:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97942",
    "user": "kcrisman"
}
```

Just FYI - this appears to still apply cleanly after the review patch at #9879.



---

archive/issue_comments_097943.json:
```json
{
    "body": "Okay, this looks good on both Pynac and Sage side - with the exception that I think the documentation needed slightly more clarity, and that some of the examples got misplaced to `binomial` for some reason.  Positive review; apply reviewer patch after initial patch.",
    "created_at": "2010-10-05T00:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97943",
    "user": "kcrisman"
}
```

Okay, this looks good on both Pynac and Sage side - with the exception that I think the documentation needed slightly more clarity, and that some of the examples got misplaced to `binomial` for some reason.  Positive review; apply reviewer patch after initial patch.



---

archive/issue_comments_097944.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-05T00:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97944",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097945.json:
```json
{
    "body": "Apply after initial patch.",
    "created_at": "2010-10-05T00:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97945",
    "user": "kcrisman"
}
```

Apply after initial patch.



---

archive/issue_comments_097946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97946",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_097947.json:
```json
{
    "body": "Attachment [trac_9881-csgn-reviewer.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn-reviewer.patch) by mpatel created at 2010-10-06 03:20:19",
    "created_at": "2010-10-06T03:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9880#issuecomment-97947",
    "user": "mpatel"
}
```

Attachment [trac_9881-csgn-reviewer.patch](tarball://root/attachments/some-uuid/ticket9881/trac_9881-csgn-reviewer.patch) by mpatel created at 2010-10-06 03:20:19
