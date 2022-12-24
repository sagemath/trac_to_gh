# Issue 3240: notebook -- implement page dedicated to worksheet publishing

archive/issues_003240.json:
```json
{
    "body": "Assignee: boothby\n\nCreate a clone of Google Docs' \"Publish this document\" page found by going to a document clicking \"Share\" then \"Publish as web page...\". This involves implementing \"Stop publishing\", \"Automatically re-publish when changes are made\", and \"Re-publish document\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/3240\n\n",
    "created_at": "2008-05-17T17:53:34Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "notebook -- implement page dedicated to worksheet publishing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3240",
    "user": "TimothyClemans"
}
```
Assignee: boothby

Create a clone of Google Docs' "Publish this document" page found by going to a document clicking "Share" then "Publish as web page...". This involves implementing "Stop publishing", "Automatically re-publish when changes are made", and "Re-publish document".

Issue created by migration from https://trac.sagemath.org/ticket/3240





---

archive/issue_comments_022435.json:
```json
{
    "body": "depends on #3050",
    "created_at": "2008-05-17T23:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22435",
    "user": "TimothyClemans"
}
```

depends on #3050



---

archive/issue_comments_022436.json:
```json
{
    "body": "Attachment [3240.patch](tarball://root/attachments/some-uuid/ticket3240/3240.patch) by TimothyClemans created at 2008-05-17 23:11:55",
    "created_at": "2008-05-17T23:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22436",
    "user": "TimothyClemans"
}
```

Attachment [3240.patch](tarball://root/attachments/some-uuid/ticket3240/3240.patch) by TimothyClemans created at 2008-05-17 23:11:55



---

archive/issue_comments_022437.json:
```json
{
    "body": "REMARKS:\n\nI will not require doctests everywhere for notebook code yet, since not enough infrastructure is in place.  But at least every new function should have a full docstring documenting inputs/outputs, etc.  This makes the code easier to referee/review.  Could you add such docstrings to all functions introduced in this patch?  Thanks!",
    "created_at": "2008-05-19T03:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22437",
    "user": "was"
}
```

REMARKS:

I will not require doctests everywhere for notebook code yet, since not enough infrastructure is in place.  But at least every new function should have a full docstring documenting inputs/outputs, etc.  This makes the code easier to referee/review.  Could you add such docstrings to all functions introduced in this patch?  Thanks!



---

archive/issue_comments_022438.json:
```json
{
    "body": "I published a worksheet, then tried to edit this and everything broke (i.e., the notebook stopped responding).  The server log contained this traceback:\n\n```\nteragon-2:~ was$ sagenb\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.1, Release Date: 2008-05-04                       |\n| Type notebook() for the GUI, and license() for information.        |\nPlease wait while the SAGE Notebook server starts...\n...\nThe notebook files are stored in: misc\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n2008-05-18 20:59:12-0700 [-] Log opened.\n2008-05-18 20:59:12-0700 [-] twistd 8.0.1 (/Users/was/build/build/sage-3.0.1/local/bin/python 2.5.2) starting up\n2008-05-18 20:59:12-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2008-05-18 20:59:12-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8000\n2008-05-18 20:59:12-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x26da698>\n2008-05-18 20:59:54-0700 [HTTPChannel,1,127.0.0.1] \n2008-05-18 21:00:32-0700 [HTTPChannel,3,127.0.0.1] Exception rendering:\n2008-05-18 21:00:32-0700 [HTTPChannel,3,127.0.0.1] Unhandled Error\n\tTraceback (most recent call last):\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 609, in gotResult\n\t    _deferGenerator(g, deferred)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 586, in _deferGenerator\n\t    deferred.callback(result)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 242, in callback\n\t    self._startRunCallbacks(result)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 307, in _startRunCallbacks\n\t    self._runCallbacks()\n\t--- <exception caught here> ---\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n\t    self.result = callback(self.result, *args, **kw)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 230, in <lambda>\n\t    ).addCallback(lambda res: self.render(request))\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1084, in render\n\t    cell.evaluate(username = self.username)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 688, in evaluate\n\t    self.__worksheet.enqueue(self, username=username)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 1689, in enqueue\n\t    self._record_that_we_are_computing(username)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 1652, in _record_that_we_are_computing\n\t    self.record_edit(username)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 1088, in record_edit\n\t    self.autosave(user)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 656, in autosave\n\t    self.save_snapshot(username)\n\t  File \"/Users/was/build/build/sage-3.0.1/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 638, in save_snapshot\n\t    self.__notebook.publish_worksheet(self, user)\n\texceptions.AttributeError: Worksheet instance has no attribute '_Worksheet__notebook'\n\t\n```\n",
    "created_at": "2008-05-19T04:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22438",
    "user": "was"
}
```

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

archive/issue_comments_022439.json:
```json
{
    "body": "Attachment [3240_2.patch](tarball://root/attachments/some-uuid/ticket3240/3240_2.patch) by TimothyClemans created at 2008-05-19 05:35:08",
    "created_at": "2008-05-19T05:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22439",
    "user": "TimothyClemans"
}
```

Attachment [3240_2.patch](tarball://root/attachments/some-uuid/ticket3240/3240_2.patch) by TimothyClemans created at 2008-05-19 05:35:08



---

archive/issue_comments_022440.json:
```json
{
    "body": "Attachment [3240_3.patch](tarball://root/attachments/some-uuid/ticket3240/3240_3.patch) by TimothyClemans created at 2008-05-19 06:15:02\n\ndocstring for Worksheet_publish",
    "created_at": "2008-05-19T06:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22440",
    "user": "TimothyClemans"
}
```

Attachment [3240_3.patch](tarball://root/attachments/some-uuid/ticket3240/3240_3.patch) by TimothyClemans created at 2008-05-19 06:15:02

docstring for Worksheet_publish



---

archive/issue_comments_022441.json:
```json
{
    "body": "I tried to publish a worksheet with auto-publish on, and got an internal sever error:\n\n\n```\n2008-06-14 17:09:42-0700 [HTTPChannel,11,69.91.136.33] Exception rendering:\n2008-06-14 17:09:42-0700 [HTTPChannel,11,69.91.136.33] Unhandled Error\n        Traceback (most recent call last):\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 185, in addCallbacks\n            self._runCallbacks()\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 284, in _continue\n            self.unpause()\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 280, in unpause\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n            d.addCallback(lambda res, req: res.renderHTTP(req), self)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n            return method(request)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n            return super(Resource, self).http_GET(request)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n            return self.render(request)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1186, in render\n            notebook.publish_worksheet(self.worksheet, self.username)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 396, in publish_worksheet\n            W = self.create_new_worksheet(worksheet.name(), 'pub')\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 438, in create_new_worksheet\n            auto_publish = False)\n          File \"/home/boothby/sage/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 129, in __init__\n            self.__dir = '%s/%s'%(notebook.worksheet_directory(), filename)\n        exceptions.NameError: global name 'notebook' is not defined\n```\n",
    "created_at": "2008-06-15T00:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22441",
    "user": "boothby"
}
```

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

archive/issue_comments_022442.json:
```json
{
    "body": "Attachment [3240_4.patch](tarball://root/attachments/some-uuid/ticket3240/3240_4.patch) by TimothyClemans created at 2008-06-15 04:51:13\n\nfixes issue found by Tom",
    "created_at": "2008-06-15T04:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22442",
    "user": "TimothyClemans"
}
```

Attachment [3240_4.patch](tarball://root/attachments/some-uuid/ticket3240/3240_4.patch) by TimothyClemans created at 2008-06-15 04:51:13

fixes issue found by Tom



---

archive/issue_comments_022443.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-15T21:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22443",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_022444.json:
```json
{
    "body": "works for me",
    "created_at": "2008-06-16T05:40:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22444",
    "user": "boothby"
}
```

works for me



---

archive/issue_comments_022445.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T12:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22445",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022446.json:
```json
{
    "body": "Merged all four patches in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T12:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3240#issuecomment-22446",
    "user": "mabshoff"
}
```

Merged all four patches in Sage 3.0.4.alpha0
