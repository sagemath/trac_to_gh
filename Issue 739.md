# Issue 739: hang doctesting const.tex

archive/issues_000739.json:
```json
{
    "body": "Assignee: failure\n\nMany people (John Cremona and David Harvey at least) had the following problem:\n\n```\nI upgraded to 2.8.5 ok (kubuntu 7.04, kernel 2.6.20-16-generic, gcc\nversion 4.1.2).\n\nsage --testall hangs at this point:\nTesting SAGE constructions guide\nsage -t  const.tex\n\nand \"ps -ux\" shows that all the processes are in swap (S status).\nAlso Ctrl-C did not kill it, I am having to kill all the processes one\nby one.\n\nJohn\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/739\n\n",
    "closed_at": "2007-09-23T21:41:56Z",
    "created_at": "2007-09-22T22:02:03Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5.1",
    "title": "hang doctesting const.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/739",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

Many people (John Cremona and David Harvey at least) had the following problem:

```
I upgraded to 2.8.5 ok (kubuntu 7.04, kernel 2.6.20-16-generic, gcc
version 4.1.2).

sage --testall hangs at this point:
Testing SAGE constructions guide
sage -t  const.tex

and "ps -ux" shows that all the processes are in swap (S status).
Also Ctrl-C did not kill it, I am having to kill all the processes one
by one.

John
```

Issue created by migration from https://trac.sagemath.org/ticket/739





---

archive/issue_comments_004313.json:
```json
{
    "body": "It turns out that \"hangs forever\" means takes longer than 30 seconds for many people :-). \nThis actually works fine -- it's just that const.tex is really long (nearly a minute!).",
    "created_at": "2007-09-23T21:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/739#issuecomment-4313",
    "user": "https://github.com/williamstein"
}
```

It turns out that "hangs forever" means takes longer than 30 seconds for many people :-). 
This actually works fine -- it's just that const.tex is really long (nearly a minute!).



---

archive/issue_comments_004314.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-09-23T21:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/739#issuecomment-4314",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_events_002014.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-23T21:41:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/739",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/739#event-2014"
}
```
