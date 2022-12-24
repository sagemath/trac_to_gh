# Issue 8234: Data file deletion in notebook throws errors

archive/issues_008234.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robert-marik\n\nDelete a file in the data directory of the notebook and you get a page back about an \"Internal Server Error\"  (by selecting the file in the drop-down box, and clicking on the \"delete\" hyperlink).  File is actually deleted, though.\n\nTrace back from Sage command-line invocation of `notebook()` below.\n\nThis does not happen on 4.3.2rc0, but does happen on 4.3.2.  Some discussion, but not much that isn't here already:  \nhttp://groups.google.com/group/sage-notebook/browse_thread/thread/dd2e03d2af01f852\n\n\n```\n2010-02-10 09:22:48-0800 [HTTPChannel,10,127.0.0.1] Exception rendering:\n2010-02-10 09:22:48-0800 [HTTPChannel,10,127.0.0.1] Unhandled Error\n        Traceback (most recent call last):\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n            self._runCallbacks()\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 289, in _continue\n            self.unpause()\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 285, in unpause\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n            d.addCallback(lambda res, req: res.renderHTTP(req), self)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n            return method(request)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n            return super(Resource, self).http_GET(request)\n          File \"/sage/dev/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n            return self.render(request)\n          File \"/sage/dev/local/lib/python2.6/site-packages/sagenb-0.7.4-py2.6.egg/sagenb/notebook/twist.py\", line 671, in render\n            title=u'%s delete successful' % filename))\n        exceptions.TypeError: message() got an unexpected keyword argument 'title'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8234\n\n",
    "created_at": "2010-02-10T18:45:13Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Data file deletion in notebook throws errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8234",
    "user": "@rbeezer"
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

archive/issue_comments_072734.json:
```json
{
    "body": "#6069 should fix this.  If it doesn't, please let me know.",
    "created_at": "2010-02-14T00:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72734",
    "user": "@qed777"
}
```

#6069 should fix this.  If it doesn't, please let me know.



---

archive/issue_comments_072735.json:
```json
{
    "body": "But we still need to fix the page title (\"Error -- Sage\"), which is wrong.",
    "created_at": "2010-02-14T00:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72735",
    "user": "@qed777"
}
```

But we still need to fix the page title ("Error -- Sage"), which is wrong.



---

archive/issue_comments_072736.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> But we still need to fix the page title (\"Error -- Sage\"), which is wrong.\nSee V3 at #6069.",
    "created_at": "2010-02-14T01:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72736",
    "user": "@qed777"
}
```

Replying to [comment:2 mpatel]:
> But we still need to fix the page title ("Error -- Sage"), which is wrong.
See V3 at #6069.



---

archive/issue_comments_072737.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-14T01:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72737",
    "user": "@qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_072738.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T03:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72738",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072739.json:
```json
{
    "body": "When #6069 is merged, we should close this ticket.",
    "created_at": "2010-03-12T18:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72739",
    "user": "@qed777"
}
```

When #6069 is merged, we should close this ticket.



---

archive/issue_comments_072740.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72740",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072741.json:
```json
{
    "body": "As #6069 is marked as positive review, I'll do the same for this.",
    "created_at": "2010-03-15T09:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72741",
    "user": "@TimDumol"
}
```

As #6069 is marked as positive review, I'll do the same for this.



---

archive/issue_comments_072742.json:
```json
{
    "body": "(I'm not changing any notebook code in Sage 4.4.)",
    "created_at": "2010-04-23T04:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72742",
    "user": "@jhpalmieri"
}
```

(I'm not changing any notebook code in Sage 4.4.)



---

archive/issue_comments_072743.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8234#issuecomment-72743",
    "user": "@TimDumol"
}
```

Resolution: fixed
