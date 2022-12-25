# Issue 9200: Add left and right directions to limits

archive/issues_009200.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout @rbeezer\n\n1. Add `from_left` and `from_right` for `dir` keyword.\n\n2. Improve error message `dir` keyword.\n\n3. Add doctests and tests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9200\n\n",
    "created_at": "2010-06-10T02:26:53Z",
    "labels": [
        "component: calculus",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Add left and right directions to limits",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9200",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```
Assignee: @burcin

CC:  @jasongrout @rbeezer

1. Add `from_left` and `from_right` for `dir` keyword.

2. Improve error message `dir` keyword.

3. Add doctests and tests.

Issue created by migration from https://trac.sagemath.org/ticket/9200





---

archive/issue_comments_085924.json:
```json
{
    "body": "Attachment [trac_9200-left-right-limits.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-left-right-limits.patch) by DanaErnst created at 2010-06-10 02:47:58",
    "created_at": "2010-06-10T02:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85924",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

Attachment [trac_9200-left-right-limits.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-left-right-limits.patch) by DanaErnst created at 2010-06-10 02:47:58



---

archive/issue_comments_085925.json:
```json
{
    "body": "Patch passes tests in `sage/calculus`.  Need to test full Sage library.",
    "created_at": "2010-06-10T02:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85925",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

Patch passes tests in `sage/calculus`.  Need to test full Sage library.



---

archive/issue_comments_085926.json:
```json
{
    "body": "stand alone patch",
    "created_at": "2010-07-22T19:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85926",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

stand alone patch



---

archive/issue_comments_085927.json:
```json
{
    "body": "Attachment [trac_9200-left-right-limits-v2.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-left-right-limits-v2.patch) by DanaErnst created at 2010-07-22 19:42:07\n\nRebased for version 4.5.1, apply only v2 patch.",
    "created_at": "2010-07-22T19:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85927",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

Attachment [trac_9200-left-right-limits-v2.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-left-right-limits-v2.patch) by DanaErnst created at 2010-07-22 19:42:07

Rebased for version 4.5.1, apply only v2 patch.



---

archive/issue_comments_085928.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T12:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85928",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085929.json:
```json
{
    "body": "* All tests passed on version 4.5.1 (running OSX 10.6)\n  * HTML & PDF reference built without problem",
    "created_at": "2010-07-23T12:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85929",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

* All tests passed on version 4.5.1 (running OSX 10.6)
  * HTML & PDF reference built without problem



---

archive/issue_comments_085930.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-24T00:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85930",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085931.json:
```json
{
    "body": "Applies, builds, passes all tests, and docs look fine; on 4.5.2.alpha0.  So this is a positive review.\n\nNice job on your first contribution!",
    "created_at": "2010-07-24T00:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85931",
    "user": "https://github.com/rbeezer"
}
```

Applies, builds, passes all tests, and docs look fine; on 4.5.2.alpha0.  So this is a positive review.

Nice job on your first contribution!



---

archive/issue_comments_085932.json:
```json
{
    "body": "Do we really need new keywords for this? And if we do, should it be `from_{right,left}`?\n\nI think a user interface decision like this needs more input from other developers. I'll post to sage-devel with this question.",
    "created_at": "2010-07-24T21:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85932",
    "user": "https://github.com/burcin"
}
```

Do we really need new keywords for this? And if we do, should it be `from_{right,left}`?

I think a user interface decision like this needs more input from other developers. I'll post to sage-devel with this question.



---

archive/issue_comments_085933.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-07-24T21:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85933",
    "user": "https://github.com/burcin"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_085934.json:
```json
{
    "body": "The idea for this came up during one of the online sessions for the MAA PREP Workshop for Sage (organized by Rob Beezer, Jason Grout, and Karl-Dieter Crisman) that I am currently enrolled in.  While we were discussing calculus during one of our workshop sessions, one of the participants remarked that most students learn one-sided limits as \"from the left\" and \"from the right.\"  Rob, Jason, and Karl-Dieter knew that I was interested in getting involved in Sage development and remarked that I could add that this terminology to Sage if I was interested.  I figured that it was an easy way to get my feet wet.\n\nI have been using Sage for almost a year, so I would consider myself a newbie.  I'm not personally attached to this patch and if others feel that it is unnecessary bloat, then my feelings won't be hurt.",
    "created_at": "2010-07-25T02:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85934",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

The idea for this came up during one of the online sessions for the MAA PREP Workshop for Sage (organized by Rob Beezer, Jason Grout, and Karl-Dieter Crisman) that I am currently enrolled in.  While we were discussing calculus during one of our workshop sessions, one of the participants remarked that most students learn one-sided limits as "from the left" and "from the right."  Rob, Jason, and Karl-Dieter knew that I was interested in getting involved in Sage development and remarked that I could add that this terminology to Sage if I was interested.  I figured that it was an easy way to get my feet wet.

I have been using Sage for almost a year, so I would consider myself a newbie.  I'm not personally attached to this patch and if others feel that it is unnecessary bloat, then my feelings won't be hurt.



---

archive/issue_comments_085935.json:
```json
{
    "body": "Attachment [trac_9200-deprecation.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-deprecation.patch) by @burcin created at 2010-09-08 21:13:47\n\nadd deprecation warnings",
    "created_at": "2010-09-08T21:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85935",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9200-deprecation.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-deprecation.patch) by @burcin created at 2010-09-08 21:13:47

add deprecation warnings



---

archive/issue_comments_085936.json:
```json
{
    "body": "This was discussed in the thread:\n\nhttp://groups.google.com/group/sage-devel/t/9dd6dfe26f09be93\n\nThe resulting decision was to deprecate 'above' and 'below' and add support for '+', '-', 'right', and 'left'.\n\nattachment:trac_9200-deprecation.patch makes the necessary changes, on top of Dana's patch.\n\nPatches to be applied in this order:\n* attachment:trac_9200-left-right-limits-v2.patch\n* attachment:trac_9200-deprecation.patch",
    "created_at": "2010-09-08T21:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85936",
    "user": "https://github.com/burcin"
}
```

This was discussed in the thread:

http://groups.google.com/group/sage-devel/t/9dd6dfe26f09be93

The resulting decision was to deprecate 'above' and 'below' and add support for '+', '-', 'right', and 'left'.

attachment:trac_9200-deprecation.patch makes the necessary changes, on top of Dana's patch.

Patches to be applied in this order:
* attachment:trac_9200-left-right-limits-v2.patch
* attachment:trac_9200-deprecation.patch



---

archive/issue_comments_085937.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-08T21:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85937",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_085938.json:
```json
{
    "body": "Burcin,\n\nThanks for picking up the ball on this.  I was planning on attacking this in a few weeks after the initial craziness of my semester settled down.  Now, I get to cross something off my todo list:)\n\nDana",
    "created_at": "2010-09-09T00:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85938",
    "user": "https://trac.sagemath.org/admin/accounts/users/DanaErnst"
}
```

Burcin,

Thanks for picking up the ball on this.  I was planning on attacking this in a few weeks after the initial craziness of my semester settled down.  Now, I get to cross something off my todo list:)

Dana



---

archive/issue_comments_085939.json:
```json
{
    "body": "Attachment [trac_9200-deprecation-v2.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-deprecation-v2.patch) by @rbeezer created at 2010-09-09 05:58:11",
    "created_at": "2010-09-09T05:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85939",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9200-deprecation-v2.patch](tarball://root/attachments/some-uuid/ticket9200/trac_9200-deprecation-v2.patch) by @rbeezer created at 2010-09-09 05:58:11



---

archive/issue_comments_085940.json:
```json
{
    "body": "I noticed while reviewing this that there are two \"TEST\" headers in the docstring for limit().  So I removed the second one and uploaded a new version of the \"documentation\" patch - only change is the removal of the header (still has Burcin's name on it too).\n\nI'm running tests overnight and then plan to give this a positive review.  \n\nBurcin - I'll wait for you to check-off on the one change to your patch.\n\nRob",
    "created_at": "2010-09-09T06:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85940",
    "user": "https://github.com/rbeezer"
}
```

I noticed while reviewing this that there are two "TEST" headers in the docstring for limit().  So I removed the second one and uploaded a new version of the "documentation" patch - only change is the removal of the header (still has Burcin's name on it too).

I'm running tests overnight and then plan to give this a positive review.  

Burcin - I'll wait for you to check-off on the one change to your patch.

Rob



---

archive/issue_comments_085941.json:
```json
{
    "body": "Thanks for taking care of the `TEST` headers Rob. I'm ok with your change. Looking forward to that positive review. :)",
    "created_at": "2010-09-09T07:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85941",
    "user": "https://github.com/burcin"
}
```

Thanks for taking care of the `TEST` headers Rob. I'm ok with your change. Looking forward to that positive review. :)



---

archive/issue_comments_085942.json:
```json
{
    "body": "Thanks, Burcin, for the go-ahead and for prompting the discussion on this one.  Builds (on 4.5.2), docs look good, passes all tests (sage -testall) and is consistent with discussion on sage-devel.  Positive review.\n\nCongrats to Dana Ernst on his first contribution.  Next one will probably engender less discussion.  ;-)\n\n## Release Manager\n\n Patches to be applied in this order:\n* attachment:trac_9200-left-right-limits-v2.patch\n* attachment:trac_9200-deprecation-v2.patch\n\nDana Ernst is first-time contributor (for release notes).",
    "created_at": "2010-09-09T20:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85942",
    "user": "https://github.com/rbeezer"
}
```

Thanks, Burcin, for the go-ahead and for prompting the discussion on this one.  Builds (on 4.5.2), docs look good, passes all tests (sage -testall) and is consistent with discussion on sage-devel.  Positive review.

Congrats to Dana Ernst on his first contribution.  Next one will probably engender less discussion.  ;-)

## Release Manager

 Patches to be applied in this order:
* attachment:trac_9200-left-right-limits-v2.patch
* attachment:trac_9200-deprecation-v2.patch

Dana Ernst is first-time contributor (for release notes).



---

archive/issue_comments_085943.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-09T20:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85943",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009354.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-15T11:13:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9200#event-9354"
}
```



---

archive/issue_comments_085944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9200#issuecomment-85944",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
