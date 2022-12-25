# Issue 7242: Convert sage to use the new standard libary multiprocessing module rather than processing

archive/issues_007242.json:
```json
{
    "body": "Assignee: mabshoff\n\nI notice that sage is still including the Python processing module.  It \nseems that in Python 2.6, a version of the processing module was merged   \ninto the Python standard library under the name \"multiprocessing\".  I am  \ntold that it should be possible to convert by just replacing the references to processing with new ones to multiprocessing.\n\nSee <http://www.python.org/dev/peps/pep-0371/>\n\nWe should then be able to drop the \"processing\" spkg.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7242\n\n",
    "created_at": "2009-10-18T23:46:15Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Convert sage to use the new standard libary multiprocessing module rather than processing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7242",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

I notice that sage is still including the Python processing module.  It 
seems that in Python 2.6, a version of the processing module was merged   
into the Python standard library under the name "multiprocessing".  I am  
told that it should be possible to convert by just replacing the references to processing with new ones to multiprocessing.

See <http://www.python.org/dev/peps/pep-0371/>

We should then be able to drop the "processing" spkg.


Issue created by migration from https://trac.sagemath.org/ticket/7242





---

archive/issue_comments_060020.json:
```json
{
    "body": "Duplicate of #6503.  I'll get to this today.",
    "created_at": "2009-10-19T04:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7242#issuecomment-60020",
    "user": "https://github.com/mwhansen"
}
```

Duplicate of #6503.  I'll get to this today.



---

archive/issue_events_007461.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-19T04:28:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7242",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7242#event-7461"
}
```



---

archive/issue_comments_060021.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-19T04:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7242#issuecomment-60021",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate
