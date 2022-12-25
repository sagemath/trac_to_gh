# Issue 7330: notebook download to a file broken

archive/issues_007330.json:
```json
{
    "body": "Assignee: boothby\n\nThis is with a pre-4.1.2 notebook, upgraded to 4.1.2\n\n```\n2009-10-28 02:17:46-0700 [HTTPChannel,3,127.0.0.1] Exception rendering:\n2009-10-28 02:17:46-0700 [HTTPChannel,3,127.0.0.1] Unhandled Error\nTraceback (most recent call last):\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n    self.result = callback(self.result, *args, **kw)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 324, in _getChild\n    return result.addCallback(self._handleSegment, res, path, updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 195, in addCallback\n    callbackKeywords=kw)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n    self._runCallbacks()\n--- <exception caught here> ---\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n    self.result = callback(self.result, *args, **kw)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 367, in _handleSegment\n    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 326, in _getChild\n    return self._handleSegment(result, res, path, updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 367, in _handleSegment\n    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 326, in _getChild\n    return self._handleSegment(result, res, path, updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 367, in _handleSegment\n    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 326, in _getChild\n    return self._handleSegment(result, res, path, updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 367, in _handleSegment\n    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 326, in _getChild\n    return self._handleSegment(result, res, path, updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 367, in _handleSegment\n    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 322, in _getChild\n    result = res.locateChild(self, path)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 167, in locateChild\n    r = factory(request, segments[0])\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/twist.py\", line 1312, in childFactory\n    notebook.export_worksheet(worksheet_name, filename)\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py\", line 951, in export_worksheet\t    W.save()\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 1842, in save\n    save(self.conf(), path + '/conf.sobj')\n  File \"/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 400, in conf\n    C = load(file)\n  File \"sage_object.pyx\", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6480)\n    \n  File \"sage_object.pyx\", line 727, in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)\n    \nexceptions.EOFError: \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7330\n\n",
    "closed_at": "2010-01-25T16:35:24Z",
    "created_at": "2009-10-28T09:15:58Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook download to a file broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7330",
    "user": "https://github.com/robertwb"
}
```
Assignee: boothby

This is with a pre-4.1.2 notebook, upgraded to 4.1.2

```
2009-10-28 02:17:46-0700 [HTTPChannel,3,127.0.0.1] Exception rendering:
2009-10-28 02:17:46-0700 [HTTPChannel,3,127.0.0.1] Unhandled Error
Traceback (most recent call last):
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
    self.result = callback(self.result, *args, **kw)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 324, in _getChild
    return result.addCallback(self._handleSegment, res, path, updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 195, in addCallback
    callbackKeywords=kw)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
    self._runCallbacks()
--- <exception caught here> ---
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
    self.result = callback(self.result, *args, **kw)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 367, in _handleSegment
    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 326, in _getChild
    return self._handleSegment(result, res, path, updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 367, in _handleSegment
    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 326, in _getChild
    return self._handleSegment(result, res, path, updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 367, in _handleSegment
    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 326, in _getChild
    return self._handleSegment(result, res, path, updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 367, in _handleSegment
    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 326, in _getChild
    return self._handleSegment(result, res, path, updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 367, in _handleSegment
    child = self._getChild(None, newres, newpath, updatepaths=updatepaths)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/server.py", line 322, in _getChild
    result = res.locateChild(self, path)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 167, in locateChild
    r = factory(request, segments[0])
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/twist.py", line 1312, in childFactory
    notebook.export_worksheet(worksheet_name, filename)
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py", line 951, in export_worksheet	    W.save()
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 1842, in save
    save(self.conf(), path + '/conf.sobj')
  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 400, in conf
    C = load(file)
  File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6480)
    
  File "sage_object.pyx", line 727, in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)
    
exceptions.EOFError: 
```

Issue created by migration from https://trac.sagemath.org/ticket/7330





---

archive/issue_comments_061185.json:
```json
{
    "body": "Huh!?\n\nBased on the ticket description and traceback, I don't have even the slightest idea what bug you're reporting, what version of the notebook you're using or anything else. Huh?",
    "created_at": "2009-10-28T18:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7330#issuecomment-61185",
    "user": "https://github.com/williamstein"
}
```

Huh!?

Based on the ticket description and traceback, I don't have even the slightest idea what bug you're reporting, what version of the notebook you're using or anything else. Huh?



---

archive/issue_comments_061186.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-25T16:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7330#issuecomment-61186",
    "user": "https://github.com/qed777"
}
```

Resolution: invalid



---

archive/issue_events_017350.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T16:35:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7330",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7330#event-17350"
}
```



---

archive/issue_comments_061187.json:
```json
{
    "body": "I'm closing this for lack of additional information.  But please reopen it, if the problem is still around.",
    "created_at": "2010-01-25T16:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7330#issuecomment-61187",
    "user": "https://github.com/qed777"
}
```

I'm closing this for lack of additional information.  But please reopen it, if the problem is still around.



---

archive/issue_events_017351.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-26T00:27:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7330",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7330#event-17351"
}
```
