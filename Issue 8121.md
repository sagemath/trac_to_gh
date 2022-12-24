# Issue 8121: preparsing of "time" special command inconsistent in company of parenthesis

archive/issues_008121.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @fchapoton\n\nOn the Sage (=IPython) command line:\n\n```\nsage: time (2+2)/3\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n4/3\nsage: time(2+2)/3\n...\nNameError: name 'time' is not defined\n```\n\n\nIn the notebook\n\n```\nsage: time     (2+2)/3\n...\nNameError: name 'time' is not defined\n```\n\n\nThis is happening because in some cases Sage treats \"time <foo>\" as a function call, and sometimes not.  In the notebook it is always a function, when <foo> starts with a paren, but on the command line it is a function only if there is no space between time and (.   \n\nFIX: Make the notebook work exactly the same was as the command line, in this instance.  That seems like a reasonable solution or compromise. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8121\n\n",
    "created_at": "2010-01-29T16:29:52Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "preparsing of \"time\" special command inconsistent in company of parenthesis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8121",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @fchapoton

On the Sage (=IPython) command line:

```
sage: time (2+2)/3
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4/3
sage: time(2+2)/3
...
NameError: name 'time' is not defined
```


In the notebook

```
sage: time     (2+2)/3
...
NameError: name 'time' is not defined
```


This is happening because in some cases Sage treats "time <foo>" as a function call, and sometimes not.  In the notebook it is always a function, when <foo> starts with a paren, but on the command line it is a function only if there is no space between time and (.   

FIX: Make the notebook work exactly the same was as the command line, in this instance.  That seems like a reasonable solution or compromise. 



Issue created by migration from https://trac.sagemath.org/ticket/8121





---

archive/issue_comments_071399.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8121#issuecomment-71399",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071400.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8121#issuecomment-71400",
    "user": "@mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_071401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-22T08:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8121#issuecomment-71401",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071402.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-22T08:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8121#issuecomment-71402",
    "user": "@fchapoton"
}
```

Resolution: invalid
