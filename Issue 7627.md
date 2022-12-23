# Issue 7627: Settings page (for converted notebook?) gives errors

archive/issues_007627.json:
```json
{
    "body": "Assignee: was\n\nI started sage 4.2.1 and did:\n\n```\n% sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: notebook()\nThe notebook files are stored in: sage_notebook.sagenb\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n2009-12-08 13:27:27-0600 [-] Log opened.\n2009-12-08 13:27:27-0600 [-] twistd 8.2.0 (/home/jason/sage/local/bin/python 2.6.2) starting up.\n2009-12-08 13:27:27-0600 [-] reactor class: twisted.internet.selectreactor.SelectReactor.\n2009-12-08 13:27:27-0600 [-] twisted.web2.channel.http.HTTPFactory starting on 8000\n2009-12-08 13:27:27-0600 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xb5f3dcc>\n```\n\n| Sage Version 4.2.1, Release Date: 2009-11-14                       |\n| Type notebook() for the GUI, and license() for information.        |\nThen I clicked on \"Settings\", and then \"Notebook Settings\", and I got the following webpage:\n\n\n```\n Internal Server Error\n\nAn error occurred rendering the requested page. More information is available in the server log.\n```\n\nand the following error in the log:\n\n```\n2009-12-08 13:27:51-0600 [HTTPChannel,1,127.0.0.1] Exception rendering:\n2009-12-08 13:27:51-0600 [HTTPChannel,1,127.0.0.1] Unhandled Error\n   Traceback (most recent call last):\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n       self._runCallbacks()\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n       self.result = callback(self.result, *args, **kw)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 289, in _continue\n       self.unpause()\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 285, in unpause\n       self._runCallbacks()\n   --- <exception caught here> ---\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n       self.result = callback(self.result, *args, **kw)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n       d.addCallback(lambda res, req: res.renderHTTP(req), self)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n       return method(request)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n       return super(Resource, self).http_GET(request)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n       return self.render(request)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py\", line 978, in render\n       template_dict['auto_table'] = notebook.conf().html_table(updated)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/conf.py\", line 123, in html_table\n       G[DS[key][GROUP]] = [key]\n   exceptions.KeyError: 'number_of_backups'\n\n```\n\nI believe this was a notebook that was automatically converted from the old format. \n\n\n```\n\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7627\n\n",
    "created_at": "2009-12-08T19:54:56Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Settings page (for converted notebook?) gives errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7627",
    "user": "jason"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/7627





---

archive/issue_comments_065163.json:
```json
{
    "body": "I moved .sage and restarted the notebook, and the Settings then worked fine.",
    "created_at": "2009-12-08T19:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65163",
    "user": "jason"
}
```

I moved .sage and restarted the notebook, and the Settings then worked fine.



---

archive/issue_comments_065164.json:
```json
{
    "body": "Attachment\n\nSkip obsolete or improperly annotated notebook settings.  Depends on #7625.  sagenb repo.",
    "created_at": "2009-12-08T23:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65164",
    "user": "mpatel"
}
```

Attachment

Skip obsolete or improperly annotated notebook settings.  Depends on #7625.  sagenb repo.



---

archive/issue_comments_065165.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-08T23:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65165",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065166.json:
```json
{
    "body": "With the patch, the rendered notebook settings page should contain only current (i.e., present in `sagenb.notebook.server_conf.defaults`) or \"properly\" annotated (see `sagenb.notebook.server_conf.defaults_descriptions`) settings.\n\nThe server should now also look up [incoming] request arguments in `defaults_descriptions`.",
    "created_at": "2009-12-08T23:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65166",
    "user": "mpatel"
}
```

With the patch, the rendered notebook settings page should contain only current (i.e., present in `sagenb.notebook.server_conf.defaults`) or "properly" annotated (see `sagenb.notebook.server_conf.defaults_descriptions`) settings.

The server should now also look up [incoming] request arguments in `defaults_descriptions`.



---

archive/issue_comments_065167.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T00:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65167",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065168.json:
```json
{
    "body": "Very nice!  This is a great improvement -- the notebook settings actually work!",
    "created_at": "2009-12-09T00:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65168",
    "user": "was"
}
```

Very nice!  This is a great improvement -- the notebook settings actually work!



---

archive/issue_comments_065169.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-12-09T00:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65169",
    "user": "was"
}
```

Changing priority from major to critical.



---

archive/issue_comments_065170.json:
```json
{
    "body": "merged into sagenb-0.4.6",
    "created_at": "2009-12-09T01:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65170",
    "user": "was"
}
```

merged into sagenb-0.4.6



---

archive/issue_comments_065171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T01:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7627#issuecomment-65171",
    "user": "was"
}
```

Resolution: fixed
