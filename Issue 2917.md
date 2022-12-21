# Issue 2917: internal server error in notebook sage-3.0.alpha4

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-04-14 15:06:50

Assignee: boothby

but on opening a new worksheet (and alson on opening an existing ws)
got an internal server error.

See below,

Jaap


```
sage: notebook()
The notebook files are stored in: /home/jaap/.sage//sage_notebook
Port 8000 is already in use.
Trying next port...
****************************************************
*                                                  *
* Open your web browser to https://localhost:8001  *
*                                                  *
****************************************************
There is an admin account.  If you do not remember the password,
quit the notebook and type notebook(reset=True).
Removing stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd
2008-04-14 11:49:14+0200 [-] Log opened.
2008-04-14 11:49:14+0200 [-] twistd 8.0.1 (/home/jaap/downloads/sage-3.0.alpha4/local/bin/python 2.5.1) starting up
2008-04-14 11:49:14+0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-04-14 11:49:14+0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001
2008-04-14 11:49:14+0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xa76b76c>
2008-04-14 11:49:23+0200 [HTTPChannel,0,127.0.0.1] Exception rendering:
2008-04-14 11:49:23+0200 [HTTPChannel,0,127.0.0.1] Unhandled Error
         Traceback (most recent call last):
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 185, in addCallbacks
             self._runCallbacks()
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
             self.result = callback(self.result, *args, **kw)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 284, in _continue
             self.unpause()
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 280, in unpause
             self._runCallbacks()
         --- <exception caught here> ---
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
             self.result = callback(self.result, *args, **kw)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/server.py", line 296, in <lambda>
             d.addCallback(lambda res, req: res.renderHTTP(req), self)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
             return method(request)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 202, in http_GET
             return super(Resource, self).http_GET(request)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 128, in http_GET
             return self.render(request)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1148, in render
             s = notebook.html(worksheet_filename = self.name,  username=self.username)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 1936, in html
             body = self._html_body(worksheet_filename=worksheet_filename, username=username, show_debug=show_debug)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 1609, in _html_body
             worksheet_html = worksheet.html()
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 828, in html
             s += self.html_worksheet_body(do_print=do_print)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 984, in html_worksheet_body
             s += cell.html(ncols, do_print=do_print) + '\n'
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 609, in html
             html_in  = self.html_in(do_print=do_print)
           File "/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 659, in html_in
             """%(cls, r, ncols, id, id, id, id, id, 'readonly=1' if do_print else '', t)
         exceptions.TypeError: not enough arguments for format string

2008-04-14 11:50:56+0200 [-] (Notebook cleanly saved. Press control-C again to exit.)

```


Boothby:


```
Looks like this was due to a bad merge of #2883.  My guess is, adding another 'id,' to sage/server/notebook/cell.py, line 659 will do the trick -- unless something tricky is going on.  I'll check it around 1:30 Monday.

```




---

Comment by mabshoff created at 2008-04-14 18:44:26

Unsurprisingly this must be fixed before 3.0.final ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-14 18:44:26

Changing priority from major to blocker.


---

Attachment


---

Comment by mhansen created at 2008-04-15 01:00:05

This fixes the problem for me.


---

Comment by mabshoff created at 2008-04-15 01:04:33

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 01:04:33

Merged in Sage 3.0.alpha5
