# Issue 2917: internal server error in notebook sage-3.0.alpha4

archive/issues_002917.json:
```json
{
    "body": "Assignee: boothby\n\nbut on opening a new worksheet (and alson on opening an existing ws)\ngot an internal server error.\n\nSee below,\n\nJaap\n\n\n```\nsage: notebook()\nThe notebook files are stored in: /home/jaap/.sage//sage_notebook\nPort 8000 is already in use.\nTrying next port...\n****************************************************\n*                                                  *\n* Open your web browser to https://localhost:8001  *\n*                                                  *\n****************************************************\nThere is an admin account.  If you do not remember the password,\nquit the notebook and type notebook(reset=True).\nRemoving stale pidfile /home/jaap/.sage/sage_notebook/twistd.pd\n2008-04-14 11:49:14+0200 [-] Log opened.\n2008-04-14 11:49:14+0200 [-] twistd 8.0.1 (/home/jaap/downloads/sage-3.0.alpha4/local/bin/python 2.5.1) starting up\n2008-04-14 11:49:14+0200 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>\n2008-04-14 11:49:14+0200 [-] twisted.web2.channel.http.HTTPFactory starting on 8001\n2008-04-14 11:49:14+0200 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0xa76b76c>\n2008-04-14 11:49:23+0200 [HTTPChannel,0,127.0.0.1] Exception rendering:\n2008-04-14 11:49:23+0200 [HTTPChannel,0,127.0.0.1] Unhandled Error\n         Traceback (most recent call last):\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 185, in addCallbacks\n             self._runCallbacks()\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n             self.result = callback(self.result, *args, **kw)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 284, in _continue\n             self.unpause()\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 280, in unpause\n             self._runCallbacks()\n         --- <exception caught here> ---\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n             self.result = callback(self.result, *args, **kw)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n             d.addCallback(lambda res, req: res.renderHTTP(req), self)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n             return method(request)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n             return super(Resource, self).http_GET(request)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n             return self.render(request)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 1148, in render\n             s = notebook.html(worksheet_filename = self.name,  username=self.username)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 1936, in html\n             body = self._html_body(worksheet_filename=worksheet_filename, username=username, show_debug=show_debug)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 1609, in _html_body\n             worksheet_html = worksheet.html()\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 828, in html\n             s += self.html_worksheet_body(do_print=do_print)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 984, in html_worksheet_body\n             s += cell.html(ncols, do_print=do_print) + '\\n'\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 609, in html\n             html_in  = self.html_in(do_print=do_print)\n           File \"/home/jaap/downloads/sage-3.0.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py\", line 659, in html_in\n             \"\"\"%(cls, r, ncols, id, id, id, id, id, 'readonly=1' if do_print else '', t)\n         exceptions.TypeError: not enough arguments for format string\n\n2008-04-14 11:50:56+0200 [-] (Notebook cleanly saved. Press control-C again to exit.)\n\n```\n\n\nBoothby:\n\n\n```\nLooks like this was due to a bad merge of #2883.  My guess is, adding another 'id,' to sage/server/notebook/cell.py, line 659 will do the trick -- unless something tricky is going on.  I'll check it around 1:30 Monday.\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2917\n\n",
    "created_at": "2008-04-14T15:06:50Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "internal server error in notebook sage-3.0.alpha4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2917",
    "user": "jsp"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/2917





---

archive/issue_comments_020090.json:
```json
{
    "body": "Unsurprisingly this must be fixed before 3.0.final ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T18:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2917#issuecomment-20090",
    "user": "mabshoff"
}
```

Unsurprisingly this must be fixed before 3.0.final ;)

Cheers,

Michael



---

archive/issue_comments_020091.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-14T18:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2917#issuecomment-20091",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_020092.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-15T00:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2917#issuecomment-20092",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_020093.json:
```json
{
    "body": "This fixes the problem for me.",
    "created_at": "2008-04-15T01:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2917#issuecomment-20093",
    "user": "mhansen"
}
```

This fixes the problem for me.



---

archive/issue_comments_020094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T01:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2917#issuecomment-20094",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020095.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T01:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2917#issuecomment-20095",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
