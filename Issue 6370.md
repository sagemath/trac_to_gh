# Issue 6370: notebook -- REST search of docs in live mode is completely broken

archive/issues_006370.json:
```json
{
    "body": "Assignee: boothby\n\nTry this:\n\n1. Start the sage notebook and go to this URL:\n\n```\nhttp://localhost:8000/doc/live/reference/sage/games/sudoku.html\n```\nYou can do that, e.g, by just clicking on Help, Reference Manual, etc.\n\n2. Try to search for anything, e.g, integer.  \n\n3. It doesn't work at all. \n\n\n\nI consider this a pretty serious bug.  Some ideas:\n\n* make the search box actually bring up the static docs instead, where search *DOES* work\n\n* disable search in the live docs.\n\n* fix the real problem so search works in the live docs as it should.\n\nAny of the above would be way way better than the current situation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6370\n\n",
    "created_at": "2009-06-20T15:38:51Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "notebook -- REST search of docs in live mode is completely broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6370",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Try this:

1. Start the sage notebook and go to this URL:

```
http://localhost:8000/doc/live/reference/sage/games/sudoku.html
```
You can do that, e.g, by just clicking on Help, Reference Manual, etc.

2. Try to search for anything, e.g, integer.  

3. It doesn't work at all. 



I consider this a pretty serious bug.  Some ideas:

* make the search box actually bring up the static docs instead, where search *DOES* work

* disable search in the live docs.

* fix the real problem so search works in the live docs as it should.

Any of the above would be way way better than the current situation.

Issue created by migration from https://trac.sagemath.org/ticket/6370





---

archive/issue_comments_050849.json:
```json
{
    "body": "I don't see the search box on that page anymore.  However, if you go to the table of contents, there is a search page listed (for example, at /doc/live/tutorial/index.html).  Clicking on the link to the search page gives the error:\n\nPlease activate JavaScript to enable the search functionality. \n\nOf course, javascript is already enabled.",
    "created_at": "2010-05-15T20:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50849",
    "user": "https://github.com/jasongrout"
}
```

I don't see the search box on that page anymore.  However, if you go to the table of contents, there is a search page listed (for example, at /doc/live/tutorial/index.html).  Clicking on the link to the search page gives the error:

Please activate JavaScript to enable the search functionality. 

Of course, javascript is already enabled.



---

archive/issue_events_014996.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-14996"
}
```



---

archive/issue_events_014997.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-14997"
}
```



---

archive/issue_events_014998.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-14998"
}
```



---

archive/issue_events_014999.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-14999"
}
```



---

archive/issue_events_015000.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-15000"
}
```



---

archive/issue_events_015001.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-15001"
}
```



---

archive/issue_events_015002.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-15002"
}
```



---

archive/issue_comments_050850.json:
```json
{
    "body": "Now the javascript message is also gone, but still no search box.  This is already open upstream at https://github.com/sagemath/sagenb/issues/79.",
    "created_at": "2014-09-17T18:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50850",
    "user": "https://github.com/kcrisman"
}
```

Now the javascript message is also gone, but still no search box.  This is already open upstream at https://github.com/sagemath/sagenb/issues/79.



---

archive/issue_events_015003.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2020-03-29T02:12:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6370#event-15003"
}
```



---

archive/issue_comments_050851.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50851",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_050852.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50852",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: invalid
