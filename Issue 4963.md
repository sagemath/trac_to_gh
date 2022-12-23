# Issue 4963: Make a screen-full of whitespace at the bottom of the notebook cells

archive/issues_004963.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mhansen tclemans\n\nNot having this causes interacts to jump off the page when updating, for example.  See http://groups.google.com/group/sage-devel/browse_thread/thread/51b538c8212fa2a/b61655921eb0ebab\n\nIssue created by migration from https://trac.sagemath.org/ticket/4963\n\n",
    "created_at": "2009-01-11T00:55:31Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Make a screen-full of whitespace at the bottom of the notebook cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4963",
    "user": "jason"
}
```
Assignee: boothby

CC:  mhansen tclemans

Not having this causes interacts to jump off the page when updating, for example.  See http://groups.google.com/group/sage-devel/browse_thread/thread/51b538c8212fa2a/b61655921eb0ebab

Issue created by migration from https://trac.sagemath.org/ticket/4963





---

archive/issue_comments_037714.json:
```json
{
    "body": "Fixing this might also help in resolving #2629",
    "created_at": "2009-01-11T00:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37714",
    "user": "jason"
}
```

Fixing this might also help in resolving #2629



---

archive/issue_comments_037715.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2009-01-14T08:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37715",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_037716.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-14T08:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37716",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037717.json:
```json
{
    "body": "After testing with Firefox 2 and 3 and Safari on OSX.4 PPC, it seems to perform as advertised.  So positive review of its effect!  This is very useful to those of us who use interacts a lot in class, where the jumping away from the interact makes Sage look cheap as in beer, not free as in speech (or beer).\n\nIt does not resolve #2629 (though it makes it less likely to happen; see comments on #2629).\n\nBut I request another review or additional work, because the aesthetics of adding that margin-bottom 80% are still hackish at best.  For instance, very often the browser does not now jump to the next cell (where the focus has shifted), even if the jump would be fairly minimal but at the bottom of the browser.  Is this a somewhat different behavior than in the past?  It could be especially weird if someone hasn't used the notebook before, and hence doesn't know what happened to the focus after evaluating - again, if this is new behavior; perhaps it is not.\n\nGiven the discussion mentioned in the description, it sounds like this is not a big deal, but I don't feel comfortable giving final positive review on that aspect of things, since I haven't worked on the notebook, I just use it.",
    "created_at": "2009-01-21T17:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37717",
    "user": "kcrisman"
}
```

After testing with Firefox 2 and 3 and Safari on OSX.4 PPC, it seems to perform as advertised.  So positive review of its effect!  This is very useful to those of us who use interacts a lot in class, where the jumping away from the interact makes Sage look cheap as in beer, not free as in speech (or beer).

It does not resolve #2629 (though it makes it less likely to happen; see comments on #2629).

But I request another review or additional work, because the aesthetics of adding that margin-bottom 80% are still hackish at best.  For instance, very often the browser does not now jump to the next cell (where the focus has shifted), even if the jump would be fairly minimal but at the bottom of the browser.  Is this a somewhat different behavior than in the past?  It could be especially weird if someone hasn't used the notebook before, and hence doesn't know what happened to the focus after evaluating - again, if this is new behavior; perhaps it is not.

Given the discussion mentioned in the description, it sounds like this is not a big deal, but I don't feel comfortable giving final positive review on that aspect of things, since I haven't worked on the notebook, I just use it.



---

archive/issue_comments_037718.json:
```json
{
    "body": "Before this patch, we still have problems with the browser scrolling not following the focus or tab-completion menu, like described above.  I thought maybe this fix would help, but apparently more needs to be done.\n\nI did notice that this patch also extends the \"Home\" page of the notebook which lists the worksheets.  The problem there is that the \"body\" command used in each page is the same.  I've updated the patch to fix this.  This should probably be re-reviewed.  One thing that might be reviewed is that I actually changed *two* body elements; is one of them redundant?",
    "created_at": "2009-01-21T23:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37718",
    "user": "jason"
}
```

Before this patch, we still have problems with the browser scrolling not following the focus or tab-completion menu, like described above.  I thought maybe this fix would help, but apparently more needs to be done.

I did notice that this patch also extends the "Home" page of the notebook which lists the worksheets.  The problem there is that the "body" command used in each page is the same.  I've updated the patch to fix this.  This should probably be re-reviewed.  One thing that might be reviewed is that I actually changed *two* body elements; is one of them redundant?



---

archive/issue_comments_037719.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-21T23:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37719",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_037720.json:
```json
{
    "body": "That is, in fact, a large amount of space.  Well done.",
    "created_at": "2009-01-22T18:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37720",
    "user": "boothby"
}
```

That is, in fact, a large amount of space.  Well done.



---

archive/issue_comments_037721.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T09:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37721",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_comments_037722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4963#issuecomment-37722",
    "user": "mabshoff"
}
```

Resolution: fixed
