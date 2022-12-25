# Issue 6918: notebook -- try harder to create worksheet process??

archive/issues_006918.json:
```json
{
    "body": "Assignee: boothby\n\n```\n2009-09-10 11:49:14-0700 [HTTPChannel,38908,127.0.0.1] [Errno 5] Input/output error\n2009-09-10 11:49:14-0700 [HTTPChannel,38908,127.0.0.1] Exception rendering:\n2009-09-10 11:49:14-0700 [HTTPChannel,38908,127.0.0.1] Unhandled Error\nTraceback (most recent call last):\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n    self._runCallbacks()\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n    self.result = callback(self.result, *args, **kw)\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 289, in _continue\n    self.unpause()\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 285, in unpause\n    self._runCallbacks()\n--- <exception caught here> ---\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n    self.result = callback(self.result, *args, **kw)\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n    d.addCallback(lambda res, req: res.renderHTTP(req), self)\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n    return method(request)\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n    return super(Resource, self).http_GET(request)\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n    return self.render(request)\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/server/notebook/twist.py\", line 1430, in render\n    self.worksheet.sage()\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 2830, in sage\n    self.initialize_sage()\n  File \"/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 2803, in initialize_sage\n    raise RuntimeError\nexceptions.RuntimeError: \t\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6918\n\n",
    "closed_at": "2010-01-19T07:33:26Z",
    "created_at": "2009-09-10T18:50:25Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook -- try harder to create worksheet process??",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6918",
    "user": "https://github.com/williamstein"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/6918





---

archive/issue_events_016250.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T07:33:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6918",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6918#event-16250"
}
```



---

archive/issue_comments_057010.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-19T07:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6918#issuecomment-57010",
    "user": "https://github.com/TimDumol"
}
```

Resolution: invalid
