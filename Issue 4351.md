# Issue 4351: bugs in abelian variety homspace computation

archive/issues_004351.json:
```json
{
    "body": "Assignee: @craigcitro\n\nPlease see #4346 first and apply the patch there.\n\nAfter applying this patch and doctesting all sage, there are a bunch of failures in the modular abelian varieties code:\n\n```\n\tsage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 3 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/homspace.py # 34 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/abvar.py # 11 doctests failed\n```\n\n\nThese are because of bugs in that code exposed by doing proper bounds checking.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4351\n\n",
    "created_at": "2008-10-23T19:34:51Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "bugs in abelian variety homspace computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4351",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

Please see #4346 first and apply the patch there.

After applying this patch and doctesting all sage, there are a bunch of failures in the modular abelian varieties code:

```
	sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 34 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 11 doctests failed
```


These are because of bugs in that code exposed by doing proper bounds checking.

Issue created by migration from https://trac.sagemath.org/ticket/4351





---

archive/issue_comments_031895.json:
```json
{
    "body": "This is a red herring.  It is fixed by #4350, and there were never any bugs suggested by this ticket.",
    "created_at": "2008-10-23T20:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4351#issuecomment-31895",
    "user": "https://github.com/williamstein"
}
```

This is a red herring.  It is fixed by #4350, and there were never any bugs suggested by this ticket.



---

archive/issue_comments_031896.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-23T20:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4351#issuecomment-31896",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_events_004597.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-10-23T20:27:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4351",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4351#event-4597"
}
```
