# Issue 3783: cached_method could use some improvements

archive/issues_003783.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @ncalexan simonking\n\nThe cached_method decorator from #3781 could use some improvements:\n\n\n```\n<mhansen> Does anyone feel up for reviewing #3781 for me?\n<ncalexan> I'll look at it, one moment.  I've wanted this for a while.\n<mhansen> Awesome.  It doesn't work on C extension types though since they don't have a __dict__.  This could be done by storing the cache in the decorator object with a weakref though.\n<ncalexan> The problem is much more complicated than this.\n<ncalexan> Okay, there are other problems too, like un-hashable arguments will break it.\n<mhansen> Yep\n<ncalexan> And there is no way to clear the cache...\n<ncalexan> And the tests don't actually demonstrate that the cache is workin.\n<ncalexan> (One could touch the cache with an incorrect answer, then verify it is \"correctly\" returning that value)\n<ncalexan> For what it is, though, it's fine.  It will hurt nothing -- shall I review positive?\n<mhansen> If you could, that'd be great.  I do know it's limitations, but there are some big patches going in that depend on it.  I'll make a ticket with your comments for improvement.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3783\n\n",
    "created_at": "2008-08-06T23:31:20Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cached_method could use some improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3783",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  @ncalexan simonking

The cached_method decorator from #3781 could use some improvements:


```
<mhansen> Does anyone feel up for reviewing #3781 for me?
<ncalexan> I'll look at it, one moment.  I've wanted this for a while.
<mhansen> Awesome.  It doesn't work on C extension types though since they don't have a __dict__.  This could be done by storing the cache in the decorator object with a weakref though.
<ncalexan> The problem is much more complicated than this.
<ncalexan> Okay, there are other problems too, like un-hashable arguments will break it.
<mhansen> Yep
<ncalexan> And there is no way to clear the cache...
<ncalexan> And the tests don't actually demonstrate that the cache is workin.
<ncalexan> (One could touch the cache with an incorrect answer, then verify it is "correctly" returning that value)
<ncalexan> For what it is, though, it's fine.  It will hurt nothing -- shall I review positive?
<mhansen> If you could, that'd be great.  I do know it's limitations, but there are some big patches going in that depend on it.  I'll make a ticket with your comments for improvement.
```


Issue created by migration from https://trac.sagemath.org/ticket/3783





---

archive/issue_comments_026833.json:
```json
{
    "body": "The description isn't very clear. What exactly is requested? What part of it isn't fixed yet?",
    "created_at": "2012-06-25T09:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3783#issuecomment-26833",
    "user": "https://github.com/simon-king-jena"
}
```

The description isn't very clear. What exactly is requested? What part of it isn't fixed yet?



---

archive/issue_comments_026834.json:
```json
{
    "body": "Have all the issues mentioned in the description been fixed?",
    "created_at": "2015-04-13T16:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3783#issuecomment-26834",
    "user": "https://github.com/mezzarobba"
}
```

Have all the issues mentioned in the description been fixed?



---

archive/issue_comments_026835.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T16:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3783#issuecomment-26835",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026836.json:
```json
{
    "body": "Replying to [comment:8 mmezzarobba]:\n> Have all the issues mentioned in the description been fixed?\n\n- It does work on C extension types, provided they inherit from `Parent`.\n- If I am not mistaken, it is now possible to define a function that does some preprocessing on the key. Thus, unhashable arguments should be fine, but certainly not out of the box.\n- There is a way to clear the cache. It is a method of the cached method.\n- I think the tests do demonstrate that the cache is working.",
    "created_at": "2015-04-13T18:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3783#issuecomment-26836",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:8 mmezzarobba]:
> Have all the issues mentioned in the description been fixed?

- It does work on C extension types, provided they inherit from `Parent`.
- If I am not mistaken, it is now possible to define a function that does some preprocessing on the key. Thus, unhashable arguments should be fine, but certainly not out of the box.
- There is a way to clear the cache. It is a method of the cached method.
- I think the tests do demonstrate that the cache is working.



---

archive/issue_comments_026837.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-24T21:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3783#issuecomment-26837",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026838.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-26T01:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3783#issuecomment-26838",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_004005.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-26T01:45:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3783#event-4005"
}
```
