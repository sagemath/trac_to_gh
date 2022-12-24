# Issue 5257: Clicking on "Log" in the notebook (bringing you to the /history page) gives errors

archive/issues_005257.json:
```json
{
    "body": "Assignee: boothby\n\nIn the browser, I get:\n\n\n```\nInternal Server Error\nAn error occurred rendering the requested page. More information is available in the server log.\n```\n\n\nand I get a traceback as well:\n\n\n```\n2009-02-13 12:39:32-0600 [HTTPChannel,101,127.0.0.1] Exception rendering:\n2009-02-13 12:39:32-0600 [HTTPChannel,101,127.0.0.1] Unhandled Error\n\tTraceback (most recent call last):\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py\", line 186, in addCallbacks\n\t    self._runCallbacks()\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py\", line 328, in _runCallbacks\n\t    self.result = callback(self.result, *args, **kw)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py\", line 289, in _continue\n\t    self.unpause()\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py\", line 285, in unpause\n\t    self._runCallbacks()\n\t--- <exception caught here> ---\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py\", line 328, in _runCallbacks\n\t    self.result = callback(self.result, *args, **kw)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/server.py\", line 296, in <lambda>\n\t    d.addCallback(lambda res, req: res.renderHTTP(req), self)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/resource.py\", line 85, in renderHTTP\n\t    return method(request)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/resource.py\", line 202, in http_GET\n\t    return super(Resource, self).http_GET(request)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/resource.py\", line 128, in http_GET\n\t    return self.render(request)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1633, in render\n\t    s = notebook.user_history_html(self.username)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 842, in user_history_html\n\t    \"\"\"%(username, self.html_worksheet_list_top(username, actions=False), t)\n\t  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 1318, in html_worksheet_list_top\n\t    s += self.html_new_or_upload()\n\texceptions.AttributeError: 'Notebook' object has no attribute 'html_new_or_upload'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5257\n\n",
    "created_at": "2009-02-13T18:48:32Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Clicking on \"Log\" in the notebook (bringing you to the /history page) gives errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5257",
    "user": "@jasongrout"
}
```
Assignee: boothby

In the browser, I get:


```
Internal Server Error
An error occurred rendering the requested page. More information is available in the server log.
```


and I get a traceback as well:


```
2009-02-13 12:39:32-0600 [HTTPChannel,101,127.0.0.1] Exception rendering:
2009-02-13 12:39:32-0600 [HTTPChannel,101,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py", line 186, in addCallbacks
	    self._runCallbacks()
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py", line 289, in _continue
	    self.unpause()
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py", line 285, in unpause
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/server.py", line 296, in <lambda>
	    d.addCallback(lambda res, req: res.renderHTTP(req), self)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/resource.py", line 85, in renderHTTP
	    return method(request)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/resource.py", line 202, in http_GET
	    return super(Resource, self).http_GET(request)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-i686.egg/twisted/web2/resource.py", line 128, in http_GET
	    return self.render(request)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1633, in render
	    s = notebook.user_history_html(self.username)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 842, in user_history_html
	    """%(username, self.html_worksheet_list_top(username, actions=False), t)
	  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 1318, in html_worksheet_list_top
	    s += self.html_new_or_upload()
	exceptions.AttributeError: 'Notebook' object has no attribute 'html_new_or_upload'
```


Issue created by migration from https://trac.sagemath.org/ticket/5257





---

archive/issue_comments_040345.json:
```json
{
    "body": "If humanly possible this should be fixed in 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40345",
    "user": "mabshoff"
}
```

If humanly possible this should be fixed in 3.3.

Cheers,

Michael



---

archive/issue_comments_040346.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-15T04:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40346",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040347.json:
```json
{
    "body": "The following patch replace the user_history_html function with a templated version.  With this removed, there were a number of unused html_* methods that could be removed.  Additionally, I got rid unified list_top.html and list_top_public.html by moving all the worksheet listing specific stuff to worksheet_listing.html.\n\nI tested this patch out pretty thoroughly and everything seems to be behaving correctly.  I'll also add a test to my Selenium suite to test this in the future.",
    "created_at": "2009-02-15T04:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40347",
    "user": "@mwhansen"
}
```

The following patch replace the user_history_html function with a templated version.  With this removed, there were a number of unused html_* methods that could be removed.  Additionally, I got rid unified list_top.html and list_top_public.html by moving all the worksheet listing specific stuff to worksheet_listing.html.

I tested this patch out pretty thoroughly and everything seems to be behaving correctly.  I'll also add a test to my Selenium suite to test this in the future.



---

archive/issue_comments_040348.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-02-15T04:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40348",
    "user": "@mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_040349.json:
```json
{
    "body": "The patch looks good, but it needs to be rebased against 3.3.rc1 once it is out:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5257.patch \npatching file sage/server/notebook/notebook.py\nReversed (or previously applied) patch detected!  Assume -R? [n] Y\nApply anyway? [n] Y\nSkipping patch.\n3 out of 3 hunks ignored -- saving rejects to file sage/server/notebook/notebook.py.rej\npatching file sage/server/notebook/templates/history.html\npatching file sage/server/notebook/templates/list_top.html\npatching file sage/server/notebook/templates/list_top_public.html\npatching file sage/server/notebook/templates/worksheet_listing.html\npatching file sage/server/notebook/twist.py\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T08:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40349",
    "user": "mabshoff"
}
```

The patch looks good, but it needs to be rebased against 3.3.rc1 once it is out:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5257.patch 
patching file sage/server/notebook/notebook.py
Reversed (or previously applied) patch detected!  Assume -R? [n] Y
Apply anyway? [n] Y
Skipping patch.
3 out of 3 hunks ignored -- saving rejects to file sage/server/notebook/notebook.py.rej
patching file sage/server/notebook/templates/history.html
patching file sage/server/notebook/templates/list_top.html
patching file sage/server/notebook/templates/list_top_public.html
patching file sage/server/notebook/templates/worksheet_listing.html
patching file sage/server/notebook/twist.py
```


Cheers,

Michael



---

archive/issue_comments_040350.json:
```json
{
    "body": "Attachment [trac_5257.patch](tarball://root/attachments/some-uuid/ticket5257/trac_5257.patch) by @mwhansen created at 2009-02-19 11:42:32\n\nI've posted a rebased patch against 3.3.rc1.",
    "created_at": "2009-02-19T11:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40350",
    "user": "@mwhansen"
}
```

Attachment [trac_5257.patch](tarball://root/attachments/some-uuid/ticket5257/trac_5257.patch) by @mwhansen created at 2009-02-19 11:42:32

I've posted a rebased patch against 3.3.rc1.



---

archive/issue_comments_040351.json:
```json
{
    "body": "Looks good to me and fixes the bug in question. I am somewhat relying on Mike's automated testing here.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T11:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40351",
    "user": "mabshoff"
}
```

Looks good to me and fixes the bug in question. I am somewhat relying on Mike's automated testing here.

Cheers,

Michael



---

archive/issue_comments_040352.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T11:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40352",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_040353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T11:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5257#issuecomment-40353",
    "user": "mabshoff"
}
```

Resolution: fixed
