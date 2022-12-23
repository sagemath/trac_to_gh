# Issue 9547: x * Infinity assumes that x is positive

archive/issues_009547.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  kcrisman\n\n\n```\nsage: var('x') * Infinity\n+Infinity\n```\n\n\nThis is not right; x could represent something non-positive.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9547\n\n",
    "created_at": "2010-07-19T08:25:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "x * Infinity assumes that x is positive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9547",
    "user": "fredrik.johansson"
}
```
Assignee: AlexGhitza

CC:  kcrisman


```
sage: var('x') * Infinity
+Infinity
```


This is not right; x could represent something non-positive.

Issue created by migration from https://trac.sagemath.org/ticket/9547





---

archive/issue_comments_092028.json:
```json
{
    "body": "Likely the solution will be related with #11506.",
    "created_at": "2012-05-11T13:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92028",
    "user": "tscrim"
}
```

Likely the solution will be related with #11506.



---

archive/issue_comments_092029.json:
```json
{
    "body": "Changing component from algebra to symbolics.",
    "created_at": "2012-05-15T22:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92029",
    "user": "burcin"
}
```

Changing component from algebra to symbolics.



---

archive/issue_comments_092030.json:
```json
{
    "body": "Changing assignee from AlexGhitza to burcin.",
    "created_at": "2012-05-15T22:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92030",
    "user": "burcin"
}
```

Changing assignee from AlexGhitza to burcin.



---

archive/issue_comments_092031.json:
```json
{
    "body": "This is fixed by #12950. There is a doctest on line 2429 of `sage/symbolic/expression.pyx`. We should close this ticket when that is merged.",
    "created_at": "2012-05-15T22:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92031",
    "user": "burcin"
}
```

This is fixed by #12950. There is a doctest on line 2429 of `sage/symbolic/expression.pyx`. We should close this ticket when that is merged.



---

archive/issue_comments_092032.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-29T10:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92032",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092033.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-29T10:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92033",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092034.json:
```json
{
    "body": "Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.",
    "created_at": "2012-06-29T13:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92034",
    "user": "kcrisman"
}
```

Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.



---

archive/issue_comments_092035.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.\nSame question as #1861: why doesn't this count as duplicate/invalid/wontfix?",
    "created_at": "2012-06-29T14:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92035",
    "user": "jdemeyer"
}
```

Replying to [comment:6 kcrisman]:
> Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.
Same question as #1861: why doesn't this count as duplicate/invalid/wontfix?



---

archive/issue_comments_092036.json:
```json
{
    "body": "> > Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.\n> Same question as #1861: why doesn't this count as duplicate/invalid/wontfix?\nIn my opinion (only?), tickets that are closed by metatickets are not duplicates.  It seems better to me (only?) to make it clear that work went into all of the issues we close, instead of making it seem like we have hundreds of duplicates that people open.  We already *do* have enough duplicates as it is :) \n\nAnd we certainly fixed it, so it's not \"wontfix\", and it's not invalid either, or at least wasn't before #12950, which however, explicitly refers to this ticket - it's not like some other change in #12950 made this invalid, which does sometimes happen.",
    "created_at": "2012-06-29T15:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92036",
    "user": "kcrisman"
}
```

> > Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.
> Same question as #1861: why doesn't this count as duplicate/invalid/wontfix?
In my opinion (only?), tickets that are closed by metatickets are not duplicates.  It seems better to me (only?) to make it clear that work went into all of the issues we close, instead of making it seem like we have hundreds of duplicates that people open.  We already *do* have enough duplicates as it is :) 

And we certainly fixed it, so it's not "wontfix", and it's not invalid either, or at least wasn't before #12950, which however, explicitly refers to this ticket - it's not like some other change in #12950 made this invalid, which does sometimes happen.



---

archive/issue_comments_092037.json:
```json
{
    "body": "If the issue is fixed by a *different* ticket, then this ticket should be either a \"duplicate\" or a \"worksforme\".\n\nHas a doctest been added for this?  If not, one could consider needs_work.",
    "created_at": "2012-06-29T15:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92037",
    "user": "jdemeyer"
}
```

If the issue is fixed by a *different* ticket, then this ticket should be either a "duplicate" or a "worksforme".

Has a doctest been added for this?  If not, one could consider needs_work.



---

archive/issue_comments_092038.json:
```json
{
    "body": "> If the issue is fixed by a *different* ticket, then this ticket should be either a \"duplicate\" or a \"worksforme\".\nI simply disagree.  So you are saying that, hypothetically, a gigantic metaticket for foo.spkg that bundles fifty changes, all of which are doctested by some huge patch at that ticket, means all the others are duplicates?  That seems to denigrate the hard work that went into each of those other tickets.  Although the people currently working on these particular tickets are not counting on this material for promotion, that is certainly a future possibility, as standards evolve, especially at less research-focused institutions.\n> Has a doctest been added for this?  If not, one could consider needs_work.\nYes, it is at #12950.",
    "created_at": "2012-06-29T15:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92038",
    "user": "kcrisman"
}
```

> If the issue is fixed by a *different* ticket, then this ticket should be either a "duplicate" or a "worksforme".
I simply disagree.  So you are saying that, hypothetically, a gigantic metaticket for foo.spkg that bundles fifty changes, all of which are doctested by some huge patch at that ticket, means all the others are duplicates?  That seems to denigrate the hard work that went into each of those other tickets.  Although the people currently working on these particular tickets are not counting on this material for promotion, that is certainly a future possibility, as standards evolve, especially at less research-focused institutions.
> Has a doctest been added for this?  If not, one could consider needs_work.
Yes, it is at #12950.



---

archive/issue_comments_092039.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> > If the issue is fixed by a *different* ticket, then this ticket should be either a \"duplicate\" or a \"worksforme\".\n> I simply disagree.  So you are saying that, hypothetically, a gigantic metaticket for foo.spkg that bundles fifty changes, all of which are doctested by some huge patch at that ticket, means all the others are duplicates?  That seems to denigrate the hard work that went into each of those other tickets.  Although the people currently working on these particular tickets are not counting on this material for promotion, that is certainly a future possibility, as standards evolve, especially at less research-focused institutions.\nYou could give credit to those people on the other gigantic metaticket.\n\nOn this particular ticket here, I don't see any work done, so I would simply close it as duplicate.",
    "created_at": "2012-06-29T16:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92039",
    "user": "jdemeyer"
}
```

Replying to [comment:10 kcrisman]:
> > If the issue is fixed by a *different* ticket, then this ticket should be either a "duplicate" or a "worksforme".
> I simply disagree.  So you are saying that, hypothetically, a gigantic metaticket for foo.spkg that bundles fifty changes, all of which are doctested by some huge patch at that ticket, means all the others are duplicates?  That seems to denigrate the hard work that went into each of those other tickets.  Although the people currently working on these particular tickets are not counting on this material for promotion, that is certainly a future possibility, as standards evolve, especially at less research-focused institutions.
You could give credit to those people on the other gigantic metaticket.

On this particular ticket here, I don't see any work done, so I would simply close it as duplicate.



---

archive/issue_comments_092040.json:
```json
{
    "body": "> You could give credit to those people on the other gigantic metaticket.\nWhich Burcin did.  The point was that although a ticket isn't a great measure of work, we don't have to make it an even worse measure.\n> On this particular ticket here, I don't see any work done, so I would simply close it as duplicate.\nWell, I was going by the fact that someone else filled in author and reviewer fields and the work \"just happened\" to be there; see also the discussion at #12950.  But if you insist, I suppose I've engaged in enough bikeshedding for one day.",
    "created_at": "2012-06-29T16:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92040",
    "user": "kcrisman"
}
```

> You could give credit to those people on the other gigantic metaticket.
Which Burcin did.  The point was that although a ticket isn't a great measure of work, we don't have to make it an even worse measure.
> On this particular ticket here, I don't see any work done, so I would simply close it as duplicate.
Well, I was going by the fact that someone else filled in author and reviewer fields and the work "just happened" to be there; see also the discussion at #12950.  But if you insist, I suppose I've engaged in enough bikeshedding for one day.



---

archive/issue_comments_092041.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-07-04T07:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9547#issuecomment-92041",
    "user": "jdemeyer"
}
```

Resolution: duplicate
