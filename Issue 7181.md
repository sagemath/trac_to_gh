# Issue 7181: We must ensure we have GNU make, not HP-UX or Solaris 'make'

archive/issues_007181.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: HP-UX Solaris make\n\nAlthough I noticed this issue on HP-UX, I know it affects Solaris too. The 'make' program certainly can not be Sun's on Solaris, and while it looks like a minor mod would allow the 'make' on HP-UX to work, it seems sensible we just check for GNU make.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7181\n\n",
    "created_at": "2009-10-10T09:30:33Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "We must ensure we have GNU make, not HP-UX or Solaris 'make'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7181",
    "user": "drkirkby"
}
```
Assignee: tbd

Keywords: HP-UX Solaris make

Although I noticed this issue on HP-UX, I know it affects Solaris too. The 'make' program certainly can not be Sun's on Solaris, and while it looks like a minor mod would allow the 'make' on HP-UX to work, it seems sensible we just check for GNU make.

Issue created by migration from https://trac.sagemath.org/ticket/7181





---

archive/issue_comments_059479.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T06:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7181#issuecomment-59479",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059480.json:
```json
{
    "body": "Fixed by #7352",
    "created_at": "2009-11-20T06:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7181#issuecomment-59480",
    "user": "mhansen"
}
```

Fixed by #7352
