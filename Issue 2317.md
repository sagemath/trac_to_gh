# Issue 2317: possible job starvation of dsage server

archive/issues_002317.json:
```json
{
    "body": "Assignee: @yqiang\n\nCurrently if a worker gets a job and never submits it back (either maliciously or because of a bug), the server will never know the difference. Hence someone could just ask for a bunch of jobs and never do them, which starves the server of jobs.\n\nProposed fixes:\n1) Server pings the worker which has the job and asks for its status periodically, if the worker does not reply for some number of attempts, reinject the job into the queue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2317\n\n",
    "created_at": "2008-02-26T17:42:21Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "possible job starvation of dsage server",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2317",
    "user": "@yqiang"
}
```
Assignee: @yqiang

Currently if a worker gets a job and never submits it back (either maliciously or because of a bug), the server will never know the difference. Hence someone could just ask for a bunch of jobs and never do them, which starves the server of jobs.

Proposed fixes:
1) Server pings the worker which has the job and asks for its status periodically, if the worker does not reply for some number of attempts, reinject the job into the queue.

Issue created by migration from https://trac.sagemath.org/ticket/2317





---

archive/issue_comments_015419.json:
```json
{
    "body": "Dsage has been deprecated.",
    "created_at": "2010-01-19T07:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2317#issuecomment-15419",
    "user": "@williamstein"
}
```

Dsage has been deprecated.



---

archive/issue_comments_015420.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-19T07:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2317#issuecomment-15420",
    "user": "@williamstein"
}
```

Resolution: wontfix
