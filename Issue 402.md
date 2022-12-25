# Issue 402: %slide directive produces segfault in dvipng

archive/issues_000402.json:
```json
{
    "body": "Assignee: boothby\n\nCurrently, both in sage 2.6 and William's online notebook (which I guess is also sage 2.6)\n\n```\n%slide\nsome text here\n```\n\nfails with\n\n```\nsh: line 1: 23279 Segmentation fault      dvipng -q* -T bbox -D 256 sage6.dvi\n>/dev/null 2>/dev/null\nAn error occured.\n[...]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/402\n\n",
    "created_at": "2007-07-11T20:25:07Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "%slide directive produces segfault in dvipng",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/402",
    "user": "https://github.com/nbruin"
}
```
Assignee: boothby

Currently, both in sage 2.6 and William's online notebook (which I guess is also sage 2.6)

```
%slide
some text here
```

fails with

```
sh: line 1: 23279 Segmentation fault      dvipng -q* -T bbox -D 256 sage6.dvi
>/dev/null 2>/dev/null
An error occured.
[...]
```


Issue created by migration from https://trac.sagemath.org/ticket/402





---

archive/issue_comments_001968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T23:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/402#issuecomment-1968",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000428.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T23:34:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/402",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/402#event-428"
}
```
