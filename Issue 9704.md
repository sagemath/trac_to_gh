# Issue 9704: refactor "trace" -- make trace command call trace method on input if available

archive/issues_009704.json:
```json
{
    "body": "Assignee: jason\n\nThis is confusing.  Refactor to fix it:\n\n\n```\nsage: det(matrix(2,[1,2,3,4]))\n-2\nsage: trace(matrix(2,[1,2,3,4]))\nTraceback (most recent call last)\n...\nAttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_dense' object has no attribute 'lstrip'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9704\n\n",
    "created_at": "2010-08-07T17:31:41Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "refactor \"trace\" -- make trace command call trace method on input if available",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9704",
    "user": "was"
}
```
Assignee: jason

This is confusing.  Refactor to fix it:


```
sage: det(matrix(2,[1,2,3,4]))
-2
sage: trace(matrix(2,[1,2,3,4]))
Traceback (most recent call last)
...
AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_dense' object has no attribute 'lstrip'
```


Issue created by migration from https://trac.sagemath.org/ticket/9704





---

archive/issue_comments_094396.json:
```json
{
    "body": "Attachment [trac_9704-trace.patch](tarball://root/attachments/some-uuid/ticket9704/trac_9704-trace.patch) by was created at 2010-08-07 17:43:27",
    "created_at": "2010-08-07T17:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94396",
    "user": "was"
}
```

Attachment [trac_9704-trace.patch](tarball://root/attachments/some-uuid/ticket9704/trac_9704-trace.patch) by was created at 2010-08-07 17:43:27



---

archive/issue_comments_094397.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-07T17:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94397",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094398.json:
```json
{
    "body": "-1 on this idea.  This means that \"trace\" means *completely* different things depending on the input.  Instead, we ought to decide what \"trace\" means and make two functions.  I think trace(x) should be x.trace (and give a mathematical meaning), and the current trace should be code_trace or trace_execution or something like that.",
    "created_at": "2010-08-07T17:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94398",
    "user": "jason"
}
```

-1 on this idea.  This means that "trace" means *completely* different things depending on the input.  Instead, we ought to decide what "trace" means and make two functions.  I think trace(x) should be x.trace (and give a mathematical meaning), and the current trace should be code_trace or trace_execution or something like that.



---

archive/issue_comments_094399.json:
```json
{
    "body": "I would just say leave it like it is except to add a deprecation warning to use \"trace_execution\" in the string case.  That way we get something that is backward compatible.",
    "created_at": "2010-08-07T18:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94399",
    "user": "mhansen"
}
```

I would just say leave it like it is except to add a deprecation warning to use "trace_execution" in the string case.  That way we get something that is backward compatible.



---

archive/issue_comments_094400.json:
```json
{
    "body": "* jason -- trace already means two different things, at least.   I'm not adding a new meaning. \n\n* regarding adding a deprecation warning, I think that is reasonable, but that should not go in this ticket.  If you want to do that, make it another ticket and do it.",
    "created_at": "2010-08-07T19:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94400",
    "user": "was"
}
```

* jason -- trace already means two different things, at least.   I'm not adding a new meaning. 

* regarding adding a deprecation warning, I think that is reasonable, but that should not go in this ticket.  If you want to do that, make it another ticket and do it.



---

archive/issue_comments_094401.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> * jason -- trace already means two different things, at least.   I'm not adding a new meaning. \n\nWhen I read the code, trace() has one purpose, not two.  Your patch will mean that the trace function has two completely different purposes, depending on the input.  That is what I'm -1 on.\n\nIf we change the trace() function so that it instead computes the trace of an object (i.e., x.trace()), then I agree that for a short amount of time, a deprecation warning should be added and trace() will have to serve two purposes.\n\n\n> \n> * regarding adding a deprecation warning, I think that is reasonable, but that should not go in this ticket.  If you want to do that, make it another ticket and do it. \n\nI'm -1 on a ticket (this one) which makes the Sage trace() function have two purposes (unless it's a temporary thing that is deprecated, of course).",
    "created_at": "2010-08-07T19:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94401",
    "user": "jason"
}
```

Replying to [comment:4 was]:
> * jason -- trace already means two different things, at least.   I'm not adding a new meaning. 

When I read the code, trace() has one purpose, not two.  Your patch will mean that the trace function has two completely different purposes, depending on the input.  That is what I'm -1 on.

If we change the trace() function so that it instead computes the trace of an object (i.e., x.trace()), then I agree that for a short amount of time, a deprecation warning should be added and trace() will have to serve two purposes.


> 
> * regarding adding a deprecation warning, I think that is reasonable, but that should not go in this ticket.  If you want to do that, make it another ticket and do it. 

I'm -1 on a ticket (this one) which makes the Sage trace() function have two purposes (unless it's a temporary thing that is deprecated, of course).



---

archive/issue_comments_094402.json:
```json
{
    "body": "Sage already has _lots_ of functions f() which do very different things depending on the type of the arguments.\n\nHow about making the trace(x) function do what others do, which is to try returning x.trace() and if that fails do what the code_trace function does?",
    "created_at": "2010-08-11T15:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94402",
    "user": "cremona"
}
```

Sage already has _lots_ of functions f() which do very different things depending on the type of the arguments.

How about making the trace(x) function do what others do, which is to try returning x.trace() and if that fails do what the code_trace function does?



---

archive/issue_comments_094403.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> Sage already has _lots_ of functions f() which do very different things depending on the type of the arguments.\n> \n> How about making the trace(x) function do what others do, which is to try returning x.trace() and if that fails do what the code_trace function does?\n\nIs there any other examples in Sage where a function does:\n\n* mathematically meaningful stuff (which may differ, depending on the mathematical object), and returns a mathematical answer\n* and also does something which is entirely non-mathematical, on a completely different level (a programming nuts-and-bolts debugging level, rather than a math level)?\n\nThe big conceptual difference between those two purposes is why I think having two functions, say `trace()` (which calls `x.trace()`) and `trace_execution()` (which does what trace does right now) is a much better design than lumping things into one function.",
    "created_at": "2010-08-12T03:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94403",
    "user": "jason"
}
```

Replying to [comment:6 cremona]:
> Sage already has _lots_ of functions f() which do very different things depending on the type of the arguments.
> 
> How about making the trace(x) function do what others do, which is to try returning x.trace() and if that fails do what the code_trace function does?

Is there any other examples in Sage where a function does:

* mathematically meaningful stuff (which may differ, depending on the mathematical object), and returns a mathematical answer
* and also does something which is entirely non-mathematical, on a completely different level (a programming nuts-and-bolts debugging level, rather than a math level)?

The big conceptual difference between those two purposes is why I think having two functions, say `trace()` (which calls `x.trace()`) and `trace_execution()` (which does what trace does right now) is a much better design than lumping things into one function.



---

archive/issue_comments_094404.json:
```json
{
    "body": "Look Jason, this \"trace\" having two meanings is *already* in Sage.  Whether or not that changes is orthogonal to this ticket.   You could post a patch *after* this ticket gets in later if you're really worried.\n\nEnglish has words with different meanings.  Sorry. It's just the way the language works.",
    "created_at": "2010-08-12T11:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94404",
    "user": "was"
}
```

Look Jason, this "trace" having two meanings is *already* in Sage.  Whether or not that changes is orthogonal to this ticket.   You could post a patch *after* this ticket gets in later if you're really worried.

English has words with different meanings.  Sorry. It's just the way the language works.



---

archive/issue_comments_094405.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> Look Jason, this \"trace\" having two meanings is *already* in Sage.  \n\nNo, it doesn't at the top level, and not in the same function.\n\n> Whether or not that changes is orthogonal to this ticket.   You could post a patch *after* this ticket gets in later if you're really worried.\n> \n\nI'm posting one right now.\n\n\n> English has words with different meanings.  Sorry. It's just the way the language works. \n\nSure, but that doesn't excuse a bad design.",
    "created_at": "2010-08-12T11:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94405",
    "user": "jason"
}
```

Replying to [comment:8 was]:
> Look Jason, this "trace" having two meanings is *already* in Sage.  

No, it doesn't at the top level, and not in the same function.

> Whether or not that changes is orthogonal to this ticket.   You could post a patch *after* this ticket gets in later if you're really worried.
> 

I'm posting one right now.


> English has words with different meanings.  Sorry. It's just the way the language works. 

Sure, but that doesn't excuse a bad design.



---

archive/issue_comments_094406.json:
```json
{
    "body": "My patch may cause some doctest somewhere to fail because of deprecation warnings.  I've tested the misc/*.py and matrix/*.py* files (and only got errors that should be from other patches on my stack).",
    "created_at": "2010-08-12T12:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94406",
    "user": "jason"
}
```

My patch may cause some doctest somewhere to fail because of deprecation warnings.  I've tested the misc/*.py and matrix/*.py* files (and only got errors that should be from other patches on my stack).



---

archive/issue_comments_094407.json:
```json
{
    "body": "apply instead of previous patch",
    "created_at": "2010-08-12T12:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94407",
    "user": "jason"
}
```

apply instead of previous patch



---

archive/issue_comments_094408.json:
```json
{
    "body": "Attachment [trac-9704-trace.patch](tarball://root/attachments/some-uuid/ticket9704/trac-9704-trace.patch) by klee created at 2010-08-14 04:22:53\n\nI incline to Jason's argument. I propose 'trace_through' as a more palpable name than Jason's 'trace_execution'.",
    "created_at": "2010-08-14T04:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94408",
    "user": "klee"
}
```

Attachment [trac-9704-trace.patch](tarball://root/attachments/some-uuid/ticket9704/trac-9704-trace.patch) by klee created at 2010-08-14 04:22:53

I incline to Jason's argument. I propose 'trace_through' as a more palpable name than Jason's 'trace_execution'.



---

archive/issue_comments_094409.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-11-11T13:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94409",
    "user": "rlm"
}
```

LGTM.



---

archive/issue_comments_094410.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-11T13:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94410",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094411.json:
```json
{
    "body": "Sorry, but the discussion at sage-devel yielded very few people in favour of this patch, so I'm not planning to merge it.",
    "created_at": "2010-11-15T15:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94411",
    "user": "jdemeyer"
}
```

Sorry, but the discussion at sage-devel yielded very few people in favour of this patch, so I'm not planning to merge it.



---

archive/issue_comments_094412.json:
```json
{
    "body": "Thanks for asking on sage-devel.  I'm still in favor of it, since (as a linear algebra person and a math teacher) I'd rather have trace have mathematical meaning instead of programming meaning, and it is a natural complement to having a top-level det function.  My vote wasn't counted on sage-devel yet, so add another +1.",
    "created_at": "2010-11-15T16:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94412",
    "user": "jason"
}
```

Thanks for asking on sage-devel.  I'm still in favor of it, since (as a linear algebra person and a math teacher) I'd rather have trace have mathematical meaning instead of programming meaning, and it is a natural complement to having a top-level det function.  My vote wasn't counted on sage-devel yet, so add another +1.



---

archive/issue_comments_094413.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-06-30T18:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94413",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094414.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-06-30T18:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94414",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_094415.json:
```json
{
    "body": "Since there seems to have been a vote that this patch should not be merged, I think we should close it as **wontfix**.",
    "created_at": "2012-06-30T18:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94415",
    "user": "vbraun"
}
```

Since there seems to have been a vote that this patch should not be merged, I think we should close it as **wontfix**.



---

archive/issue_comments_094416.json:
```json
{
    "body": "I think we should have another vote.  I was the major -1 vote, and I fixed the issues I had with it in my updated patch.\n\nI'll post to sage-devel one more time.  It's been a long time since this issue was raised.",
    "created_at": "2012-06-30T18:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94416",
    "user": "jason"
}
```

I think we should have another vote.  I was the major -1 vote, and I fixed the issues I had with it in my updated patch.

I'll post to sage-devel one more time.  It's been a long time since this issue was raised.



---

archive/issue_comments_094417.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-06-30T18:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94417",
    "user": "jason"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_094418.json:
```json
{
    "body": "I've posted to sage-devel again: https://groups.google.com/group/sage-devel/browse_thread/thread/61ca252973c4930f",
    "created_at": "2012-06-30T18:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94418",
    "user": "jason"
}
```

I've posted to sage-devel again: https://groups.google.com/group/sage-devel/browse_thread/thread/61ca252973c4930f



---

archive/issue_comments_094419.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-27T05:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94419",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_094420.json:
```json
{
    "body": "As not everyone is happy with refactoring `trace()` for dual purposes, we may add `tr()` for mathematical trace instead of `trace()`. Actually I guess that it is more frequent and convenient to think of `tr(m)` than `trace(m)` for a non-programmer mathematician. Also it nicely balances with `det(m)`",
    "created_at": "2016-04-27T05:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94420",
    "user": "klee"
}
```

As not everyone is happy with refactoring `trace()` for dual purposes, we may add `tr()` for mathematical trace instead of `trace()`. Actually I guess that it is more frequent and convenient to think of `tr(m)` than `trace(m)` for a non-programmer mathematician. Also it nicely balances with `det(m)`



---

archive/issue_comments_094421.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2016-04-27T05:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94421",
    "user": "klee"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_094422.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-11-06T18:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94422",
    "user": "klee"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094423.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-11-06T18:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94423",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_094424.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-11-06T18:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94424",
    "user": "klee"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094425.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2017-08-04T07:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94425",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_094426.json:
```json
{
    "body": "Previously I somehow ended up kidnapping this ticket, and uploaded a patch not for the original purpose of the ticket. I felt guilty, so now I recover the ticket for the original purpose. \n\nThe newly pushed branch only contains the code by Jason with slight changes. The code by Jason implements the idea discussed in https://groups.google.com/group/sage-devel/browse_thread/thread/61ca252973c4930f",
    "created_at": "2017-08-04T07:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94426",
    "user": "klee"
}
```

Previously I somehow ended up kidnapping this ticket, and uploaded a patch not for the original purpose of the ticket. I felt guilty, so now I recover the ticket for the original purpose. 

The newly pushed branch only contains the code by Jason with slight changes. The code by Jason implements the idea discussed in https://groups.google.com/group/sage-devel/browse_thread/thread/61ca252973c4930f



---

archive/issue_comments_094427.json:
```json
{
    "body": "does not apply",
    "created_at": "2018-03-11T17:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94427",
    "user": "chapoton"
}
```

does not apply



---

archive/issue_comments_094428.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2018-03-11T17:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94428",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094429.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-03-12T00:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94429",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_094430.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-03-13T00:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94430",
    "user": "klee"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094431.json:
```json
{
    "body": "It seems that there is no enough consensus in changing the meaning of `trace` command, which is now commonly used to trace code execution in Sage.\n\nAt least I myself prefer to use the methods `m.det()` and `m.trace()` than the functions `det(m)` or `trace(m)`. So I would rather remove the function `det` instead of introducing new `trace` function.\n\nHence I close this ticket as \"won't fix\".",
    "created_at": "2019-05-07T05:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9704#issuecomment-94431",
    "user": "klee"
}
```

It seems that there is no enough consensus in changing the meaning of `trace` command, which is now commonly used to trace code execution in Sage.

At least I myself prefer to use the methods `m.det()` and `m.trace()` than the functions `det(m)` or `trace(m)`. So I would rather remove the function `det` instead of introducing new `trace` function.

Hence I close this ticket as "won't fix".
