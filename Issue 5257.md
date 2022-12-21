# Issue 5257: Clicking on "Log" in the notebook (bringing you to the /history page) gives errors

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-13 18:48:32

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



---

Comment by mabshoff created at 2009-02-14 02:49:15

If humanly possible this should be fixed in 3.3.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-15 04:11:44

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-15 04:11:44

The following patch replace the user_history_html function with a templated version.  With this removed, there were a number of unused html_* methods that could be removed.  Additionally, I got rid unified list_top.html and list_top_public.html by moving all the worksheet listing specific stuff to worksheet_listing.html.

I tested this patch out pretty thoroughly and everything seems to be behaving correctly.  I'll also add a test to my Selenium suite to test this in the future.


---

Comment by mhansen created at 2009-02-15 04:11:44

Changing assignee from boothby to mhansen.


---

Comment by mabshoff created at 2009-02-16 08:36:44

The patch looks good, but it needs to be rebased against 3.3.rc1 once it is out:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5257.patch 
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

Attachment

I've posted a rebased patch against 3.3.rc1.


---

Comment by mabshoff created at 2009-02-20 11:11:52

Looks good to me and fixes the bug in question. I am somewhat relying on Mike's automated testing here.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 11:12:56

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 11:12:56

Resolution: fixed
