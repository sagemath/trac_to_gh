# Issue 9899: better conjugation for special functions

archive/issues_009899.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: pynac\n\nAdd doctests to test enhancements to conjugates of some special functions in pynac/GiNaC.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9900\n\n",
    "created_at": "2010-09-12T09:52:40Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "better conjugation for special functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9899",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Keywords: pynac

Add doctests to test enhancements to conjugates of some special functions in pynac/GiNaC.

Issue created by migration from https://trac.sagemath.org/ticket/9900





---

archive/issue_comments_098251.json:
```json
{
    "body": "Attachment [trac_9900_conjugate_doctests.patch](tarball://root/attachments/some-uuid/ticket9900/trac_9900_conjugate_doctests.patch) by @burcin created at 2010-09-12 11:08:12",
    "created_at": "2010-09-12T11:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98251",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9900_conjugate_doctests.patch](tarball://root/attachments/some-uuid/ticket9900/trac_9900_conjugate_doctests.patch) by @burcin created at 2010-09-12 11:08:12



---

archive/issue_comments_098252.json:
```json
{
    "body": "attachment:trac_9900_conjugate_doctests.patch adds doctests to reflect the changes in the new pynac version at #9901.\n\nThe pynac package includes patches for #9394, #9834, #9878, #9879, #9881 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.",
    "created_at": "2010-09-12T12:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98252",
    "user": "https://github.com/burcin"
}
```

attachment:trac_9900_conjugate_doctests.patch adds doctests to reflect the changes in the new pynac version at #9901.

The pynac package includes patches for #9394, #9834, #9878, #9879, #9881 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.



---

archive/issue_comments_098253.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-12T12:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98253",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098254.json:
```json
{
    "body": "This patch depends on knowing the branch cuts we wish to use.  A followup ticket for giving references for these choices (and/or for making sure they're the same as used for our numerical approximations of these!) is at #10033.",
    "created_at": "2010-09-29T18:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98254",
    "user": "https://github.com/kcrisman"
}
```

This patch depends on knowing the branch cuts we wish to use.  A followup ticket for giving references for these choices (and/or for making sure they're the same as used for our numerical approximations of these!) is at #10033.



---

archive/issue_comments_098255.json:
```json
{
    "body": "This comes from upstream in Ginac.  According to Burcin:\n\n just imported Richard Kreckel's [patch from upstream](http://www.ginac.de/ginac.git?p=ginac.git;a=commit;h=ff8b400eb500618644231ed9e6f199c3b0b25135).",
    "created_at": "2010-09-29T19:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98255",
    "user": "https://github.com/kcrisman"
}
```

This comes from upstream in Ginac.  According to Burcin:

 just imported Richard Kreckel's [patch from upstream](http://www.ginac.de/ginac.git?p=ginac.git;a=commit;h=ff8b400eb500618644231ed9e6f199c3b0b25135).



---

archive/issue_comments_098256.json:
```json
{
    "body": "Other than one spot where `arccos` should be `arccosh` in the new doctests, this is fine.  However, it seems good to add some more doctests, especially for the branch cuts to make sure they stay unsimplified.   A patch for this should be done by tomorrow sometime.",
    "created_at": "2010-10-05T00:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98256",
    "user": "https://github.com/kcrisman"
}
```

Other than one spot where `arccos` should be `arccosh` in the new doctests, this is fine.  However, it seems good to add some more doctests, especially for the branch cuts to make sure they stay unsimplified.   A patch for this should be done by tomorrow sometime.



---

archive/issue_comments_098257.json:
```json
{
    "body": "Attachment [trac_9900_conjugate_doctests-rebase.patch](tarball://root/attachments/some-uuid/ticket9900/trac_9900_conjugate_doctests-rebase.patch) by @kcrisman created at 2010-10-05 01:14:14\n\nRebase of original patch with respect to reviewer patches of #9879 and #9881",
    "created_at": "2010-10-05T01:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98257",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9900_conjugate_doctests-rebase.patch](tarball://root/attachments/some-uuid/ticket9900/trac_9900_conjugate_doctests-rebase.patch) by @kcrisman created at 2010-10-05 01:14:14

Rebase of original patch with respect to reviewer patches of #9879 and #9881



---

archive/issue_comments_098258.json:
```json
{
    "body": "Okay, reviewer patch is ready and coming right up.   Positive review.\n\nTo release manager: please merge first rebase patch, then reviewer patch.",
    "created_at": "2010-10-05T13:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98258",
    "user": "https://github.com/kcrisman"
}
```

Okay, reviewer patch is ready and coming right up.   Positive review.

To release manager: please merge first rebase patch, then reviewer patch.



---

archive/issue_comments_098259.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-05T13:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98259",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098260.json:
```json
{
    "body": "Attachment [trac_9900-reviewer.patch](tarball://root/attachments/some-uuid/ticket9900/trac_9900-reviewer.patch) by @kcrisman created at 2010-10-05 13:01:38\n\nReviewer patch, apply after rebase patch",
    "created_at": "2010-10-05T13:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98260",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9900-reviewer.patch](tarball://root/attachments/some-uuid/ticket9900/trac_9900-reviewer.patch) by @kcrisman created at 2010-10-05 13:01:38

Reviewer patch, apply after rebase patch



---

archive/issue_comments_098261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9899#issuecomment-98261",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024940.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-06T03:20:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9899#event-24940"
}
```
