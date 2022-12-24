# Issue 9961: vector plot should have optional "start" argument

archive/issues_009961.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  ryan kcrisman\n\nKeywords: beginner\n\nIt would be really nice if this plotted an arrow from (1,2) to (3,4):\n\n\n```\nsage: v=vector([1,2])\nsage: u=vector([2,2])\nsage: plot(u,start=v)\n```\n\n\nor maybe the option should be \"base\" or \"origin\"\n\nTo fix this, just change the plot method in `devel/sage/sage/modules/free_module_element.pyx`\n\nIssue created by migration from https://trac.sagemath.org/ticket/9962\n\n",
    "created_at": "2010-09-21T20:02:44Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "vector plot should have optional \"start\" argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9961",
    "user": "jason"
}
```
Assignee: jason, was

CC:  ryan kcrisman

Keywords: beginner

It would be really nice if this plotted an arrow from (1,2) to (3,4):


```
sage: v=vector([1,2])
sage: u=vector([2,2])
sage: plot(u,start=v)
```


or maybe the option should be "base" or "origin"

To fix this, just change the plot method in `devel/sage/sage/modules/free_module_element.pyx`

Issue created by migration from https://trac.sagemath.org/ticket/9962





---

archive/issue_comments_099764.json:
```json
{
    "body": "I think \"start=list/tuple/vector\" is the best convention for this option.",
    "created_at": "2010-09-21T20:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99764",
    "user": "jason"
}
```

I think "start=list/tuple/vector" is the best convention for this option.



---

archive/issue_comments_099765.json:
```json
{
    "body": "tentative patch",
    "created_at": "2011-01-09T06:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99765",
    "user": "ryan"
}
```

tentative patch



---

archive/issue_comments_099766.json:
```json
{
    "body": "Attachment [trac_9962_start_vector.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_start_vector.patch) by ryan created at 2011-01-09 06:26:25\n\nthe patch gives the described output, but someone should double check my code for correctness.",
    "created_at": "2011-01-09T06:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99766",
    "user": "ryan"
}
```

Attachment [trac_9962_start_vector.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_start_vector.patch) by ryan created at 2011-01-09 06:26:25

the patch gives the described output, but someone should double check my code for correctness.



---

archive/issue_comments_099767.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-09T06:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99767",
    "user": "ryan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099768.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-09T16:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99768",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099769.json:
```json
{
    "body": "Replying to [comment:2 ryan]:\n> the patch gives the described output, but someone should double check my code for correctness.\n\nIt looks good to me.",
    "created_at": "2011-01-09T16:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99769",
    "user": "aly.deines"
}
```

Replying to [comment:2 ryan]:
> the patch gives the described output, but someone should double check my code for correctness.

It looks good to me.



---

archive/issue_comments_099770.json:
```json
{
    "body": "updated patch",
    "created_at": "2011-01-10T23:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99770",
    "user": "ryan"
}
```

updated patch



---

archive/issue_comments_099771.json:
```json
{
    "body": "Attachment [trac_9962_vector_start.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.patch) by ryan created at 2011-01-11 00:36:37",
    "created_at": "2011-01-11T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99771",
    "user": "ryan"
}
```

Attachment [trac_9962_vector_start.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.patch) by ryan created at 2011-01-11 00:36:37



---

archive/issue_comments_099772.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-11T00:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99772",
    "user": "ryan"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099773.json:
```json
{
    "body": "updated patch + doctests",
    "created_at": "2011-01-11T00:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99773",
    "user": "ryan"
}
```

updated patch + doctests



---

archive/issue_comments_099774.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-11T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99774",
    "user": "ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099775.json:
```json
{
    "body": "Attachment [trac_9962_vector_start.2.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.2.patch) by ryan created at 2011-01-11 00:46:08\n\nupdated patch:\n\nIncluded error handling for some cases where the two coordinates are not of the same dimension.  Also, added doctests.\n\nMuch cleaner patch.\n\nI appreciate the suggestions for making this patch better.",
    "created_at": "2011-01-11T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99775",
    "user": "ryan"
}
```

Attachment [trac_9962_vector_start.2.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962_vector_start.2.patch) by ryan created at 2011-01-11 00:46:08

updated patch:

Included error handling for some cases where the two coordinates are not of the same dimension.  Also, added doctests.

Much cleaner patch.

I appreciate the suggestions for making this patch better.



---

archive/issue_comments_099776.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-11T22:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99776",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099777.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:",
    "created_at": "2011-01-11T22:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99777",
    "user": "aly.deines"
}
```

Replying to [comment:7 kcrisman]:



---

archive/issue_comments_099778.json:
```json
{
    "body": "Please make it clear which patches have to be applied.",
    "created_at": "2011-01-17T17:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99778",
    "user": "jdemeyer"
}
```

Please make it clear which patches have to be applied.



---

archive/issue_comments_099779.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-17T17:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99779",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_099780.json:
```json
{
    "body": "It would be the latest patch, trac_9962_vector_start.2.patch",
    "created_at": "2011-01-17T17:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99780",
    "user": "ryan"
}
```

It would be the latest patch, trac_9962_vector_start.2.patch



---

archive/issue_comments_099781.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T17:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99781",
    "user": "ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099782.json:
```json
{
    "body": "You may want to check whether this really does the same thing as `v.plot()` - see #10638.",
    "created_at": "2011-01-17T20:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99782",
    "user": "kcrisman"
}
```

You may want to check whether this really does the same thing as `v.plot()` - see #10638.



---

archive/issue_comments_099783.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n> You may want to check whether this really does the same thing as `v.plot()` - see #10638.\n\nI am interpreting this comment as a needs_work (if it's not, then please set positive_review).",
    "created_at": "2011-01-19T01:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99783",
    "user": "jdemeyer"
}
```

Replying to [comment:11 kcrisman]:
> You may want to check whether this really does the same thing as `v.plot()` - see #10638.

I am interpreting this comment as a needs_work (if it's not, then please set positive_review).



---

archive/issue_comments_099784.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-19T01:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99784",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099785.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T02:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99785",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099786.json:
```json
{
    "body": "No, it's neither positive review nor needs work.  I haven't had the time to review this, but any reviewer should be sure to check this out.  That's all I am saying.",
    "created_at": "2011-01-19T02:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99786",
    "user": "kcrisman"
}
```

No, it's neither positive review nor needs work.  I haven't had the time to review this, but any reviewer should be sure to check this out.  That's all I am saying.



---

archive/issue_comments_099787.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-13T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99787",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099788.json:
```json
{
    "body": "This patch causes an amusing error, which does not occur in the vanilla Sage:\n\n```\n\nsage: plot(vector([1]))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2, 0))\n\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n<snip>\nArithmeticError: Cross product only defined for vectors of length three or seven, not (3 and 1)\n```\n\nI think I can fix this, so patch hopefully coming up.",
    "created_at": "2011-03-13T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99788",
    "user": "kcrisman"
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

archive/issue_comments_099789.json:
```json
{
    "body": "I think I have it fixed.  However, the bizarre error messages remain for one-dimensional arrows, so I have created followup ticket #10925 for that.",
    "created_at": "2011-03-13T01:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99789",
    "user": "kcrisman"
}
```

I think I have it fixed.  However, the bizarre error messages remain for one-dimensional arrows, so I have created followup ticket #10925 for that.



---

archive/issue_comments_099790.json:
```json
{
    "body": "Attachment [trac_9962-reviewer.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962-reviewer.patch) by kcrisman created at 2011-03-13 01:58:22\n\nApply after vector_start.2 patch",
    "created_at": "2011-03-13T01:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99790",
    "user": "kcrisman"
}
```

Attachment [trac_9962-reviewer.patch](tarball://root/attachments/some-uuid/ticket9962/trac_9962-reviewer.patch) by kcrisman created at 2011-03-13 01:58:22

Apply after vector_start.2 patch



---

archive/issue_comments_099791.json:
```json
{
    "body": "Okay, positive review on this nice addition from the original patch.  \n\nThe reviewer patch still needs review; it fixes the problem by extending the one-dimensional start as well, and adds/spruces up some documentation.  Reviewer should check things work, doctests, and that documentation looks ok.",
    "created_at": "2011-03-13T02:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99791",
    "user": "kcrisman"
}
```

Okay, positive review on this nice addition from the original patch.  

The reviewer patch still needs review; it fixes the problem by extending the one-dimensional start as well, and adds/spruces up some documentation.  Reviewer should check things work, doctests, and that documentation looks ok.



---

archive/issue_comments_099792.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-13T02:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99792",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099793.json:
```json
{
    "body": "Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.",
    "created_at": "2011-05-11T18:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99793",
    "user": "kcrisman"
}
```

Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.



---

archive/issue_comments_099794.json:
```json
{
    "body": "Replying to [comment:17 kcrisman]:\n> Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.\n\nI'll look at it this evening.",
    "created_at": "2011-05-13T16:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99794",
    "user": "ryan"
}
```

Replying to [comment:17 kcrisman]:
> Ryan, you can totally review the reviewer patch.  Just check that it still does what you wanted, that the doctests are correct and pass, and that `./sage -docbuild reference html` looks nice in the documentation for free modules.

I'll look at it this evening.



---

archive/issue_comments_099795.json:
```json
{
    "body": "everything looks good here.  I'm going to go ahead an change this to positive review for the reviewer patch.",
    "created_at": "2011-05-14T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99795",
    "user": "ryan"
}
```

everything looks good here.  I'm going to go ahead an change this to positive review for the reviewer patch.



---

archive/issue_comments_099796.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-14T06:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99796",
    "user": "ryan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-31T17:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9961#issuecomment-99797",
    "user": "jdemeyer"
}
```

Resolution: fixed
