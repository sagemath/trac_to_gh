# Issue 302: Improved error reporting for notebook

archive/issues_000302.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf the notebook server gets messed up, the notebook server should display a web page in place of any other pages. \n\nIssue created by migration from https://trac.sagemath.org/ticket/302\n\n",
    "created_at": "2007-03-01T06:04:32Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Improved error reporting for notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/302",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: @williamstein

If the notebook server gets messed up, the notebook server should display a web page in place of any other pages. 

Issue created by migration from https://trac.sagemath.org/ticket/302





---

archive/issue_comments_001433.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-01T18:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1433",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_events_000703.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-03-01T18:07:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/302#event-703"
}
```



---

archive/issue_comments_001434.json:
```json
{
    "body": "This doesn't make sense.  If the notebook server is \"messed up\", then it can't display anything, since it's messed up.  Messed up, means it crashed.",
    "created_at": "2007-03-01T18:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1434",
    "user": "https://github.com/williamstein"
}
```

This doesn't make sense.  If the notebook server is "messed up", then it can't display anything, since it's messed up.  Messed up, means it crashed.



---

archive/issue_comments_001435.json:
```json
{
    "body": "\"chmod -w nb.sobj\" messes up the notebook.\n\n    self.save_notebook_every_so_often()\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/server/notebook/server.py\", line 320, in save_notebook_every_so_often\n    notebook.save()\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 750, in save\n    SageObject.save(self, F, compress=False)\n  File \"sage_object.pyx\", line 139, in sage_object.SageObject.save\nIOError: [Errno 13] Permission denied: '/home/Timothy/sage_notebook/nb.sobj'\n\n---\nlocalhost.localdomain - - [01/Mar/2007 14:22:37] \"GET / HTTP/1.1\" 200 -\nlocalhost.localdomain - - [01/Mar/2007 14:22:37] \"GET /jsmath/plugins/noImageFonts.js HTTP/1.1\" 200 -\nlocalhost.localdomain - - [01/Mar/2007 14:22:37] \"GET /jsmath/jsMath.js HTTP/1.1\" 200 -\nlocalhost.localdomain - - [01/Mar/2007 14:22:37] \"GET /sagelogo.png HTTP/1.1\" 200 -\nlocalhost.localdomain - - [01/Mar/2007 14:22:37] \"GET /corner.png HTTP/1.1\" 200 -\nlocalhost.localdomain - - [01/Mar/2007 14:22:38] \"GET /jsmath/jsMath-fallback-unix.js HTTP/1.1\" 200 -\n\n The notebook stops running computations, however it is still serving web pages. It should stop serving those pages and show an error.",
    "created_at": "2007-03-01T22:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1435",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

"chmod -w nb.sobj" messes up the notebook.

    self.save_notebook_every_so_often()
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/server/notebook/server.py", line 320, in save_notebook_every_so_often
    notebook.save()
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 750, in save
    SageObject.save(self, F, compress=False)
  File "sage_object.pyx", line 139, in sage_object.SageObject.save
IOError: [Errno 13] Permission denied: '/home/Timothy/sage_notebook/nb.sobj'

---
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET / HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /jsmath/plugins/noImageFonts.js HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /jsmath/jsMath.js HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /sagelogo.png HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /corner.png HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:38] "GET /jsmath/jsMath-fallback-unix.js HTTP/1.1" 200 -

 The notebook stops running computations, however it is still serving web pages. It should stop serving those pages and show an error.



---

archive/issue_comments_001436.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-03-01T22:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1436",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_001437.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-03-01T22:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1437",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000704.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans",
    "created_at": "2007-03-01T22:27:51Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/302#event-704"
}
```



---

archive/issue_comments_001438.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-03-26T03:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1438",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001439.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2007-03-26T03:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1439",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing priority from critical to minor.



---

archive/issue_events_000705.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-10T05:32:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/302#event-705"
}
```



---

archive/issue_comments_001440.json:
```json
{
    "body": "Please close this ticket as invalid.",
    "created_at": "2008-07-04T18:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1440",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Please close this ticket as invalid.



---

archive/issue_comments_001441.json:
```json
{
    "body": "Timothy,\n\ncould you give a reason for the record why this should be invalid?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-04T20:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1441",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Timothy,

could you give a reason for the record why this should be invalid?

Cheers,

Michael



---

archive/issue_comments_001442.json:
```json
{
    "body": "I think it should be marked as invalid because we don't have a good list of the errors that could pop up. When we do then this will become more necessary. \n\nFor example on the TRAC server for Knoboo I've seen it report that the server is having database trouble. If we discover that a Sage Notebook can become unusable then this sort of error reporting would become necessary.",
    "created_at": "2008-07-04T21:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1442",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I think it should be marked as invalid because we don't have a good list of the errors that could pop up. When we do then this will become more necessary. 

For example on the TRAC server for Knoboo I've seen it report that the server is having database trouble. If we discover that a Sage Notebook can become unusable then this sort of error reporting would become necessary.



---

archive/issue_events_000706.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-04T21:40:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/302#event-706"
}
```



---

archive/issue_comments_001443.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-04T21:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_001444.json:
```json
{
    "body": "Sounds reasonable to me. Invalidated.",
    "created_at": "2008-07-04T21:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/302#issuecomment-1444",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sounds reasonable to me. Invalidated.



---

archive/issue_events_000707.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-04T21:40:22Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/302",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/302#event-707"
}
```
