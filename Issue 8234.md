# Issue 8234: Data file deletion in notebook throws errors

Issue created by migration from https://trac.sagemath.org/ticket/8234

Original creator: rbeezer

Original creation time: 2010-02-10 18:45:13

Assignee: was

CC:  robert.marik

Delete a file in the data directory of the notebook and you get a page back about an "Internal Server Error"  (by selecting the file in the drop-down box, and clicking on the "delete" hyperlink).  File is actually deleted, though.

Trace back from Sage command-line invocation of `notebook()` below.

This does not happen on 4.3.2rc0, but does happen on 4.3.2.  Some discussion, but not much that isn't here already:  
http://groups.google.com/group/sage-notebook/browse_thread/thread/dd2e03d2af01f852


```
2010-02-10 09:22:48-0800 [HTTPChannel,10,127.0.0.1] Exception rendering:
2010-02-10 09:22:48-0800 [HTTPChannel,10,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
            self._runCallbacks()
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 289, in _continue
            self.unpause()
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 285, in unpause
            self._runCallbacks()
        --- <exception caught here> ---
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/web2/server.py", line 296, in <lambda>
            d.addCallback(lambda res, req: res.renderHTTP(req), self)
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
            return method(request)
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 202, in http_GET
            return super(Resource, self).http_GET(request)
          File "/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 128, in http_GET
            return self.render(request)
          File "/sage/dev/local/lib/python2.6/site-packages/sagenb-0.7.4-py2.6.egg/sagenb/notebook/twist.py", line 671, in render
            title=u'%s delete successful' % filename))
        exceptions.TypeError: message() got an unexpected keyword argument 'title'
```



---

Comment by mpatel created at 2010-02-14 00:16:42

#6069 should fix this.  If it doesn't, please let me know.


---

Comment by mpatel created at 2010-02-14 00:20:32

But we still need to fix the page title ("Error -- Sage"), which is wrong.


---

Comment by mpatel created at 2010-02-14 01:22:19

Replying to [comment:2 mpatel]:
> But we still need to fix the page title ("Error -- Sage"), which is wrong.
See V3 at #6069.


---

Comment by mpatel created at 2010-02-14 01:32:19

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-02-14 03:38:31

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-03-12 18:26:17

When #6069 is merged, we should close this ticket.


---

Comment by timdumol created at 2010-03-15 09:10:52

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-03-15 09:10:52

As #6069 is marked as positive review, I'll do the same for this.


---

Comment by jhpalmieri created at 2010-04-23 04:41:11

(I'm not changing any notebook code in Sage 4.4.)


---

Comment by timdumol created at 2010-05-04 04:42:59

Resolution: fixed
