# Issue 9677: Sage Sets don't implement genuine comparison

archive/issues_009677.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @kini\n\nRight now there is either equals, or less than. If `a != b`, then we get `a < b` but not `b > a`:\n\n```\nsage: a = Set([1])\nsage: b = Set([])\nsage: a == b\nFalse\nsage: a < b\nTrue\nsage: b > a\nFalse\n```\n\nThis came up in\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/1c058efd05d3b91f\n\nIssue created by migration from https://trac.sagemath.org/ticket/9677\n\n",
    "created_at": "2010-08-03T20:41:08Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Sage Sets don't implement genuine comparison",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9677",
    "user": "https://github.com/rlmill"
}
```
Assignee: @aghitza

CC:  @kini

Right now there is either equals, or less than. If `a != b`, then we get `a < b` but not `b > a`:

```
sage: a = Set([1])
sage: b = Set([])
sage: a == b
False
sage: a < b
True
sage: b > a
False
```

This came up in

http://groups.google.com/group/sage-devel/browse_thread/thread/1c058efd05d3b91f

Issue created by migration from https://trac.sagemath.org/ticket/9677





---

archive/issue_comments_093910.json:
```json
{
    "body": "The noted behaviour is definitely a bug. However, the attached patch solves this by introducing an attempt at inducing a total ordering on Sets by sorting them first by cardinality and then by lexicographic ordering on the sorted list of set elements. This only works if the elements of the set have a total ordering implemented.\n\nWhile python used to try to have a total ordering on all objects, this has been abandoned (e.g. python complex numbers and python sets)\n\nShouldn't the sage design follow python in this respect? See also\n\nhttp://groups.google.ca/group/sage-devel/msg/eab3aafb319a2769",
    "created_at": "2010-08-04T02:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93910",
    "user": "https://github.com/nbruin"
}
```

The noted behaviour is definitely a bug. However, the attached patch solves this by introducing an attempt at inducing a total ordering on Sets by sorting them first by cardinality and then by lexicographic ordering on the sorted list of set elements. This only works if the elements of the set have a total ordering implemented.

While python used to try to have a total ordering on all objects, this has been abandoned (e.g. python complex numbers and python sets)

Shouldn't the sage design follow python in this respect? See also

http://groups.google.ca/group/sage-devel/msg/eab3aafb319a2769



---

archive/issue_comments_093911.json:
```json
{
    "body": "I completely, emphatically disagree. I think that total orderings are very important to try to preserve wherever possible, especially in this case.",
    "created_at": "2010-08-04T11:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93911",
    "user": "https://github.com/rlmill"
}
```

I completely, emphatically disagree. I think that total orderings are very important to try to preserve wherever possible, especially in this case.



---

archive/issue_comments_093912.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n> I completely, emphatically disagree. I think that total orderings are very important to try to preserve wherever possible, especially in this case.\n\n\nSee also my comments on the thread referenced above.",
    "created_at": "2010-08-04T11:24:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93912",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:2 rlm]:
> I completely, emphatically disagree. I think that total orderings are very important to try to preserve wherever possible, especially in this case.


See also my comments on the thread referenced above.



---

archive/issue_comments_093913.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-04T12:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93913",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093914.json:
```json
{
    "body": "I don't understand why you have these lines:\n\n```\n            if len_self != len_other: \n\t                return cmp(len_self, len_other) \n```\nthat just makes it so that the comparison is incompatible with what it is for lists.  Why not just make it the same?",
    "created_at": "2010-08-04T17:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93914",
    "user": "https://github.com/williamstein"
}
```

I don't understand why you have these lines:

```
            if len_self != len_other: 
	                return cmp(len_self, len_other) 
```
that just makes it so that the comparison is incompatible with what it is for lists.  Why not just make it the same?



---

archive/issue_comments_093915.json:
```json
{
    "body": "You mean just remove those lines? That's fine with me. This was just meant to be an optimization.",
    "created_at": "2010-08-04T18:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93915",
    "user": "https://github.com/rlmill"
}
```

You mean just remove those lines? That's fine with me. This was just meant to be an optimization.



---

archive/issue_comments_093916.json:
```json
{
    "body": "Patch is updated.",
    "created_at": "2010-08-04T18:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93916",
    "user": "https://github.com/rlmill"
}
```

Patch is updated.



---

archive/issue_comments_093917.json:
```json
{
    "body": "I guess you didn't test your patch?\nI just applied it and ran tests on sage.math, and got:\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n        sage -t  devel/sage/sage/graphs/graph_generators.py # 2 doctests failed\n        sage -t  devel/sage/sage/graphs/digraph.py # 2 doctests failed\n        sage -t  devel/sage/sage/combinat/sf/powersum.py # 0 doctests failed\n        sage -t  devel/sage/sage/graphs/graph.py # Time out\n----------------------------------------------------------------------\nTimings have been updated.\nTotal time for all tests: 488.9 seconds\n```",
    "created_at": "2010-08-05T03:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93917",
    "user": "https://github.com/williamstein"
}
```

I guess you didn't test your patch?
I just applied it and ran tests on sage.math, and got:

```
----------------------------------------------------------------------
The following tests failed:

        sage -t  devel/sage/sage/graphs/graph_generators.py # 2 doctests failed
        sage -t  devel/sage/sage/graphs/digraph.py # 2 doctests failed
        sage -t  devel/sage/sage/combinat/sf/powersum.py # 0 doctests failed
        sage -t  devel/sage/sage/graphs/graph.py # Time out
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 488.9 seconds
```



---

archive/issue_comments_093918.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-05T03:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93918",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093919.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-12-18T16:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93919",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093920.json:
```json
{
    "body": "Attachment [trac_9677.patch](tarball://root/attachments/some-uuid/ticket9677/trac_9677.patch) by @mwhansen created at 2011-12-18 16:09:49\n\nI rebased the patch and ran the tests which do pass.  I think we can give this positive review.",
    "created_at": "2011-12-18T16:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93920",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_9677.patch](tarball://root/attachments/some-uuid/ticket9677/trac_9677.patch) by @mwhansen created at 2011-12-18 16:09:49

I rebased the patch and ran the tests which do pass.  I think we can give this positive review.



---

archive/issue_comments_093921.json:
```json
{
    "body": "I think the patch behaviour of\n\n```\n\nsage: a = [2,3]\nsage: b = [2,3,4j]\nsage: set(a) < set(b)\nTrue\nsage: Set(a) < Set(b)\nFalse\n\n```\n\nis too dangerous to let pass unremarked.",
    "created_at": "2011-12-18T20:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93921",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

I think the patch behaviour of

```

sage: a = [2,3]
sage: b = [2,3,4j]
sage: set(a) < set(b)
True
sage: Set(a) < Set(b)
False

```

is too dangerous to let pass unremarked.



---

archive/issue_comments_093922.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-12-18T20:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93922",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093923.json:
```json
{
    "body": "Replying to [comment:11 dsm]:\n> I think the patch behaviour of\n> \n> \n> ```\n> \n> sage: a = [2,3]\n> sage: b = [2,3,4j]\n> sage: set(a) < set(b)\n> True\n> sage: Set(a) < Set(b)\n> False\n> \n> ```\n> \n> is too dangerous to let pass unremarked.\n\n\nIn Python (according to http://docs.python.org/library/sets.html) for the set type we have: \"The subset and equality comparisons do not generalize to a complete ordering function. For example, any two disjoint sets are not equal and are not subsets of each other, so all of the following return False: a<b, a==b, or a>b. Accordingly, sets do not implement the __cmp__() method.\"\n\nThe Python convention does make sense and is what most people would expect... and is the direction Sage should move in.\n\nRLM who wrote \"I completely, emphatically disagree.\" has got sucked up into an industry job, so isn't involved in Sage development right now, so I don't think he'll care much what happens with this ticket. \n\nThat said, having a total ordering -- which is different and inconsistent with set's order -- is useful (!).  However, it can be done as a separate explicit function or method, which can get passed to the sort method explicitly.",
    "created_at": "2012-02-26T17:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9677#issuecomment-93923",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:11 dsm]:
> I think the patch behaviour of
> 
> 
> ```
> 
> sage: a = [2,3]
> sage: b = [2,3,4j]
> sage: set(a) < set(b)
> True
> sage: Set(a) < Set(b)
> False
> 
> ```
> 
> is too dangerous to let pass unremarked.


In Python (according to http://docs.python.org/library/sets.html) for the set type we have: "The subset and equality comparisons do not generalize to a complete ordering function. For example, any two disjoint sets are not equal and are not subsets of each other, so all of the following return False: a<b, a==b, or a>b. Accordingly, sets do not implement the __cmp__() method."

The Python convention does make sense and is what most people would expect... and is the direction Sage should move in.

RLM who wrote "I completely, emphatically disagree." has got sucked up into an industry job, so isn't involved in Sage development right now, so I don't think he'll care much what happens with this ticket. 

That said, having a total ordering -- which is different and inconsistent with set's order -- is useful (!).  However, it can be done as a separate explicit function or method, which can get passed to the sort method explicitly.



---

archive/issue_events_024144.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24144"
}
```



---

archive/issue_events_024145.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24145"
}
```



---

archive/issue_events_024146.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24146"
}
```



---

archive/issue_events_024147.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24147"
}
```



---

archive/issue_events_024148.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24148"
}
```



---

archive/issue_events_024149.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24149"
}
```



---

archive/issue_events_024150.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9677",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9677#event-24150"
}
```
