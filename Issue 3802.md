# Issue 3802: notebook -- run server locally and logout then go to local server again and get KeyError in server log and internal server error

Issue created by migration from https://trac.sagemath.org/ticket/3802

Original creator: was

Original creation time: 2008-08-10 23:29:52

Assignee: boothby


```
	
2008-08-10 16:25:31-0700 [HTTPChannel,133,127.0.0.1] Exception rendering:
2008-08-10 16:25:31-0700 [HTTPChannel,133,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/internet/defer.py", line 185, in addCallbacks
	    self._runCallbacks()
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/internet/defer.py", line 323, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/internet/defer.py", line 284, in _continue
	    self.unpause()
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/internet/defer.py", line 280, in unpause
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/internet/defer.py", line 323, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/web2/server.py", line 296, in <lambda>
	    d.addCallback(lambda res, req: res.renderHTTP(req), self)
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/web2/resource.py", line 85, in renderHTTP
	    return method(request)
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/web2/resource.py", line 202, in http_GET
	    return super(Resource, self).http_GET(request)
	  File "/Users/was/s/local/lib/python2.5/site-packages/Twisted-8.0.1-py2.5-macosx-10.3-i386.egg/twisted/web2/resource.py", line 128, in http_GET
	    return self.render(request)
	  File "/Users/was/s/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 2139, in render
	    return http.Response(stream =  login_page_template(notebook.get_accounts(), notebook.default_user()))
	  File "/Users/was/s/local/lib/python2.5/site-packages/sage/server/notebook/template.py", line 59, in login_page_template
	    return login_template(register = reg, default=default_user, username_error=u_e, password_error=p_e, welcome=welcome)
	  File "/Users/was/s/local/lib/python2.5/site-packages/sage/server/notebook/template.py", line 34, in __call__
	    return self.__template.substitute(kwds)
	  File "/Users/was/s/local/lib/python2.5/string.py", line 170, in substitute
	    return self.pattern.sub(convert, self.template)
	  File "/Users/was/s/local/lib/python2.5/string.py", line 160, in convert
	    val = mapping[named]
	exceptions.KeyError: 'forgot_pass'
	


```



---

Comment by timdumol created at 2009-11-19 20:27:03

Is this still an issue? I'm guessing you mean logging out of the Mac OSX system?


---

Comment by was created at 2009-11-19 23:36:56

Resolution: fixed


---

Comment by was created at 2009-11-19 23:36:56

timdumol -- I think this is not an issue.  It looks like a bug in the old templating code that you have long since replaced in sagenb.  So closed as fixed.   (And I can't replicate it.)
