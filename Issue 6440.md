# Issue 6440: hg_sage.serve() is broken in 4.1.alpha1 (mainly on Mac?)

archive/issues_006440.json:
```json
{
    "body": "Assignee: cwitty\n\nhg_sage.serve() works in Sage 4.0.2 but is broken in 4.1.alpha1.  On an Intel Mac running OS X 10.5, I see this:\n\n```\nsage: hg_sage.serve()\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8200 *\n*                                                *\n**************************************************\ncd \"/Applications/sage/devel/sage\" && hg serve --address localhost --port 8200  \n127.0.0.1 - - [28/Jun/2009 08:06:08] \"GET / HTTP/1.1\" 200 -\nsh: line 1: 47150 Bus error               hg serve --address localhost --port 8200\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8200 *\n*                                                *\n**************************************************\n```\n\nThen the web page \"http://localhost:8200/\" is pretty broken -- see the picture \"serve.png\".  \n\nOn sage.math, the web page seems to work, but I get a long list of messages:\n\n```\n**************************************************                                                                                   \n*                                                *                                                                                   \n* Open your web browser to http://localhost:8200 *                                                                                   \n*                                                *                                                                                   \n**************************************************                                                                                   \ncd \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/devel/sage\" && hg serve --address localhost --port 8200            \n127.0.0.1 - - [28/Jun/2009 08:22:50] \"GET / HTTP/1.1\" 200 -                                                                          \n127.0.0.1 - - [28/Jun/2009 08:22:51] \"GET /static/hglogo.png HTTP/1.1\" 500 -                                                         \n127.0.0.1 - - [28/Jun/2009 08:22:51] \"GET /static/style-paper.css HTTP/1.1\" 200 -                                                    \n127.0.0.1 - - [28/Jun/2009 08:22:51] Exception happened during processing request '/static/hglogo.png':                              \nTraceback (most recent call last):                                                                                                   \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py\", line 68, in do_POST                                                                                                                                   \n    self.do_write()                                                                                                                  \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py\", line 61, in do_write                                                                                                                                  \n    self.do_hgweb()                                                                                                                  \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py\", line 125, in do_hgweb                                                                                                                                 \n    for chunk in self.server.application(env, self._start_response):                                                                 \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/hgweb_mod.py\", line 80, in __call__                                                                                                                               \n    return self.run_wsgi(req)                                                                                                        \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/hgweb_mod.py\", line 182, in run_wsgi                                                                                                                              \n    content = getattr(webcommands, cmd)(self, req, tmpl)                                                                             \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/webcommands.py\", line 622, in static                                                                                                                              \n    return [staticfile(static, fname, req)]                                                                                          \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/common.py\", line 69, in staticfile                                                                                                                                \n    ct = mimetypes.guess_type(path)[0] or \"text/plain\"                                                                               \n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py\", line 242, in guess_type        \n    return guess_type(url, strict)              \n\n[many identical lines]\n\n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py\", line 242, in guess_type\n    return guess_type(url, strict)\n  File \"/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py\", line 242, in guess_type\n    return guess_type(url, strict)\nRuntimeError: maximum recursion depth exceeded\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6440\n\n",
    "created_at": "2009-06-28T15:28:33Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "hg_sage.serve() is broken in 4.1.alpha1 (mainly on Mac?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6440",
    "user": "jhpalmieri"
}
```
Assignee: cwitty

hg_sage.serve() works in Sage 4.0.2 but is broken in 4.1.alpha1.  On an Intel Mac running OS X 10.5, I see this:

```
sage: hg_sage.serve()
**************************************************
*                                                *
* Open your web browser to http://localhost:8200 *
*                                                *
**************************************************
cd "/Applications/sage/devel/sage" && hg serve --address localhost --port 8200  
127.0.0.1 - - [28/Jun/2009 08:06:08] "GET / HTTP/1.1" 200 -
sh: line 1: 47150 Bus error               hg serve --address localhost --port 8200
**************************************************
*                                                *
* Open your web browser to http://localhost:8200 *
*                                                *
**************************************************
```

Then the web page "http://localhost:8200/" is pretty broken -- see the picture "serve.png".  

On sage.math, the web page seems to work, but I get a long list of messages:

```
**************************************************                                                                                   
*                                                *                                                                                   
* Open your web browser to http://localhost:8200 *                                                                                   
*                                                *                                                                                   
**************************************************                                                                                   
cd "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/devel/sage" && hg serve --address localhost --port 8200            
127.0.0.1 - - [28/Jun/2009 08:22:50] "GET / HTTP/1.1" 200 -                                                                          
127.0.0.1 - - [28/Jun/2009 08:22:51] "GET /static/hglogo.png HTTP/1.1" 500 -                                                         
127.0.0.1 - - [28/Jun/2009 08:22:51] "GET /static/style-paper.css HTTP/1.1" 200 -                                                    
127.0.0.1 - - [28/Jun/2009 08:22:51] Exception happened during processing request '/static/hglogo.png':                              
Traceback (most recent call last):                                                                                                   
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py", line 68, in do_POST                                                                                                                                   
    self.do_write()                                                                                                                  
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py", line 61, in do_write                                                                                                                                  
    self.do_hgweb()                                                                                                                  
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py", line 125, in do_hgweb                                                                                                                                 
    for chunk in self.server.application(env, self._start_response):                                                                 
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/hgweb_mod.py", line 80, in __call__                                                                                                                               
    return self.run_wsgi(req)                                                                                                        
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/hgweb_mod.py", line 182, in run_wsgi                                                                                                                              
    content = getattr(webcommands, cmd)(self, req, tmpl)                                                                             
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/webcommands.py", line 622, in static                                                                                                                              
    return [staticfile(static, fname, req)]                                                                                          
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/common.py", line 69, in staticfile                                                                                                                                
    ct = mimetypes.guess_type(path)[0] or "text/plain"                                                                               
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py", line 242, in guess_type        
    return guess_type(url, strict)              

[many identical lines]

  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py", line 242, in guess_type
    return guess_type(url, strict)
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py", line 242, in guess_type
    return guess_type(url, strict)
RuntimeError: maximum recursion depth exceeded
```



Issue created by migration from https://trac.sagemath.org/ticket/6440





---

archive/issue_comments_051694.json:
```json
{
    "body": "Attachment [serve.png](tarball://root/attachments/some-uuid/ticket6440/serve.png) by jason created at 2009-09-15 04:36:22\n\nSee #6906 for apparently the solution (upgrade mercurial)",
    "created_at": "2009-09-15T04:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6440#issuecomment-51694",
    "user": "jason"
}
```

Attachment [serve.png](tarball://root/attachments/some-uuid/ticket6440/serve.png) by jason created at 2009-09-15 04:36:22

See #6906 for apparently the solution (upgrade mercurial)



---

archive/issue_comments_051695.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6440#issuecomment-51695",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_051696.json:
```json
{
    "body": "Closed by #6906",
    "created_at": "2009-10-15T09:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6440#issuecomment-51696",
    "user": "mhansen"
}
```

Closed by #6906
