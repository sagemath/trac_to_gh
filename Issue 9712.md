# Issue 9712: Make building PolyBoRi depend on GD

archive/issues_009712.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @malb\n\nFrom #9472:\n\n \"Since PolyBoRi also uses GD, `$SAGE_ROOT/spkg/standard/deps` should be updated (but there seem to have been no issues with that in the past).\"\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9712\n\n",
    "created_at": "2010-08-09T22:35:52Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Make building PolyBoRi depend on GD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9712",
    "user": "https://github.com/nexttime"
}
```
Assignee: tbd

CC:  @nexttime @malb

From #9472:

 "Since PolyBoRi also uses GD, `$SAGE_ROOT/spkg/standard/deps` should be updated (but there seem to have been no issues with that in the past)."


Issue created by migration from https://trac.sagemath.org/ticket/9712





---

archive/issue_comments_094498.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket9712/deps) by @qed777 created at 2010-08-09 23:12:38\n\nUpdated `spkg/standard/deps`.  Based on 4.5.2 + #8316.",
    "created_at": "2010-08-09T23:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94498",
    "user": "https://github.com/qed777"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket9712/deps) by @qed777 created at 2010-08-09 23:12:38

Updated `spkg/standard/deps`.  Based on 4.5.2 + #8316.



---

archive/issue_comments_094499.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9712/deps.diff) by @qed777 created at 2010-08-09 23:13:26\n\nDiff of `spkg/standard/deps` vs. 4.5.2 + #8316.",
    "created_at": "2010-08-09T23:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94499",
    "user": "https://github.com/qed777"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9712/deps.diff) by @qed777 created at 2010-08-09 23:13:26

Diff of `spkg/standard/deps` vs. 4.5.2 + #8316.



---

archive/issue_comments_094500.json:
```json
{
    "body": "I've attached a new `deps` and `deps.diff`.\n\nI'm not sure whether to put Leif or Martin as the author, or both Leif and Martin.  Can someone please update the field?",
    "created_at": "2010-08-09T23:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94500",
    "user": "https://github.com/qed777"
}
```

I've attached a new `deps` and `deps.diff`.

I'm not sure whether to put Leif or Martin as the author, or both Leif and Martin.  Can someone please update the field?



---

archive/issue_comments_094501.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-09T23:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94501",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094502.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> I'm not sure whether to put Leif or Martin as the author, or both Leif and Martin.  Can someone please update the field?\n\nCan you update the *\"Reported by:\"* field? ;-)\n\nFrom PolyBoRi's `SPKG.txt`:\n\n```\n...\n\n## Dependencies\n\n * Python\n * Scons\n * Boost\n * gd (FIXME/TODO: should be added to deps, I think. Leif, 2010-07-10)\n * M4RI/libm4ri (already included in deps)\n * png/libpng12 (accomplished because Python and gd depend on it, too)\n * libz         (accomplished because e.g. libpng depends on it)\n\n...\n```\n\n\nI must admit I did not check *all* transitive dependencies, i.e. if some package that PolyBoRi (indirectly) depends on pulls in the GD dependency. Anyway, I think it's always better to add an explicit, perhaps \"redundant\" dependency rather than to omit it, (not only) since the deps of other packages might change over the time. (Same for explicitly linking against libraries directly used despite other used libraries - *currently* - already doing so.)\n\nThe only package in `standard/deps` that's listed to **directly** depend on GD is `gdmodule`, which in turn is only listed as a (direct) dependency of MatPlotLib (and the Sage library).",
    "created_at": "2010-08-10T00:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94502",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:1 mpatel]:
> I'm not sure whether to put Leif or Martin as the author, or both Leif and Martin.  Can someone please update the field?

Can you update the *"Reported by:"* field? ;-)

From PolyBoRi's `SPKG.txt`:

```
...

## Dependencies

 * Python
 * Scons
 * Boost
 * gd (FIXME/TODO: should be added to deps, I think. Leif, 2010-07-10)
 * M4RI/libm4ri (already included in deps)
 * png/libpng12 (accomplished because Python and gd depend on it, too)
 * libz         (accomplished because e.g. libpng depends on it)

...
```


I must admit I did not check *all* transitive dependencies, i.e. if some package that PolyBoRi (indirectly) depends on pulls in the GD dependency. Anyway, I think it's always better to add an explicit, perhaps "redundant" dependency rather than to omit it, (not only) since the deps of other packages might change over the time. (Same for explicitly linking against libraries directly used despite other used libraries - *currently* - already doing so.)

The only package in `standard/deps` that's listed to **directly** depend on GD is `gdmodule`, which in turn is only listed as a (direct) dependency of MatPlotLib (and the Sage library).



---

archive/issue_comments_094503.json:
```json
{
    "body": "I've only \"reviewed\" `deps.diff` though... :)",
    "created_at": "2010-08-10T00:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94503",
    "user": "https://github.com/nexttime"
}
```

I've only "reviewed" `deps.diff` though... :)



---

archive/issue_comments_094504.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T00:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94504",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094505.json:
```json
{
    "body": "I'm pretty sure it's just good luck this ever worked. GD is one of the \"early\" packages, and all of these take little time to build.\n\nI'll perhaps verify that later by forcing GD to be built very late.",
    "created_at": "2010-08-10T13:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94505",
    "user": "https://github.com/nexttime"
}
```

I'm pretty sure it's just good luck this ever worked. GD is one of the "early" packages, and all of these take little time to build.

I'll perhaps verify that later by forcing GD to be built very late.



---

archive/issue_comments_094506.json:
```json
{
    "body": "P.S.: The suggestion to change the \"Reported by:\" field was just a joke.",
    "created_at": "2010-08-10T13:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94506",
    "user": "https://github.com/nexttime"
}
```

P.S.: The suggestion to change the "Reported by:" field was just a joke.



---

archive/issue_events_024291.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-15T06:57:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9712#event-24291"
}
```



---

archive/issue_comments_094507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T06:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9712#issuecomment-94507",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
