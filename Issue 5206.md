# Issue 5206: attach command doesn't handle carriage returns correctly

archive/issues_005206.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: attach\n\nThis problem is specific to attaching files ending with \".py\" in the notebook.  It does not seem to affect the command-line, or files ending with \".sage\".  Some files that are moved around from different filesystems and editors end up having end-of-line commands that look like: \"\\r\\n\".  These raise a syntax error when attached.  Here is an example (of course you need to change the path):\n\n\n```\ntestfile = file('/home/marshall/Desktop/misc/testrn.py','w')\ntestfile.write('my_var = 2\\r\\n')\ntestfile.close()\nattach /home/marshall/Desktop/misc/testrn.py\n\n    Syntax Error:\n        attach /home/marshall/Desktop/misc/testrn.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5206\n\n",
    "created_at": "2009-02-08T08:18:24Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "attach command doesn't handle carriage returns correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: boothby

Keywords: attach

This problem is specific to attaching files ending with ".py" in the notebook.  It does not seem to affect the command-line, or files ending with ".sage".  Some files that are moved around from different filesystems and editors end up having end-of-line commands that look like: "\r\n".  These raise a syntax error when attached.  Here is an example (of course you need to change the path):


```
testfile = file('/home/marshall/Desktop/misc/testrn.py','w')
testfile.write('my_var = 2\r\n')
testfile.close()
attach /home/marshall/Desktop/misc/testrn.py

    Syntax Error:
        attach /home/marshall/Desktop/misc/testrn.py
```


Issue created by migration from https://trac.sagemath.org/ticket/5206





---

archive/issue_comments_039813.json:
```json
{
    "body": "No ticket without patches that aren't blockers should be assigned to 3.3 or 3.4 at this stage.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T08:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5206#issuecomment-39813",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

No ticket without patches that aren't blockers should be assigned to 3.3 or 3.4 at this stage.

Cheers,

Michael



---

archive/issue_comments_039814.json:
```json
{
    "body": "This seems to be fixed already (probably by #7514).",
    "created_at": "2010-01-17T10:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5206#issuecomment-39814",
    "user": "https://github.com/TimDumol"
}
```

This seems to be fixed already (probably by #7514).



---

archive/issue_events_005461.json:
```json
{
    "actor": "@TimDumol",
    "created_at": "2010-01-19T02:59:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5206",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5206#event-5461"
}
```



---

archive/issue_comments_039815.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T02:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5206#issuecomment-39815",
    "user": "https://github.com/TimDumol"
}
```

Resolution: duplicate



---

archive/issue_comments_039816.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-01-19T03:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5206#issuecomment-39816",
    "user": "https://github.com/TimDumol"
}
```

Resolution changed from duplicate to fixed
