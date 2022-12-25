# Issue 5481: devel/doc/output/* should be filtered from the list of files to doctest

archive/issues_005481.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mwhansen\n\nThere can be many rst files under devel/doc/output - those should be filtered from the list of files to doctest since they are duplicate doctests from the main Sage library in many cases.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5481\n\n",
    "created_at": "2009-03-11T06:31:10Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "devel/doc/output/* should be filtered from the list of files to doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5481",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @mwhansen

There can be many rst files under devel/doc/output - those should be filtered from the list of files to doctest since they are duplicate doctests from the main Sage library in many cases.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5481





---

archive/issue_comments_042441.json:
```json
{
    "body": "Has this been fixed?  The file sage-maketest looks good to me already.",
    "created_at": "2009-06-09T22:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42441",
    "user": "https://github.com/jhpalmieri"
}
```

Has this been fixed?  The file sage-maketest looks good to me already.



---

archive/issue_comments_042442.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42442",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_042443.json:
```json
{
    "body": "Maybe sage-ptest needs changing.  I'm still trying to figure out what the issue is here.",
    "created_at": "2009-06-16T03:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42443",
    "user": "https://github.com/jhpalmieri"
}
```

Maybe sage-ptest needs changing.  I'm still trying to figure out what the issue is here.



---

archive/issue_comments_042444.json:
```json
{
    "body": "Attachment [trac_5481_scripts.patch](tarball://root/attachments/some-uuid/ticket5481/trac_5481_scripts.patch) by @jhpalmieri created at 2009-06-16 03:28:03\n\nHere's a patch.  (The first change -- deleting all.py and __init__.py -- comes from #6108.)",
    "created_at": "2009-06-16T03:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42444",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_5481_scripts.patch](tarball://root/attachments/some-uuid/ticket5481/trac_5481_scripts.patch) by @jhpalmieri created at 2009-06-16 03:28:03

Here's a patch.  (The first change -- deleting all.py and __init__.py -- comes from #6108.)



---

archive/issue_comments_042445.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-20T01:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42445",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_042446.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T01:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42446",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042447.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T01:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42447",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_042448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5481#issuecomment-42448",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed



---

archive/issue_events_005735.json:
```json
{
    "actor": "boothby",
    "created_at": "2009-06-26T17:43:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5481",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5481#event-5735"
}
```
