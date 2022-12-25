# Issue 1403: mwrank: crash upon exit

archive/issues_001403.json:
```json
{
    "body": "Assignee: @williamstein\n\nJustin Walker reported:\n\n```\n'mwrank' doesn't like it if you just exit (by typing \"^D\" or, more or  \nless equivalently, by \"ending a file\").\n\nThus, if you run 'mwrank' and give it a file containing, for example,  \n\"[0,0,1,-1,0]\" and nothing else, it will barf at the end.  If your  \nfile contains \"[0,0,0,0,0]\", the program sweetly closes up shop (when  \nit reads this) and quits.\n\nThe error I get is\n   bad ZZ input\n   Abort trap\n\nAnyone know why this doesn't show up in the test logs?  Is it worth  \ntracking down?\n\nThe issue is that the terminating condition for input processing in  \n'getcurve()' is a \"null curve\" (\"\"[0,0,0,0,0]\"\"), rather than EOF.  \nAn EOF is an error condition, hence the abort(). \n```\n\n\nSee also #1402.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1403\n\n",
    "created_at": "2007-12-05T11:42:07Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "mwrank: crash upon exit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Justin Walker reported:

```
'mwrank' doesn't like it if you just exit (by typing "^D" or, more or  
less equivalently, by "ending a file").

Thus, if you run 'mwrank' and give it a file containing, for example,  
"[0,0,1,-1,0]" and nothing else, it will barf at the end.  If your  
file contains "[0,0,0,0,0]", the program sweetly closes up shop (when  
it reads this) and quits.

The error I get is
   bad ZZ input
   Abort trap

Anyone know why this doesn't show up in the test logs?  Is it worth  
tracking down?

The issue is that the terminating condition for input processing in  
'getcurve()' is a "null curve" (""[0,0,0,0,0]""), rather than EOF.  
An EOF is an error condition, hence the abort(). 
```


See also #1402.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1403





---

archive/issue_comments_009025.json:
```json
{
    "body": "John Cremona wrote:\n\n```\ni.e. mwrank crashed rather than stopping cleanly when reachinf EOF on\ninput.  Should be an easy fix to qrank/getcurve.cc, so I'll do it.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T19:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John Cremona wrote:

```
i.e. mwrank crashed rather than stopping cleanly when reachinf EOF on
input.  Should be an easy fix to qrank/getcurve.cc, so I'll do it.
```


Cheers,

Michael



---

archive/issue_comments_009026.json:
```json
{
    "body": "patch for file qrank/getcurve.cc which fixes the problem",
    "created_at": "2007-12-05T20:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9026",
    "user": "https://github.com/JohnCremona"
}
```

patch for file qrank/getcurve.cc which fixes the problem



---

archive/issue_comments_009027.json:
```json
{
    "body": "Attachment [getcurve.patch](tarball://root/attachments/some-uuid/ticket1403/getcurve.patch) by @JohnCremona created at 2007-12-05 20:23:15\n\nI have fixed this.  Patch attached.  JEC",
    "created_at": "2007-12-05T20:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9027",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [getcurve.patch](tarball://root/attachments/some-uuid/ticket1403/getcurve.patch) by @JohnCremona created at 2007-12-05 20:23:15

I have fixed this.  Patch attached.  JEC



---

archive/issue_events_001547.json:
```json
{
    "actor": "@JohnCremona",
    "created_at": "2007-12-05T20:23:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1403#event-1547"
}
```



---

archive/issue_comments_009028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-05T20:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9028",
    "user": "https://github.com/JohnCremona"
}
```

Resolution: fixed



---

archive/issue_comments_009029.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-05T21:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9029",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009030.json:
```json
{
    "body": "Hello John,\n\nthe release manager usually closes the ticket once the patch has been applied into the current release tree. That way we do not lose fixes.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T21:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello John,

the release manager usually closes the ticket once the patch has been applied into the current release tree. That way we do not lose fixes.

Cheers,

Michael



---

archive/issue_comments_009031.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-05T21:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001548.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-05T21:13:52Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1403#event-1548"
}
```



---

archive/issue_comments_009032.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha0.



---

archive/issue_comments_009033.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9033",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001549.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-06T02:04:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1403#event-1549"
}
```



---

archive/issue_comments_009034.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha0.



---

archive/issue_comments_009035.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-06T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9035",
    "user": "https://github.com/JohnCremona"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009036.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-06T09:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9036",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001550.json:
```json
{
    "actor": "@JohnCremona",
    "created_at": "2007-12-06T09:06:57Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1403#event-1550"
}
```



---

archive/issue_comments_009037.json:
```json
{
    "body": "Attachment [reader.h.patch](tarball://root/attachments/some-uuid/ticket1403/reader.h.patch) by @JohnCremona created at 2007-12-06 09:09:08\n\nSecond patch file reader.h.patch to be applied to qcurves/reader.h will stop the same happening for other binaries (e.g. tate, conductor etc) built in the qcurves directory.",
    "created_at": "2007-12-06T09:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9037",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [reader.h.patch](tarball://root/attachments/some-uuid/ticket1403/reader.h.patch) by @JohnCremona created at 2007-12-06 09:09:08

Second patch file reader.h.patch to be applied to qcurves/reader.h will stop the same happening for other binaries (e.g. tate, conductor etc) built in the qcurves directory.



---

archive/issue_comments_009038.json:
```json
{
    "body": "Second patch merged in 2.9.alpha1.",
    "created_at": "2007-12-06T13:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9038",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Second patch merged in 2.9.alpha1.



---

archive/issue_events_001551.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-06T13:13:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1403#event-1551"
}
```



---

archive/issue_comments_009039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T13:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1403",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1403#issuecomment-9039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
