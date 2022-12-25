# Issue 7563: Interval Graphs : recognition and interval representation

archive/issues_007563.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @dimpase mvngu @rlmill @wdjoyner @jasongrout\n\nRecognition of interval graphs and representation of a given graph as a list of intervals\n\nIssue created by migration from https://trac.sagemath.org/ticket/7563\n\n",
    "created_at": "2009-11-30T18:18:46Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Interval Graphs : recognition and interval representation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7563",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  @dimpase mvngu @rlmill @wdjoyner @jasongrout

Recognition of interval graphs and representation of a given graph as a list of intervals

Issue created by migration from https://trac.sagemath.org/ticket/7563





---

archive/issue_comments_064236.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64236",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_064237.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-12T15:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64237",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064238.json:
```json
{
    "body": "Oh yes, and... There are many missing doctests, but as this algorithm heavily uses dictionaries I wondered whether this could be done without being platform-dependent ^^;\n\nAny idea welcome, here too.. Even though those functions will never be needed directly by the users, and all of them are indirectly tested anyway through the docstrings of is_interval.\n\nNathann",
    "created_at": "2010-06-12T15:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64238",
    "user": "https://github.com/nathanncohen"
}
```

Oh yes, and... There are many missing doctests, but as this algorithm heavily uses dictionaries I wondered whether this could be done without being platform-dependent ^^;

Any idea welcome, here too.. Even though those functions will never be needed directly by the users, and all of them are indirectly tested anyway through the docstrings of is_interval.

Nathann



---

archive/issue_comments_064239.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Oh yes, and... There are many missing doctests\n\nOuch.  That's a problem.  I don't think the ticket should go into Sage without doctests on each python function.\n\n(I haven't had time to look at the rest of the patch, though.)",
    "created_at": "2010-06-12T17:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64239",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:3 ncohen]:
> Oh yes, and... There are many missing doctests

Ouch.  That's a problem.  I don't think the ticket should go into Sage without doctests on each python function.

(I haven't had time to look at the rest of the patch, though.)



---

archive/issue_comments_064240.json:
```json
{
    "body": "\"Your wish is my command\" :-)\n\nNathann",
    "created_at": "2010-06-12T20:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64240",
    "user": "https://github.com/nathanncohen"
}
```

"Your wish is my command" :-)

Nathann



---

archive/issue_comments_064241.json:
```json
{
    "body": "Attachment [trac_7563.patch](tarball://root/attachments/some-uuid/ticket7563/trac_7563.patch) by @nathanncohen created at 2010-06-12 20:45:06",
    "created_at": "2010-06-12T20:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64241",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7563.patch](tarball://root/attachments/some-uuid/ticket7563/trac_7563.patch) by @nathanncohen created at 2010-06-12 20:45:06



---

archive/issue_comments_064242.json:
```json
{
    "body": "Applies after #8284 and passes all its tests :). Coverage looks much better.",
    "created_at": "2010-06-18T23:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64242",
    "user": "https://github.com/rlmill"
}
```

Applies after #8284 and passes all its tests :). Coverage looks much better.



---

archive/issue_comments_064243.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T23:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64243",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017933.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-29T16:43:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7563#event-17933"
}
```



---

archive/issue_comments_064244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7563#issuecomment-64244",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
