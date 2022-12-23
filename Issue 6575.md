# Issue 6575: notebook bug in do_sage_extension_preparsing

Issue created by migration from https://trac.sagemath.org/ticket/6575

Original creator: was

Original creation time: 2009-07-21 00:47:07

Assignee: boothby

I got this traceback with sage-4.1:

```
2009-07-20 15:22:18-0700 [HTTPChannel,3400,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 630, in gotResult
	    _deferGenerator(g, deferred)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 607, in _deferGenerator
	    deferred.callback(result)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 243, in callback
	    self._startRunCallbacks(result)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 312, in _startRunCallbacks
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 230, in <lambda>
	    ).addCallback(lambda res: self.render(request))
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/twist.py", line 1152, in render
	    worksheet.start_next_comp()
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 2922, in start_next_comp
	    input += self.preparse_input(I, C)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 3406, in preparse_input
	    input = self.preparse_nonswitched_input(input)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 3440, in preparse_nonswitched_input
	    input = self.do_sage_extensions_preparsing(input)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 3693, in do_sage_extensions_preparsing
	    filename = self.hunt_file(filename)
	exceptions.UnboundLocalError: local variable 'filename' referenced before assignment
	
```


Inspection of the relevant source code should make this trivial to fix.


---

Comment by mpatel created at 2010-01-25 15:48:51

Resolution: invalid


---

Comment by mpatel created at 2010-01-25 15:48:51

I'm closing this, since we've removed `Worksheet.do_sage_extensions_preparsing` and no longer use `Worksheet.hunt_file` (cf. #7483).  We can open a separate ticket to trim obsolete code from `worksheet.py`.
