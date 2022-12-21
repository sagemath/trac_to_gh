# Issue 7627: Settings page (for converted notebook?) gives errors

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-12-08 19:54:56

Assignee: was

I started sage 4.2.1 and did:

```
% sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: notebook()
The notebook files are stored in: sage_notebook.sagenb
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
2009-12-08 13:27:27-0600 [-] Log opened.
2009-12-08 13:27:27-0600 [-] twistd 8.2.0 (/home/jason/sage/local/bin/python 2.6.2) starting up.
2009-12-08 13:27:27-0600 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-12-08 13:27:27-0600 [-] twisted.web2.channel.http.HTTPFactory starting on 8000
2009-12-08 13:27:27-0600 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xb5f3dcc>
```

| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
Then I clicked on "Settings", and then "Notebook Settings", and I got the following webpage:


```
 Internal Server Error

An error occurred rendering the requested page. More information is available in the server log.
```

and the following error in the log:

```
2009-12-08 13:27:51-0600 [HTTPChannel,1,127.0.0.1] Exception rendering:
2009-12-08 13:27:51-0600 [HTTPChannel,1,127.0.0.1] Unhandled Error
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
     File "/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 978, in render
       template_dict['auto_table'] = notebook.conf().html_table(updated)
     File "/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/conf.py", line 123, in html_table
       G[DS[key][GROUP]] = [key]
   exceptions.KeyError: 'number_of_backups'

```

I believe this was a notebook that was automatically converted from the old format. 


```



```



---

Comment by jason created at 2009-12-08 19:55:19

I moved .sage and restarted the notebook, and the Settings then worked fine.


---

Attachment

Skip obsolete or improperly annotated notebook settings.  Depends on #7625.  sagenb repo.


---

Comment by mpatel created at 2009-12-08 23:52:51

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-12-08 23:52:51

With the patch, the rendered notebook settings page should contain only current (i.e., present in `sagenb.notebook.server_conf.defaults`) or "properly" annotated (see `sagenb.notebook.server_conf.defaults_descriptions`) settings.

The server should now also look up [incoming] request arguments in `defaults_descriptions`.


---

Comment by was created at 2009-12-09 00:17:56

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 00:17:56

Very nice!  This is a great improvement -- the notebook settings actually work!


---

Comment by was created at 2009-12-09 00:17:56

Changing priority from major to critical.


---

Comment by was created at 2009-12-09 01:03:47

merged into sagenb-0.4.6


---

Comment by was created at 2009-12-09 01:03:47

Resolution: fixed
