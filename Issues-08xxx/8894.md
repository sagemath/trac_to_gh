# Issue 8894: topological minor

archive/issues_008894.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nGraph.topological_minor ! \n\nI hope it will be useful, though the performances of GLPK are veeeery bad on this kind of problem... CPLEX can solve immediately problems GLPK can not handle (find there is no topological K5 minor in a Petersen Graph for example, or the same in a Grid2d graph). \n\nI mentionned it in the docstring.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8894\n\n",
    "closed_at": "2011-01-19T22:19:49Z",
    "created_at": "2010-05-05T18:24:48Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "topological minor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8894",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

Graph.topological_minor ! 

I hope it will be useful, though the performances of GLPK are veeeery bad on this kind of problem... CPLEX can solve immediately problems GLPK can not handle (find there is no topological K5 minor in a Petersen Graph for example, or the same in a Grid2d graph). 

I mentionned it in the docstring.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8894





---

archive/issue_comments_081635.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81635",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081636.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-19T00:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81636",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081637.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-19T00:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81637",
    "user": "https://github.com/nathanncohen"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_081638.json:
```json
{
    "body": "The patch seens to be correct and I believe it is ready to be merged to sage.",
    "created_at": "2011-01-10T16:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81638",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

The patch seens to be correct and I believe it is ready to be merged to sage.



---

archive/issue_comments_081639.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T16:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81639",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_021702.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-10T21:10:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8894#event-21702"
}
```



---

archive/issue_comments_081640.json:
```json
{
    "body": "Even though the patch applies (with fuzz and large offset), you should rebase it to sage-4.6.2.alpha0:\n\n```\npatching file sage/graphs/graph.py\nHunk #1 succeeded at 2960 with fuzz 2 (offset 461 lines).\n```",
    "created_at": "2011-01-18T13:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81640",
    "user": "https://github.com/jdemeyer"
}
```

Even though the patch applies (with fuzz and large offset), you should rebase it to sage-4.6.2.alpha0:

```
patching file sage/graphs/graph.py
Hunk #1 succeeded at 2960 with fuzz 2 (offset 461 lines).
```



---

archive/issue_comments_081641.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-18T13:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81641",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081642.json:
```json
{
    "body": "Attachment [trac_8894.patch](tarball://root/attachments/some-uuid/ticket8894/trac_8894.patch) by @nathanncohen created at 2011-01-18 17:24:18",
    "created_at": "2011-01-18T17:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81642",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_8894.patch](tarball://root/attachments/some-uuid/ticket8894/trac_8894.patch) by @nathanncohen created at 2011-01-18 17:24:18



---

archive/issue_comments_081643.json:
```json
{
    "body": "Done !\n\nNathann",
    "created_at": "2011-01-18T17:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81643",
    "user": "https://github.com/nathanncohen"
}
```

Done !

Nathann



---

archive/issue_comments_081644.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-18T17:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81644",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_021703.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:19:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8894#event-21703"
}
```



---

archive/issue_comments_081645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8894#issuecomment-81645",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
