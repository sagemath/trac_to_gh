# Issue 8956: Fix notebook help on auto-evaluation

archive/issues_008956.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  jdemeyer\n\nKeywords: autoevaluate, auto-evaluate\n\nApparently, #auto should be %auto now.  But the help page for the notebook doesn't say so.  As far as I can tell, both work?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8956\n\n",
    "created_at": "2010-05-12T15:45:09Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Fix notebook help on auto-evaluation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8956",
    "user": "kcrisman"
}
```
Assignee: jason, was

CC:  jdemeyer

Keywords: autoevaluate, auto-evaluate

Apparently, #auto should be %auto now.  But the help page for the notebook doesn't say so.  As far as I can tell, both work?

Issue created by migration from https://trac.sagemath.org/ticket/8956





---

archive/issue_comments_082559.json:
```json
{
    "body": "Yes, there is code in the notebook to explicitly allow #auto, but %auto is preferred since it matches up with the other cell directives.",
    "created_at": "2010-05-12T16:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82559",
    "user": "mhansen"
}
```

Yes, there is code in the notebook to explicitly allow #auto, but %auto is preferred since it matches up with the other cell directives.



---

archive/issue_comments_082560.json:
```json
{
    "body": "See #7002 for a fix that you made 8 months ago :).",
    "created_at": "2010-05-12T16:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82560",
    "user": "jason"
}
```

See #7002 for a fix that you made 8 months ago :).



---

archive/issue_comments_082561.json:
```json
{
    "body": "Annoying.  Would it be pretty easy for someone with access to the notebook code (i.e. not me) to just rebase that patch to SageNB?  Aargh.",
    "created_at": "2010-05-12T17:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82561",
    "user": "kcrisman"
}
```

Annoying.  Would it be pretty easy for someone with access to the notebook code (i.e. not me) to just rebase that patch to SageNB?  Aargh.



---

archive/issue_comments_082562.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-20T15:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82562",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082563.json:
```json
{
    "body": "Okay, it turns out that this was finally merged in #7002 very recently.  Hooray!\n\nTo release manager: this can be closed.",
    "created_at": "2011-06-20T15:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82563",
    "user": "kcrisman"
}
```

Okay, it turns out that this was finally merged in #7002 very recently.  Hooray!

To release manager: this can be closed.



---

archive/issue_comments_082564.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-20T15:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82564",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082565.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-06-20T18:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8956#issuecomment-82565",
    "user": "jdemeyer"
}
```

Resolution: duplicate
