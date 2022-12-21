# Issue 7330: notebook download to a file broken

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-10-28 09:15:58

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
	  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py", line 951, in export_worksheet
	    W.save()
	  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 1842, in save
	    save(self.conf(), path + '/conf.sobj')
	  File "/Users/robertwb/sage/sage-4.0/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 400, in conf
	    C = load(file)
	  File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6480)
	    
	  File "sage_object.pyx", line 727, in sage.structure.sage_object.loads (sage/structure/sage_object.c:8076)
	    
	exceptions.EOFError: 
```



---

Comment by was created at 2009-10-28 18:44:39

Huh!?

Based on the ticket description and traceback, I don't have even the slightest idea what bug you're reporting, what version of the notebook you're using or anything else. Huh?


---

Comment by mpatel created at 2010-01-25 16:35:24

Resolution: invalid


---

Comment by mpatel created at 2010-01-25 16:35:24

I'm closing this for lack of additional information.  But please reopen it, if the problem is still around.
