# Issue 6538: bug in Partitions

archive/issues_006538.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  brunellus\n\nKeywords: partitions\n\nLooks like there is a bug in Partitions.  Partitions(n, max_slope=-1)  should give the partitions of n with distinct parts, right?\n\n```\nsage: Partitions(2, max_slope=-1).list()\n[[2]]\nsage: Partitions(4, max_slope=-1).list()\n[[4], [3, 1]]\n```\n\nBut if you add the \"length\" keyword, it doesn't work anymore, at least not completely:\n\n```\nsage: Partitions(2, max_slope=-1, length=2).list()  # doesn't work\n[[1, 1]]\nsage: Partitions(4, max_slope=-1, length=2).list()  # works\n[[3, 1]]\nsage: Partitions(4, max_slope=-1, length=3).list()  # doesn't work\n[[2, 1, 1]]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6538\n\n",
    "created_at": "2009-07-15T18:55:17Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.3",
    "title": "bug in Partitions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6538",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @mwhansen

CC:  brunellus

Keywords: partitions

Looks like there is a bug in Partitions.  Partitions(n, max_slope=-1)  should give the partitions of n with distinct parts, right?

```
sage: Partitions(2, max_slope=-1).list()
[[2]]
sage: Partitions(4, max_slope=-1).list()
[[4], [3, 1]]
```

But if you add the "length" keyword, it doesn't work anymore, at least not completely:

```
sage: Partitions(2, max_slope=-1, length=2).list()  # doesn't work
[[1, 1]]
sage: Partitions(4, max_slope=-1, length=2).list()  # works
[[3, 1]]
sage: Partitions(4, max_slope=-1, length=3).list()  # doesn't work
[[2, 1, 1]]
```


Issue created by migration from https://trac.sagemath.org/ticket/6538





---

archive/issue_comments_053189.json:
```json
{
    "body": "Fixed by making changes to IntergerListLex and not increasing algorithm's complexity. Fixed some other bugs in IntegerListLex and Partitions when bad input is given.\n\nNote: most of the work on this patch was done during Sage Days 38.",
    "created_at": "2012-05-16T04:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53189",
    "user": "https://github.com/tscrim"
}
```

Fixed by making changes to IntergerListLex and not increasing algorithm's complexity. Fixed some other bugs in IntegerListLex and Partitions when bad input is given.

Note: most of the work on this patch was done during Sage Days 38.



---

archive/issue_comments_053190.json:
```json
{
    "body": "Changing keywords from \"partitions\" to \"partitions, days38\".",
    "created_at": "2012-05-16T04:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53190",
    "user": "https://github.com/tscrim"
}
```

Changing keywords from "partitions" to "partitions, days38".



---

archive/issue_comments_053191.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-16T04:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53191",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053192.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-05T14:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53192",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053193.json:
```json
{
    "body": "The code you've written looks good. I think you should also add a few doctests in EXAMPLES or TESTS where appropriate to demonstrate that the issue in this ticket it resolved.",
    "created_at": "2012-06-05T14:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53193",
    "user": "https://github.com/benjaminfjones"
}
```

The code you've written looks good. I think you should also add a few doctests in EXAMPLES or TESTS where appropriate to demonstrate that the issue in this ticket it resolved.



---

archive/issue_comments_053194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-27T03:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53194",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053195.json:
```json
{
    "body": "Doctests have been added.\n\nThanks for reviewing.",
    "created_at": "2012-06-27T03:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53195",
    "user": "https://github.com/tscrim"
}
```

Doctests have been added.

Thanks for reviewing.



---

archive/issue_comments_053196.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-27T19:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53196",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053197.json:
```json
{
    "body": "Changes look good and thanks for adding the doctests. You done some nice code cleanup too, which is great. Positive review pending `make ptestlong`.",
    "created_at": "2012-06-27T19:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53197",
    "user": "https://github.com/benjaminfjones"
}
```

Changes look good and thanks for adding the doctests. You done some nice code cleanup too, which is great. Positive review pending `make ptestlong`.



---

archive/issue_comments_053198.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-07-02T20:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53198",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_053199.json:
```json
{
    "body": "It fails a doctest:\n\n```\nsage -t  -force_lib devel/sage/sage/combinat/integer_vector.py\n**********************************************************************\nFile \"/release/merger/sage-5.2.beta1/devel/sage-main/sage/combinat/integer_vector.py\", line 988:\n    sage: IntegerVectors(3, 0, min_part=1).list()\nExpected:\n    []\nGot:\n    [[3]]\n**********************************************************************\n```\n\nIt also fails a test added by #12925:\n\n```\nsage -t  -force_lib devel/sage/sage/combinat/tutorial.py\n**********************************************************************\nFile \"/release/merger/sage-5.2.beta1/devel/sage-main/sage/combinat/tutorial.py\", line 1635:\n    sage: Partitions(2, max_slope=-1, length=2).list()\nExpected:\n    [[1, 1]]\nGot:\n    []\n**********************************************************************\n```\n",
    "created_at": "2012-07-02T20:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53199",
    "user": "https://github.com/jdemeyer"
}
```

It fails a doctest:

```
sage -t  -force_lib devel/sage/sage/combinat/integer_vector.py
**********************************************************************
File "/release/merger/sage-5.2.beta1/devel/sage-main/sage/combinat/integer_vector.py", line 988:
    sage: IntegerVectors(3, 0, min_part=1).list()
Expected:
    []
Got:
    [[3]]
**********************************************************************
```

It also fails a test added by #12925:

```
sage -t  -force_lib devel/sage/sage/combinat/tutorial.py
**********************************************************************
File "/release/merger/sage-5.2.beta1/devel/sage-main/sage/combinat/tutorial.py", line 1635:
    sage: Partitions(2, max_slope=-1, length=2).list()
Expected:
    [[1, 1]]
Got:
    []
**********************************************************************
```




---

archive/issue_comments_053200.json:
```json
{
    "body": "It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)",
    "created_at": "2012-07-11T11:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53200",
    "user": "https://github.com/tscrim"
}
```

It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)



---

archive/issue_comments_053201.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-11T11:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53201",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053202.json:
```json
{
    "body": "Replying to [comment:8 tscrim]:\n> It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)\nI have reopened that ticket, so they can fix their test.",
    "created_at": "2012-07-11T11:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53202",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:8 tscrim]:
> It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)
I have reopened that ticket, so they can fix their test.



---

archive/issue_comments_053203.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> Replying to [comment:8 tscrim]:\n> > It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)\n> I have reopened that ticket, so they can fix their test.\n\nHave you read the text just above that doctest? It is precisely *documenting* this bug.\n\nSo, I am glad that you fixed that bug, but this ticket #6538 is responsible for updating the tutorial accordingly. Please merge back #12925! It's been delayed long enough.",
    "created_at": "2012-07-11T14:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53203",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 tscrim]:
> > It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)
> I have reopened that ticket, so they can fix their test.

Have you read the text just above that doctest? It is precisely *documenting* this bug.

So, I am glad that you fixed that bug, but this ticket #6538 is responsible for updating the tutorial accordingly. Please merge back #12925! It's been delayed long enough.



---

archive/issue_comments_053204.json:
```json
{
    "body": "Replying to [comment:10 nthiery]:\n> Replying to [comment:9 jdemeyer]:\n> > Replying to [comment:8 tscrim]:\n> > > It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)\n> > I have reopened that ticket, so they can fix their test.\n> \n> Have you read the text just above that doctest? It is precisely *documenting* this bug.\n> \n> So, I am glad that you fixed that bug, but this ticket #6538 is responsible for updating the tutorial accordingly. Please merge back #12925! It's been delayed long enough.\n\nTutorial updated accordingly.",
    "created_at": "2012-07-13T10:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53204",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:10 nthiery]:
> Replying to [comment:9 jdemeyer]:
> > Replying to [comment:8 tscrim]:
> > > It now passes the test for integer_vector.py, however the test in #12925 is incorrect since the partition [1, 1] has a slope 0 > -1. (Or am I now responsible for correcting this because #12925 has been closed?)
> > I have reopened that ticket, so they can fix their test.
> 
> Have you read the text just above that doctest? It is precisely *documenting* this bug.
> 
> So, I am glad that you fixed that bug, but this ticket #6538 is responsible for updating the tutorial accordingly. Please merge back #12925! It's been delayed long enough.

Tutorial updated accordingly.



---

archive/issue_comments_053205.json:
```json
{
    "body": "> Tutorial updated accordingly.\n\nThanks! I am fine with this change.\n\nStill, I am pretty sure that the underlying engine is still broken; if you can come up with an example illustrating that, please add it there!\n\nThanks,\n                           Nicolas",
    "created_at": "2012-07-13T18:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53205",
    "user": "https://github.com/nthiery"
}
```

> Tutorial updated accordingly.

Thanks! I am fine with this change.

Still, I am pretty sure that the underlying engine is still broken; if you can come up with an example illustrating that, please add it there!

Thanks,
                           Nicolas



---

archive/issue_comments_053206.json:
```json
{
    "body": "Nicolas: it's not clear whether your comment should be interpreted as positive_review or needs_work?  Could you change the ticket status to either of these two?",
    "created_at": "2012-08-08T13:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53206",
    "user": "https://github.com/jdemeyer"
}
```

Nicolas: it's not clear whether your comment should be interpreted as positive_review or needs_work?  Could you change the ticket status to either of these two?



---

archive/issue_comments_053207.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n\n> Nicolas: it's not clear whether your comment should be interpreted as positive_review or needs_work?  Could you change the ticket status to either of these two?\n\nSorry if I was unclear. Travis: I leave that decision to you. If you have an example, please add it. Otherwise you can put a positive review under hand.\n\nCheers,",
    "created_at": "2012-08-08T13:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53207",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:13 jdemeyer]:

> Nicolas: it's not clear whether your comment should be interpreted as positive_review or needs_work?  Could you change the ticket status to either of these two?

Sorry if I was unclear. Travis: I leave that decision to you. If you have an example, please add it. Otherwise you can put a positive review under hand.

Cheers,



---

archive/issue_comments_053208.json:
```json
{
    "body": "I can't find an example right now. I've tried with max_slope, min_slope, inner, outer, max_length, min_length, and multiple combinations of them and could not get any wrong results.",
    "created_at": "2012-08-08T20:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53208",
    "user": "https://github.com/tscrim"
}
```

I can't find an example right now. I've tried with max_slope, min_slope, inner, outer, max_length, min_length, and multiple combinations of them and could not get any wrong results.



---

archive/issue_comments_053209.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-08T20:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53209",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053210.json:
```json
{
    "body": "Attachment [trac_6538-partitions_max_slope-ts.patch](tarball://root/attachments/some-uuid/ticket6538/trac_6538-partitions_max_slope-ts.patch) by @jdemeyer created at 2012-08-13 10:09:55\n\nRebased to sage-5.3.beta1",
    "created_at": "2012-08-13T10:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53210",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_6538-partitions_max_slope-ts.patch](tarball://root/attachments/some-uuid/ticket6538/trac_6538-partitions_max_slope-ts.patch) by @jdemeyer created at 2012-08-13 10:09:55

Rebased to sage-5.3.beta1



---

archive/issue_comments_053211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-14T07:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53211",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_006774.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-08-14T07:02:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6538#event-6774"
}
```



---

archive/issue_comments_053212.json:
```json
{
    "body": "If you're still looking for something that gives the wrong answer, use `parts_in`:\n\n```\nsage: [len(p) for p in Partitions(10, length=6, parts_in=[1,2])]\n[5, 6, 7, 8, 9, 10]\nsage: Partitions(10, parts_in=[1,2]).cardinality() == Partitions(10, length=6, parts_in=[1,2]).cardinality()\nTrue\n```\n\nAnother ticket?\n\nEdit: I guess this is #12278.)",
    "created_at": "2012-08-29T17:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53212",
    "user": "https://github.com/jhpalmieri"
}
```

If you're still looking for something that gives the wrong answer, use `parts_in`:

```
sage: [len(p) for p in Partitions(10, length=6, parts_in=[1,2])]
[5, 6, 7, 8, 9, 10]
sage: Partitions(10, parts_in=[1,2]).cardinality() == Partitions(10, length=6, parts_in=[1,2]).cardinality()
True
```

Another ticket?

Edit: I guess this is #12278.)



---

archive/issue_comments_053213.json:
```json
{
    "body": "Replying to [comment:17 jhpalmieri]:\n> If you're still looking for something that gives the wrong answer, use `parts_in`:\n> {{{\n> sage: [len(p) for p in Partitions(10, length=6, parts_in=[1,2])]\n> [5, 6, 7, 8, 9, 10]\n> sage: Partitions(10, parts_in=[1,2]).cardinality() == Partitions(10, length=6, parts_in=[1,2]).cardinality()\n> True\n> }}}\n> Another ticket?\n> \n> Edit: I guess this is #12278.)\n\nYup: I copy pasted this example as a comment in #12278!\n\nHowever, I was looking for an example giving wrong results while only using the IntegerListsLex engine (i.e. without parts_in). Thanks though :-)",
    "created_at": "2012-08-31T06:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6538#issuecomment-53213",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:17 jhpalmieri]:
> If you're still looking for something that gives the wrong answer, use `parts_in`:
> {{{
> sage: [len(p) for p in Partitions(10, length=6, parts_in=[1,2])]
> [5, 6, 7, 8, 9, 10]
> sage: Partitions(10, parts_in=[1,2]).cardinality() == Partitions(10, length=6, parts_in=[1,2]).cardinality()
> True
> }}}
> Another ticket?
> 
> Edit: I guess this is #12278.)

Yup: I copy pasted this example as a comment in #12278!

However, I was looking for an example giving wrong results while only using the IntegerListsLex engine (i.e. without parts_in). Thanks though :-)
