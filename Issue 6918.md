# Issue 6918: notebook -- try harder to create worksheet process??

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-10 18:50:25

Assignee: boothby


```
2009-09-10 11:49:14-0700 [HTTPChannel,38908,127.0.0.1] [Errno 5] Input/output error
2009-09-10 11:49:14-0700 [HTTPChannel,38908,127.0.0.1] Exception rendering:
2009-09-10 11:49:14-0700 [HTTPChannel,38908,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
	    self._runCallbacks()
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 289, in _continue
	    self.unpause()
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 285, in unpause
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/server.py", line 296, in <lambda>
	    d.addCallback(lambda res, req: res.renderHTTP(req), self)
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
	    return method(request)
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 202, in http_GET
	    return super(Resource, self).http_GET(request)
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 128, in http_GET
	    return self.render(request)
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/server/notebook/twist.py", line 1430, in render
	    self.worksheet.sage()
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 2830, in sage
	    self.initialize_sage()
	  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 2803, in initialize_sage
	    raise RuntimeError
	exceptions.RuntimeError: 
	
```



---

Comment by timdumol created at 2010-01-19 07:33:26

Resolution: invalid
