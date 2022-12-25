# Issue 8556: simple server API broken

archive/issues_008556.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @dandrake\n\nWhen I try to access Sage using the Simple API, I get failures, even though apparently doctests pass in the file.\n\nHere is the server transcript:\n\n```\n$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: notebook()\nThe notebook files are stored in: sage_notebook.sagenb\nRemoving stale pidfile sage_notebook.sagenb/twistd.pid\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n2010-03-18 00:05:32-0600 [-] Log opened.\n2010-03-18 00:05:32-0600 [-] twistd 8.2.0 (/home/grout/sage/local/bin/python 2.6.4) starting up.\n2010-03-18 00:05:32-0600 [-] reactor class: twisted.internet.selectreactor.SelectReactor.\n2010-03-18 00:05:32-0600 [-] twisted.web2.channel.http.HTTPFactory starting on 8000\n2010-03-18 00:05:32-0600 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xb8340ac>\n2010-03-18 00:06:01-0600 [HTTPChannel,6,127.0.0.1] Exception rendering:\n2010-03-18 00:06:01-0600 [HTTPChannel,6,127.0.0.1] Unhandled Error\n    Traceback (most recent call last):\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n        self._runCallbacks()\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n        self.result = callback(self.result, *args, **kw)\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 289, in _continue\n        self.unpause()\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 285, in unpause\n        self._runCallbacks()\n    --- <exception caught here> ---\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n        self.result = callback(self.result, *args, **kw)\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n        d.addCallback(lambda res, req: res.renderHTTP(req), self)\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n        return method(request)\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n        return super(Resource, self).http_GET(request)\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n        return self.render(request)\n      File \"/home/grout/sage/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/simple/twist.py\", line 205, in render\n        U = notebook_twist.notebook.user(username)\n    exceptions.AttributeError: 'NoneType' object has no attribute 'user'\n   \n```\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n\nHere is the client transcript, copied almost verbatim from the doctests in simple.py:\n\n```\nIn [1]: import urllib, re\n\nIn [2]: def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data\n   ...:\n\nIn [3]: login_page = get_url('http://localhost:8000/simple/login?username=admin&password=<DELETED>')\n\nIn [4]: print login_page\n------> print(login_page)\n<html><head><title>Internal Server Error</title></head><body><h1>Internal Server Error</h1>An error occurred rendering the requested page. More information is available in the server log.</body></html>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8556\n\n",
    "closed_at": "2013-05-16T07:43:29Z",
    "created_at": "2010-03-18T06:10:39Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "simple server API broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8556",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @dandrake

When I try to access Sage using the Simple API, I get failures, even though apparently doctests pass in the file.

Here is the server transcript:

```
$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: notebook()
The notebook files are stored in: sage_notebook.sagenb
Removing stale pidfile sage_notebook.sagenb/twistd.pid
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
2010-03-18 00:05:32-0600 [-] Log opened.
2010-03-18 00:05:32-0600 [-] twistd 8.2.0 (/home/grout/sage/local/bin/python 2.6.4) starting up.
2010-03-18 00:05:32-0600 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2010-03-18 00:05:32-0600 [-] twisted.web2.channel.http.HTTPFactory starting on 8000
2010-03-18 00:05:32-0600 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xb8340ac>
2010-03-18 00:06:01-0600 [HTTPChannel,6,127.0.0.1] Exception rendering:
2010-03-18 00:06:01-0600 [HTTPChannel,6,127.0.0.1] Unhandled Error
    Traceback (most recent call last):
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
        self._runCallbacks()
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
        self.result = callback(self.result, *args, **kw)
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 289, in _continue
        self.unpause()
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 285, in unpause
        self._runCallbacks()
    --- <exception caught here> ---
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
        self.result = callback(self.result, *args, **kw)
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/server.py", line 296, in <lambda>
        d.addCallback(lambda res, req: res.renderHTTP(req), self)
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
        return method(request)
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 202, in http_GET
        return super(Resource, self).http_GET(request)
      File "/home/grout/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 128, in http_GET
        return self.render(request)
      File "/home/grout/sage/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/simple/twist.py", line 205, in render
        U = notebook_twist.notebook.user(username)
    exceptions.AttributeError: 'NoneType' object has no attribute 'user'
   
```
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |

Here is the client transcript, copied almost verbatim from the doctests in simple.py:

```
In [1]: import urllib, re

In [2]: def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data
   ...:

In [3]: login_page = get_url('http://localhost:8000/simple/login?username=admin&password=<DELETED>')

In [4]: print login_page
------> print(login_page)
<html><head><title>Internal Server Error</title></head><body><h1>Internal Server Error</h1>An error occurred rendering the requested page. More information is available in the server log.</body></html>
```

Issue created by migration from https://trac.sagemath.org/ticket/8556





---

archive/issue_comments_077281.json:
```json
{
    "body": "I should add that this breaks the remote sagetex functionality that lets people that don't have Sage installed to use sagetex through a remote server.",
    "created_at": "2010-03-18T06:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8556#issuecomment-77281",
    "user": "https://github.com/jasongrout"
}
```

I should add that this breaks the remote sagetex functionality that lets people that don't have Sage installed to use sagetex through a remote server.



---

archive/issue_comments_077282.json:
```json
{
    "body": "Closing as it's about a very outdated notebook version.",
    "created_at": "2013-05-16T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8556#issuecomment-77282",
    "user": "https://github.com/jdemeyer"
}
```

Closing as it's about a very outdated notebook version.



---

archive/issue_events_020617.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-16T07:43:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8556",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8556#event-20617"
}
```



---

archive/issue_comments_077283.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-16T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8556#issuecomment-77283",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_020618.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-16T07:43:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8556",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8556#event-20618"
}
```
