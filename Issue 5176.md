# Issue 5176: notebook chokes horribly on Umlautes

Issue created by migration from https://trac.sagemath.org/ticket/5176

Original creator: malb

Original creation time: 2009-02-04 17:23:06

Assignee: boothby

I have worksheet with the word "Gröbner" in it which prevents me from using the notebook at all because the listing of worksheets crashes.


```
        Traceback (most recent call last):
          File ".../twisted/internet/defer.py", line 186, in addCallbacks
            self._runCallbacks()
          File ".../twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File ".../twisted/internet/defer.py", line 289, in _continue
            self.unpause()
          File ".../twisted/internet/defer.py", line 285, in unpause
            self._runCallbacks()
        --- <exception caught here> ---
          File ".../twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File ".../twisted/web2/server.py", line 296, in <lambda>
            d.addCallback(lambda res, req: res.renderHTTP(req), self)
          File ".../twisted/web2/resource.py", line 85, in renderHTTP
            return method(request)
          File ".../twisted/web2/resource.py", line 202, in http_GET
            return super(Resource, self).http_GET(request)
          File ".../twisted/web2/resource.py", line 128, in http_GET
            return self.render(request)
          File ".../sage/server/notebook/twist.py", line 1408, in render
            return self.render_list(ctx)
          File ".../sage/server/notebook/twist.py", line 1403, in render_list
            s = render_worksheet_list(ctx.args, pub=False, username=self.user)
          File ".../sage/server/notebook/twist.py", line 1390, in render_worksheet_list
            return template('worksheet_listing.html', **locals())
          File ".../sage/server/notebook/template.py", line 70, in template
            return str(tmpl.render(**context))
        exceptions.UnicodeEncodeError: 'ascii' codec can't encode character u'\xf6' in position 4445: ordinal not in range(128)
```


Before umlauts where displayed wrong but at least they didn't crash the server.


---

Attachment


---

Attachment

patch looks good, fixes the crashing for me, and is doctested.  Positive review.


---

Comment by jason created at 2009-02-05 19:18:55


```
[13:09] <mabshoff> Someone needs to make sure we can still clone the repo with that patch since last time we had Nicola's name spelled correctly in a patch we had issues like that.
```


I did not do the above.  mabshoff, if you feel it's needed, can you check it before you merge?


---

Comment by mabshoff created at 2009-02-06 22:52:08

I tested cloning on sage.math and it works there. I will only merge trac_5176.2.patch. 

Jason: when you review tickets with multiple patches please make clear which patches need to be applied. In this case it was obvious once I looked at both patches.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 22:57:18

Resolution: fixed


---

Comment by mabshoff created at 2009-02-06 22:57:18

Merged trac_5176.2.patch only in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by jason created at 2009-02-06 23:14:12

sorry.  You're right to merge the .2.patch file.
