# Issue 9961: vector plot should have optional "start" argument

archive/issues_009961.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  ryan @kcrisman\n\nKeywords: beginner\n\nIt would be really nice if this plotted an arrow from (1,2) to (3,4):\n\n```\nsage: v=vector([1,2])\nsage: u=vector([2,2])\nsage: plot(u,start=v)\n```\n\nor maybe the option should be \"base\" or \"origin\"\n\nTo fix this, just change the plot method in `devel/sage/sage/modules/free_module_element.pyx`\n\n---\n\nApply attachment:trac_9962_vector_start.2.patch and attachment:trac_9962-reviewer.patch\n\nIssue created by migration from https://trac.sagemath.org/ticket/9962\n\n",
    "closed_at": "2011-05-31T17:07:11Z",
    "created_at": "2010-09-21T20:02:44Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "vector plot should have optional \"start\" argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9961",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  ryan @kcrisman

Keywords: beginner

It would be really nice if this plotted an arrow from (1,2) to (3,4):

```
sage: v=vector([1,2])
sage: u=vector([2,2])
sage: plot(u,start=v)
```

or maybe the option should be "base" or "origin"

To fix this, just change the plot method in `devel/sage/sage/modules/free_module_element.pyx`

---

Apply attachment:trac_9962_vector_start.2.patch and attachment:trac_9962-reviewer.patch

Issue created by migration from https://trac.sagemath.org/ticket/9962





---

archive/issue_comments_099599.json:
```json
{
    "body": "I think \"start=list/tuple/vector\" is the best convention for this option.",
    "created_at": "2010-09-21T20:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99599",
    "user": "https://github.com/jasongrout"
}
```

I think "start=list/tuple/vector" is the best convention for this option.



---

archive/issue_comments_099600.json:
```json
{
    "body": "tentative patch",
    "created_at": "2011-01-09T06:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99600",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

tentative patch



---

archive/issue_comments_099601.json:
```json
{
    "body": "Attachment [trac_9962_start_vector.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_start_vector.patch) by ryan created at 2011-01-09 06:26:25\n\nthe patch gives the described output, but someone should double check my code for correctness.",
    "created_at": "2011-01-09T06:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99601",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_9962_start_vector.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_start_vector.patch) by ryan created at 2011-01-09 06:26:25

the patch gives the described output, but someone should double check my code for correctness.



---

archive/issue_comments_099602.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-09T06:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99602",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099603.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-09T16:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99603",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099604.json:
```json
{
    "body": "Replying to [comment:2 ryan]:\n> the patch gives the described output, but someone should double check my code for correctness.\n\n\nIt looks good to me.",
    "created_at": "2011-01-09T16:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99604",
    "user": "https://github.com/adeines"
}
```

Replying to [comment:2 ryan]:
> the patch gives the described output, but someone should double check my code for correctness.


It looks good to me.



---

archive/issue_events_025133.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-09T19:03:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9961#event-25133"
}
```



---

archive/issue_comments_099605.json:
```json
{
    "body": "updated patch",
    "created_at": "2011-01-10T23:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99605",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

updated patch



---

archive/issue_comments_099606.json:
```json
{
    "body": "Attachment [trac_9962_vector_start.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.patch) by ryan created at 2011-01-11 00:36:37",
    "created_at": "2011-01-11T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99606",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_9962_vector_start.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.patch) by ryan created at 2011-01-11 00:36:37



---

archive/issue_comments_099607.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-11T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99607",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099608.json:
```json
{
    "body": "updated patch + doctests",
    "created_at": "2011-01-11T00:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99608",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

updated patch + doctests



---

archive/issue_comments_099609.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-11T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99609",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099610.json:
```json
{
    "body": "Attachment [trac_9962_vector_start.2.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.2.patch) by ryan created at 2011-01-11 00:46:08\n\nupdated patch:\n\nIncluded error handling for some cases where the two coordinates are not of the same dimension.  Also, added doctests.\n\nMuch cleaner patch.\n\nI appreciate the suggestions for making this patch better.",
    "created_at": "2011-01-11T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99610",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_9962_vector_start.2.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.2.patch) by ryan created at 2011-01-11 00:46:08

updated patch:

Included error handling for some cases where the two coordinates are not of the same dimension.  Also, added doctests.

Much cleaner patch.

I appreciate the suggestions for making this patch better.



---

archive/issue_comments_099611.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-11T22:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99611",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099612.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:",
    "created_at": "2011-01-11T22:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99612",
    "user": "https://github.com/adeines"
}
```

Replying to [comment:7 kcrisman]:



---

archive/issue_comments_099613.json:
```json
{
    "body": "Please make it clear which patches have to be applied.",
    "created_at": "2011-01-17T17:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99613",
    "user": "https://github.com/jdemeyer"
}
```

Please make it clear which patches have to be applied.



---

archive/issue_comments_099614.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-17T17:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99614",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099615.json:
```json
{
    "body": "It would be the latest patch, trac_9962_vector_start.2.patch",
    "created_at": "2011-01-17T17:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99615",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

It would be the latest patch, trac_9962_vector_start.2.patch



---

archive/issue_comments_099616.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T17:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99616",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099617.json:
```json
{
    "body": "You may want to check whether this really does the same thing as `v.plot()` - see #10638.",
    "created_at": "2011-01-17T20:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99617",
    "user": "https://github.com/kcrisman"
}
```

You may want to check whether this really does the same thing as `v.plot()` - see #10638.



---

archive/issue_comments_099618.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n> You may want to check whether this really does the same thing as `v.plot()` - see #10638.\n\n\nI am interpreting this comment as a needs_work (if it's not, then please set positive_review).",
    "created_at": "2011-01-19T01:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99618",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:11 kcrisman]:
> You may want to check whether this really does the same thing as `v.plot()` - see #10638.


I am interpreting this comment as a needs_work (if it's not, then please set positive_review).



---

archive/issue_comments_099619.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-19T01:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99619",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099620.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T02:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99620",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099621.json:
```json
{
    "body": "No, it's neither positive review nor needs work.  I haven't had the time to review this, but any reviewer should be sure to check this out.  That's all I am saying.",
    "created_at": "2011-01-19T02:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99621",
    "user": "https://github.com/kcrisman"
}
```

No, it's neither positive review nor needs work.  I haven't had the time to review this, but any reviewer should be sure to check this out.  That's all I am saying.



---

archive/issue_comments_099622.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-13T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99622",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099623.json:
```json
{
    "body": "This patch causes an amusing error, which does not occur in the vanilla Sage:\n\n```\n\nsage: plot(vector([1]))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2, 0))\n\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n<snip>\nArithmeticError: Cross product only defined for vectors of length three or seven, not (3 and 1)\n```\nI think I can fix this, so patch hopefully coming up.",
    "created_at": "2011-03-13T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99623",
    "user": "https://github.com/kcrisman"
}
```

This patch causes an amusing error, which does not occur in the vanilla Sage:

```

sage: plot(vector([1]))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2, 0))

---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
<snip>
ArithmeticError: Cross product only defined for vectors of length three or seven, not (3 and 1)
```
I think I can fix this, so patch hopefully coming up.



---

archive/issue_comments_099624.json:
```json
{
    "body": "I think I have it fixed.  However, the bizarre error messages remain for one-dimensional arrows, so I have created followup ticket #10925 for that.",
    "created_at": "2011-03-13T01:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99624",
    "user": "https://github.com/kcrisman"
}
```

I think I have it fixed.  However, the bizarre error messages remain for one-dimensional arrows, so I have created followup ticket #10925 for that.



---

archive/issue_comments_099625.json:
```json
{
    "body": "Attachment [trac_9962-reviewer.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962-reviewer.patch) by @kcrisman created at 2011-03-13 01:58:22\n\nApply after vector_start.2 patch",
    "created_at": "2011-03-13T01:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99625",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9962-reviewer.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962-reviewer.patch) by @kcrisman created at 2011-03-13 01:58:22

Apply after vector_start.2 patch



---

archive/issue_comments_099626.json:
```json
{
    "body": "Okay, positive review on this nice addition from the original patch.  \n\nThe reviewer patch still needs review; it fixes the problem by extending the one-dimensional start as well, and adds/spruces up some documentation.  Reviewer should check things work, doctests, and that documentation looks ok.",
    "created_at": "2011-03-13T02:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99626",
    "user": "https://github.com/kcrisman"
}
```

Okay, positive review on this nice addition from the original patch.  

The reviewer patch still needs review; it fixes the problem by extending the one-dimensional start as well, and adds/spruces up some documentation.  Reviewer should check things work, doctests, and that documentation looks ok.



---

archive/issue_comments_099627.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-13T02:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99627",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099628.json:
```json
{
    "body": "Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.",
    "created_at": "2011-05-11T18:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99628",
    "user": "https://github.com/kcrisman"
}
```

Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.



---

archive/issue_comments_099629.json:
```json
{
    "body": "Replying to [comment:17 kcrisman]:\n> Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.\n\n\nI'll look at it this evening.",
    "created_at": "2011-05-13T16:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99629",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Replying to [comment:17 kcrisman]:
> Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.


I'll look at it this evening.



---

archive/issue_comments_099630.json:
```json
{
    "body": "everything looks good here.  I'm going to go ahead an change this to positive review for the reviewer patch.",
    "created_at": "2011-05-14T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99630",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

everything looks good here.  I'm going to go ahead an change this to positive review for the reviewer patch.



---

archive/issue_comments_099631.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-14T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99631",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_025134.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-15T14:54:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9961#event-25134"
}
```



---

archive/issue_events_025135.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-15T14:54:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9961#event-25135"
}
```



---

archive/issue_comments_099632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-31T17:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99632",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_025136.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-31T17:07:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9961#event-25136"
}
```
