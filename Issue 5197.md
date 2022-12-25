# Issue 5197: notebook -- render worksheet list now totally broken on sagenb.org by somebody naming a worksheet with a character u'\xa7'

archive/issues_005197.json:
```json
{
    "body": "Assignee: boothby\n\nWhen one clicks on \"view published worksheets\" at sagenb.org you get a server Internal Error and:\n\n\n```\n2009-02-06 15:52:20-0800 [HTTPChannel,12,172.16.147.1] Unhandled Error\n        Traceback (most recent call last):\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n            self._runCallbacks()\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 289, in _continue\n            self.unpause()\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 285, in unpause\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n            d.addCallback(lambda res, req: res.renderHTTP(req), self)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n            return method(request)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n            return super(Resource, self).http_GET(request)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n            return self.render(request)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1541, in render\n            s = render_worksheet_list(ctx.args, pub=True, username=self.username)\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1390, in render_worksheet_list\n            return template('worksheet_listing.html', **locals())\n          File \"/home/sage/sage/local/lib/python2.5/site-packages/sage/server/notebook/template.py\", line 70, in template\n            return str(tmpl.render(**context))\n        exceptions.UnicodeEncodeError: 'ascii' codec can't encode character u'\\xa7' in position 19932: ordinal not in range(128)\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5197\n\n",
    "created_at": "2009-02-06T23:58:02Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "notebook -- render worksheet list now totally broken on sagenb.org by somebody naming a worksheet with a character u'\\xa7'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5197",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/5197





---

archive/issue_comments_039755.json:
```json
{
    "body": "Sounds like a dupe of #5176 to me. There is a patch that was merged in Sage 3.3.alpha6, so you can try that.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T00:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5197#issuecomment-39755",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sounds like a dupe of #5176 to me. There is a patch that was merged in Sage 3.3.alpha6, so you can try that.

Cheers,

Michael



---

archive/issue_events_012032.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-02-07T00:26:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5197",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5197#event-12032"
}
```



---

archive/issue_comments_039756.json:
```json
{
    "body": "I have confirmed that the patch at #5176 fixes this book.",
    "created_at": "2009-02-07T00:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5197#issuecomment-39756",
    "user": "https://github.com/williamstein"
}
```

I have confirmed that the patch at #5176 fixes this book.



---

archive/issue_comments_039757.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-02-07T00:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5197",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5197#issuecomment-39757",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate
