# Issue 8234: Data file deletion in notebook throws errors

archive/issues_008234.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robert-marik\n\nDelete a file in the data directory of the notebook and you get a page back about an \"Internal Server Error\"  (by selecting the file in the drop-down box, and clicking on the \"delete\" hyperlink).  File is actually deleted, though.\n\nTrace back from Sage command-line invocation of `notebook()` below.\n\nThis does not happen on 4.3.2rc0, but does happen on 4.3.2.  Some discussion, but not much that isn't here already:  \nhttp://groups.google.com/group/sage-notebook/browse_thread/thread/dd2e03d2af01f852\n\n\n```\n2010-02-10 09:22:48-0800 [HTTPChannel,10,127.0.0.1] Exception rendering:\n2010-02-10 09:22:48-0800 [HTTPChannel,10,127.0.0.1] Unhandled Error\n        Traceback (most recent call last):\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n            self._runCallbacks()\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 289, in _continue\n            self.unpause()\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 285, in unpause\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n            d.addCallback(lambda res, req: res.renderHTTP(req), self)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n            return method(request)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n            return super(Resource, self).http_GET(request)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n            return self.render(request)\n          File \"/sage/dev/local/lib/python2.6/site-packages/sagenb-0.7.4-py2.6.egg/sagenb/notebook/twist.py\", line 671, in render\n            title=u'%s delete successful' % filename))\n        exceptions.TypeError: message() got an unexpected keyword argument 'title'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8234\n\n",
    "created_at": "2010-02-10T18:45:13Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Data file deletion in notebook throws errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8234",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @williamstein

CC:  @robert-marik

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


Issue created by migration from https://trac.sagemath.org/ticket/8234





---

archive/issue_comments_072612.json:
```json
{
    "body": "#6069 should fix this.  If it doesn't, please let me know.",
    "created_at": "2010-02-14T00:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72612",
    "user": "https://github.com/qed777"
}
```

#6069 should fix this.  If it doesn't, please let me know.



---

archive/issue_comments_072613.json:
```json
{
    "body": "But we still need to fix the page title (\"Error -- Sage\"), which is wrong.",
    "created_at": "2010-02-14T00:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72613",
    "user": "https://github.com/qed777"
}
```

But we still need to fix the page title ("Error -- Sage"), which is wrong.



---

archive/issue_comments_072614.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> But we still need to fix the page title (\"Error -- Sage\"), which is wrong.\nSee V3 at #6069.",
    "created_at": "2010-02-14T01:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72614",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:2 mpatel]:
> But we still need to fix the page title ("Error -- Sage"), which is wrong.
See V3 at #6069.



---

archive/issue_comments_072615.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-14T01:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72615",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_072616.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T03:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72616",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072617.json:
```json
{
    "body": "When #6069 is merged, we should close this ticket.",
    "created_at": "2010-03-12T18:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72617",
    "user": "https://github.com/qed777"
}
```

When #6069 is merged, we should close this ticket.



---

archive/issue_comments_072618.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72618",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072619.json:
```json
{
    "body": "As #6069 is marked as positive review, I'll do the same for this.",
    "created_at": "2010-03-15T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72619",
    "user": "https://github.com/TimDumol"
}
```

As #6069 is marked as positive review, I'll do the same for this.



---

archive/issue_comments_072620.json:
```json
{
    "body": "(I'm not changing any notebook code in Sage 4.4.)",
    "created_at": "2010-04-23T04:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72620",
    "user": "https://github.com/jhpalmieri"
}
```

(I'm not changing any notebook code in Sage 4.4.)



---

archive/issue_events_019696.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-23T04:41:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8234#event-19696"
}
```



---

archive/issue_comments_072621.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72621",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_019697.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-05-04T04:42:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8234#event-19697"
}
```



---

archive/issue_events_019698.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-25T17:07:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8234#event-19698"
}
```



---

archive/issue_events_019699.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-25T17:07:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8234#event-19699"
}
```
