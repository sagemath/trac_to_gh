# Issue 7248: include jinja2 / upgrade jinja spkg

archive/issues_007248.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jhpalmieri\n\nI'm not sure whether this is an upgrade or a new spkg, but the plan is to switch the notebook to Jinja2, which will require updating/replacing the current Jinja spkg.\n\nJohn Palmieri has a proposed spkg at #6586.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7248\n\n",
    "created_at": "2009-10-19T08:42:29Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "include jinja2 / upgrade jinja spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7248",
    "user": "https://github.com/dandrake"
}
```
Assignee: boothby

CC:  @jhpalmieri

I'm not sure whether this is an upgrade or a new spkg, but the plan is to switch the notebook to Jinja2, which will require updating/replacing the current Jinja spkg.

John Palmieri has a proposed spkg at #6586.

Issue created by migration from https://trac.sagemath.org/ticket/7248





---

archive/issue_comments_060059.json:
```json
{
    "body": "> John Palmieri has a proposed spkg at #6586.\n\n\"Proposed\"?  It's in Sage 4.2.alpha0.\n\nSome work needs to be done if you want to get rid of Jinja -- last time I checked, some parts of the Sage library use things from Jinja that it wasn't immediately obvious how to replace using Jinja2: see [this comment from #6586](http://trac.sagemath.org/sage_trac/ticket/6586#comment:49).",
    "created_at": "2009-10-19T19:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60059",
    "user": "https://github.com/jhpalmieri"
}
```

> John Palmieri has a proposed spkg at #6586.

"Proposed"?  It's in Sage 4.2.alpha0.

Some work needs to be done if you want to get rid of Jinja -- last time I checked, some parts of the Sage library use things from Jinja that it wasn't immediately obvious how to replace using Jinja2: see [this comment from #6586](http://trac.sagemath.org/sage_trac/ticket/6586#comment:49).



---

archive/issue_comments_060060.json:
```json
{
    "body": "Replying to [comment:1 jhpalmieri]:\n> > John Palmieri has a proposed spkg at #6586.\n> \n> \"Proposed\"?  It's in Sage 4.2.alpha0.\n\nOops. I didn't know.\n \n> Some work needs to be done if you want to get rid of Jinja\n\nFor this ticket, I was thinking of just getting jinja2 in. We can do another ticket later for removing jinja. I'll close this since it's already done.",
    "created_at": "2009-10-19T23:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60060",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:1 jhpalmieri]:
> > John Palmieri has a proposed spkg at #6586.
> 
> "Proposed"?  It's in Sage 4.2.alpha0.

Oops. I didn't know.
 
> Some work needs to be done if you want to get rid of Jinja

For this ticket, I was thinking of just getting jinja2 in. We can do another ticket later for removing jinja. I'll close this since it's already done.



---

archive/issue_events_017158.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2009-10-19T23:22:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7248#event-17158"
}
```



---

archive/issue_comments_060061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T23:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60061",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_060062.json:
```json
{
    "body": "Actually, the notebook hasn't switched over.  The only thing in Sage 4.2 that uses Jinja2 is Sphinx.",
    "created_at": "2009-10-20T03:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60062",
    "user": "https://github.com/mwhansen"
}
```

Actually, the notebook hasn't switched over.  The only thing in Sage 4.2 that uses Jinja2 is Sphinx.



---

archive/issue_comments_060063.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-10-20T03:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60063",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to new.



---

archive/issue_events_017159.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-20T03:32:06Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7248#event-17159"
}
```



---

archive/issue_comments_060064.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-10-20T03:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60064",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_060065.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> Actually, the notebook hasn't switched over.  The only thing in Sage 4.2 that uses Jinja2 is Sphinx.\n\nThis ticket isn't about switching anything to Jinja2. The title is \"include jinja2 / upgrade jinja spkg\", and I closed it because you had already done exactly that in 4.2.alpha0.\n\n#7249 is about switching, and it has a patch and awaits review.",
    "created_at": "2009-10-20T05:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60065",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:3 mhansen]:
> Actually, the notebook hasn't switched over.  The only thing in Sage 4.2 that uses Jinja2 is Sphinx.

This ticket isn't about switching anything to Jinja2. The title is "include jinja2 / upgrade jinja spkg", and I closed it because you had already done exactly that in 4.2.alpha0.

#7249 is about switching, and it has a patch and awaits review.



---

archive/issue_comments_060066.json:
```json
{
    "body": "Duplicate of #6586.",
    "created_at": "2009-10-20T05:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60066",
    "user": "https://github.com/mwhansen"
}
```

Duplicate of #6586.



---

archive/issue_comments_060067.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-20T05:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7248#issuecomment-60067",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_017160.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-20T05:32:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7248#event-17160"
}
```
