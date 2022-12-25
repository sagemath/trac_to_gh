# Issue 408: Notebook glitch in Safari

archive/issues_000408.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is on Mac OS X, 10.4.10, with Safari, using SAGE 2.7.1.\n\nIf I create a worksheet, fiddle around with it, and then quit and restart the server,\ngoing to \"localhost/8000\" gives me a page with the worksheet shown (as possibly\none of many).  If I click the adjacent check box and then the DELETE button, the\ncheck box is cleared but the worksheet entry remains.  Only when I 'refresh' the page\ndoes the worksheet entry disappear.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/408\n\n",
    "created_at": "2007-07-27T05:16:05Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Notebook glitch in Safari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/408",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

This is on Mac OS X, 10.4.10, with Safari, using SAGE 2.7.1.

If I create a worksheet, fiddle around with it, and then quit and restart the server,
going to "localhost/8000" gives me a page with the worksheet shown (as possibly
one of many).  If I click the adjacent check box and then the DELETE button, the
check box is cleared but the worksheet entry remains.  Only when I 'refresh' the page
does the worksheet entry disappear.


Issue created by migration from https://trac.sagemath.org/ticket/408





---

archive/issue_comments_001998.json:
```json
{
    "body": "Oh: on a MacBook Pro, FWIW.",
    "created_at": "2007-07-27T05:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-1998",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Oh: on a MacBook Pro, FWIW.



---

archive/issue_comments_001999.json:
```json
{
    "body": "Changing assignee from @williamstein to boothby.",
    "created_at": "2007-07-27T19:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-1999",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @williamstein to boothby.



---

archive/issue_comments_002000.json:
```json
{
    "body": "Changing component from algebraic geometry to notebook.",
    "created_at": "2007-07-27T19:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2000",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to notebook.



---

archive/issue_comments_002001.json:
```json
{
    "body": "I think this is indeed safari-specific.  I think for some reason safari doesn't\nupdate the page when the javascript attempts a refresh, though firefox does.\nWe need to either directly modify the DOM (more work, but the right thing to do), \nor improve the refresh() javascript function so it also works with safari.",
    "created_at": "2007-07-27T19:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2001",
    "user": "https://github.com/williamstein"
}
```

I think this is indeed safari-specific.  I think for some reason safari doesn't
update the page when the javascript attempts a refresh, though firefox does.
We need to either directly modify the DOM (more work, but the right thing to do), 
or improve the refresh() javascript function so it also works with safari.



---

archive/issue_comments_002002.json:
```json
{
    "body": "This is really an enhancement -- i.e., this dynamic stuff needs to be implemented for that screen (without\nusing refresh).",
    "created_at": "2007-08-19T08:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2002",
    "user": "https://github.com/williamstein"
}
```

This is really an enhancement -- i.e., this dynamic stuff needs to be implemented for that screen (without
using refresh).



---

archive/issue_comments_002003.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-19T08:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2003",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_002004.json:
```json
{
    "body": "This is quite an old ticket. Can somebody check with 3.0 if this is still a problem?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T07:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2004",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is quite an old ticket. Can somebody check with 3.0 if this is still a problem?

Cheers,

Michael



---

archive/issue_comments_002005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-10T20:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2005",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002006.json:
```json
{
    "body": "I fixed this.  It is no longer a problem.",
    "created_at": "2008-05-10T20:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2006",
    "user": "https://github.com/williamstein"
}
```

I fixed this.  It is no longer a problem.



---

archive/issue_events_000434.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2008-05-10T20:30:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/408#event-434"
}
```
