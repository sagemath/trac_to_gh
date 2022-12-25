# Issue 8956: Fix notebook help on auto-evaluation

archive/issues_008956.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jdemeyer\n\nKeywords: autoevaluate, auto-evaluate\n\nApparently, #auto should be %auto now.  But the help page for the notebook doesn't say so.  As far as I can tell, both work?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8956\n\n",
    "closed_at": "2011-06-20T18:53:53Z",
    "created_at": "2010-05-12T15:45:09Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix notebook help on auto-evaluation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8956",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

CC:  @jdemeyer

Keywords: autoevaluate, auto-evaluate

Apparently, #auto should be %auto now.  But the help page for the notebook doesn't say so.  As far as I can tell, both work?

Issue created by migration from https://trac.sagemath.org/ticket/8956





---

archive/issue_comments_082424.json:
```json
{
    "body": "Yes, there is code in the notebook to explicitly allow #auto, but %auto is preferred since it matches up with the other cell directives.",
    "created_at": "2010-05-12T16:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82424",
    "user": "https://github.com/mwhansen"
}
```

Yes, there is code in the notebook to explicitly allow #auto, but %auto is preferred since it matches up with the other cell directives.



---

archive/issue_comments_082425.json:
```json
{
    "body": "See #7002 for a fix that you made 8 months ago :).",
    "created_at": "2010-05-12T16:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82425",
    "user": "https://github.com/jasongrout"
}
```

See #7002 for a fix that you made 8 months ago :).



---

archive/issue_comments_082426.json:
```json
{
    "body": "Annoying.  Would it be pretty easy for someone with access to the notebook code (i.e. not me) to just rebase that patch to SageNB?  Aargh.",
    "created_at": "2010-05-12T17:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82426",
    "user": "https://github.com/kcrisman"
}
```

Annoying.  Would it be pretty easy for someone with access to the notebook code (i.e. not me) to just rebase that patch to SageNB?  Aargh.



---

archive/issue_comments_082427.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-20T15:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82427",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082428.json:
```json
{
    "body": "Okay, it turns out that this was finally merged in #7002 very recently.  Hooray!\n\nTo release manager: this can be closed.",
    "created_at": "2011-06-20T15:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82428",
    "user": "https://github.com/kcrisman"
}
```

Okay, it turns out that this was finally merged in #7002 very recently.  Hooray!

To release manager: this can be closed.



---

archive/issue_comments_082429.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-20T15:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82429",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021874.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-20T18:48:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8956#event-21874"
}
```



---

archive/issue_events_021875.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-20T18:53:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8956#event-21875"
}
```



---

archive/issue_comments_082430.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-06-20T18:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82430",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
