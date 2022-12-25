# Issue 4790: sage -t does not take into account the current directory

archive/issues_004790.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a split of #3677.  \nAt the end of testing when reporting the results, sage -t does not take into account the current directory. It produces output like this: \n\n```\n        sage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py\n\tsage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py\n```\n\n\nwhen it should be giving output like \n\n\n```\n        sage -t  ambient_space.py\n\tsage -t  root_lattice_realization.py\n\tsage -t  root_space.py\n\tsage -t  root_system.py\n\tsage -t  weight_space.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4790\n\n",
    "created_at": "2008-12-14T05:28:39Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -t does not take into account the current directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4790",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: mabshoff

This is a split of #3677.  
At the end of testing when reporting the results, sage -t does not take into account the current directory. It produces output like this: 

```
        sage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py
```


when it should be giving output like 


```
        sage -t  ambient_space.py
	sage -t  root_lattice_realization.py
	sage -t  root_space.py
	sage -t  root_system.py
	sage -t  weight_space.py
```


Issue created by migration from https://trac.sagemath.org/ticket/4790





---

archive/issue_comments_036239.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-14T21:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4790#issuecomment-36239",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036240.json:
```json
{
    "body": "This is resolved by #12415.",
    "created_at": "2013-03-14T21:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4790#issuecomment-36240",
    "user": "https://github.com/roed314"
}
```

This is resolved by #12415.



---

archive/issue_comments_036241.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-14T21:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4790#issuecomment-36241",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_010953.json:
```json
{
    "actor": "https://github.com/roed314",
    "created_at": "2013-03-14T21:56:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4790",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4790#event-10953"
}
```



---

archive/issue_comments_036242.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-15T13:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4790#issuecomment-36242",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_010954.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-15T13:00:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4790",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4790#event-10954"
}
```
