# Issue 4547: The Sage Notebook doesn't specify the Content-Type header in its responses

Issue created by migration from https://trac.sagemath.org/ticket/4547

Original creator: mhansen

Original creation time: 2008-11-19 15:01:12

Assignee: boothby

CC:  jason

This causes Apache rewriting for example to just display plain text instead of HTML.  This hasn't been an issue because browsers are relatively smart about dealing with unspecified Content-Types.


---

Comment by mhansen created at 2008-11-19 15:02:45

I attached a patch (which may or may not apply to the current version) which only fixes the problem for HTML pages.  CSS, Javascript, etc. should also be handled.


---

Comment by was created at 2008-11-20 05:09:57

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

Comment by ddrake created at 2009-02-10 09:42:01

I rebased Mike's patch against 3.3.alpha6, and added a "charset: utf-8" bit; this ticket is in some sense the other half of #5211.

This ticket was originally motivated by Apache rewriting; I'm here because some users have UTF-8 text in their worksheets and browsers are not always figuring out the correct encoding. If my patch fixes the encoding/browser problems, perhaps we should merge this ticket and open another for adding Content-Type headers to CSS, Javascript, and so on.


---

Comment by mabshoff created at 2009-02-10 09:45:51

Since you rebased the patch please change the summary to "needs review" as I just did. Otherwise it will just bitrot since no one will know it is even there :(

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 09:48:19

Well, looking around further into the ticket history it seems that additional work is needed. But if this patch does get a positive review I would recommend to open another ticket to deal with CSS and javasscript encoding settings, even though this is somewhat less pressing (who adds  utf-8 characters into CSS or javasscript?).

Mike: any take on this?

Cheers,

Michael


---

Comment by ddrake created at 2009-03-02 06:55:08

I've rebased the patch against 3.4.alpha0 -- that's "trac_4547-ddrake.2.patch", which is the only one of the three patches which needs to be applied.


---

Comment by TimothyClemans created at 2009-03-16 20:15:00

apply trac-4547_3.patch


---

Comment by TimothyClemans created at 2009-03-16 20:15:45

Depends on #4135


---

Comment by ddrake created at 2009-03-16 23:50:47

I've noticed that some javascript and css doesn't have content-type headers being sent (but some do); should we open separate tickets for those as well?

Also, Timothy, can you take a look at #5211 as well? That adds a http-equiv header to the html itself, just to make sure browsers really do understand that we're sending utf8.


---

Comment by mhansen created at 2009-03-19 12:00:19

Changing status from new to assigned.


---

Comment by mhansen created at 2009-03-19 12:00:19

I've attached trac_4547.patch which applies cleanly against 3.4.  Note that this patch DOES NOT depend on #4135.

We should open new tickets for CSS / Javascript / etc.


---

Comment by mhansen created at 2009-03-19 12:00:19

Changing assignee from boothby to mhansen.


---

Comment by mabshoff created at 2009-03-23 18:58:36

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

Attachment

Update version of mhansen's patch that does pass doctests


---

Comment by mabshoff created at 2009-03-23 21:53:16

How on earth can this patch get a positive review when it doesn't even pass doctests for the file it patches?

I have update mhansen's patch to pass doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 21:54:54

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 21:54:54

Resolution: fixed
