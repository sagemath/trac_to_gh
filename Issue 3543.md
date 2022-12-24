# Issue 3543: Unify jquery libraries in devel/sage and data/extcode

archive/issues_003543.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason timdumol\n\nWe currently ship two copies of the jquery javascript library:\n\n* jQuery 1.2.6 - New Wave Javascript - $Rev: 5685 $ in devel/sage-main/sage/dsage/web/static/jquery.js\n* jQuery 1.2.3 - New Wave Javascript - $Rev: 4663 $ in data/extcode/notebook/javascript/jquery/jquery.js\n\nBut we should on ship one copy.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3543\n\n",
    "created_at": "2008-07-03T04:29:24Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Unify jquery libraries in devel/sage and data/extcode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3543",
    "user": "mabshoff"
}
```
Assignee: was

CC:  jason timdumol

We currently ship two copies of the jquery javascript library:

* jQuery 1.2.6 - New Wave Javascript - $Rev: 5685 $ in devel/sage-main/sage/dsage/web/static/jquery.js
* jQuery 1.2.3 - New Wave Javascript - $Rev: 4663 $ in data/extcode/notebook/javascript/jquery/jquery.js

But we should on ship one copy.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3543





---

archive/issue_comments_025055.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2008-10-10T23:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25055",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_025056.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-10T23:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25056",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025057.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-12-05T10:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25057",
    "user": "jason"
}
```

Changing status from assigned to new.



---

archive/issue_comments_025058.json:
```json
{
    "body": "Remove assignee jason.",
    "created_at": "2008-12-05T10:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25058",
    "user": "jason"
}
```

Remove assignee jason.



---

archive/issue_comments_025059.json:
```json
{
    "body": "I'm not sure what is going on with dsage; someone familiar with dsage will have to look at that.",
    "created_at": "2008-12-05T10:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25059",
    "user": "jason"
}
```

I'm not sure what is going on with dsage; someone familiar with dsage will have to look at that.



---

archive/issue_comments_025060.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25060",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_025061.json:
```json
{
    "body": "All that is needed is that dsage needs to change its /static directory to point to local/notebook/javascript/<appropriate directory>.  I'm making this minor since:\n\n1. the small space wasted with duplicated code is not worth the risk of breaking dsage, especially since\n2. it seems that the future of dsage is uncertain.\n\nThings work now.",
    "created_at": "2009-01-22T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25061",
    "user": "jason"
}
```

All that is needed is that dsage needs to change its /static directory to point to local/notebook/javascript/<appropriate directory>.  I'm making this minor since:

1. the small space wasted with duplicated code is not worth the risk of breaking dsage, especially since
2. it seems that the future of dsage is uncertain.

Things work now.



---

archive/issue_comments_025062.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-01-22T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25062",
    "user": "jason"
}
```

Changing priority from major to minor.



---

archive/issue_comments_025063.json:
```json
{
    "body": "Tim,\n\nCan you comment on this ticket?  You probably know more about this than anyone at this point.",
    "created_at": "2010-05-11T05:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25063",
    "user": "jason"
}
```

Tim,

Can you comment on this ticket?  You probably know more about this than anyone at this point.



---

archive/issue_comments_025064.json:
```json
{
    "body": "dsage is gone, so that doesn't matter. The files in `data/extcode/...` are used by the old notebook (in sage.server.notebook). Since the old notebook isn't used anymore except in migration to the new one, the files should be safe to delete.",
    "created_at": "2010-05-11T05:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25064",
    "user": "timdumol"
}
```

dsage is gone, so that doesn't matter. The files in `data/extcode/...` are used by the old notebook (in sage.server.notebook). Since the old notebook isn't used anymore except in migration to the new one, the files should be safe to delete.



---

archive/issue_comments_025065.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-22T09:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25065",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025066.json:
```json
{
    "body": "The Sage library doesn't ship `jquery`. Various packages do, in particular `sagenb`, `Sphinx`, `matplotlib`, `ppl`, `jsmol`, `IPython` and `WerkZeug`. I don't think it's feasible to unify them, so close this ticket as \"wontfix\".",
    "created_at": "2015-04-22T09:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25066",
    "user": "jdemeyer"
}
```

The Sage library doesn't ship `jquery`. Various packages do, in particular `sagenb`, `Sphinx`, `matplotlib`, `ppl`, `jsmol`, `IPython` and `WerkZeug`. I don't think it's feasible to unify them, so close this ticket as "wontfix".



---

archive/issue_comments_025067.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-22T09:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25067",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025068.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-04-23T01:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3543#issuecomment-25068",
    "user": "vbraun"
}
```

Resolution: wontfix
