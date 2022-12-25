# Issue 3543: Unify jquery libraries in devel/sage and data/extcode

archive/issues_003543.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @TimDumol\n\nWe currently ship two copies of the jquery javascript library:\n\n* jQuery 1.2.6 - New Wave Javascript - $Rev: 5685 $ in devel/sage-main/sage/dsage/web/static/jquery.js\n* jQuery 1.2.3 - New Wave Javascript - $Rev: 4663 $ in data/extcode/notebook/javascript/jquery/jquery.js\n\nBut we should on ship one copy.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3543\n\n",
    "created_at": "2008-07-03T04:29:24Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Unify jquery libraries in devel/sage and data/extcode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3543",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

CC:  @jasongrout @TimDumol

We currently ship two copies of the jquery javascript library:

* jQuery 1.2.6 - New Wave Javascript - $Rev: 5685 $ in devel/sage-main/sage/dsage/web/static/jquery.js
* jQuery 1.2.3 - New Wave Javascript - $Rev: 4663 $ in data/extcode/notebook/javascript/jquery/jquery.js

But we should on ship one copy.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3543





---

archive/issue_comments_025005.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2008-10-10T23:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25005",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_025006.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-10T23:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25006",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025007.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-12-05T10:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25007",
    "user": "https://github.com/jasongrout"
}
```

Changing status from assigned to new.



---

archive/issue_comments_025008.json:
```json
{
    "body": "Remove assignee @jasongrout.",
    "created_at": "2008-12-05T10:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25008",
    "user": "https://github.com/jasongrout"
}
```

Remove assignee @jasongrout.



---

archive/issue_comments_025009.json:
```json
{
    "body": "I'm not sure what is going on with dsage; someone familiar with dsage will have to look at that.",
    "created_at": "2008-12-05T10:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25009",
    "user": "https://github.com/jasongrout"
}
```

I'm not sure what is going on with dsage; someone familiar with dsage will have to look at that.



---

archive/issue_comments_025010.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25010",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_025011.json:
```json
{
    "body": "All that is needed is that dsage needs to change its /static directory to point to local/notebook/javascript/<appropriate directory>.  I'm making this minor since:\n\n1. the small space wasted with duplicated code is not worth the risk of breaking dsage, especially since\n2. it seems that the future of dsage is uncertain.\n\nThings work now.",
    "created_at": "2009-01-22T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25011",
    "user": "https://github.com/jasongrout"
}
```

All that is needed is that dsage needs to change its /static directory to point to local/notebook/javascript/<appropriate directory>.  I'm making this minor since:

1. the small space wasted with duplicated code is not worth the risk of breaking dsage, especially since
2. it seems that the future of dsage is uncertain.

Things work now.



---

archive/issue_comments_025012.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-01-22T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25012",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_comments_025013.json:
```json
{
    "body": "Tim,\n\nCan you comment on this ticket?  You probably know more about this than anyone at this point.",
    "created_at": "2010-05-11T05:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25013",
    "user": "https://github.com/jasongrout"
}
```

Tim,

Can you comment on this ticket?  You probably know more about this than anyone at this point.



---

archive/issue_comments_025014.json:
```json
{
    "body": "dsage is gone, so that doesn't matter. The files in `data/extcode/...` are used by the old notebook (in sage.server.notebook). Since the old notebook isn't used anymore except in migration to the new one, the files should be safe to delete.",
    "created_at": "2010-05-11T05:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25014",
    "user": "https://github.com/TimDumol"
}
```

dsage is gone, so that doesn't matter. The files in `data/extcode/...` are used by the old notebook (in sage.server.notebook). Since the old notebook isn't used anymore except in migration to the new one, the files should be safe to delete.



---

archive/issue_comments_025015.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-22T09:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25015",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025016.json:
```json
{
    "body": "The Sage library doesn't ship `jquery`. Various packages do, in particular `sagenb`, `Sphinx`, `matplotlib`, `ppl`, `jsmol`, `IPython` and `WerkZeug`. I don't think it's feasible to unify them, so close this ticket as \"wontfix\".",
    "created_at": "2015-04-22T09:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25016",
    "user": "https://github.com/jdemeyer"
}
```

The Sage library doesn't ship `jquery`. Various packages do, in particular `sagenb`, `Sphinx`, `matplotlib`, `ppl`, `jsmol`, `IPython` and `WerkZeug`. I don't think it's feasible to unify them, so close this ticket as "wontfix".



---

archive/issue_comments_025017.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-22T09:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25017",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_003763.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-23T01:43:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3543#event-3763"
}
```



---

archive/issue_comments_025018.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-04-23T01:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25018",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
