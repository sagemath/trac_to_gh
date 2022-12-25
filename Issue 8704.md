# Issue 8704: Improve the _repr_ of IntegerRange

archive/issues_008704.json:
```json
{
    "body": "Assignee: @hivert\n\nThe actual printing in in discussion on [this thread](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/5ff945e9d813392c) of sage-combinat-devel. I'll implement it as soon as the decision is made.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8704\n\n",
    "created_at": "2010-04-17T09:53:05Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Improve the _repr_ of IntegerRange",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8704",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

The actual printing in in discussion on [this thread](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/5ff945e9d813392c) of sage-combinat-devel. I'll implement it as soon as the decision is made.

Issue created by migration from https://trac.sagemath.org/ticket/8704





---

archive/issue_comments_079265.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-13T17:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79265",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079266.json:
```json
{
    "body": "Changing keywords from \"\" to \"integer range\".",
    "created_at": "2010-05-13T17:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79266",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "" to "integer range".



---

archive/issue_comments_079267.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-05-13T17:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79267",
    "user": "https://github.com/hivert"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_079268.json:
```json
{
    "body": "I fixed a doctest failure... All tests should pass now.",
    "created_at": "2010-05-15T17:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79268",
    "user": "https://github.com/hivert"
}
```

I fixed a doctest failure... All tests should pass now.



---

archive/issue_comments_079269.json:
```json
{
    "body": "I fixed the following issues raised by Nicolas on sage-combinat-devel\n\n```\n> >> The output of IntegerRange is much nicer now. I was about to put a\n> >> positive review, when I had a last doubt about the consistency between:\n> >>\n> >>      sage: I = IntegerRange(2,100,5); I\n> >>      {2, 7 .. 97}\n> >>      sage: I = IntegerRange(54,Infinity,3); I\n> >>      {54, 57, ..}\n> >>\n> >> Should there be a comma in both cases, in none, or is it good as is?\n> >\n> > I would say {2, 7 .. 97} should be replaced by {2, 7, .., 97} for\n> > consistency.\n```\n",
    "created_at": "2010-05-31T21:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79269",
    "user": "https://github.com/hivert"
}
```

I fixed the following issues raised by Nicolas on sage-combinat-devel

```
> >> The output of IntegerRange is much nicer now. I was about to put a
> >> positive review, when I had a last doubt about the consistency between:
> >>
> >>      sage: I = IntegerRange(2,100,5); I
> >>      {2, 7 .. 97}
> >>      sage: I = IntegerRange(54,Infinity,3); I
> >>      {54, 57, ..}
> >>
> >> Should there be a comma in both cases, in none, or is it good as is?
> >
> > I would say {2, 7 .. 97} should be replaced by {2, 7, .., 97} for
> > consistency.
```




---

archive/issue_comments_079270.json:
```json
{
    "body": "Attachment [trac_8704-integer_range_print-fh.patch](tarball://root/attachments/some-uuid/ticket8704/trac_8704-integer_range_print-fh.patch) by @hivert created at 2010-05-31 21:51:51",
    "created_at": "2010-05-31T21:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79270",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8704-integer_range_print-fh.patch](tarball://root/attachments/some-uuid/ticket8704/trac_8704-integer_range_print-fh.patch) by @hivert created at 2010-05-31 21:51:51



---

archive/issue_comments_079271.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-06T08:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79271",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079272.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-06T08:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79272",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_008874.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-06T08:35:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8704#event-8874"
}
```



---

archive/issue_comments_079273.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T08:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8704#issuecomment-79273",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
