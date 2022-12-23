# Issue 6370: notebook -- REST search of docs in live mode is completely broken

archive/issues_006370.json:
```json
{
    "body": "Assignee: boothby\n\nTry this:\n\n1. Start the sage notebook and go to this URL:\n\n```\nhttp://localhost:8000/doc/live/reference/sage/games/sudoku.html\n```\n\nYou can do that, e.g, by just clicking on Help, Reference Manual, etc.\n\n2. Try to search for anything, e.g, integer.  \n\n3. It doesn't work at all. \n\n\n\nI consider this a pretty serious bug.  Some ideas:\n\n* make the search box actually bring up the static docs instead, where search *DOES* work\n\n* disable search in the live docs.\n\n* fix the real problem so search works in the live docs as it should.\n\nAny of the above would be way way better than the current situation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6370\n\n",
    "created_at": "2009-06-20T15:38:51Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- REST search of docs in live mode is completely broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6370",
    "user": "was"
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

archive/issue_comments_050946.json:
```json
{
    "body": "I don't see the search box on that page anymore.  However, if you go to the table of contents, there is a search page listed (for example, at /doc/live/tutorial/index.html).  Clicking on the link to the search page gives the error:\n\nPlease activate JavaScript to enable the search functionality. \n\nOf course, javascript is already enabled.",
    "created_at": "2010-05-15T20:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50946",
    "user": "jason"
}
```

I don't see the search box on that page anymore.  However, if you go to the table of contents, there is a search page listed (for example, at /doc/live/tutorial/index.html).  Clicking on the link to the search page gives the error:

Please activate JavaScript to enable the search functionality. 

Of course, javascript is already enabled.



---

archive/issue_comments_050947.json:
```json
{
    "body": "Now the javascript message is also gone, but still no search box.  This is already open upstream at https://github.com/sagemath/sagenb/issues/79.",
    "created_at": "2014-09-17T18:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50947",
    "user": "kcrisman"
}
```

Now the javascript message is also gone, but still no search box.  This is already open upstream at https://github.com/sagemath/sagenb/issues/79.



---

archive/issue_comments_050948.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50948",
    "user": "boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_050949.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6370",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6370#issuecomment-50949",
    "user": "boothby"
}
```

Resolution: invalid
