# Issue 4547: The Sage Notebook doesn't specify the Content-Type header in its responses

archive/issues_004547.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  jason\n\nThis causes Apache rewriting for example to just display plain text instead of HTML.  This hasn't been an issue because browsers are relatively smart about dealing with unspecified Content-Types.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4547\n\n",
    "created_at": "2008-11-19T15:01:12Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "The Sage Notebook doesn't specify the Content-Type header in its responses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4547",
    "user": "mhansen"
}
```
Assignee: boothby

CC:  jason

This causes Apache rewriting for example to just display plain text instead of HTML.  This hasn't been an issue because browsers are relatively smart about dealing with unspecified Content-Types.

Issue created by migration from https://trac.sagemath.org/ticket/4547





---

archive/issue_comments_034058.json:
```json
{
    "body": "I attached a patch (which may or may not apply to the current version) which only fixes the problem for HTML pages.  CSS, Javascript, etc. should also be handled.",
    "created_at": "2008-11-19T15:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34058",
    "user": "mhansen"
}
```

I attached a patch (which may or may not apply to the current version) which only fixes the problem for HTML pages.  CSS, Javascript, etc. should also be handled.



---

archive/issue_comments_034059.json:
```json
{
    "body": "This *has* been an issue.   I have been working around by putting this in my httpd.conf:\n\n```\n\n<VirtualHost *>\n        ServerName sagenb.org\n        ProxyPass    / http://sagenb.org:8000/\n        ProxyPassReverse / http://sagenb.org:8000/\n\n        <Location />\n           DefaultType text/html\n        </Location>\n</VirtualHost>\n\n\n```\n",
    "created_at": "2008-11-20T05:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34059",
    "user": "was"
}
```

This *has* been an issue.   I have been working around by putting this in my httpd.conf:

```

<VirtualHost *>
        ServerName sagenb.org
        ProxyPass    / http://sagenb.org:8000/
        ProxyPassReverse / http://sagenb.org:8000/

        <Location />
           DefaultType text/html
        </Location>
</VirtualHost>


```




---

archive/issue_comments_034060.json:
```json
{
    "body": "I rebased Mike's patch against 3.3.alpha6, and added a \"charset: utf-8\" bit; this ticket is in some sense the other half of #5211.\n\nThis ticket was originally motivated by Apache rewriting; I'm here because some users have UTF-8 text in their worksheets and browsers are not always figuring out the correct encoding. If my patch fixes the encoding/browser problems, perhaps we should merge this ticket and open another for adding Content-Type headers to CSS, Javascript, and so on.",
    "created_at": "2009-02-10T09:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34060",
    "user": "ddrake"
}
```

I rebased Mike's patch against 3.3.alpha6, and added a "charset: utf-8" bit; this ticket is in some sense the other half of #5211.

This ticket was originally motivated by Apache rewriting; I'm here because some users have UTF-8 text in their worksheets and browsers are not always figuring out the correct encoding. If my patch fixes the encoding/browser problems, perhaps we should merge this ticket and open another for adding Content-Type headers to CSS, Javascript, and so on.



---

archive/issue_comments_034061.json:
```json
{
    "body": "Since you rebased the patch please change the summary to \"needs review\" as I just did. Otherwise it will just bitrot since no one will know it is even there :(\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T09:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34061",
    "user": "mabshoff"
}
```

Since you rebased the patch please change the summary to "needs review" as I just did. Otherwise it will just bitrot since no one will know it is even there :(

Cheers,

Michael



---

archive/issue_comments_034062.json:
```json
{
    "body": "Well, looking around further into the ticket history it seems that additional work is needed. But if this patch does get a positive review I would recommend to open another ticket to deal with CSS and javasscript encoding settings, even though this is somewhat less pressing (who adds  utf-8 characters into CSS or javasscript?).\n\nMike: any take on this?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T09:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34062",
    "user": "mabshoff"
}
```

Well, looking around further into the ticket history it seems that additional work is needed. But if this patch does get a positive review I would recommend to open another ticket to deal with CSS and javasscript encoding settings, even though this is somewhat less pressing (who adds  utf-8 characters into CSS or javasscript?).

Mike: any take on this?

Cheers,

Michael



---

archive/issue_comments_034063.json:
```json
{
    "body": "I've rebased the patch against 3.4.alpha0 -- that's \"trac_4547-ddrake.2.patch\", which is the only one of the three patches which needs to be applied.",
    "created_at": "2009-03-02T06:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34063",
    "user": "ddrake"
}
```

I've rebased the patch against 3.4.alpha0 -- that's "trac_4547-ddrake.2.patch", which is the only one of the three patches which needs to be applied.



---

archive/issue_comments_034064.json:
```json
{
    "body": "apply trac-4547_3.patch",
    "created_at": "2009-03-16T20:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34064",
    "user": "TimothyClemans"
}
```

apply trac-4547_3.patch



---

archive/issue_comments_034065.json:
```json
{
    "body": "Depends on #4135",
    "created_at": "2009-03-16T20:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34065",
    "user": "TimothyClemans"
}
```

Depends on #4135



---

archive/issue_comments_034066.json:
```json
{
    "body": "I've noticed that some javascript and css doesn't have content-type headers being sent (but some do); should we open separate tickets for those as well?\n\nAlso, Timothy, can you take a look at #5211 as well? That adds a http-equiv header to the html itself, just to make sure browsers really do understand that we're sending utf8.",
    "created_at": "2009-03-16T23:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34066",
    "user": "ddrake"
}
```

I've noticed that some javascript and css doesn't have content-type headers being sent (but some do); should we open separate tickets for those as well?

Also, Timothy, can you take a look at #5211 as well? That adds a http-equiv header to the html itself, just to make sure browsers really do understand that we're sending utf8.



---

archive/issue_comments_034067.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-19T12:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34067",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034068.json:
```json
{
    "body": "I've attached trac_4547.patch which applies cleanly against 3.4.  Note that this patch DOES NOT depend on #4135.\n\nWe should open new tickets for CSS / Javascript / etc.",
    "created_at": "2009-03-19T12:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34068",
    "user": "mhansen"
}
```

I've attached trac_4547.patch which applies cleanly against 3.4.  Note that this patch DOES NOT depend on #4135.

We should open new tickets for CSS / Javascript / etc.



---

archive/issue_comments_034069.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-03-19T12:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34069",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_034070.json:
```json
{
    "body": "This patch requires two trivial fixes unless these are provided via some other patch as a dependency:\n\n```\nsage-3.4.1.alpha0$ ./sage -t -long devel/sage/sage/server/notebook/twist.py \nsage -t -long \"devel/sage/sage/server/notebook/twist.py\"    \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/server/notebook/twist.py\", line 139:\n    sage: response.headers\nExpected:\n    <Headers: Raw: {'content-type': ['text/html']} Parsed: {'content-type': <RecalcNeeded>}>\nGot:\n    <Headers: Raw: {'content-type': ['text/html; charset=utf-8']} Parsed: {'content-type': <RecalcNeeded>}>\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/server/notebook/twist.py\", line 1511:\n    sage: E.render(None)\nExpected:\n    <twisted.web2.HTMLResponse code=200, streamlen=...>\nGot:\n    <twisted.web2.http.Response code=200, streamlen=240>\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T18:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34070",
    "user": "mabshoff"
}
```

This patch requires two trivial fixes unless these are provided via some other patch as a dependency:

```
sage-3.4.1.alpha0$ ./sage -t -long devel/sage/sage/server/notebook/twist.py 
sage -t -long "devel/sage/sage/server/notebook/twist.py"    
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/server/notebook/twist.py", line 139:
    sage: response.headers
Expected:
    <Headers: Raw: {'content-type': ['text/html']} Parsed: {'content-type': <RecalcNeeded>}>
Got:
    <Headers: Raw: {'content-type': ['text/html; charset=utf-8']} Parsed: {'content-type': <RecalcNeeded>}>
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/server/notebook/twist.py", line 1511:
    sage: E.render(None)
Expected:
    <twisted.web2.HTMLResponse code=200, streamlen=...>
Got:
    <twisted.web2.http.Response code=200, streamlen=240>
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_034071.json:
```json
{
    "body": "Attachment\n\nUpdate version of mhansen's patch that does pass doctests",
    "created_at": "2009-03-23T21:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34071",
    "user": "mabshoff"
}
```

Attachment

Update version of mhansen's patch that does pass doctests



---

archive/issue_comments_034072.json:
```json
{
    "body": "How on earth can this patch get a positive review when it doesn't even pass doctests for the file it patches?\n\nI have update mhansen's patch to pass doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34072",
    "user": "mabshoff"
}
```

How on earth can this patch get a positive review when it doesn't even pass doctests for the file it patches?

I have update mhansen's patch to pass doctests.

Cheers,

Michael



---

archive/issue_comments_034073.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34073",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_034074.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4547#issuecomment-34074",
    "user": "mabshoff"
}
```

Resolution: fixed
