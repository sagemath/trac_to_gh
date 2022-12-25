# Issue 2319: change dsage docstrings to match rest of sage

archive/issues_002319.json:
```json
{
    "body": "Assignee: @yqiang\n\nCurrently much of the dsage docstrings are written using reST syntax which apparently Sage does not use. It should be rewritten to be more like the other Sage docstrings. An alternative is for new Sage documentation to be written in something like reST which would allow much easier API doc generation through something like epydoc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2319\n\n",
    "created_at": "2008-02-26T17:45:06Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "change dsage docstrings to match rest of sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2319",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

Currently much of the dsage docstrings are written using reST syntax which apparently Sage does not use. It should be rewritten to be more like the other Sage docstrings. An alternative is for new Sage documentation to be written in something like reST which would allow much easier API doc generation through something like epydoc.

Issue created by migration from https://trac.sagemath.org/ticket/2319





---

archive/issue_comments_015391.json:
```json
{
    "body": "> Currently much of the dsage docstrings are written using reST syntax \n> which apparently Sage does not use. It should be rewritten to be more \n> like the other Sage docstrings. \n> An alternative is for new Sage\n> documentation to be written in something like reST which would \n> allow much easier API doc generation through something like epydoc.\n\nSome comments:\n\n* Sage is MATH SOFTWARE, and as such reST is not what we want -- Latex very much is what we want.  For math, Latex is by far the best choice.  We're definitely not changing the docstring format in the rest of Sage (not an option). \n\n* DSage -- except for the examples -- is not specifically math software.  For dsage, latex is potentially just a nuisance.  \n\nJust keep those points in mind when thinking about this issue.",
    "created_at": "2008-02-27T12:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2319#issuecomment-15391",
    "user": "https://github.com/williamstein"
}
```

> Currently much of the dsage docstrings are written using reST syntax 
> which apparently Sage does not use. It should be rewritten to be more 
> like the other Sage docstrings. 
> An alternative is for new Sage
> documentation to be written in something like reST which would 
> allow much easier API doc generation through something like epydoc.

Some comments:

* Sage is MATH SOFTWARE, and as such reST is not what we want -- Latex very much is what we want.  For math, Latex is by far the best choice.  We're definitely not changing the docstring format in the rest of Sage (not an option). 

* DSage -- except for the examples -- is not specifically math software.  For dsage, latex is potentially just a nuisance.  

Just keep those points in mind when thinking about this issue.



---

archive/issue_comments_015392.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-19T07:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2319#issuecomment-15392",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_015393.json:
```json
{
    "body": "Dsage has been deprecated.",
    "created_at": "2010-01-19T07:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2319#issuecomment-15393",
    "user": "https://github.com/williamstein"
}
```

Dsage has been deprecated.



---

archive/issue_events_002495.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-19T07:39:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2319",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2319#event-2495"
}
```
