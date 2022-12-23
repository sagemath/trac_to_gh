# Issue 3240: notebook -- implement page dedicated to worksheet publishing

Issue created by migration from https://trac.sagemath.org/ticket/3240

Original creator: TimothyClemans

Original creation time: 2008-05-17 17:53:34

Assignee: boothby

Create a clone of Google Docs' "Publish this document" page found by going to a document clicking "Share" then "Publish as web page...". This involves implementing "Stop publishing", "Automatically re-publish when changes are made", and "Re-publish document".


---

Comment by TimothyClemans created at 2008-05-17 23:09:55

depends on #3050


---

Attachment


---

Comment by was created at 2008-05-19 03:58:26

REMARKS:

I will not require doctests everywhere for notebook code yet, since not enough infrastructure is in place.  But at least every new function should have a full docstring documenting inputs/outputs, etc.  This makes the code easier to referee/review.  Could you add such docstrings to all functions introduced in this patch?  Thanks!


---

Comment by was created at 2008-05-19 04:01:40

I published a worksheet, then tried to edit this and everything broke (i.e., the notebook stopped responding).  The server log contained this traceback:

```
teragon-2:~ was$ sagenb
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.1, Release Date: 2008-05-04                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
...
The notebook files are stored in: misc
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
2008-05-18 20:59:12-0700 [-] Log opened.
2008-05-18 20:59:12-0700 [-] twistd 8.0.1 (/Users/was/build/build/sage-3.0.1/local/bin/python 2.5.2) starting up
2008-05-18 20:59:12-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-05-18 20:59:12-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8000
2008-05-18 20:59:12-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x26da698>
2008-05-18 20:59:54-0700 [HTTPChannel,1,127.0.0.1] 
2008-05-18 21:00:32-0700 [HTTPChannel,3,127.0.0.1] Exception rendering:
2008-05-18 21:00:32-0700 [HTTPChannel,3,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 609, in gotResult
	    _deferGenerator(g, deferred)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 586, in _deferGenerator
	    deferred.callback(result)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 242, in callback
	    self._startRunCallbacks(result)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 307, in _startRunCallbacks
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 230, in <lambda>
	    ).addCallback(lambda res: self.render(request))
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1084, in render
	    cell.evaluate(username = self.username)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 688, in evaluate
	    self.__worksheet.enqueue(self, username=username)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1689, in enqueue
	    self._record_that_we_are_computing(username)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1652, in _record_that_we_are_computing
	    self.record_edit(username)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1088, in record_edit
	    self.autosave(user)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 656, in autosave
	    self.save_snapshot(username)
	  File "/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 638, in save_snapshot
	    self.__notebook.publish_worksheet(self, user)
	exceptions.AttributeError: Worksheet instance has no attribute '_Worksheet__notebook'
	
```



---

Attachment


---

Attachment

docstring for Worksheet_publish


---

Comment by boothby created at 2008-06-15 00:45:50

I tried to publish a worksheet with auto-publish on, and got an internal sever error:


```
2008-06-14 17:09:42-0700 [HTTPChannel,11,69.91.136.33] Exception rendering:
2008-06-14 17:09:42-0700 [HTTPChannel,11,69.91.136.33] Unhandled Error
        Traceback (most recent call last):
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 185, in addCallbacks
            self._runCallbacks()
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 284, in _continue
            self.unpause()
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 280, in unpause
            self._runCallbacks()
        --- <exception caught here> ---
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/server.py", line 296, in <lambda>
            d.addCallback(lambda res, req: res.renderHTTP(req), self)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
            return method(request)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 202, in http_GET
            return super(Resource, self).http_GET(request)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 128, in http_GET
            return self.render(request)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1186, in render
            notebook.publish_worksheet(self.worksheet, self.username)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 396, in publish_worksheet
            W = self.create_new_worksheet(worksheet.name(), 'pub')
          File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 438, in create_new_worksheet
            auto_publish = False)
          File "/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 129, in __init__
            self.__dir = '%s/%s'%(notebook.worksheet_directory(), filename)
        exceptions.NameError: global name 'notebook' is not defined
```



---

Attachment

fixes issue found by Tom


---

Comment by craigcitro created at 2008-06-15 21:46:24

Changing keywords from "" to "editor_wstein".


---

Comment by boothby created at 2008-06-16 05:40:28

works for me


---

Comment by mabshoff created at 2008-06-23 12:59:57

Resolution: fixed


---

Comment by mabshoff created at 2008-06-23 12:59:57

Merged all four patches in Sage 3.0.4.alpha0
