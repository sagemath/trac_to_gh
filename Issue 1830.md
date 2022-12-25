# Issue 1830: sage-current-location.txt not unpdated on "make install"

archive/issues_001830.json:
```json
{
    "body": "Assignee: cwitty\n\nwhen running \"DESTDIR=/usr/lib make install\", the file /usr/lib/sage/local/lib/sage-current-location.txt should be updated with the correct new path of $DESTDIR/sage\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1830\n\n",
    "created_at": "2008-01-18T13:42:02Z",
    "labels": [
        "component: relocation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "sage-current-location.txt not unpdated on \"make install\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1830",
    "user": "https://trac.sagemath.org/admin/accounts/users/pgrinber"
}
```
Assignee: cwitty

when running "DESTDIR=/usr/lib make install", the file /usr/lib/sage/local/lib/sage-current-location.txt should be updated with the correct new path of $DESTDIR/sage


Issue created by migration from https://trac.sagemath.org/ticket/1830





---

archive/issue_comments_011557.json:
```json
{
    "body": "I disagree.  /usr/lib/sage/local/lib/sage-current-location.txt should *only* be updated if Sage is actually run in the new location.   And if \"make install\" hasn't run the Sage in the new location, then you better not update that file (or Sage will be installed in a totally broken state).  \n\nMaybe what I'm saying is that \"make install\" should run the Sage in the install location once in order to update sage-current-location.txt.",
    "created_at": "2008-01-18T16:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1830#issuecomment-11557",
    "user": "https://github.com/williamstein"
}
```

I disagree.  /usr/lib/sage/local/lib/sage-current-location.txt should *only* be updated if Sage is actually run in the new location.   And if "make install" hasn't run the Sage in the new location, then you better not update that file (or Sage will be installed in a totally broken state).  

Maybe what I'm saying is that "make install" should run the Sage in the install location once in order to update sage-current-location.txt.



---

archive/issue_comments_011558.json:
```json
{
    "body": "This seems closely related to #3122. The fix that William suggests should be implemented since otherwise people will complain about this issue again in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T04:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1830#issuecomment-11558",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This seems closely related to #3122. The fix that William suggests should be implemented since otherwise people will complain about this issue again in the future.

Cheers,

Michael



---

archive/issue_comments_011559.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-29T10:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1830#issuecomment-11559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_events_001989.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-01T08:31:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1830",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1830#event-1989"
}
```



---

archive/issue_comments_011560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T08:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1830#issuecomment-11560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011561.json:
```json
{
    "body": "This is fixed via #3122.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T08:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1830#issuecomment-11561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is fixed via #3122.

Cheers,

Michael
