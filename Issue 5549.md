# Issue 5549: ?? help in notebook is broken for functions defined in C

archive/issues_005549.json:
```json
{
    "body": "Assignee: tba\n\nAt the command line,\n\n```\nimport scipy\nscipy.sin??\n```\n\nfalls back to just giving the docstring (like `scipy.sin?`), plus an additional notation that says `[source file open failed]`.  In the notebook, the same thing only gives \n\n```\nNo object scipy.sin\n```\n\nThe notebook should fall back to ? help when ?? help fails, like the command line does.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5549\n\n",
    "created_at": "2009-03-17T14:44:44Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "?? help in notebook is broken for functions defined in C",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5549",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: tba

At the command line,

```
import scipy
scipy.sin??
```

falls back to just giving the docstring (like `scipy.sin?`), plus an additional notation that says `[source file open failed]`.  In the notebook, the same thing only gives 

```
No object scipy.sin
```

The notebook should fall back to ? help when ?? help fails, like the command line does.

Issue created by migration from https://trac.sagemath.org/ticket/5549





---

archive/issue_comments_043082.json:
```json
{
    "body": "Confirmed.  This is reported \"upstream\" at [this issue](https://github.com/sagemath/sagenb/issues/207).",
    "created_at": "2014-05-21T13:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5549#issuecomment-43082",
    "user": "https://github.com/kcrisman"
}
```

Confirmed.  This is reported "upstream" at [this issue](https://github.com/sagemath/sagenb/issues/207).



---

archive/issue_comments_043083.json:
```json
{
    "body": "Proposed easier solution is at [this pull request](https://github.com/sagemath/sagenb/pull/209).",
    "created_at": "2014-08-06T03:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5549#issuecomment-43083",
    "user": "https://github.com/kcrisman"
}
```

Proposed easier solution is at [this pull request](https://github.com/sagemath/sagenb/pull/209).



---

archive/issue_comments_043084.json:
```json
{
    "body": "FWIW this appears to be fixed.  I don't know since when, but it's probably been fixed in IPython for a while.  Indeed `??` now falls back on `?` if it can't get the source code of an object.",
    "created_at": "2018-08-10T09:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5549#issuecomment-43084",
    "user": "https://github.com/embray"
}
```

FWIW this appears to be fixed.  I don't know since when, but it's probably been fixed in IPython for a while.  Indeed `??` now falls back on `?` if it can't get the source code of an object.



---

archive/issue_events_005794.json:
```json
{
    "actor": "@embray",
    "created_at": "2018-08-10T09:37:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5549",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5549#event-5794"
}
```



---

archive/issue_comments_043085.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2018-08-10T09:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5549#issuecomment-43085",
    "user": "https://github.com/embray"
}
```

Resolution: worksforme
