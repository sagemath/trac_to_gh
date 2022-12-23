# Issue 408: Notebook glitch in Safari

archive/issues_000408.json:
```json
{
    "body": "Assignee: was\n\nThis is on Mac OS X, 10.4.10, with Safari, using SAGE 2.7.1.\n\nIf I create a worksheet, fiddle around with it, and then quit and restart the server,\ngoing to \"localhost/8000\" gives me a page with the worksheet shown (as possibly\none of many).  If I click the adjacent check box and then the DELETE button, the\ncheck box is cleared but the worksheet entry remains.  Only when I 'refresh' the page\ndoes the worksheet entry disappear.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/408\n\n",
    "created_at": "2007-07-27T05:16:05Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Notebook glitch in Safari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/408",
    "user": "justin"
}
```
Assignee: was

This is on Mac OS X, 10.4.10, with Safari, using SAGE 2.7.1.

If I create a worksheet, fiddle around with it, and then quit and restart the server,
going to "localhost/8000" gives me a page with the worksheet shown (as possibly
one of many).  If I click the adjacent check box and then the DELETE button, the
check box is cleared but the worksheet entry remains.  Only when I 'refresh' the page
does the worksheet entry disappear.


Issue created by migration from https://trac.sagemath.org/ticket/408





---

archive/issue_comments_002007.json:
```json
{
    "body": "Oh: on a MacBook Pro, FWIW.",
    "created_at": "2007-07-27T05:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2007",
    "user": "justin"
}
```

Oh: on a MacBook Pro, FWIW.



---

archive/issue_comments_002008.json:
```json
{
    "body": "Changing assignee from was to boothby.",
    "created_at": "2007-07-27T19:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2008",
    "user": "was"
}
```

Changing assignee from was to boothby.



---

archive/issue_comments_002009.json:
```json
{
    "body": "Changing component from algebraic geometry to notebook.",
    "created_at": "2007-07-27T19:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2009",
    "user": "was"
}
```

Changing component from algebraic geometry to notebook.



---

archive/issue_comments_002010.json:
```json
{
    "body": "I think this is indeed safari-specific.  I think for some reason safari doesn't\nupdate the page when the javascript attempts a refresh, though firefox does.\nWe need to either directly modify the DOM (more work, but the right thing to do), \nor improve the refresh() javascript function so it also works with safari.",
    "created_at": "2007-07-27T19:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2010",
    "user": "was"
}
```

I think this is indeed safari-specific.  I think for some reason safari doesn't
update the page when the javascript attempts a refresh, though firefox does.
We need to either directly modify the DOM (more work, but the right thing to do), 
or improve the refresh() javascript function so it also works with safari.



---

archive/issue_comments_002011.json:
```json
{
    "body": "This is really an enhancement -- i.e., this dynamic stuff needs to be implemented for that screen (without\nusing refresh).",
    "created_at": "2007-08-19T08:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2011",
    "user": "was"
}
```

This is really an enhancement -- i.e., this dynamic stuff needs to be implemented for that screen (without
using refresh).



---

archive/issue_comments_002012.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-19T08:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2012",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_002013.json:
```json
{
    "body": "This is quite an old ticket. Can somebody check with 3.0 if this is still a problem?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T07:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2013",
    "user": "mabshoff"
}
```

This is quite an old ticket. Can somebody check with 3.0 if this is still a problem?

Cheers,

Michael



---

archive/issue_comments_002014.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-10T20:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2014",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002015.json:
```json
{
    "body": "I fixed this.  It is no longer a problem.",
    "created_at": "2008-05-10T20:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/408#issuecomment-2015",
    "user": "was"
}
```

I fixed this.  It is no longer a problem.
