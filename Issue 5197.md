# Issue 5197: notebook -- render worksheet list now totally broken on sagenb.org by somebody naming a worksheet with a character u'\xa7'

Issue created by migration from https://trac.sagemath.org/ticket/5197

Original creator: was

Original creation time: 2009-02-06 23:58:02

Assignee: boothby

When one clicks on "view published worksheets" at sagenb.org you get a server Internal Error and:


```
2009-02-06 15:52:20-0800 [HTTPChannel,12,172.16.147.1] Unhandled Error
        Traceback (most recent call last):
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
            self._runCallbacks()
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 289, in _continue
            self.unpause()
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 285, in unpause
            self._runCallbacks()
        --- <exception caught here> ---
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/server.py", line 296, in <lambda>
            d.addCallback(lambda res, req: res.renderHTTP(req), self)
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
            return method(request)
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 202, in http_GET
            return super(Resource, self).http_GET(request)
          File "/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 128, in http_GET
            return self.render(request)
          File "/home/sage/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1541, in render
            s = render_worksheet_list(ctx.args, pub=True, username=self.username)
          File "/home/sage/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 1390, in render_worksheet_list
            return template('worksheet_listing.html', **locals())
          File "/home/sage/sage/local/lib/python2.5/site-packages/sage/server/notebook/template.py", line 70, in template
            return str(tmpl.render(**context))
        exceptions.UnicodeEncodeError: 'ascii' codec can't encode character u'\xa7' in position 19932: ordinal not in range(128)

```



---

Comment by mabshoff created at 2009-02-07 00:02:09

Sounds like a dupe of #5176 to me. There is a patch that was merged in Sage 3.3.alpha6, so you can try that.

Cheers,

Michael


---

Comment by was created at 2009-02-07 00:26:13

I have confirmed that the patch at #5176 fixes this book.


---

Comment by was created at 2009-02-07 00:26:13

Resolution: duplicate
