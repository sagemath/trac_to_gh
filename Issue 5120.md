# Issue 5120: abstract class for unique representation

archive/issues_005120.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat\n\nImplement a sage.structure.UniqueRepresentation class. \nSubclasses inherit from it a unique representation behavior for its elements.\n\nPatch under construction, starting from sage.categories.category.uniq.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5120\n\n",
    "created_at": "2009-01-28T19:47:27Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "abstract class for unique representation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5120",
    "user": "nthiery"
}
```
Assignee: cwitty

CC:  sage-combinat

Implement a sage.structure.UniqueRepresentation class. 
Subclasses inherit from it a unique representation behavior for its elements.

Patch under construction, starting from sage.categories.category.uniq.

Issue created by migration from https://trac.sagemath.org/ticket/5120





---

archive/issue_comments_039126.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-28T22:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39126",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_039127.json:
```json
{
    "body": "Duplicate of #5119",
    "created_at": "2009-01-28T22:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39127",
    "user": "mhansen"
}
```

Duplicate of #5119



---

archive/issue_comments_039128.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-01-28T23:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39128",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_039129.json:
```json
{
    "body": "Well, Nicolas closed #5119 as a dupe, so I am reopening this one since I assume one ticket ought to stay open :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T23:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39129",
    "user": "mabshoff"
}
```

Well, Nicolas closed #5119 as a dupe, so I am reopening this one since I assume one ticket ought to stay open :)

Cheers,

Michael



---

archive/issue_comments_039130.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2009-01-28T23:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39130",
    "user": "mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_039131.json:
```json
{
    "body": "Changing assignee from cwitty to nthiery.",
    "created_at": "2009-03-04T04:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39131",
    "user": "nthiery"
}
```

Changing assignee from cwitty to nthiery.



---

archive/issue_comments_039132.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-03-04T04:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39132",
    "user": "nthiery"
}
```

Changing priority from minor to major.



---

archive/issue_comments_039133.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2009-03-04T04:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39133",
    "user": "nthiery"
}
```

Changing status from reopened to new.



---

archive/issue_comments_039134.json:
```json
{
    "body": "I'm sure there are good reasons why this is needed, but I think it would be helpful to potential reviewers of you could give a real-life example where this class will be used!",
    "created_at": "2009-03-14T20:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39134",
    "user": "cremona"
}
```

I'm sure there are good reasons why this is needed, but I think it would be helpful to potential reviewers of you could give a real-life example where this class will be used!



---

archive/issue_comments_039135.json:
```json
{
    "body": "1) The first line of one of the files is:\n\n```\n\u00ef\u00bb\u00bfr\"\"\" \n```\n\nI.e., lots of weird corrupted characters.\n\n2) There are no doctests for any of the actual functions you defined.  Code can't go into sage without 100% doctest coverage of each new function.",
    "created_at": "2009-04-12T06:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39135",
    "user": "was"
}
```

1) The first line of one of the files is:

```
ï»¿r""" 
```

I.e., lots of weird corrupted characters.

2) There are no doctests for any of the actual functions you defined.  Code can't go into sage without 100% doctest coverage of each new function.



---

archive/issue_comments_039136.json:
```json
{
    "body": "Uploaded an updated patch which fixes 1) and 2)\n\nOk to abide to a rule, even in a corner case like this where the extra doc really does not add any strength to the test suite, while actually making the code less readable. But it's frustrating to get complained at about documentation for a patch which has a doc/code ratio of 15/1. Next time a please will work better than a gun. \n\n       Grumpy O' Pa :-)",
    "created_at": "2009-04-13T19:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39136",
    "user": "nthiery"
}
```

Uploaded an updated patch which fixes 1) and 2)

Ok to abide to a rule, even in a corner case like this where the extra doc really does not add any strength to the test suite, while actually making the code less readable. But it's frustrating to get complained at about documentation for a patch which has a doc/code ratio of 15/1. Next time a please will work better than a gun. 

       Grumpy O' Pa :-)



---

archive/issue_comments_039137.json:
```json
{
    "body": "The patch doesn't apply cleanly to sage-3.4.1 since the hunk in\nsage/structure/all.py needs to be corrected by hand.",
    "created_at": "2009-04-24T20:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39137",
    "user": "bump"
}
```

The patch doesn't apply cleanly to sage-3.4.1 since the hunk in
sage/structure/all.py needs to be corrected by hand.



---

archive/issue_comments_039138.json:
```json
{
    "body": "Replying to [comment:8 bump]:\n> The patch doesn't apply cleanly to sage-3.4.1 since the hunk in\n> sage/structure/all.py needs to be corrected by hand.\nThanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two\nlittle other improvements.",
    "created_at": "2009-04-24T21:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39138",
    "user": "nthiery"
}
```

Replying to [comment:8 bump]:
> The patch doesn't apply cleanly to sage-3.4.1 since the hunk in
> sage/structure/all.py needs to be corrected by hand.
Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two
little other improvements.



---

archive/issue_comments_039139.json:
```json
{
    "body": "Replying to [comment:9 nthiery]:\n> Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two\n> little other improvements.\n\nI just updated the patch, rebased for 3.4.1, with description header, default implementation of copy/deepcopy, and pickling by reduce rather than getnewargs.\n\nThis later change is debatable. For some reason the reduce way was preferable for some application to categories, but I badly enough did not take notes about why",
    "created_at": "2009-04-24T23:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39139",
    "user": "nthiery"
}
```

Replying to [comment:9 nthiery]:
> Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two
> little other improvements.

I just updated the patch, rebased for 3.4.1, with description header, default implementation of copy/deepcopy, and pickling by reduce rather than getnewargs.

This later change is debatable. For some reason the reduce way was preferable for some application to categories, but I badly enough did not take notes about why



---

archive/issue_comments_039140.json:
```json
{
    "body": "Replying to [comment:10 nthiery]:\n> Replying to [comment:9 nthiery]:\n> > Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two\n> > little other improvements.\n> \n> I just updated the patch, rebased for 3.4.1, with description header, default implementation of copy/deepcopy, and pickling by reduce rather than getnewargs.\n> \n> This later change is debatable. For some reason the reduce way was preferable for some application to categories, but I badly enough did not take notes about why\n\nAh, I know why: keyword arguments. See updated, 100% doctested and proofread patch.",
    "created_at": "2009-04-25T07:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39140",
    "user": "nthiery"
}
```

Replying to [comment:10 nthiery]:
> Replying to [comment:9 nthiery]:
> > Thanks for the notice. The patch on sage-combinat has been rebased. I'll try to upload it today, after folding in two
> > little other improvements.
> 
> I just updated the patch, rebased for 3.4.1, with description header, default implementation of copy/deepcopy, and pickling by reduce rather than getnewargs.
> 
> This later change is debatable. For some reason the reduce way was preferable for some application to categories, but I badly enough did not take notes about why

Ah, I know why: keyword arguments. See updated, 100% doctested and proofread patch.



---

archive/issue_comments_039141.json:
```json
{
    "body": "> Ah, I know why: keyword arguments. See updated, 100% doctested and proofread patch.\n\nOops trivial update to apply cleanly on 3.4.1. Thanks Dan for the notice.\n\nMichael: could we change the milestone to 3.4.2?",
    "created_at": "2009-04-25T15:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39141",
    "user": "nthiery"
}
```

> Ah, I know why: keyword arguments. See updated, 100% doctested and proofread patch.

Oops trivial update to apply cleanly on 3.4.1. Thanks Dan for the notice.

Michael: could we change the milestone to 3.4.2?



---

archive/issue_comments_039142.json:
```json
{
    "body": "Replying to [comment:12 nthiery]:\n\nI deleted the old patch.\n\n> Michael: could we change the milestone to 3.4.2?\n\nThe assignment of milestones is generally insignificant (an exception is like right now when 3.4.2.rc0 was the last merge release and we are in blocker fixes only mode), but as long as this ticket would have gotten a positive review it would have had a chance to go into 3.4.2 regardless which milestone it would have been assigned to.\n\nThis patch is also a new design pattern which warrants to be mentioned on sage-devel. It seems to be very well documented and AFAIK it should be properly covered :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T22:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39142",
    "user": "mabshoff"
}
```

Replying to [comment:12 nthiery]:

I deleted the old patch.

> Michael: could we change the milestone to 3.4.2?

The assignment of milestones is generally insignificant (an exception is like right now when 3.4.2.rc0 was the last merge release and we are in blocker fixes only mode), but as long as this ticket would have gotten a positive review it would have had a chance to go into 3.4.2 regardless which milestone it would have been assigned to.

This patch is also a new design pattern which warrants to be mentioned on sage-devel. It seems to be very well documented and AFAIK it should be properly covered :)

Cheers,

Michael



---

archive/issue_comments_039143.json:
```json
{
    "body": "Applies cleanly to sage-3.4.2.rc0 and passes all tests.",
    "created_at": "2009-05-02T20:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39143",
    "user": "bump"
}
```

Applies cleanly to sage-3.4.2.rc0 and passes all tests.



---

archive/issue_comments_039144.json:
```json
{
    "body": "Note that #5879 exposes a problem with this patch. To quote Anne:\n\n```\nI just talked to Nicolas about the pickling problem; this is a shortcoming \nof the current unique representation patch and he will try to find a solution \nto the problem in patch 5120.\n```\n\n\nI will mark this \"needs work\" until this issue is resolved. \n\nCheers,\n\nMichael",
    "created_at": "2009-05-08T00:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39144",
    "user": "mabshoff"
}
```

Note that #5879 exposes a problem with this patch. To quote Anne:

```
I just talked to Nicolas about the pickling problem; this is a shortcoming 
of the current unique representation patch and he will try to find a solution 
to the problem in patch 5120.
```


I will mark this "needs work" until this issue is resolved. 

Cheers,

Michael



---

archive/issue_comments_039145.json:
```json
{
    "body": "Changing keywords from \"\" to \"unique representation\".",
    "created_at": "2009-05-08T21:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39145",
    "user": "nthiery"
}
```

Changing keywords from "" to "unique representation".



---

archive/issue_comments_039146.json:
```json
{
    "body": "I changed a bit the underlying implementation which fixes the code and should be more robust.\nI also added 2 pages of doc, and extracted a trivial yet general purpose CallclassMetaclass (Florent will be interested).\nUpdated patch upload in a couple minutes.",
    "created_at": "2009-05-08T21:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39146",
    "user": "nthiery"
}
```

I changed a bit the underlying implementation which fixes the code and should be more robust.
I also added 2 pages of doc, and extracted a trivial yet general purpose CallclassMetaclass (Florent will be interested).
Updated patch upload in a couple minutes.



---

archive/issue_comments_039147.json:
```json
{
    "body": "Updated patch includes ReST fixes suggested by David Roe, as well as an example on how to handle properly default arguments.",
    "created_at": "2009-05-19T06:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39147",
    "user": "nthiery"
}
```

Updated patch includes ReST fixes suggested by David Roe, as well as an example on how to handle properly default arguments.



---

archive/issue_comments_039148.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39148",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039149.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-19T07:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39149",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_039150.json:
```json
{
    "body": "I'd like to see some more thought go into what use cases are best served by UniqueRepresentation and what by UniqueFactory.  But the code is well documented, does what it claims to do, and UniqueRepresentation is easier to use than UniqueFactory.  So positive review.",
    "created_at": "2009-05-19T07:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39150",
    "user": "roed"
}
```

I'd like to see some more thought go into what use cases are best served by UniqueRepresentation and what by UniqueFactory.  But the code is well documented, does what it claims to do, and UniqueRepresentation is easier to use than UniqueFactory.  So positive review.



---

archive/issue_comments_039151.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T00:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39151",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_039152.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T00:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5120#issuecomment-39152",
    "user": "mabshoff"
}
```

Resolution: fixed
