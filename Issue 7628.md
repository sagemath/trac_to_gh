# Issue 7628: Error on account creation still creates (half of) an account

Issue created by migration from https://trac.sagemath.org/ticket/7628

Original creator: jason

Original creation time: 2009-12-08 19:56:28

Assignee: was

I went to the settings page and checked yes to allowing new registrations and requiring an email address.  I then created an account with username asdf and password asdf.  It returned an error (bad password; contains the username).  I logged out anyway and logged back in as admin.  Then I clicked on Settings, and got the following error:



```


2009-12-08 13:34:06-0600 [HTTPChannel,3,127.0.0.1] Exception rendering:
2009-12-08 13:34:06-0600 [HTTPChannel,3,127.0.0.1] Unhandled Error
   Traceback (most recent call last):
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
       self._runCallbacks()
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
       self.result = callback(self.result, *args, **kw)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 289, in _continue
       self.unpause()
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 285, in unpause
       self._runCallbacks()
   --- <exception caught here> ---
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
       self.result = callback(self.result, *args, **kw)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/server.py", line 296, in <lambda>
       d.addCallback(lambda res, req: res.renderHTTP(req), self)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
       return method(request)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 202, in http_GET
       return super(Resource, self).http_GET(request)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 128, in http_GET
       return self.render(request)
     File "/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 962, in render
       template_dict['email_address'] = 'None' if not notebook.user(self.username)._User__email else notebook.user(self.username)._User__email
   exceptions.AttributeError: 'User' object has no attribute '_User__email' 


---

Comment by mpatel created at 2009-12-09 01:00:26

Just prevents the error.  Depends on #7625.  sagenb repo.


---

Comment by mpatel created at 2009-12-09 01:09:29

Changing status from new to needs_review.


---

Attachment

The patch should prevent the error.  It does not activate the email system.

In the future, we could auto-generate the user settings page, with drop-down menus for key-bindings, a la the notebook settings page.  From `todo.txt`:

```
[ ] move is_valid_username (etc.) out of twist.py, which is definitely *not* where it belongs
```

How about a `validate.py`, with functions for other fields, too?


---

Comment by was created at 2009-12-09 03:44:06

Looks good. Thanks.


---

Comment by was created at 2009-12-09 03:44:06

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 06:34:52

Merged into 0.4.7 (which isn't released yet).


---

Comment by was created at 2009-12-09 06:34:52

Resolution: fixed
