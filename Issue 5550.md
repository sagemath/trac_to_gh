# Issue 5550: .../doc/output/html/en/index.html should include "/index.html" in links

archive/issues_005550.json:
```json
{
    "body": "Assignee: tba\n\nThe web page produced for \"all the documentation\" at .../doc/output/html/en/index.html doesn't work when browsing the documentation locally with `file:///` URLs, because the \".../\" -> \".../index.html\" redirect is done by the web server, and there's no web server involved for `file:///`.  So clicking on \"Reference Manual\" brings you to a directory listing for the reference manual, not to the index.html that lets you actually read the reference manual.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5550\n\n",
    "created_at": "2009-03-17T15:04:43Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": ".../doc/output/html/en/index.html should include \"/index.html\" in links",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5550",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: tba

The web page produced for "all the documentation" at .../doc/output/html/en/index.html doesn't work when browsing the documentation locally with `file:///` URLs, because the ".../" -> ".../index.html" redirect is done by the web server, and there's no web server involved for `file:///`.  So clicking on "Reference Manual" brings you to a directory listing for the reference manual, not to the index.html that lets you actually read the reference manual.

Issue created by migration from https://trac.sagemath.org/ticket/5550





---

archive/issue_comments_043086.json:
```json
{
    "body": "Ticket #6485 seems to be a duplicate of this one. I suggest we close this one and keep #6485, since there is already a patch there.",
    "created_at": "2009-07-13T16:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5550#issuecomment-43086",
    "user": "https://github.com/loefflerd"
}
```

Ticket #6485 seems to be a duplicate of this one. I suggest we close this one and keep #6485, since there is already a patch there.



---

archive/issue_events_005795.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-18T20:15:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5550",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5550#event-5795"
}
```



---

archive/issue_comments_043087.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-18T20:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5550#issuecomment-43087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate
