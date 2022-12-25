# Issue 7971: Change all occurrences of "method" to "algorithm" in coding/code_bounds.py

archive/issues_007971.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nCC:  @wdjoyner\n\nThis is a follow-on to #6094.  More places where the keyword argument \"method=\" should be changed to \"algorithm=\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/7971\n\n",
    "closed_at": "2010-11-09T11:06:03Z",
    "created_at": "2010-01-18T04:37:28Z",
    "labels": [
        "component: coding theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Change all occurrences of \"method\" to \"algorithm\" in coding/code_bounds.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7971",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @wdjoyner

CC:  @wdjoyner

This is a follow-on to #6094.  More places where the keyword argument "method=" should be changed to "algorithm=".

Issue created by migration from https://trac.sagemath.org/ticket/7971





---

archive/issue_comments_069411.json:
```json
{
    "body": "This patch will build, and the tests in sage/coding all pass.  But I don't have Guava installed, which is needed for most of the affected doctests.\n\nDavid - maybe you can run the optional tests as part of a review?",
    "created_at": "2010-01-18T05:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69411",
    "user": "https://github.com/rbeezer"
}
```

This patch will build, and the tests in sage/coding all pass.  But I don't have Guava installed, which is needed for most of the affected doctests.

David - maybe you can run the optional tests as part of a review?



---

archive/issue_comments_069412.json:
```json
{
    "body": "Attachment [trac_7971_method_algorithm.patch](tarball://root/attachments/some-uuid/ticket7971/trac_7971_method_algorithm.patch) by @rbeezer created at 2010-01-18 05:42:18",
    "created_at": "2010-01-18T05:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69412",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7971_method_algorithm.patch](tarball://root/attachments/some-uuid/ticket7971/trac_7971_method_algorithm.patch) by @rbeezer created at 2010-01-18 05:42:18



---

archive/issue_comments_069413.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T05:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69413",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069414.json:
```json
{
    "body": "Passes all doctests on Sage 4.3.1.rc0 with or without the patch. To run the optional doctests that require Guava: After applying the patch, install the optional Guava package by installing the package [gap_packages-4.4.10_6.spkg](http://www.sagemath.org/packages/optional/gap_packages-4.4.10_6.spkg). Running doctest on \"sage/coding/code_bounds.py\" with the options\n\n```\n-t -long -optional\n```\nresults in all doctests passed. Positive review.",
    "created_at": "2010-01-18T06:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69414",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Passes all doctests on Sage 4.3.1.rc0 with or without the patch. To run the optional doctests that require Guava: After applying the patch, install the optional Guava package by installing the package [gap_packages-4.4.10_6.spkg](http://www.sagemath.org/packages/optional/gap_packages-4.4.10_6.spkg). Running doctest on "sage/coding/code_bounds.py" with the options

```
-t -long -optional
```
results in all doctests passed. Positive review.



---

archive/issue_comments_069415.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69415",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069416.json:
```json
{
    "body": "This needs work (deprecation warnings) and so should just be handled as part of #6094.  \n\nI've marked this as \"needs work\" but should be marked some form of invalid.",
    "created_at": "2010-01-18T21:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69416",
    "user": "https://github.com/rbeezer"
}
```

This needs work (deprecation warnings) and so should just be handled as part of #6094.  

I've marked this as "needs work" but should be marked some form of invalid.



---

archive/issue_comments_069417.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-18T21:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69417",
    "user": "https://github.com/rbeezer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069418.json:
```json
{
    "body": "The currently newest uploaded patch for Trac #6094 -- needing a positive review -- handles all these cases, so this Trac should just be closed.",
    "created_at": "2010-11-02T14:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69418",
    "user": "https://github.com/johanrosenkilde"
}
```

The currently newest uploaded patch for Trac #6094 -- needing a positive review -- handles all these cases, so this Trac should just be closed.



---

archive/issue_comments_069419.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-09T11:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7971#issuecomment-69419",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate



---

archive/issue_events_019074.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-11-09T11:06:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7971#event-19074"
}
```



---

archive/issue_events_019075.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-11-09T11:12:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7971",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7971#event-19075"
}
```
