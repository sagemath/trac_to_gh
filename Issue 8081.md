# Issue 8081: documentation bug on new gale_ryser_theorem()

archive/issues_008081.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @nathanncohen @wdjoyner\n\nIn the module `sage/combinat/integer_vector.py`, the documentation for the function `gale_ryser_theorem()` should be fixed as per the following suggestion:\n\n```\nOn the recently added\ngale_ryser_theorem()\nthere's a documentation bug (also present on the changelog)\n\n\"The Gale Ryser theorem asserts that if p1;p2  are two partitions of\nn  of respective lengths k1;k2 , then there is a binary k1\u00c2k2  matrix\nM  such that p1  is the vector of row sums and p2  is the vector of\ncolumn sums of M , if and only if p2  dominates p1 .\"\n\nAt the end it should say\n\n\"p2  conjugate (transpose) dominates p1\"\n\nThe theorem is mis-stated yet the function seems to be working\n```\nSee this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/5014758cac3b9e5d) for the original bug report.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8081\n\n",
    "created_at": "2010-01-26T18:01:53Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "documentation bug on new gale_ryser_theorem()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @nathanncohen @wdjoyner

In the module `sage/combinat/integer_vector.py`, the documentation for the function `gale_ryser_theorem()` should be fixed as per the following suggestion:

```
On the recently added
gale_ryser_theorem()
there's a documentation bug (also present on the changelog)

"The Gale Ryser theorem asserts that if p1;p2  are two partitions of
n  of respective lengths k1;k2 , then there is a binary k1Âk2  matrix
M  such that p1  is the vector of row sums and p2  is the vector of
column sums of M , if and only if p2  dominates p1 ."

At the end it should say

"p2  conjugate (transpose) dominates p1"

The theorem is mis-stated yet the function seems to be working
```
See this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/5014758cac3b9e5d) for the original bug report.

Issue created by migration from https://trac.sagemath.org/ticket/8081





---

archive/issue_comments_070698.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-28T11:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8081#issuecomment-70698",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070699.json:
```json
{
    "body": "Here it is !!!",
    "created_at": "2010-01-28T11:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8081#issuecomment-70699",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !!!



---

archive/issue_comments_070700.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T14:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8081#issuecomment-70700",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070701.json:
```json
{
    "body": "Attachment [trac_8081.patch](tarball://root/attachments/some-uuid/ticket8081/trac_8081.patch) by @wdjoyner created at 2010-01-28 14:15:02\n\nApplies fine to 4.3.2.a0 and passes all but the 2 tests that failed previously on a mac 10.6.2.\n\nGood docstring patch. Thanks Nathann!\n\nPositive review.",
    "created_at": "2010-01-28T14:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8081#issuecomment-70701",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_8081.patch](tarball://root/attachments/some-uuid/ticket8081/trac_8081.patch) by @wdjoyner created at 2010-01-28 14:15:02

Applies fine to 4.3.2.a0 and passes all but the 2 tests that failed previously on a mac 10.6.2.

Good docstring patch. Thanks Nathann!

Positive review.



---

archive/issue_comments_070702.json:
```json
{
    "body": "Nathann, the ticket number is very useful for tracking down changes. You might consider putting it in your commit message. See [this section](http://www.sagemath.org/doc/developer/producing_patches.html#quick-mercurial-tutorial-for-sage) of the Developers' Guide.",
    "created_at": "2010-01-29T22:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8081#issuecomment-70702",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Nathann, the ticket number is very useful for tracking down changes. You might consider putting it in your commit message. See [this section](http://www.sagemath.org/doc/developer/producing_patches.html#quick-mercurial-tutorial-for-sage) of the Developers' Guide.



---

archive/issue_events_019349.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-31T00:14:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8081#event-19349"
}
```



---

archive/issue_comments_070703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T00:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8081",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8081#issuecomment-70703",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
