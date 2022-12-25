# Issue 2474: RealIntervalField should have a round method (maybe ComplexIntervalField should too)

archive/issues_002474.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @ncalexan\n\nKeywords: RIF CIF RealIntervalField ComplexIntervalField round\n\n\n```\nsage: round(RIF(10))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/sage-2.10.3.rc3/<ipython console> in <module>()\n\n/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py in round(x, ndigits)\n    864     else:\n    865         try: return x.round()\n--> 866         except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))\n    867 \n    868 def quotient(x, y, *args, **kwds):\n\n<type 'exceptions.TypeError'>: a float is required\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2474\n\n",
    "created_at": "2008-03-11T22:09:18Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "RealIntervalField should have a round method (maybe ComplexIntervalField should too)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2474",
    "user": "https://github.com/ncalexan"
}
```
Assignee: somebody

CC:  @ncalexan

Keywords: RIF CIF RealIntervalField ComplexIntervalField round


```
sage: round(RIF(10))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-2.10.3.rc3/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py in round(x, ndigits)
    864     else:
    865         try: return x.round()
--> 866         except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))
    867 
    868 def quotient(x, y, *args, **kwds):

<type 'exceptions.TypeError'>: a float is required
```


Issue created by migration from https://trac.sagemath.org/ticket/2474





---

archive/issue_comments_016717.json:
```json
{
    "body": "But what should it return?  In particular, what should round(RIF(1.5, 12345.678)) return, and why?\n\nMy vote is that RIF should not have a round method, since I can't think of a definition that's sensible and useful.",
    "created_at": "2008-03-12T01:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16717",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

But what should it return?  In particular, what should round(RIF(1.5, 12345.678)) return, and why?

My vote is that RIF should not have a round method, since I can't think of a definition that's sensible and useful.



---

archive/issue_comments_016718.json:
```json
{
    "body": "This now exists, with some definition.",
    "created_at": "2017-09-13T19:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16718",
    "user": "https://github.com/fchapoton"
}
```

This now exists, with some definition.



---

archive/issue_comments_016719.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-13T19:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16719",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016720.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-09-15T08:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16720",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016721.json:
```json
{
    "body": "Indeed!",
    "created_at": "2017-09-15T08:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16721",
    "user": "https://github.com/videlec"
}
```

Indeed!



---

archive/issue_comments_016722.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16722",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_events_002653.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2017-12-12T08:23:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2474#event-2653"
}
```



---

archive/issue_comments_016723.json:
```json
{
    "body": "I wonder why \"wontfix\" since this now seems to work:\n\n```\nsage: sage.rings.real_mpfi.printing_style = 'brackets'\nsage: round(RIF(1.5, 12345.678)) \n[2.0000000000000000 .. 12346.000000000000]\n```\n",
    "created_at": "2017-12-12T09:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16723",
    "user": "https://github.com/zimmermann6"
}
```

I wonder why "wontfix" since this now seems to work:

```
sage: sage.rings.real_mpfi.printing_style = 'brackets'
sage: round(RIF(1.5, 12345.678)) 
[2.0000000000000000 .. 12346.000000000000]
```




---

archive/issue_comments_016724.json:
```json
{
    "body": "It was a batch edit; it doesn't make a lot of difference either way but I suppose \"worksforme\" would be more appropriate (but \"wontfix\" could also be read as \"won't fix because it's already fixed\" :)",
    "created_at": "2017-12-12T13:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16724",
    "user": "https://github.com/embray"
}
```

It was a batch edit; it doesn't make a lot of difference either way but I suppose "worksforme" would be more appropriate (but "wontfix" could also be read as "won't fix because it's already fixed" :)



---

archive/issue_comments_016725.json:
```json
{
    "body": "Resolution changed from wontfix to worksforme",
    "created_at": "2017-12-12T13:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16725",
    "user": "https://github.com/embray"
}
```

Resolution changed from wontfix to worksforme
