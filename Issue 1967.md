# Issue 1967: fix matplotlib local-related bugs once and for all (?)

archive/issues_001967.json:
```json
{
    "body": "Assignee: @williamstein\n\nMany people have reported issues with locale.py going boom on quite a range of different OS X (and Linux?) machines.  The very slightly patched version of \n\n  SAGE_ROOT/local/lib/python2.5/site-packages/matplotlib/cbook.py\n\nattached to this ticket may very likely fix the problem.  See this thread:\n  \n  http://groups.google.com/group/sage-support/browse_thread/thread/edcf2740f7276e6a?hl=en#78ee7d78a0a99f12\n\nIf this really turns out to be the fix, cbook.py should be put into the matplotlib spkg as a patch. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1967\n\n",
    "created_at": "2008-01-29T09:57:58Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "fix matplotlib local-related bugs once and for all (?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1967",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Many people have reported issues with locale.py going boom on quite a range of different OS X (and Linux?) machines.  The very slightly patched version of 

  SAGE_ROOT/local/lib/python2.5/site-packages/matplotlib/cbook.py

attached to this ticket may very likely fix the problem.  See this thread:
  
  http://groups.google.com/group/sage-support/browse_thread/thread/edcf2740f7276e6a?hl=en#78ee7d78a0a99f12

If this really turns out to be the fix, cbook.py should be put into the matplotlib spkg as a patch. 



Issue created by migration from https://trac.sagemath.org/ticket/1967





---

archive/issue_comments_012707.json:
```json
{
    "body": "Attachment [cbook.py](tarball://root/attachments/some-uuid/ticket1967/cbook.py) by mabshoff created at 2008-02-01 00:42:04\n\nThe spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/matplotlib-0.91.1.p3.spkg\n\nfixes this issue as well as #2014\n\nCheers,\n\nMichael",
    "created_at": "2008-02-01T00:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1967#issuecomment-12707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [cbook.py](tarball://root/attachments/some-uuid/ticket1967/cbook.py) by mabshoff created at 2008-02-01 00:42:04

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc4/matplotlib-0.91.1.p3.spkg

fixes this issue as well as #2014

Cheers,

Michael



---

archive/issue_events_004765.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-01T02:00:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1967",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1967#event-4765"
}
```



---

archive/issue_comments_012708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T02:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1967#issuecomment-12708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012709.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T02:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1967#issuecomment-12709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc4
